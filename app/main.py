import logging
import sys
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.config.settings import settings


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


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    logger.info(f"{settings.APP_NAME} iniciado em modo {settings.APP_ENV}")
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(chat_router)
