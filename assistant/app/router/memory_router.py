from typing import AsyncIterator
import time
from pathlib import Path
from loguru import logger
from langchain_core.messages import SystemMessage, HumanMessage
from app.config.settings import settings
from app.llm.factory import LLMFactory
from app.rag.retriever.semantic_retriever import SemanticRetriever

MEMORY_SYSTEM_PROMPT = """Voce e um assistente com acesso ao vault Obsidian do usuario.
Use o contexto recuperado abaixo para responder. Se o contexto nao for suficiente, informe claramente."""


class MemoryRouter:
    def __init__(self, model: str | None = None):
        logger.info("[start] MemoryRouter - __init__")
        self._retriever = SemanticRetriever()
        self._factory = LLMFactory()
        self._model_key = model or settings.API_MODEL_ID
        self._vault_path: Path | None = None
        self._wiki_cache: str | None = None
        logger.debug("[finish] MemoryRouter - __init__")

    def _get_vault_path(self) -> Path | None:
        """Retorna o caminho do vault, se configurado."""
        if self._vault_path is None:
            vault = settings.OBSIDIAN_VAULT_PATH
            if vault:
                self._vault_path = Path(vault)
        return self._vault_path

    def _search_wiki_local(self, query: str) -> str:
        """Busca no wiki local (wiki/index.md + wiki/synthesis/) antes de ir ao Qdrant.

        Implementa o padrao Wiki-First: consulta o indice local primeiro,
        que eh mais rapido e nao depende do Qdrant.
        """
        vault = self._get_vault_path()
        if not vault:
            return ""

        query_lower = query.lower()
        matches: list[str] = []
        wiki_paths = [
            vault / "wiki" / "index.md",
            vault / "wiki" / "synthesis",
        ]

        # Buscar no wiki/index.md
        index_path = wiki_paths[0]
        if index_path.exists():
            try:
                content = index_path.read_text(encoding="utf-8")
                if query_lower in content.lower():
                    idx = content.lower().index(query_lower)
                    start = max(0, idx - 100)
                    end = min(len(content), idx + 300)
                    matches.append(f"[wiki/index.md]\n{content[start:end].strip()}")
            except (OSError, UnicodeDecodeError):
                pass

        # Buscar na pasta wiki/synthesis/
        synth_path = wiki_paths[1]
        if synth_path.exists() and synth_path.is_dir():
            try:
                for f in sorted(synth_path.glob("*.md")):
                    if f.name.startswith("."):
                        continue
                    content = f.read_text(encoding="utf-8")
                    if query_lower in content.lower():
                        idx = content.lower().index(query_lower)
                        start = max(0, idx - 100)
                        end = min(len(content), idx + 300)
                        matches.append(
                            f"[{f.relative_to(vault)}]\n{content[start:end].strip()}"
                        )
                        if len(matches) >= 3:  # max 3 wiki matches
                            break
            except (OSError, UnicodeDecodeError):
                pass

        return "\n\n".join(matches)

    async def retrieve_context(self, query: str) -> str:
        start = time.perf_counter()

        # Wiki-First: buscar no wiki local primeiro
        wiki_context = self._search_wiki_local(query)

        # Se encontrou match via wiki, usar esse resultado (mais rapido)
        if wiki_context:
            elapsed = (time.perf_counter() - start) * 1000
            logger.info(
                f"[metrics] MemoryRouter - wiki_first: {elapsed:.0f}ms (wiki match)"
            )
            return wiki_context

        # Fallback para busca vetorial no Qdrant
        results = self._retriever.search(query=query, limit=5)
        elapsed = (time.perf_counter() - start) * 1000
        logger.info(
            f"[metrics] MemoryRouter - retrieve_context: {elapsed:.0f}ms results={len(results)}"
        )
        if not results:
            return ""
        return "\n\n".join(
            f"[{r.path} (score={r.score:.2f})]\n{r.excerpt}" for r in results
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
        provider = self._factory.build(self._model_key)
        response = await provider.ainvoke(messages)
        elapsed = (time.perf_counter() - start) * 1000
        logger.info(
            f"[metrics] MemoryRouter - process: {elapsed:.0f}ms context_chars={len(context)}"
        )
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
        provider = self._factory.build(self._model_key)
        async for chunk in provider.astream(messages):
            if chunk.content:
                result_parts.append(chunk.content)
                yield chunk.content
        elapsed = (time.perf_counter() - start) * 1000
        result = "".join(result_parts)
        logger.info(
            f"[audit] generation | route=MEMORY | user={user_id} | "
            f"context_chars={len(context)} | tokens_out=~{len(result) // 4} | latency_ms={elapsed:.0f}"
        )
        logger.debug("[finish] MemoryRouter - stream")
