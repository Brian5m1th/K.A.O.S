from typing import AsyncIterator
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
        results = self._retriever.search(query=query, limit=5)
        if not results:
            return ""
        return "\n\n".join(
            f"[{r.path} (score={r.score:.2f})]\n{r.excerpt}"
            for r in results
        )

    async def process(self, user_message: str) -> str:
        logger.info("[start] MemoryRouter - process")
        context = await self.retrieve_context(user_message)
        system = MEMORY_SYSTEM_PROMPT
        if context:
            system += f"\n\nContexto do Vault:\n{context}"
        messages = [
            SystemMessage(content=system),
            HumanMessage(content=user_message),
        ]
        response = await self._llm.ainvoke(messages)
        logger.debug("[finish] MemoryRouter - process")
        return response.content

    async def stream(self, user_message: str) -> AsyncIterator[str]:
        logger.info("[start] MemoryRouter - stream")
        context = await self.retrieve_context(user_message)
        system = MEMORY_SYSTEM_PROMPT
        if context:
            system += f"\n\nContexto do Vault:\n{context}"
        messages = [
            SystemMessage(content=system),
            HumanMessage(content=user_message),
        ]
        async for chunk in self._llm.astream(messages):
            if chunk.content:
                yield chunk.content
        logger.debug("[finish] MemoryRouter - stream")