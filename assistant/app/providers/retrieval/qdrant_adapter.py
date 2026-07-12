"""
QdrantAdapter — RetrievalPort implementation backed by Qdrant.

Provides semantic vector search over the 'kaos' collection.
"""

import hashlib
from pathlib import Path

import httpx

from loguru import logger
from app.config.settings import settings
from app.domain.ports.retrieval_port import (
    RetrievalPort,
    RetrievalQuery,
    RetrievalResult,
)


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
                results.append(
                    RetrievalResult(
                        score=hit.score,
                        payload=hit.payload or {},
                        chunk_id=str(hit.id),
                        source_file=hit.payload.get("source", ""),
                        text=hit.payload.get("text", ""),
                    )
                )
        except Exception as e:
            logger.warning(f"[retrieval:qdrant] Vector search failed: {e}")

        return results

    async def index(self, documents: list[dict]) -> int:
        """Index documents in Qdrant."""
        if not documents:
            return 0

        try:
            from app.rag.indexer.vault_indexer import VaultIndexer

            indexer = VaultIndexer()
            total = 0
            for doc in documents:
                file_path = doc.get("path") or doc.get("file_path", "")
                if file_path and Path(file_path).suffix == ".md":
                    total += indexer.index_file(file_path)
                else:
                    # Generic document (non-markdown) — embed and upsert directly
                    text = doc.get("text") or doc.get("content", "")
                    metadata = doc.get("metadata", {})
                    if text:
                        from qdrant_client import QdrantClient
                        from qdrant_client.models import PointStruct
                        from app.rag.embeddings.embedder import Embedder

                        embedder = Embedder()
                        vector = await embedder.embed(text)
                        point_id = hashlib.md5(text.encode()).hexdigest()
                        client = QdrantClient(host=self._host, port=self._port)
                        client.upsert(
                            collection_name="kaos",
                            points=[
                                PointStruct(
                                    id=point_id,
                                    vector=vector,
                                    payload={
                                        "text": text,
                                        "source": metadata.get("source", "api"),
                                        **metadata,
                                    },
                                )
                            ],
                        )
                        total += 1

            logger.info(
                f"[retrieval:qdrant] Indexed {total}/{len(documents)} documents"
            )
            return total
        except Exception as exc:
            logger.error(f"[retrieval:qdrant] Index failed: {exc}")
            return 0

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
        except Exception as exc:
            logger.warning(f"[retrieval:qdrant] Count failed: {exc}")
        return 0

    async def health(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=2) as c:
                r = await c.get(f"{self._base_url}/")
                return r.is_success
        except Exception:
            return False
