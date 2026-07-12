"""
GraphRAG Experiment — Hybrid Graph + Vector Retrieval.

Combines Graphify's code knowledge graph with Qdrant's vector search
to provide context-aware retrieval that understands code structure.

H3 2026 Experiment: Tests whether adding graph traversal context
improves RAG relevance for code-related queries.
"""

import time
from dataclasses import dataclass
from typing import Optional

from loguru import logger

from app.config.settings import settings
from app.rag.embeddings.embedder import get_embedder
from app.rag.retriever.semantic import SemanticRetriever


@dataclass
class GraphRAGResult:
    """Combined graph + vector retrieval result."""

    text: str
    score: float
    source: str
    graph_context: Optional[str] = None
    chunk_id: str = ""
    path: str = ""


class GraphRAGExperiment:
    """Experimental GraphRAG pipeline — combines graph + vector context."""

    def __init__(self) -> None:
        self._retriever = SemanticRetriever()
        self._embedder = get_embedder()
        self._graph_path = settings.get("GRAPHIFY_OUT", "graphify-out/graph.json")
        self._enabled = (
            self._graph_path.exists() if hasattr(self._graph_path, "exists") else False
        )

    async def retrieve(
        self,
        query: str,
        max_results: int = 5,
        include_graph: bool = True,
    ) -> list[GraphRAGResult]:
        """Retrieve context using hybrid graph+vector approach.

        Args:
            query: User query text.
            max_results: Maximum results to return.
            include_graph: Whether to include graph context.

        Returns:
            List of GraphRAGResult with combined context.
        """
        t0 = time.monotonic()

        # 1. Vector retrieval (semantic)
        vector_results = await self._retriever.retrieve(
            query=query,
            k=max_results,
        )

        results = []
        for vr in vector_results:
            graph_ctx = None
            if include_graph and self._enabled:
                graph_ctx = self._get_graph_context(vr.get("source", ""))

            results.append(
                GraphRAGResult(
                    text=vr.get("content", vr.get("text", "")),
                    score=vr.get("score", 0.0),
                    source=vr.get("source", vr.get("path", "")),
                    graph_context=graph_ctx,
                    chunk_id=vr.get("chunk_id", ""),
                    path=vr.get("path", ""),
                )
            )

        elapsed = (time.monotonic() - t0) * 1000
        logger.info(
            "[graphrag] retrieved {} results in {:.0f}ms (graph={})",
            len(results),
            elapsed,
            include_graph,
        )
        return results

    def _get_graph_context(self, source_file: str) -> Optional[str]:
        """Get graph context for a source file from the knowledge graph."""
        try:
            import json

            if not self._graph_path.exists():
                return None

            with open(self._graph_path) as f:
                graph = json.load(f)

            # Find nodes related to this file
            related = []
            for node in graph.get("nodes", []):
                if source_file in str(node.get("file", "")):
                    related.append(node.get("label", node.get("id", "")))

            if related:
                return f"Related code symbols: {', '.join(related[:10])}"
        except Exception as exc:
            logger.debug("[graphrag] graph context failed: {}", exc)

        return None

    @staticmethod
    async def benchmark(queries: list[str]) -> dict:
        """Run a benchmark comparing RAG vs GraphRAG relevance."""
        experiment = GraphRAGExperiment()
        results = {
            "rag": {"total": 0, "avg_score": 0.0, "avg_time_ms": 0.0},
            "graphrag": {"total": 0, "avg_score": 0.0, "avg_time_ms": 0.0},
        }

        for query in queries:
            # RAG only
            t0 = time.monotonic()
            rag_results = await experiment.retrieve(query, include_graph=False)
            rag_time = (time.monotonic() - t0) * 1000

            # GraphRAG
            t0 = time.monotonic()
            graphrag_results = await experiment.retrieve(query, include_graph=True)
            graphrag_time = (time.monotonic() - t0) * 1000

            results["rag"]["total"] += len(rag_results)
            results["rag"]["avg_score"] += (
                sum(r.score for r in rag_results) if rag_results else 0
            )
            results["rag"]["avg_time_ms"] += rag_time

            results["graphrag"]["total"] += len(graphrag_results)
            results["graphrag"]["avg_score"] += (
                sum(r.score for r in graphrag_results) if graphrag_results else 0
            )
            results["graphrag"]["avg_time_ms"] += graphrag_time

        n = len(queries)
        if n > 0:
            results["rag"]["avg_score"] = round(results["rag"]["avg_score"] / n, 3)
            results["rag"]["avg_time_ms"] = round(results["rag"]["avg_time_ms"] / n, 1)
            results["graphrag"]["avg_score"] = round(
                results["graphrag"]["avg_score"] / n, 3
            )
            results["graphrag"]["avg_time_ms"] = round(
                results["graphrag"]["avg_time_ms"] / n, 1
            )

        return results
