import logging
import sys
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.api.indexing import router as indexing_router
from app.api.openai import router as openai_router, legacy_router
from app.api.rag import router as rag_router
from app.config.settings import settings
from app.obsidian.watcher.vault_watcher import VaultWatcher


def configure_logging(log_level: str) -> None:
    logger.remove()
    logger.add(
        sys.stdout,
        level=log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        colorize=True,
    )

    class InterceptHandler(logging.Handler):
        def emit(self, record: logging.LogRecord) -> None:
            logger.opt(depth=6, exception=record.exc_info).log(
                record.levelname, record.getMessage()
            )

    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)


configure_logging(settings.LOG_LEVEL)

_watcher: VaultWatcher | None = None


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    global _watcher
    logger.info(f"[start] {settings.APP_NAME} - modo {settings.APP_ENV}")
    _watcher = VaultWatcher()
    _watcher.start()
    yield
    if _watcher:
        _watcher.stop()
    logger.debug(f"[finish] {settings.APP_NAME} - encerrado")


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(indexing_router)
app.include_router(rag_router)
app.include_router(openai_router)
app.include_router(legacy_router)


@app.get("/")
async def root() -> dict:
    return {
        "name": settings.APP_NAME,
        "version": "0.1.0",
        "status": "running",
        "endpoints": {
            "health": "/health",
            "chat": "/api/chat/message",
            "openai": "/v1/chat/completions",
            "models": "/v1/models",
            "indexing": "/indexing/full",
            "rag_context": "/rag/context",
        },
    }
