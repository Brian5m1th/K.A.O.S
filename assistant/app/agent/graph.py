from loguru import logger
from langgraph.graph import END, StateGraph

from app.agent.nodes.executor import executor
from app.agent.nodes.planner import planner
from app.agent.nodes.retrieve import retrieve_context
from app.agent.state import AgentState


def should_use_tool(state: AgentState) -> str:
    if state.get("tool_to_call"):
        logger.info("[info] should_use_tool - encaminhando para executor")
        return "executor"
    return END


def build_graph() -> StateGraph:
    graph = StateGraph(AgentState)

    graph.add_node("retrieve", retrieve_context)
    graph.add_node("planner", planner)
    graph.add_node("executor", executor)

    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "planner")
    graph.add_conditional_edges("planner", should_use_tool)
    graph.add_edge("executor", "planner")

    return graph.compile()


agent_graph = build_graph()
