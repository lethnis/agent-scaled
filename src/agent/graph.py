from langchain.tools import BaseTool
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode

from src.agent.nodes import get_assistant_node
from src.agent.state import AgentState
from src.tools import ALL_TOOLS


def should_continue(state: AgentState) -> str:
    last = state["messages"][-1]
    if hasattr(last, "tool_calls") and last.tool_calls:
        return "tools"
    return END


def build_graph(extra_tools: list[BaseTool] | None = None) -> StateGraph:
    if extra_tools is None:
        extra_tools = []

    tool_node = ToolNode(ALL_TOOLS + extra_tools)

    graph = StateGraph(AgentState)
    graph.add_node("assistant", get_assistant_node(extra_tools))
    graph.add_node("tools", tool_node)

    graph.set_entry_point("assistant")
    graph.add_conditional_edges(
        "assistant",
        should_continue,
        {
            "tools": "tools",
            END: END,
        },
    )
    graph.add_edge("tools", "assistant")

    return graph


def create_agent(extra_tools: list[BaseTool] | None = None):
    graph = build_graph(extra_tools)
    return graph.compile()
