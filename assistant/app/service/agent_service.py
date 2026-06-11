from langchain_core.messages import HumanMessage
from loguru import logger

from app.agent.graph import agent_graph
from app.agent.state import AgentState


class AgentService:
    async def process_message(
        self, session_id: str, user_message: str
    ) -> str:
        logger.info("[start] AgentService - process_message")
        logger.info(f"[info] AgentService - sessao {session_id}")

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
        result = last_ai_message.content if last_ai_message else "Sem resposta."
        logger.debug("[finish] AgentService - process_message")
        return result

    async def stream_message(
        self, session_id: str, user_message: str
    ):
        logger.info("[start] AgentService - stream_message")
        logger.info(f"[info] AgentService - sessao {session_id}")

        initial_state: AgentState = {
            "messages": [HumanMessage(content=user_message)],
            "retrieved_context": [],
            "tool_to_call": None,
            "tool_args": {},
            "tool_result": None,
            "session_id": session_id,
        }

        async for event in agent_graph.astream_events(
            initial_state, version="v2"
        ):
            kind = event.get("event")
            if kind == "on_chat_model_stream":
                chunk = event.get("data", {}).get("chunk", None)
                if chunk is not None:
                    content = chunk.content
                    if content:
                        yield content

        logger.debug("[finish] AgentService - stream_message")
