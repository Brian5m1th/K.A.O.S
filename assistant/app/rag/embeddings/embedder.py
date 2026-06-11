from loguru import logger
from app.config.settings import settings

_embedder_instance: "Embedder | None" = None


class Embedder:
    MODEL_CONFIGS = {
        "bge-m3": {"name": "BAAI/bge-m3", "dim": 1024},
        "nomic": {"name": "nomic-ai/nomic-embed-text-v1.5", "dim": 768},
    }

    def __init__(self, model_key: str = "bge-m3") -> None:
        logger.info("[start] Embedder - __init__")
        if settings.HF_TOKEN:
            from huggingface_hub import login
            login(token=settings.HF_TOKEN)
            logger.info("[info] Embedder - HF_TOKEN configurado")
        else:
            logger.warning("[warn] Embedder - HF_TOKEN nao configurado no .env")

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


def get_embedder(model_key: str = "bge-m3") -> Embedder:
    global _embedder_instance
    if _embedder_instance is None:
        _embedder_instance = Embedder(model_key)
    return _embedder_instance


def warmup_embedder(model_key: str = "bge-m3") -> None:
    embedder = get_embedder(model_key)
    logger.info("[info] Embedder - warmup")
    _ = embedder.embed_single("warmup")
    logger.debug("[finish] Embedder - warmup")
