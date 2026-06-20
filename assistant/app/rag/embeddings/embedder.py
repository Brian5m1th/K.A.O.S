from loguru import logger
from app.config.settings import settings

_embedder_instance: "Embedder | None" = None


class Embedder:
    MODEL_CONFIGS = {
        "bge-m3": {"name": "BAAI/bge-m3", "dim": 1024},
        "nomic-embed-text": {"name": "nomic-ai/nomic-embed-text-v1.5", "dim": 768},
    }

    def __init__(self, model_key: str | None = None) -> None:
        logger.info("[start] Embedder - __init__")
        if settings.HF_TOKEN:
            from huggingface_hub import login

            login(token=settings.HF_TOKEN)
            logger.info("[info] Embedder - HF_TOKEN configurado")
        else:
            logger.warning("[warn] Embedder - HF_TOKEN nao configurado no .env")

        from sentence_transformers import SentenceTransformer

        model_key = model_key or settings.embedding_model
        if model_key not in self.MODEL_CONFIGS:
            raise ValueError(
                f"Modelo desconhecido: {model_key}. Disponiveis: {list(self.MODEL_CONFIGS.keys())}"
            )

        config = self.MODEL_CONFIGS[model_key]
        self._dim = config["dim"]
        self._model_key = model_key

        device = self._get_device()
        logger.info(
            f"[info] Embedder - carregando modelo: {config['name']} | device={device} | dim={self._dim}"
        )
        self._model = SentenceTransformer(
            config["name"], device=device, trust_remote_code=True
        )
        logger.debug("[finish] Embedder - __init__")

    def _get_device(self) -> str:
        import torch

        if torch.cuda.is_available():
            return "cuda"
        if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            return "mps"
        return "cpu"

    @property
    def dimension(self) -> int:
        return self._dim

    @property
    def model_key(self) -> str:
        return self._model_key

    def embed(self, texts: list[str]) -> list[list[float]]:
        logger.info(f"[start] Embedder - embed batch_size={len(texts)}")
        vectors = self._model.encode(texts, normalize_embeddings=True)
        logger.debug("[finish] Embedder - embed")
        return vectors.tolist()

    def embed_single(self, text: str) -> list[float]:
        logger.info("[start] Embedder - embed_single")
        result = self.embed([text])[0]
        logger.debug("[finish] Embedder - embed_single")
        return result

    def embed_batch(
        self, texts: list[str], batch_size: int | None = None
    ) -> list[list[float]]:
        batch_size = batch_size or settings.EMBEDDING_BATCH_SIZE
        logger.info(
            f"[start] Embedder - embed_batch size={len(texts)} batch={batch_size}"
        )
        all_vectors = []
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            vectors = self._model.encode(
                batch, normalize_embeddings=True, show_progress_bar=False
            )
            all_vectors.extend(vectors.tolist())
        logger.debug("[finish] Embedder - embed_batch")
        return all_vectors


def get_embedder(model_key: str | None = None) -> Embedder:
    global _embedder_instance
    if _embedder_instance is None:
        _embedder_instance = Embedder(model_key)
    return _embedder_instance


def warmup_embedder(model_key: str | None = None) -> None:
    embedder = get_embedder(model_key)
    logger.info("[info] Embedder - warmup")
    _ = embedder.embed_single("warmup")
    logger.debug("[finish] Embedder - warmup")
