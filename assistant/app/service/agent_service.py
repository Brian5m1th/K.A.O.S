from langchain_core.messages import HumanMessage
from loguru import logger

from app.agent.graph import agent_graph
from app.agent.state import AgentState


class AgentService:
    async def process_message(
        self, session_id: str, user_message: str
    ) -> str:
        logger.info(f"[{session_id}] Processando: {user_message[:60]}...")

        initial_state: AgentState = {
            "messages": [HumanMessage(content=user_message)],
            "retrieved_context": [],
            "tool_to_call": None,
            "tool_args": {},
            "tool_result": None,
            "session_id": session_id,
        }

        final_state = await agent_graph.ainvoke(initial_state)

        last_ai_message = next(
            (m for m in reversed(final_state["messages"]) if m.type == "ai"),
            None,
        )
        return (
            last_ai_message.content if last_ai_message else "Sem resposta."
        )

    async def stream_message(
        self, session_id: str, user_message: str
    ):
        logger.info(f"[{session_id}] Processando: {user_message[:60]}...")

        initial_state: AgentState = {
            "messages": [HumanMessage(content=user_message)],
            "retrieved_context": [],
            "tool_to_call": None,
            "tool_args": {},
            "tool_result": None,
            "session_id": session_id,
        }

        final_state = await agent_graph.ainvoke(initial_state)

        last_ai_message = next(
            (m for m in reversed(final_state["messages"]) if m.type == "ai"),
            None,
        )
        yield last_ai_message.content if last_ai_message else "Sem resposta."
