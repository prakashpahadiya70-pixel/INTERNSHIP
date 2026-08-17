from typing import TypedDict, List

from langgraph.graph import StateGraph, START, END

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from dotenv import load_dotenv
import os


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. "
        "Please add GOOGLE_API_KEY to your .env file."
    )


# ============================================================
# DOCUMENT LOADING
# ============================================================

loader = TextLoader(
    "documents/ecommerce_support.txt",
    encoding="utf-8"
)

documents = loader.load()


# ============================================================
# TEXT SPLITTING
# ============================================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)


print("\n==============================")
print("DOCUMENT SETUP")
print("==============================")
print("Documents Loaded:", len(documents))
print("Chunks Created:", len(chunks))


# ============================================================
# GEMINI EMBEDDINGS
# ============================================================

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
)


# ============================================================
# CHROMADB VECTOR STORE
# ============================================================

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="ecommerce_support_day19"
)


# ============================================================
# GEMINI LLM
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)


# ============================================================
# 1. STATE
# ============================================================

class AgentState(TypedDict):
    question: str
    context: List[str]
    answer: str
    retry_count: int
    memory: List[str]
    error: str


# ============================================================
# 2. QUESTION NODE
# ============================================================

def question_node(state: AgentState):

    print("\n[Question Node]")
    print("User Question:", state["question"])

    return {
        "question": state["question"]
    }


# ============================================================
# 3. RETRIEVER NODE
# ============================================================

def retriever_node(state: AgentState):

    print("\n[Retriever Node]")

    question = state["question"]
    retry_count = state["retry_count"]

    try:

        # First attempt = 3 documents
        # Retry attempt = 5 documents

        k = 3 if retry_count == 0 else 5

        results = vectorstore.similarity_search_with_relevance_scores(
            question,
            k=k
        )

        context = []

        for doc, score in results:

            print(f"Similarity Score: {score:.2f}")

            if score >= 0.60:
                context.append(doc.page_content)

        print("Relevant Documents:", len(context))

        return {
            "context": context,
            "error": ""
        }

    except Exception as e:

        print("\n[Retriever Error]")
        print(str(e))

        return {
            "context": [],
            "error": str(e)
        }


# ============================================================
# 4. CONDITIONAL ROUTING
# ============================================================

def check_retrieval(state: AgentState):

    context = state["context"]
    retry_count = state["retry_count"]
    error = state["error"]

    # Retriever error
    if error:

        if retry_count < 1:

            print("\n[Router]")
            print("Retriever error detected.")
            print("Routing to Retry Node.")

            return "retry"

        else:

            print("\n[Router]")
            print("Retriever failed after retry.")
            print("Routing to Error Node.")

            return "error"

    # Relevant documents found
    if context:

        print("\n[Router]")
        print("Relevant documents found.")
        print("Routing to LLM Node.")

        return "llm"

    # No relevant documents → retry
    elif retry_count < 1:

        print("\n[Router]")
        print("No relevant documents found.")
        print("Routing to Retry Node.")

        return "retry"

    # Retry completed → error
    else:

        print("\n[Router]")
        print("No relevant documents after retry.")
        print("Routing to Error Node.")

        return "error"


# ============================================================
# 5. RETRY NODE
# ============================================================

def retry_node(state: AgentState):

    print("\n[Retry Node]")

    new_retry_count = state["retry_count"] + 1

    print("Retry Count:", new_retry_count)

    return {
        "retry_count": new_retry_count,
        "context": [],
        "error": ""
    }


# ============================================================
# 6. LLM NODE
# ============================================================

def llm_node(state: AgentState):

    print("\n[LLM Node]")

    question = state["question"]
    context = state["context"]
    memory = state.get("memory", [])

    context_text = "\n\n".join(context)

    # Include previous conversation for memory
    previous_conversation = "\n".join(memory[-5:])

    prompt = f"""
You are an e-commerce customer support assistant.

Answer the user's question using ONLY the information
provided in the knowledge base context.

Do not invent or assume information.

You may use the previous conversation to understand
follow-up questions, but factual answers must come
from the provided knowledge base context.

If the answer is not available in the context,
clearly say that the information is not available.

Keep the answer short, clear and helpful.

==============================
PREVIOUS CONVERSATION
==============================

{previous_conversation}

==============================
KNOWLEDGE BASE CONTEXT
==============================

{context_text}

==============================
CURRENT USER QUESTION
==============================

{question}
"""

    try:

        response = llm.invoke(prompt)

        # Gemini may return structured content
        if isinstance(response.content, list):

            answer = "".join(
                item.get("text", "")
                for item in response.content
                if isinstance(item, dict)
            )

        else:

            answer = response.content

        print("\nGenerated Answer:")
        print(answer)

        return {
            "answer": answer,
            "error": ""
        }

    except Exception as e:

        print("\n[LLM Error]")
        print(str(e))

        return {
            "answer":
                "Sorry, an error occurred while generating the answer.",
            "error": str(e)
        }


