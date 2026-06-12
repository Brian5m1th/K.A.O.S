from typing import AsyncIterator
import time
from loguru import logger
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_ollama import ChatOllama
from app.config.settings import settings
from app.rag.retriever.semantic_retriever import SemanticRetriever

MEMORY_SYSTEM_PROMPT = """Voce e um assistente com acesso ao vault Obsidian do usuario.
Use o contexto recuperado abaixo para responder. Se o contexto nao for suficiente, informe claramente."""


class MemoryRouter:
    def __init__(self):
        logger.info("[start] MemoryRouter - __init__")
        self._retriever = SemanticRetriever()
        self._llm = ChatOllama(
            model=settings.OLLAMA_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
        )
        logger.debug("[finish] MemoryRouter - __init__")

    async def retrieve_context(self, query: str) -> str:
        start = time.perf_counter()
        results = self._retriever.search(query=query, limit=5)
        elapsed = (time.perf_counter() - start) * 1000
        logger.info(f"[metrics] MemoryRouter - retrieve_context: {elapsed:.0f}ms results={len(results)}")
        if not results:
            return ""
        return "\n\n".join(
            f"[{r.path} (score={r.score:.2f})]\n{r.excerpt}"
            for r in results
        )

    async def process(self, user_message: str, user_id: str = "") -> str:
        start = time.perf_counter()
        logger.info(f"[start] MemoryRouter - process [user={user_id}]")
        context = await self.retrieve_context(user_message)
        system = MEMORY_SYSTEM_PROMPT
        if context:
            system += f"\n\nContexto do Vault:\n{context}"
        messages = [
            SystemMessage(content=system),
            HumanMessage(content=user_message),
        ]
        response = await self._llm.ainvoke(messages)
        elapsed = (time.perf_counter() - start) * 1000
        logger.info(f"[metrics] MemoryRouter - process: {elapsed:.0f}ms context_chars={len(context)}")
        logger.debug("[finish] MemoryRouter - process")
        return response.content

    async def stream(self, user_message: str, user_id: str = "") -> AsyncIterator[str]:
        start = time.perf_counter()
        logger.info(f"[start] MemoryRouter - stream [user={user_id}]")
        context = await self.retrieve_context(user_message)
        system = MEMORY_SYSTEM_PROMPT
        if context:
            system += f"\n\nContexto do Vault:\n{context}"
        messages = [
            SystemMessage(content=system),
            HumanMessage(content=user_message),
        ]
        result_parts = []
        async for chunk in self._llm.astream(messages):
            if chunk.content:
                result_parts.append(chunk.content)
                yield chunk.content
        elapsed = (time.perf_counter() - start) * 1000
        result = "".join(result_parts)
        logger.info(
            f"[audit] generation | route=MEMORY | user={user_id} | "
            f"context_chars={len(context)} | tokens_out=~{len(result)//4} | latency_ms={elapsed:.0f}"
        )
        logger.debug("[finish] MemoryRouter - stream")