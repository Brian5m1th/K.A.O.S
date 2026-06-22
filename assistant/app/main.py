import asyncio
import logging
import sys
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from prometheus_fastapi_instrumentator import Instrumentator

import uuid
from pathlib import Path

from app.api.auth import router as auth_router
from app.api.capabilities import router as capabilities_router
from app.api.chat import router as chat_router
from app.api.feature_flags import router as feature_flags_router
from app.api.health import router as health_router
from app.api.indexing import router as indexing_router
from app.api.models import router as models_router
from app.api.openai import router as openai_router, legacy_router
from app.api.orchestrator import router as orchestrator_router
from app.api.provider_configs import router as provider_configs_router
from app.api.rag import router as rag_router
from app.api.setup import router as setup_router
from app.api.user_model_profiles import router as user_model_profiles_router
from app.api.users import router as users_router
from app.api.webhooks import router as webhooks_router
from app.api.apps_api import router as apps_router
from app.api.notifications import router as notifications_router
from app.api.audit import router as audit_router
from app.api.architecture import router as architecture_router
from app.config.settings import settings
from app.middleware.auth import ApiKeyMiddleware
from app.middleware.user_context import UserContextMiddleware
from app.observability.cost_tracker import CostTracker
from app.observability.event_bus import EventBus
from app.observability.subscribers.audit_subscriber import AuditSubscriber
from app.observability.subscribers.logger_subscriber import LoggerSubscriber
from app.observability.subscribers.metrics_subscriber import MetricsSubscriber
from app.observability.subscribers.n8n_subscriber import N8NSubscriber
from app.observability.tracing import TracingSubscriber, setup_tracing
from app.obsidian.vault_init import create_vault_structure
from app.obsidian.watcher.vault_watcher import VaultWatcher
from app.audit.drift_subscriber import DriftSubscriber, AuditScheduler
from app.audit.sdd_watcher import SDDWatcher

import json


def configure_logging(log_level: str, env: str) -> None:
    logger.remove()

    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

    logger.add(
        sys.stdout,
        level=log_level,
        format=log_format,
        colorize=True,
    )

    if env == "production":
        log_dir = Path("logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / "kaos-api.json"

        def json_sink(message):
            record = message.record
            log_entry = {
                "timestamp": record["time"].isoformat(),
                "level": record["level"].name,
                "logger": record["name"],
                "function": record["function"],
                "line": record["line"],
                "message": record["message"],
                "extra": record["extra"],
            }
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

        logger.add(json_sink, level=log_level, format="{message}", serialize=False)

    class InterceptHandler(logging.Handler):
        def emit(self, record: logging.LogRecord) -> None:
            logger.opt(depth=6, exception=record.exc_info).log(
                record.levelname, record.getMessage()
            )

    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)


configure_logging(settings.LOG_LEVEL, settings.APP_ENV)

_watcher: VaultWatcher | None = None

_embedder_ready = False
_tools_registered = False


def _init_api_key(key_path: Path) -> str:
    if settings.API_KEY:
        key = settings.API_KEY
        key_path.parent.mkdir(parents=True, exist_ok=True)
        key_path.write_text(key)
        logger.info("[auth] API key loaded from env")
        return key
    if key_path.exists():
        key = key_path.read_text().strip()
        logger.info("[auth] API key loaded from {}", key_path)
        return key
    key = uuid.uuid4().hex
    key_path.parent.mkdir(parents=True, exist_ok=True)
    key_path.write_text(key)
    logger.info("[auth] API key generated and saved to {}", key_path)
    return key


def _register_tools():
    global _tools_registered
    if not _tools_registered:
        from app.tools.github_tools import register_github_tools

        register_github_tools()
        _tools_registered = True


