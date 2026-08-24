from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.tools import tool
from langchain.agents import create_agent

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")


# -----------------------------
# 1. Gemini Embeddings
# -----------------------------

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=api_key
)


# -----------------------------
# 2. Load ChromaDB
# -----------------------------

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


# -----------------------------
# 3. Create RAG Tool
# -----------------------------

@tool
def search_company_policy(query: str) -> str:
    """
    Search the company policy knowledge base for information
    related to employee policies, leave, benefits, working hours,
    remote work, security, and other company-related questions.
    """

    results = retriever.invoke(query)

    if not results:
        return "No relevant information was found in the company policy."

    context = "\n\n".join(
        result.page_content for result in results
    )

    return context


# -----------------------------
# 4. Gemini LLM
# -----------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)


# -----------------------------
# 5. AI Agent
# -----------------------------

system_prompt = """
You are an AI Customer Support Agent for a company.

Your job is to answer customer and employee questions accurately.

You have access to a company policy search tool.

Decision-making rules:
1. Understand the user's question.
2. If the question is related to company policies or information,
   use the search_company_policy tool.
3. Analyze the information returned by the tool.
4. Answer using the retrieved company information.
5. Do not invent company policies or information.
6. If the information is not available, clearly say that the
   information was not found in the company knowledge base.

Follow a Reason → Act → Observe → Answer workflow.
"""

agent = create_agent(
    model=llm,
    tools=[search_company_policy],
    system_prompt=system_prompt
)


# -----------------------------
# 6. Test the Agent
# -----------------------------
print("\n🤖 AI CUSTOMER SUPPORT AGENT")
print("=" * 50)
print("Ask questions about company policies.")
print("Type 'exit' to stop.")
print("=" * 50)

while True:

    query = input("\n👤 You: ")

    if query.lower() == "exit":
        print("\n👋 Agent stopped. Goodbye!")
        break

    if not query.strip():
        continue

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    final_message = response["messages"][-1]
    content = final_message.content

    print("\n🤖 Agent:")

    if isinstance(content, list):
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                print(item.get("text", ""))
    else:
        print(content)