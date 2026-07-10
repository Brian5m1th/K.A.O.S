import asyncio
import logging
import sys
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
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
from app.api.providers import router as providers_router
from app.api.system import router as system_router
from app.api.prompts import router as prompts_router
from app.api.agents_api import router as agents_api_router
from app.api.observability import router as observability_router
from app.api.opencode import router as opencode_router
from app.api.admin import router as admin_router
from app.api.conversations import router as conversations_router
from app.api.kirl import router as kirl_router
from app.api.docs import router as docs_router
from app.api.settings_api import router as settings_api_router
from app.api.integrations import router as integrations_router
from app.api.mcp import router as mcp_router
from app.api.automation import router as automation_router
from app.api.plugins import router as plugins_router
from app.api.workspace_intelligence import router as workspace_intelligence_router
from app.api.opencode import set_watcher as set_opencode_watcher
from app.core.opencode_watcher import OpenCodeWatcher
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
from app.obsidian.watcher.vault_watcher import VaultWatcher
from app.audit.drift_subscriber import DriftSubscriber, AuditScheduler

# Ensure SQLAlchemy models are registered with Base.metadata before create_tables()
import app.models  # noqa: F401
from app.audit.sdd_watcher import SDDWatcher
from app.core.knowledge_graph_watcher import KnowledgeGraphWatcher
import json


def configure_logging(log_level: str, env: str) -> None:
    logger.remove()

    def patch_log(record):
        try:
            from app.middleware.user_context import user_id_context

            uid = user_id_context.get() or "anonymous"
        except ImportError:
            uid = "anonymous"
        record["extra"]["user_id"] = uid

    logger.configure(patcher=patch_log)

    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <magenta>[user={extra[user_id]}]</magenta> - <level>{message}</level>"

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
    for logger_name in ("httpx", "httpcore", "urllib3"):
        logging.getLogger(logger_name).setLevel(logging.WARNING)


configure_logging(settings.LOG_LEVEL, settings.APP_ENV)

_watcher: VaultWatcher | None = None
_opencode_watcher: OpenCodeWatcher | None = None
_kg_watcher: KnowledgeGraphWatcher | None = None

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
        from app.tools.n8n_webhook_tool import register_n8n_webhook

        register_github_tools()
        register_n8n_webhook()
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
        for event_name in settings.N8N_EVENTS:
            EventBus.subscribe(event_name, n8n_subscriber)
        logger.info(
            f"[observability] N8N subscriber registered (webhook: {settings.N8N_WEBHOOK_URL}, "
            f"events: {settings.N8N_EVENTS})"
        )

    setup_tracing(
        service_name=settings.APP_NAME,
        endpoint="",
    )

    app_state.cost_tracker = cost_tracker
    logger.info("[observability] subscribers registered")


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    global _watcher, _opencode_watcher, _kg_watcher, _embedder_ready
    logger.info("[start] {} - modo {}", settings.APP_NAME, settings.APP_ENV)

    # ── Capability Registry Autodiscover ─────────────────────────────────
    from app.capability.registry import CapabilityRegistry

    base_dir = Path(__file__).parent / "capabilities"
    CapabilityRegistry.autodiscover(base_dir)

    # ── Bootstrap Manager: pipeline completo de inicializacao ─────────────
    from app.core.bootstrap_manager import BootstrapManager

    bootstrap_result = await BootstrapManager.boot()
    _app.state.bootstrap = bootstrap_result

    _app.state.api_key = _init_api_key(Path("data/api_key.txt"))
    logger.info(
        "[auth] API key: {}***{}",
        _app.state.api_key[:4] if _app.state.api_key else "",
        _app.state.api_key[-4:] if _app.state.api_key else "",
    )

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

    # Register MCP tools in the LangGraph TOOL_REGISTRY (RF-C03 bridge)
    try:
        from app.tools.mcp_adapter import register_all_mcp_tools

        mcp_count = register_all_mcp_tools()
        logger.info("[mcp] {} MCP tools registradas no TOOL_REGISTRY", mcp_count)
    except Exception as exc:
        logger.warning("[mcp] falha ao registrar MCP tools no startup: {}", exc)

    async def _warmup():
        global _embedder_ready
        from app.rag.embeddings.embedder import warmup_embedder

        logger.info("[info] lifespan - warmup embedder")
        await asyncio.to_thread(warmup_embedder)
        _embedder_ready = True
        logger.debug("[finish] lifespan - warmup embedder")

    await _warmup()

    _watcher = VaultWatcher()
    _watcher.start()

    _opencode_watcher = OpenCodeWatcher()
    _opencode_watcher.start()
    set_opencode_watcher(_opencode_watcher)
    logger.info(
        "[opencode] watcher {} started",
        " (fallback mode)" if _opencode_watcher.is_fallback_mode() else "",
    )

    asyncio.create_task(SDDWatcher.start())
    logger.info("[kirl] SDD watcher started")

    # Start Knowledge Graph file watcher (incremental updates apos bootstrap)
    _kg_watcher = KnowledgeGraphWatcher()
    _kg_watcher.start()

    # Start Automation Engine Bus worker and auto-import templates
    try:
        from app.core.automation_bus import AutomationBus

        await AutomationBus.start_worker()
        asyncio.create_task(AutomationBus.auto_import_workflows())
        logger.info(
            "[automation] Automation Engine Bus worker started and auto-importer scheduled"
        )
    except Exception as exc:
        logger.warning("[automation] Failed to initialize automation engine: {}", exc)

    # Log all registered routes for debugging
    logger.info("[routes] Registered routes:")
    for route in _app.routes:
        methods = getattr(route, "methods", None)
        logger.info(f"[routes] Path: {route.path} | Methods: {methods}")

    # Se bootstrap falhou, logar estado
    if not bootstrap_result.is_ready:
        logger.warning(
            "[boot] Backend iniciou em estado {} com {} erros",
            bootstrap_result.state.value,
            len(bootstrap_result.errors),
        )
        for err in bootstrap_result.errors:
            logger.warning("[boot]   - {}", err)

    yield
    if _watcher:
        _watcher.stop()
    if _opencode_watcher:
        _opencode_watcher.stop()
    if _kg_watcher:
        _kg_watcher.stop()
    SDDWatcher.stop()
    try:
        from app.core.automation_bus import AutomationBus

        asyncio.run(AutomationBus.stop_worker())
    except Exception:
        pass
    logger.debug("[finish] {} - encerrado", settings.APP_NAME)


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(ApiKeyMiddleware)
app.add_middleware(UserContextMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=[
        "Authorization",
        "Content-Type",
        "X-API-Key",
        "X-User-Id",
        "X-Username",
        "X-User-Role",
    ],
)

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
app.include_router(providers_router)
app.include_router(system_router)
app.include_router(observability_router)
app.include_router(opencode_router)
app.include_router(admin_router)
app.include_router(settings_api_router)
app.include_router(integrations_router)
app.include_router(mcp_router)
app.include_router(conversations_router)
app.include_router(kirl_router)
app.include_router(docs_router)
app.include_router(automation_router)
app.include_router(prompts_router)
app.include_router(agents_api_router)
app.include_router(plugins_router)
app.include_router(workspace_intelligence_router)

# Serve workflow templates como static assets para o Marketplace
workflows_static = Path("data/workflows")
if workflows_static.exists():
    app.mount(
        "/workflows", StaticFiles(directory=str(workflows_static)), name="workflows"
    )
    logger.info(
        "[main] Workflow templates mounted at /workflows from {}",
        workflows_static.resolve(),
    )

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
