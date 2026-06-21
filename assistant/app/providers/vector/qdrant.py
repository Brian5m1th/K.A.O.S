from loguru import logger
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    FieldCondition,
    Filter,
    MatchValue,
    PointStruct,
    VectorParams,
)

from app.config.settings import settings
from app.domain.document import SearchResult
from app.providers.base.vector_store import BaseVectorStore


class QdrantVectorStore(BaseVectorStore):
    store_name = "qdrant"

    def __init__(self, collection: str | None = None):
        self._client = QdrantClient(
            host=settings.QDRANT_HOST, port=settings.QDRANT_PORT
        )
        self._collection = collection or settings.QDRANT_COLLECTION
        self._embedder = None
        self._ready = False

    def _get_embedder(self):
        if self._embedder is None:
            from app.rag.embeddings.embedder import get_embedder
            self._embedder = get_embedder()
        return self._embedder

    async def _ensure_collection(self) -> None:
        if self._ready:
            return
        try:
            embedder = self._get_embedder()
            existing = [c.name for c in self._client.get_collections().collections]
            if self._collection in existing:
                collection_info = self._client.get_collection(self._collection)
                existing_dim = collection_info.config.params.vectors.size
                if existing_dim != embedder.dimension:
                    self._client.delete_collection(self._collection)
                    existing = []
            if self._collection not in existing:
                self._client.create_collection(
                    collection_name=self._collection,
                    vectors_config=VectorParams(
                        size=embedder.dimension, distance=Distance.COSINE
                    ),
                )
            self._ready = True
        except Exception:
            logger.warning("[warn] QdrantVectorStore - Qdrant unavailable, deferring init")

    async def upsert(self, collection: str, vectors: list[dict]) -> None:
        logger.info(f"[start] QdrantVectorStore - upsert collection={collection}")

        await self._ensure_collection()

        import hashlib
        points = []
        for entry in vectors:
            point_id = hashlib.md5(
                f"{entry.get('path', '')}::{entry.get('chunk_index', 0)}".encode()
            ).hexdigest()
            points.append(
                PointStruct(
                    id=point_id,
                    vector=entry["vector"],
                    payload={k: v for k, v in entry.items() if k != "vector"},
                )
            )

        self._client.upsert(collection_name=collection, points=points)
        logger.debug(f"[finish] QdrantVectorStore - upsert ({len(points)} points)")

    async def search(
        self, collection: str, query_vector: list[float], limit: int
    ) -> list[SearchResult]:
        logger.info(f"[start] QdrantVectorStore - search collection={collection} limit={limit}")

        await self._ensure_collection()

        response = self._client.query_points(
            collection_name=collection,
            query=query_vector,
            limit=limit,
            score_threshold=settings.RAG_SCORE_THRESHOLD,
            with_payload=True,
        )
        hits = response.points

        logger.debug(f"[finish] QdrantVectorStore - search ({len(hits)} results)")
        return [
            SearchResult(
                path=hit.payload.get("path", ""),
                score=hit.score,
                excerpt=hit.payload.get("content", "")[:300],
            )
            for hit in hits
        ]

    async def delete(self, collection: str, ids: list[str]) -> None:
        logger.info(f"[start] QdrantVectorStore - delete collection={collection} ids={len(ids)}")

        await self._ensure_collection()

        self._client.delete(
            collection_name=collection,
            points_selector=Filter(
                must=[
                    FieldCondition(key="path", match=MatchValue(value=pid))
                    for pid in ids
                ]
            ),
        )
        logger.debug("[finish] QdrantVectorStore - delete")

    async def healthcheck(self) -> bool:
        try:
            self._client.get_collections()
            return True
        except Exception:
            return False
