import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

from tools.calculator import calculator
from tools.web_search import web_search
from tools.database import query_database
from tools.file_reader import read_file
from tools.weather import get_weather
from tools.email_tool import send_email
from tools.date_tool import date_tool
from tools.data_analyzer import analyze_csv


load_dotenv()


# =========================
# Calculator Tool
# =========================

@tool
def calculator_tool(operation: str, a: float, b: float):
    """Perform basic mathematical calculations."""

    return calculator(operation, a, b)


# =========================
# Web Search Tool
# =========================

@tool
def web_search_tool(query: str):
    """Search the web for current information."""

    return web_search(query)


# =========================
# Database Tool
# =========================

@tool
def database_tool(query: str):
    """Execute a SQL query on the company database."""

    return query_database(query)


# =========================
# File Reader Tool
# =========================

@tool
def file_reader_tool(file_path: str):
    """Read text content from a file."""

    return read_file(file_path)


# =========================
# Weather Tool
# =========================

@tool
def weather_tool(city: str):
    """Get current weather information for a city."""

    return get_weather(city)


# =========================
# Email Tool
# =========================

@tool
def email_tool(to: str, subject: str, body: str):
    """Prepare an email in safe testing mode."""

    return send_email(to, subject, body)


# =========================
# Date Tool
# =========================

@tool
def date_tool_function(operation: str, days: int = 0):
    """Perform date-related operations."""

    return date_tool(operation, days)


# =========================
# Data Analyzer Tool
# =========================

@tool
def data_analyzer_tool(file_path: str):
    """Analyze a CSV file using pandas."""

    if not file_path.startswith("data/"):
        file_path = os.path.join("data", file_path)

    return analyze_csv(file_path)


# =========================
# All Tools
# =========================

tools = [
    calculator_tool,
    web_search_tool,
    database_tool,
    file_reader_tool,
    weather_tool,
    email_tool,
    date_tool_function,
    data_analyzer_tool
]


# =========================
# Gemini Model
# =========================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)


# Bind tools with Gemini
llm_with_tools = llm.bind_tools(tools)


# =========================
# Tool Execution Helper
# =========================

def execute_tool(tool_name, tool_args):

    for selected_tool in tools:

        if selected_tool.name == tool_name:

            try:
                return selected_tool.invoke(tool_args)

            except Exception as e:
                return {
                    "success": False,
                    "error": f"{tool_name} failed: {str(e)}"
                }

    return {
        "success": False,
        "error": f"Tool '{tool_name}' not found."
    }


# =========================
# Function Calling + Tool Chaining Agent
# =========================

def run_agent(user_query):

    try:

        messages = [
            HumanMessage(content=user_query)
        ]

        # Maximum number of tool execution rounds
        max_iterations = 5

        for iteration in range(max_iterations):

            print(f"\n--- Agent Step {iteration + 1} ---")

            # Ask Gemini what to do
            response = llm_with_tools.invoke(messages)

            # ---------------------------------
            # No tool required
            # ---------------------------------

            if not response.tool_calls:

                print("\nFinal AI Response:")
                print("=" * 50)
                print(response.content)

                return

            # ---------------------------------
            # Tool calls detected
            # ---------------------------------

            print("\nTool Calls:")
            print("=" * 50)

            # Add Gemini response to conversation
            messages.append(response)

            tool_messages = []

            # ---------------------------------
            # Execute selected tools
            # ---------------------------------

            for call in response.tool_calls:

                tool_name = call["name"]
                tool_args = call["args"]
                tool_call_id = call["id"]

                print("Tool:", tool_name)
                print("Arguments:", tool_args)

                # Execute tool
                tool_result = execute_tool(
                    tool_name,
                    tool_args
                )

                print("Tool Result:", tool_result)

                # Send result back to Gemini
                tool_message = ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call_id
                )

                tool_messages.append(tool_message)

            # Add tool results to conversation
            messages.extend(tool_messages)

        # ---------------------------------
        # Maximum iteration protection
        # ---------------------------------

        print("\nAgent stopped.")
        print("Maximum tool execution steps reached.")

    except Exception as e:

        print("\nAgent Error:", str(e))


# =========================
# Main Program
# =========================

if __name__ == "__main__":

    print("🤖 DAY 20 AI AGENT")
    print("=" * 50)

    query = input("Ask something: ")

    run_agent(query)