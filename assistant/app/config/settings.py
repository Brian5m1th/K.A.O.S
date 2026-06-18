from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    APP_NAME: str = "K.A.O.S"
    APP_ENV: str = "development"
    APP_PORT: int = 8000
    LOG_LEVEL: str = "INFO"

    OBSIDIAN_VAULT_PATH: str = ""
    OBSIDIAN_WIKI_PATH: str = ""
    OBSIDIAN_RAW_PATH: str = ""

    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen3:14b"
    OLLAMA_FAST_MODEL: str = "qwen3:4b"
    API_MODEL_ID: str = "kaos-rag"
    FAST_MODEL_ID: str = "kaos-fast"
    DEFAULT_MODEL_ID: str = "kaos"

    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "obsidian_memory"

    DATABASE_URL: str = "postgresql://user:password@localhost:5432/kaos"

    HF_TOKEN: str = ""

    RAG_SCORE_THRESHOLD: float = 0.3
    RAG_DEFAULT_LIMIT: int = 5

    EMBEDDING_MODEL_DEV: str = "nomic-embed-text"
    EMBEDDING_MODEL_PROD: str = "BAAI/bge-m3"
    EMBEDDING_BATCH_SIZE: int = 64

    @property
    def embedding_model(self) -> str:
        return self.EMBEDDING_MODEL_DEV if self.APP_ENV == "development" else self.EMBEDDING_MODEL_PROD

    def model_post_init(self, __context) -> None:
        if self.OBSIDIAN_VAULT_PATH:
            vault = Path(self.OBSIDIAN_VAULT_PATH)
            if not self.OBSIDIAN_WIKI_PATH:
                self.OBSIDIAN_WIKI_PATH = str(vault / "wiki")
            if not self.OBSIDIAN_RAW_PATH:
                self.OBSIDIAN_RAW_PATH = str(vault / "raw")


settings = Settings()
