from loguru import logger


class Embedder:
    MODEL_CONFIGS = {
        "bge-m3": {"name": "BAAI/bge-m3", "dim": 1024},
        "nomic": {"name": "nomic-ai/nomic-embed-text-v1.5", "dim": 768},
    }

    def __init__(self, model_key: str = "bge-m3") -> None:
        logger.info("[start] Embedder - __init__")
        from sentence_transformers import SentenceTransformer

        config = self.MODEL_CONFIGS[model_key]
        self._dim = config["dim"]
        logger.info(f"[info] Embedder - carregando modelo: {config['name']}")
        self._model = SentenceTransformer(config["name"], trust_remote_code=True)
        logger.debug("[finish] Embedder - __init__")

    @property
    def dimension(self) -> int:
        return self._dim

    def embed(self, texts: list[str]) -> list[list[float]]:
        logger.info("[start] Embedder - embed")
        vectors = self._model.encode(texts, normalize_embeddings=True)
        logger.debug("[finish] Embedder - embed")
        return vectors.tolist()

    def embed_single(self, text: str) -> list[float]:
        logger.info("[start] Embedder - embed_single")
        result = self.embed([text])[0]
        logger.debug("[finish] Embedder - embed_single")
        return result
