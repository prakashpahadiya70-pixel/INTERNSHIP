from langgraph.graph import StateGraph, START, END

from state import AgentState
from agents import (
    coordinator_agent,
    research_agent,
    writer_agent
)


def build_graph():

    graph = StateGraph(AgentState)

    # Add agent nodes
    graph.add_node("coordinator", coordinator_agent)
    graph.add_node("research", research_agent)
    graph.add_node("writer", writer_agent)

    # Define communication flow
    graph.add_edge(START, "coordinator")
    graph.add_edge("coordinator", "research")
    graph.add_edge("research", "writer")
    graph.add_edge("writer", END)

    return graph.compile()