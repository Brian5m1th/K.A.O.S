import time
from langchain_core.messages import HumanMessage
from loguru import logger

from app.agent.graph import agent_graph
from app.agent.state import AgentState


class AgentService:
    async def process_message(
        self, session_id: str, user_message: str, user_id: str = "", username: str = "", role: str = "user", model: str | None = None, ingest_source_path: str | None = None
    ) -> str:
        start = time.perf_counter()
        logger.info("[start] AgentService - process_message")
        logger.info(f"[info] AgentService - sessao {session_id} [user={user_id}]")

        initial_state: AgentState = {
            "messages": [HumanMessage(content=user_message)],
            "retrieved_context": [],
            "tool_to_call": None,
            "tool_args": {},
            "tool_result": None,
            "session_id": session_id,
            "user_id": user_id,
            "username": username,
            "role": role,
            "model": model,
            "ingest_source_path": ingest_source_path,
        }

        final_state = await agent_graph.ainvoke(initial_state)

        last_ai_message = next(
            (m for m in reversed(final_state["messages"]) if m.type == "ai"),
            None,
        )
        result = last_ai_message.content if last_ai_message else "Sem resposta."
        
        elapsed = (time.perf_counter() - start) * 1000
        context = initial_state.get("retrieved_context", [])
        context_chars = sum(len(c.get("content", "")) for c in context)
        logger.info(
            f"[audit] generation | route=SMART | user={user_id} | "
            f"context_chunks={len(context)} | context_chars={context_chars} | "
            f"tokens_out=~{len(result)//4} | latency_ms={elapsed:.0f}"
        )
        logger.debug("[finish] AgentService - process_message")
        return result

    async def stream_message(
        self, session_id: str, user_message: str, user_id: str = "", username: str = "", role: str = "user", model: str | None = None, ingest_source_path: str | None = None
    ):
        start = time.perf_counter()
        logger.info("[start] AgentService - stream_message")
        logger.info(f"[info] AgentService - sessao {session_id} [user={user_id}]")

        initial_state: AgentState = {
            "messages": [HumanMessage(content=user_message)],
            "retrieved_context": [],
            "tool_to_call": None,
            "tool_args": {},
            "tool_result": None,
            "session_id": session_id,
            "user_id": user_id,
            "username": username,
            "role": role,
            "model": model,
            "ingest_source_path": ingest_source_path,
        }

        result_parts = []
        async for event in agent_graph.astream_events(
            initial_state, version="v2"
        ):
            kind = event.get("event")
            if kind == "on_chat_model_stream":
                chunk = event.get("data", {}).get("chunk", None)
                if chunk is not None:
                    content = chunk.content
                    if content:
                        result_parts.append(content)
                        yield content

        elapsed = (time.perf_counter() - start) * 1000
        result = "".join(result_parts)
        context = initial_state.get("retrieved_context", [])
        context_chars = sum(len(c.get("content", "")) for c in context)
        logger.info(
            f"[audit] generation | route=SMART | user={user_id} | "
            f"context_chunks={len(initial_state['retrieved_context'])} | context_chars={context_chars} | "
            f"tokens_out=~{len(result)//4} | latency_ms={elapsed:.0f}"
        )
        logger.debug("[finish] AgentService - stream_message")