# ============================================================
# 7. ERROR HANDLING NODE
# ============================================================

def error_node(state: AgentState):

    print("\n[Error Handling Node]")

    if state["error"]:

        answer = (
            "Sorry, I am unable to process your question "
            "because an error occurred while retrieving "
            "the required information."
        )

    else:

        answer = (
            "Sorry, I could not find relevant information "
            "in the knowledge base for your question."
        )

    print("Error Response:", answer)

    return {
        "answer": answer
    }


# ============================================================
# 8. MEMORY NODE
# ============================================================

def memory_node(state: AgentState):

    print("\n[Memory Node]")

    memory = state.get("memory", [])

    memory.append(
        f"Q: {state['question']} | A: {state['answer']}"
    )

    print("Memory Updated")

    return {
        "memory": memory
    }


# ============================================================
# 9. BUILD LANGGRAPH
# ============================================================

graph = StateGraph(AgentState)


# Add Nodes

graph.add_node("question", question_node)
graph.add_node("retriever", retriever_node)
graph.add_node("retry", retry_node)
graph.add_node("llm", llm_node)
graph.add_node("error", error_node)
graph.add_node("memory", memory_node)


# ============================================================
# GRAPH CONNECTIONS
# ============================================================

graph.add_edge(
    START,
    "question"
)

graph.add_edge(
    "question",
    "retriever"
)


# ============================================================
# CONDITIONAL ROUTING
# ============================================================

graph.add_conditional_edges(
    "retriever",
    check_retrieval,
    {
        "llm": "llm",
        "retry": "retry",
        "error": "error"
    }
)


# ============================================================
# RETRY LOOP
# ============================================================

graph.add_edge(
    "retry",
    "retriever"
)


# ============================================================
# SUCCESS PATH
# ============================================================

graph.add_edge(
    "llm",
    "memory"
)


# ============================================================
# ERROR PATH
# ============================================================

graph.add_edge(
    "error",
    "memory"
)


# ============================================================
# MEMORY → END
# ============================================================

graph.add_edge(
    "memory",
    END
)


# ============================================================
# COMPILE GRAPH
# ============================================================

app = graph.compile()


# ============================================================
# 10. INTERACTIVE CHAT
# ============================================================

if __name__ == "__main__":

    print("\n======================================")
    print("   🤖 E-COMMERCE LANGGRAPH AGENT")
    print("======================================")

    print("\nAsk questions about products, orders,")
    print("delivery, returns, refunds and payments.")

    print("\nType 'exit' to stop the chatbot.")

    # Persistent conversation memory
    conversation_memory = []

    while True:

        print("\n--------------------------------------")

        user_question = input("You: ").strip()

        # Exit condition
        if user_question.lower() in ["exit", "quit", "bye"]:

            print("\n🤖 AI: Thank you for using the")
            print("E-Commerce Customer Support Agent!")

            break

        # Empty question
        if not user_question:

            print("🤖 AI: Please enter a question.")

            continue


        # State for current question
        initial_state = {

            "question": user_question,

            "context": [],

            "answer": "",

            # Reset retry for every new question
            "retry_count": 0,

            # Keep previous conversation
            "memory": conversation_memory,

            "error": ""
        }


        # Run LangGraph
        result = app.invoke(initial_state)


        # Update persistent memory
        conversation_memory = result["memory"]


        # Display answer
        print("\n🤖 AI:", result["answer"])


        # Display retry information
        if result["retry_count"] > 0:

            print(
                f"🔄 Retrieval retries: "
                f"{result['retry_count']}"
            )


    # ========================================================
    # SESSION MEMORY
    # ========================================================

    print("\n======================================")
    print("SESSION MEMORY")
    print("======================================")

    if conversation_memory:

        for item in conversation_memory:

            print(item)

    else:

        print("No conversation history.")


    print("\n======================================")
    print("WORKFLOW COMPLETED")
    print("======================================")