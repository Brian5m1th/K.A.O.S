from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    APP_NAME: str = "K.A.O.S"
    APP_ENV: str = "development"
    APP_PORT: int = 8000
    LOG_LEVEL: str = "INFO"

    WORKSPACE_ROOT: str = "C:/workspace/Freelancer/K.A.O.S/workspace"

    OBSIDIAN_VAULT_PATH: str = ""
    OBSIDIAN_WIKI_PATH: str = ""
    OBSIDIAN_RAW_PATH: str = ""

    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen3:14b"
    OLLAMA_FAST_MODEL: str = "qwen3:4b"
    AIRLLM_MODEL: str = "airllm-llama3-70b"
    AIRLLM_SAVING_PATH: str = ""
    API_MODEL_ID: str = "kaos-rag"
    FAST_MODEL_ID: str = "kaos-fast"
    DEFAULT_MODEL_ID: str = "kaos"

    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    GEMINI_API_KEY: str = ""

    MODEL_MAP: dict[str, dict] = {}
    FALLBACK_CHAIN: str = "ollama"

    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "obsidian_memory"

    DATABASE_URL: str = "postgresql+psycopg://user:password@localhost:5432/kaos"

    API_KEY: str = ""
    CORS_ORIGINS: list[str] = [
        "http://localhost:1420",
        "http://localhost:3000",
        "tauri://localhost",
        "http://tauri.localhost",
        "https://tauri.localhost",
    ]

    HF_TOKEN: str = ""
    N8N_WEBHOOK_URL: str = ""
    N8N_API_URL: str = "http://n8n:5678"
    N8N_EVENTS: list[str] = ["workflow_completed", "drift.detected", "vault.analysis.completed"]
    KAOS_SECRET_KEY: str = ""

    # Email (IMAP/SMTP)
    EMAIL_HOST: str = ""
    EMAIL_PORT: int = 993
    EMAIL_SMTP_PORT: int = 587
    EMAIL_USER: str = ""
    EMAIL_PASS: str = ""
    EMAIL_FROM: str = ""

    # WhatsApp (Evolution API)
    WHATSAPP_API_URL: str = ""
    WHATSAPP_API_KEY: str = ""

    AUDIT_INTERVAL_DAYS: int = 7

    RAG_SCORE_THRESHOLD: float = 0.3
    RAG_DEFAULT_LIMIT: int = 5

    EMBEDDING_MODEL_DEV: str = "nomic-embed-text"
    EMBEDDING_MODEL_PROD: str = "BAAI/bge-m3"
    EMBEDDING_BATCH_SIZE: int = 64

    @property
    def embedding_model(self) -> str:
        return (
            self.EMBEDDING_MODEL_DEV
            if self.APP_ENV == "development"
            else self.EMBEDDING_MODEL_PROD
        )

    def model_post_init(self, __context) -> None:
        if self.OBSIDIAN_VAULT_PATH:
            vault = Path(self.OBSIDIAN_VAULT_PATH)
            if not self.OBSIDIAN_WIKI_PATH:
                self.OBSIDIAN_WIKI_PATH = str(vault / "wiki")
            if not self.OBSIDIAN_RAW_PATH:
                self.OBSIDIAN_RAW_PATH = str(vault / "raw")


settings = Settings()
