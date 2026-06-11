from loguru import logger
from qdrant_client import QdrantClient
from qdrant_client.models import FieldCondition, Filter, MatchValue

from app.config.settings import settings
from app.domain.document import SearchResult
from app.rag.embeddings.embedder import Embedder


class SemanticRetriever:
    def __init__(self) -> None:
        logger.info("[start] SemanticRetriever - __init__")
        self._client = QdrantClient(
            host=settings.QDRANT_HOST, port=settings.QDRANT_PORT
        )
        self._embedder = Embedder(model_key="bge-m3")
        logger.debug("[finish] SemanticRetriever - __init__")

    def search(
        self,
        query: str,
        limit: int = 5,
        folder_filter: str | None = None,
    ) -> list[SearchResult]:
        logger.info("[start] SemanticRetriever - search")
        query_vector = self._embedder.embed_single(query)
        search_filter = None
        if folder_filter:
            logger.info(f"[info] SemanticRetriever - filtrando por pasta: {folder_filter}")
            search_filter = Filter(
                must=[
                    FieldCondition(
                        key="folder", match=MatchValue(value=folder_filter)
                    )
                ]
            )

        response = self._client.query_points(
            collection_name=settings.QDRANT_COLLECTION,
            query=query_vector,
            query_filter=search_filter,
            limit=limit,
            with_payload=True,
        )
        hits = response.points

        logger.info(f"[info] SemanticRetriever - {len(hits)} resultados")
        logger.debug("[finish] SemanticRetriever - search")
        return [
            SearchResult(
                path=hit.payload["path"],
                score=hit.score,
                excerpt=hit.payload["content"][:300],
            )
            for hit in hits
        ]
