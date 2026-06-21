from loguru import logger

from app.providers.base.embedding import BaseEmbeddingProvider
from app.rag.embeddings.embedder import get_embedder


class BgeEmbeddingProvider(BaseEmbeddingProvider):
    provider_name = "bge"

    def __init__(self, model_key: str | None = None):
        self._embedder = get_embedder(model_key)

    async def embed(self, text: str) -> list[float]:
        logger.info("[start] BgeEmbeddingProvider - embed")
        result = self._embedder.embed_single(text)
        logger.debug("[finish] BgeEmbeddingProvider - embed")
        return result

    async def embed_batch(self, texts: list[str]) -> list[list[float]]:
        logger.info(f"[start] BgeEmbeddingProvider - embed_batch size={len(texts)}")
        result = self._embedder.embed_batch(texts)
        logger.debug("[finish] BgeEmbeddingProvider - embed_batch")
        return result

    async def healthcheck(self) -> bool:
        try:
            self._embedder.embed_single("healthcheck")
            return True
        except Exception:
            return False
