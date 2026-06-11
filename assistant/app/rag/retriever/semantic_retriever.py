from qdrant_client import QdrantClient
from qdrant_client.models import FieldCondition, Filter, MatchValue

from app.config.settings import settings
from app.domain.document import SearchResult
from app.rag.embeddings.embedder import Embedder


class SemanticRetriever:
    def __init__(self) -> None:
        self._client = QdrantClient(
            host=settings.QDRANT_HOST, port=settings.QDRANT_PORT
        )
        self._embedder = Embedder(model_key="bge-m3")

    def search(
        self,
        query: str,
        limit: int = 5,
        folder_filter: str | None = None,
    ) -> list[SearchResult]:
        query_vector = self._embedder.embed_single(query)
        search_filter = None
        if folder_filter:
            search_filter = Filter(
                must=[
                    FieldCondition(
                        key="folder", match=MatchValue(value=folder_filter)
                    )
                ]
            )

        hits = self._client.search(
            collection_name=settings.QDRANT_COLLECTION,
            query_vector=query_vector,
            query_filter=search_filter,
            limit=limit,
        )

        return [
            SearchResult(
                path=hit.payload["path"],
                score=hit.score,
                excerpt=hit.payload["content"][:300],
            )
            for hit in hits
        ]
