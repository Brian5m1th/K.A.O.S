from loguru import logger
from langgraph.graph import END, StateGraph

from app.agent.nodes.executor import executor
from app.agent.nodes.planner import planner
from app.agent.nodes.retrieve import retrieve_context
from app.agent.nodes.ingest import ingest_source
from app.agent.state import AgentState


def should_use_tool(state: AgentState) -> str:
    if state.get("tool_to_call"):
        logger.info("[info] should_use_tool - encaminhando para executor")
        return "executor"
    return END


def route_entry(state: AgentState) -> str:
    if state.get("ingest_source_path"):
        logger.info(f"[info] route_entry - ingest: {state['ingest_source_path']}")
        return "ingest_source"
    logger.info("[info] route_entry - query")
    return "retrieve"


def build_graph() -> StateGraph:
    graph = StateGraph(AgentState)

    graph.add_node("retrieve", retrieve_context)
    graph.add_node("planner", planner)
    graph.add_node("executor", executor)
    graph.add_node("ingest_source", ingest_source)

    graph.set_conditional_entry_point(route_entry, {
        "ingest_source": "ingest_source",
        "retrieve": "retrieve",
    })
    graph.add_edge("retrieve", "planner")
    graph.add_edge("ingest_source", END)
    graph.add_conditional_edges("planner", should_use_tool)
    graph.add_edge("executor", "planner")

    return graph.compile()


agent_graph = build_graph()
