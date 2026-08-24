from typing import TypedDict


class AgentState(TypedDict):
    user_query: str
    coordinator_result: str
    research_result: str
    final_answer: str
    error: str