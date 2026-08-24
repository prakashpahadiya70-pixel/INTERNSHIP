from langchain_ollama import ChatOllama
from state import AgentState


llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


def coordinator_agent(state: AgentState):
    print("\n[Coordinator Agent]")
    print("Analyzing user request...")

    query = state["user_query"]

    prompt = f"""
You are the Coordinator Agent in a company multi-agent system.

Analyze the user's request and decide what information
the Research Agent needs to find.

User Request:
{query}

Return a short and clear research task.
"""

    response = llm.invoke(prompt)

    result = response.content

    print("Coordinator Result:")
    print(result)

    return {
        "coordinator_result": result
    }

def research_agent(state: AgentState):
    print("\n[Research Agent]")
    print("Reading company knowledge base...")

    query = state["user_query"]
    coordinator_result = state["coordinator_result"]

    try:
        with open(
            "company_data/company_policy.txt",
            "r",
            encoding="utf-8"
        ) as file:
            company_data = file.read()

        prompt = f"""
You are the Research Agent of a company AI assistant.

You must answer the user's request using ONLY the
company knowledge provided below.

Company Knowledge:
{company_data}

User Request:
{query}

Coordinator Instructions:
{coordinator_result}

Find the information relevant to the user's request.

Do not invent company policies or information.

If the requested information is not present in the
company knowledge, clearly say:

"Information not available in the company knowledge base."

Return only the relevant information.
"""

        response = llm.invoke(prompt)

        result = response.content

        print("Research Result:")
        print(result)

        return {
            "research_result": result,
            "error": ""
        }

    except Exception as e:

        error_message = f"Research Agent Error: {str(e)}"

        print(error_message)

        return {
            "research_result": "",
            "error": error_message
        }
def writer_agent(state: AgentState):
    print("\n[Writer Agent]")
    print("Preparing final response...")

    query = state["user_query"]
    research_result = state["research_result"]
    error = state["error"]

    if error:
        return {
            "final_answer": (
                "Sorry, I was unable to retrieve the required "
                "information from the company knowledge base."
            )
        }

    prompt = f"""
You are the Writer Agent in a company AI assistant.

User Question:
{query}

Research Information:
{research_result}

Write a clear, concise and professional answer.

Use only the provided research information.

Do not invent information.

Do not mention internal agents or the workflow.
"""

    response = llm.invoke(prompt)

    result = response.content

    print("Writer Result:")
    print(result)

    return {
        "final_answer": result
    }