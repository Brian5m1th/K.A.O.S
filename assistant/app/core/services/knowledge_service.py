"""
KnowledgeService — Unified knowledge coalescing orchestrator.

Combines Graph, Memory, and Retrieval services into a single
high-level knowledge query interface. This is the service that
powers the "Knowledge Query" feature in the Desktop.

Example Desktop flow:
    User: "How does OllamaProvider connect to LLMFactory?"
    Desktop: POST /api/knowledge/query { text: "..." }
    KnowledgeService:
      1. GraphService.explain("OllamaProvider")  → code structure
      2. RetrievalService.search("ollama")       → semantic docs
      3. MemoryService.search("ollama config")   → user preferences
      4. Assembles unified response
"""

from loguru import logger
from app.domain.ports.graph_port import GraphQuery


class KnowledgeService:
    """High-level service that coalesces multiple knowledge sources."""

    def __init__(
        self,
        graph_service=None,
        memory_service=None,
        retrieval_service=None,
    ):
        self._graph = graph_service
        self._memory = memory_service
        self._retrieval = retrieval_service

    async def query(self, text: str, include_sources: list[str] | None = None) -> dict:
        """Coalescing query across all knowledge sources."""
        if include_sources is None:
            include_sources = ["graph", "retrieval", "memory"]

        results = {}

        if "graph" in include_sources and self._graph:
            try:
                results["graph"] = await self._graph.query(
                    GraphQuery(text=text, max_depth=2)
                )
            except Exception as e:
                logger.warning(f"[knowledge] Graph query failed: {e}")
                results["graph"] = None

        if "retrieval" in include_sources and self._retrieval:
            try:
                from app.domain.ports.retrieval_port import RetrievalQuery

                results["retrieval"] = await self._retrieval.search(
                    RetrievalQuery(text=text, max_results=5)
                )
            except Exception as e:
                logger.warning(f"[knowledge] Retrieval query failed: {e}")
                results["retrieval"] = []

        if "memory" in include_sources and self._memory:
            try:
                from app.domain.ports.memory_port import MemoryQuery

                results["memory"] = await self._memory.search(
                    MemoryQuery(text=text, max_results=3)
                )
            except Exception as e:
                logger.warning(f"[knowledge] Memory query failed: {e}")
                results["memory"] = []

        return {
            "query": text,
            "sources_queried": include_sources,
            "results": results,
        }

    async def health(self) -> dict:
        return {
            "service": "knowledge",
            "graph": await self._graph.health() if self._graph else None,
            "memory": await self._memory.health() if self._memory else None,
            "retrieval": await self._retrieval.health() if self._retrieval else None,
        }
