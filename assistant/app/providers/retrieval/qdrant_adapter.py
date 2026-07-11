"""
QdrantAdapter — RetrievalPort implementation backed by Qdrant.

Provides semantic vector search over the 'kaos' collection.
"""

import httpx
from typing import Optional

from loguru import logger
from app.config.settings import settings
from app.domain.ports.retrieval_port import RetrievalPort, RetrievalQuery, RetrievalResult


class QdrantAdapter(RetrievalPort):
    """Vector search adapter backed by Qdrant."""

    def __init__(self):
        self._host = settings.QDRANT_HOST
        self._port = settings.QDRANT_PORT
        self._base_url = f"http://{self._host}:{self._port}"

    @property
    def provider_name(self) -> str:
        return "qdrant"

    async def search(self, query: RetrievalQuery) -> list[RetrievalResult]:
        """Search Qdrant by keywords (full vector search via Qdrant client)."""
        results = []
        try:
            # Try full Qdrant vector search
            from qdrant_client import QdrantClient
            from app.rag.embeddings.embedder import Embedder

            client = QdrantClient(host=self._host, port=self._port)
            embedder = Embedder()
            vector = await embedder.embed(query.text)

            hits = client.search(
                collection_name=query.collection,
                query_vector=vector,
                limit=query.max_results,
                score_threshold=query.score_threshold,
            )
            for hit in hits:
                results.append(RetrievalResult(
                    score=hit.score,
                    payload=hit.payload or {},
                    chunk_id=str(hit.id),
                    source_file=hit.payload.get("source", ""),
                    text=hit.payload.get("text", ""),
                ))
        except Exception as e:
            logger.warning(f"[retrieval:qdrant] Vector search failed: {e}")

        return results

    async def index(self, documents: list[dict]) -> int:
        """Index documents in Qdrant (stub — uses existing RAG pipeline)."""
        logger.info(f"[retrieval:qdrant] Index request for {len(documents)} docs (delegated to RAG pipeline)")
        return 0  # Delegated to existing VaultIndexer

    async def count(self, collection: str = "kaos") -> int:
        """Count vectors in Qdrant collection."""
        try:
            async with httpx.AsyncClient(timeout=3) as c:
                r = await c.post(
                    f"{self._base_url}/collections/{collection}/points/count",
                    json={},
                )
                if r.is_success:
                    return r.json().get("result", {}).get("count", 0)
        except Exception:
            pass
        return 0

    async def health(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=2) as c:
                r = await c.get(f"{self._base_url}/")
                return r.is_success
        except Exception:
            return False