def _register_observability(app_state) -> None:
    logger_subscriber = LoggerSubscriber()
    metrics_subscriber = MetricsSubscriber()
    audit_subscriber = AuditSubscriber()
    cost_tracker = CostTracker()
    tracing_subscriber = TracingSubscriber()
    for name in (
        "request_started",
        "intent_classified",
        "model_selected",
        "workflow_started",
        "workflow_completed",
        "workflow_step",
        "llm_request",
        "llm_response",
        "fallback_triggered",
        "request_completed",
        "error",
        "orchestrator.execution_started",
        "orchestrator.execution_completed",
        "orchestrator.execution_failed",
        "memory.write.started",
        "memory.write.completed",
        "memory.write.failed",
        "memory.read.started",
        "memory.read.completed",
        "memory.deleted",
        "conversation.summarized",
        "conversation.stored",
    ):
        EventBus.subscribe(name, logger_subscriber)
    for name in (
        "workflow_started",
        "workflow_completed",
        "orchestrator.execution_failed",
        "llm_request",
    ):
        EventBus.subscribe(name, metrics_subscriber)
    for name in (
        "orchestrator.execution_started",
        "orchestrator.execution_completed",
        "orchestrator.execution_failed",
    ):
        EventBus.subscribe(name, audit_subscriber)
    for name in (
        "llm_request",
        "llm_response",
        "workflow_started",
        "workflow_completed",
    ):
        EventBus.subscribe(name, cost_tracker)
    for name in (
        "workflow_started",
        "workflow_completed",
        "llm_request",
        "llm_response",
        "orchestrator.execution_started",
        "orchestrator.execution_completed",
        "orchestrator.execution_failed",
    ):
        EventBus.subscribe(name, tracing_subscriber)

    if settings.N8N_WEBHOOK_URL:
        n8n_subscriber = N8NSubscriber()
        for event_name in EventBus._subscribers:
            EventBus.subscribe(event_name, n8n_subscriber)
        logger.info(
            f"[observability] N8N subscriber registered (webhook: {settings.N8N_WEBHOOK_URL})"
        )

    setup_tracing(
        service_name=settings.APP_NAME,
        endpoint="",
    )

    app_state.cost_tracker = cost_tracker
    logger.info("[observability] subscribers registered")


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    global _watcher, _embedder_ready
    logger.info("[start] {} - modo {}", settings.APP_NAME, settings.APP_ENV)
    _app.state.api_key = _init_api_key(Path("data/api_key.txt"))
    logger.info("[auth] API key: {}", _app.state.api_key)

    _register_observability(_app.state)

    drift_subscriber = DriftSubscriber()
    for event_name in ("audit.started", "audit.completed", "drift.detected"):
        EventBus.subscribe(event_name, drift_subscriber)
    logger.info("[kirl] drift subscriber registered")

    asyncio.create_task(AuditScheduler.run_periodic_audit())
    logger.info("[kirl] periodic audit scheduler started")

    logger.bind(
        app=settings.APP_NAME,
        env=settings.APP_ENV,
        log_level=settings.LOG_LEVEL,
        ollama_base=settings.OLLAMA_BASE_URL,
        qdrant_host=settings.QDRANT_HOST,
        database_url=settings.DATABASE_URL.split("@")[-1]
        if "@" in settings.DATABASE_URL
        else "local",
    ).info("startup")

    _register_tools()

    async def _warmup():
        global _embedder_ready
        from app.rag.embeddings.embedder import warmup_embedder

        logger.info("[info] lifespan - warmup embedder")
        await asyncio.to_thread(warmup_embedder)
        _embedder_ready = True
        logger.debug("[finish] lifespan - warmup embedder")

    async def _init_vault():
        logger.info("[info] lifespan - init vault structure")
        await asyncio.to_thread(create_vault_structure)
        logger.debug("[finish] lifespan - init vault structure")

    await asyncio.gather(_warmup(), _init_vault())

    _watcher = VaultWatcher()
    _watcher.start()

    asyncio.create_task(SDDWatcher.start())
    logger.info("[kirl] SDD watcher started")

    yield
    if _watcher:
        _watcher.stop()
    SDDWatcher.stop()
    logger.debug("[finish] {} - encerrado", settings.APP_NAME)


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

app.add_middleware(ApiKeyMiddleware)
app.add_middleware(UserContextMiddleware)

app.include_router(auth_router)
app.include_router(capabilities_router)
app.include_router(chat_router)
app.include_router(feature_flags_router)
app.include_router(health_router)
app.include_router(indexing_router)
app.include_router(models_router)
app.include_router(openai_router)
app.include_router(legacy_router)
app.include_router(orchestrator_router)
app.include_router(provider_configs_router)
app.include_router(rag_router)
app.include_router(setup_router)
app.include_router(user_model_profiles_router)
app.include_router(users_router)
app.include_router(webhooks_router)
app.include_router(apps_router)
app.include_router(notifications_router)
app.include_router(audit_router)
app.include_router(architecture_router)

Instrumentator(
    excluded_handlers=[".*health.*", "/metrics"],
).instrument(app).expose(app)


@app.get("/")
async def root() -> dict:
    return {
        "name": settings.APP_NAME,
        "version": "0.1.0",
        "status": "running",
        "embedder_ready": _embedder_ready,
        "endpoints": {
            "health": "/health",
            "chat": "/api/chat/message",
            "openai": "/v1/chat/completions",
            "models": "/v1/models",
            "indexing": "/indexing/full",
            "init_folders": "/indexing/init-folders",
            "rag_context": "/rag/context",
            "orchestrator": "/api/orchestrator/execute",
            "setup_provider": "/api/setup/provider",
        },
    }
