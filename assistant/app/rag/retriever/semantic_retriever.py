from loguru import logger
from qdrant_client import QdrantClient
from qdrant_client.models import FieldCondition, Filter, MatchValue

from app.config.settings import settings
from app.domain.document import SearchResult
from app.rag.embeddings.embedder import get_embedder


class SemanticRetriever:
    def __init__(self) -> None:
        logger.info("[start] SemanticRetriever - __init__")
        self._client = QdrantClient(
            host=settings.QDRANT_HOST, port=settings.QDRANT_PORT
        )
        self._embedder = get_embedder()
        logger.debug("[finish] SemanticRetriever - __init__")

    def search(
        self,
        query: str,
        limit: int = 5,
        folder_filter: str | None = None,
    ) -> list[SearchResult]:
        logger.info("[start] SemanticRetriever - search")
        logger.info(f"[info] SemanticRetriever - query='{query}' limit={limit} folder_filter='{folder_filter}'")
        
        try:
            query_vector = self._embedder.embed_single(query)
            logger.info(f"[info] SemanticRetriever - vector_size={len(query_vector)}")
        except Exception as e:
            logger.error(f"[error] SemanticRetriever - embed_single failed: {e}")
            raise

        search_filter = None
        if folder_filter and folder_filter.strip():
            logger.info(f"[info] SemanticRetriever - filtrando por pasta: {folder_filter}")
            search_filter = Filter(
                must=[
                    FieldCondition(
                        key="folder", match=MatchValue(value=folder_filter.strip())
                    )
                ]
            )
        else:
            logger.info("[info] SemanticRetriever - sem filtro de pasta")

        response = self._client.query_points(
            collection_name=settings.QDRANT_COLLECTION,
            query=query_vector,
            query_filter=search_filter,
            limit=limit,
            score_threshold=settings.RAG_SCORE_THRESHOLD,
            with_payload=True,
        )
        hits = response.points

        logger.info(f"[info] SemanticRetriever - raw_hits={len(hits)}")
        for i, hit in enumerate(hits[:3]):
            logger.info(
                f"[info] SemanticRetriever - hit[{i}] "
                f"score={hit.score:.4f} "
                f"path={hit.payload.get('path')} "
                f"keys={list(hit.payload.keys())}"
            )

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
