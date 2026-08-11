from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from prompt_template import support_prompt


# ============================================================
# 1. LOCAL AI MODEL
# ============================================================

llm = ChatOllama(
    model="llama3.2",
    temperature=0.3
)


# ============================================================
# 2. OUTPUT PARSER
# ============================================================

class SupportResponse(BaseModel):
    category: str = Field(
        description="Category of the user's support query"
    )

    answer: str = Field(
        description="Helpful answer to the user's query"
    )

    next_step: str = Field(
        description="Recommended next step for the user"
    )


parser = PydanticOutputParser(
    pydantic_object=SupportResponse
)


# ============================================================
# 3. QUERY ANALYSIS PROMPT
# ============================================================

analysis_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a support query analyzer.

Analyze the user's query and identify:
1. The category of the problem.
2. What the user is asking.
3. What kind of solution would help.

Give a short and clear analysis."""
    ),
    (
        "human",
        "{user_query}"
    )
])


# ============================================================
# 4. FINAL SUPPORT PROMPT
# ============================================================

final_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a professional AI Support Assistant.

Use the user's query and analysis to provide a helpful response.

Return the answer according to these instructions:

{format_instructions}

Be polite, simple and concise."""
    ),
    (
        "human",
        """User Query:
{user_query}

Query Analysis:
{analysis}

Previous Conversation:
{conversation_history}"""
    )
])


# ============================================================
# 5. CONVERSATION MEMORY
# ============================================================

conversation_memory = InMemoryChatMessageHistory()


# ============================================================
# 6. AI SUPPORT ASSISTANT FUNCTION
# ============================================================

def get_support_response(user_query):

    # --------------------------------------------------------
    # Step A: Analyze user query
    # --------------------------------------------------------

    analysis_chain = analysis_prompt | llm

    analysis_result = analysis_chain.invoke({
        "user_query": user_query
    })

    analysis = analysis_result.content


    # --------------------------------------------------------
    # Step B: Get previous conversation
    # --------------------------------------------------------

    previous_messages = conversation_memory.messages

    if previous_messages:

        conversation_history = "\n".join(
            [
                f"{message.type}: {message.content}"
                for message in previous_messages
            ]
        )

    else:

        conversation_history = "No previous conversation."


    # --------------------------------------------------------
    # Step C: Generate final response
    # --------------------------------------------------------

    final_chain = final_prompt | llm | parser

    response = final_chain.invoke({
        "user_query": user_query,
        "analysis": analysis,
        "conversation_history": conversation_history,
        "format_instructions": parser.get_format_instructions()
    })


    # --------------------------------------------------------
    # Step D: Save conversation to memory
    # --------------------------------------------------------

    conversation_memory.add_user_message(user_query)

    conversation_memory.add_ai_message(
        response.answer
    )


    return response


# ============================================================
# 7. MAIN PROGRAM
# ============================================================

print("=" * 60)
print("          AI SUPPORT ASSISTANT - DAY 15")
print("=" * 60)

print("Powered by Ollama + Llama 3.2 + LangChain")
print("Type 'exit' to stop.\n")


while True:

    user_query = input("You: ")

    if user_query.lower() == "exit":

        print("\nAssistant: Thank you for using AI Support Assistant!")

        break


    try:

        response = get_support_response(user_query)

        print("\nAssistant:")
        print("Category :", response.category)
        print("Answer   :", response.answer)
        print("Next Step:", response.next_step)
        print()

    except Exception as e:

        print("\nError:", e)
        print()