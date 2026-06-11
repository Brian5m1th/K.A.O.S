from loguru import logger


class Embedder:
    MODEL_CONFIGS = {
        "bge-m3": {"name": "BAAI/bge-m3", "dim": 1024},
        "nomic": {"name": "nomic-ai/nomic-embed-text-v1.5", "dim": 768},
    }

    def __init__(self, model_key: str = "bge-m3") -> None:
        from sentence_transformers import SentenceTransformer

        config = self.MODEL_CONFIGS[model_key]
        self._dim = config["dim"]
        logger.info(f"Carregando modelo de embedding: {config['name']}")
        self._model = SentenceTransformer(config["name"], trust_remote_code=True)

    @property
    def dimension(self) -> int:
        return self._dim

    def embed(self, texts: list[str]) -> list[list[float]]:
        vectors = self._model.encode(texts, normalize_embeddings=True)
        return vectors.tolist()

    def embed_single(self, text: str) -> list[float]:
        return self.embed([text])[0]
