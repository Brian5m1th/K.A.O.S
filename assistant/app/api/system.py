import asyncio
import httpx
from fastapi import APIRouter
from loguru import logger
from app.config.settings import settings

router = APIRouter(prefix="/api/system", tags=["System"])
SERVICE_TIMEOUT = 5


async def _check(name: str, url: str) -> bool:
    try:
        async with httpx.AsyncClient(timeout=SERVICE_TIMEOUT) as c:
            r = await c.get(url)
            return r.is_success
    except Exception as e:
        logger.debug("[system] {} unavailable: {}", name, e)
        return False


async def _check_postgres() -> bool:
    try:
        from sqlalchemy import text
        from app.database import async_session_factory

        factory = async_session_factory()
        async with factory() as s:
            r = await s.execute(text("SELECT 1"))
            return r.scalar() == 1
    except Exception as e:
        logger.debug("[system] postgres: {}", e)
        return False


@router.get("/status")
async def system_status():
    q_host, q_port = settings.QDRANT_HOST, settings.QDRANT_PORT
    ollama_base = settings.OLLAMA_BASE_URL.rstrip("/")
    return {
        "backend": True,
        "qdrant": await _check("qdrant", f"http://{q_host}:{q_port}/"),
        "ollama": await _check("ollama", f"{ollama_base}/api/tags"),
        "postgres": await _check_postgres(),
        "n8n": await _check("n8n", "http://n8n:5678/healthz"),
        "grafana": await _check("grafana", "http://grafana:3000/api/health"),
        "prometheus": await _check("prometheus", "http://prometheus:9090/-/ready"),
    }


@router.get("/environment")
async def system_environment():
    """Retorna diagnostico completo do ambiente (EnvironmentService)."""
    from app.core.environment_service import EnvironmentService

    env = EnvironmentService.detect()
    return env.to_dict()


@router.get("/bootstrap")
async def system_bootstrap_state():
    """Retorna estado atual do bootstrap (BootstrapManager)."""
    from app.core.bootstrap_manager import BootstrapManager

    return BootstrapManager.get_state()


@router.get("/version")
async def system_version():
    """Retorna versao, branch e commit ativo na imagem Docker do container."""
    import os
    import socket
    import platform

    return {
        "application": "K.A.O.S API",
        "environment": os.getenv("APP_ENV", "production"),
        "branch": os.getenv("BRANCH_NAME", "main"),
        "commit": os.getenv("COMMIT_SHA", "unknown"),
        "build_date": os.getenv("BUILD_DATE", "unknown"),
        "image_tag": os.getenv("API_IMAGE_TAG", "latest"),
        "container_id": socket.gethostname(),
        "runtime_version": f"Python {platform.python_version()}",
    }


@router.get("/metrics")
async def system_metrics():
    import psutil
    import subprocess
    import shutil

    # 1. CPU
    cpu_percent = psutil.cpu_percent(interval=None) or 0.0

    # 2. RAM
    mem = psutil.virtual_memory()
    ram_used = round(mem.used / (1024**3), 2)
    ram_total = round(mem.total / (1024**3), 2)

    # 3. VRAM — return null when no GPU detected (production rule: never fabricate)
    vram_used = None
    vram_total = None

    nvidia_smi = shutil.which("nvidia-smi")
    if nvidia_smi:
        try:
            res = subprocess.run(
                [
                    nvidia_smi,
                    "--query-gpu=memory.used,memory.total",
                    "--format=csv,noheader,nounits",
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True,
                timeout=1,
            )
            parts = res.stdout.strip().split(",")
            if len(parts) >= 2:
                vram_used = round(float(parts[0].strip()) / 1024.0, 2)
                vram_total = round(float(parts[1].strip()) / 1024.0, 2)
        except Exception:
            pass

    return {
        "cpu": cpu_percent,
        "ram": {"used": ram_used, "total": ram_total},
        "vram": {"used": vram_used, "total": vram_total},
    }


@router.get("/dashboard")
async def system_dashboard():
    """
    Consolidated dashboard endpoint.
    Replaces 5+ parallel frontend calls with a single backend-composed
    response built via asyncio.gather.

    Returns services, runtime, metrics, costs, DLQ, and alert data.
    """
    # Run all independent queries in parallel
    (
        services_status,
        runtime_info,
        metrics_data,
        costs_data,
        dlq_data,
        alerts_data,
    ) = await asyncio.gather(
        _get_services_status(),
        _get_runtime_info(),
        _get_metrics_data(),
        _get_costs_data(),
        _get_dlq_data(),
        _get_alerts_data(),
        return_exceptions=True,
    )

    return {
        "services": services_status if not isinstance(services_status, Exception) else _fallback_services(),
        "runtime": runtime_info if not isinstance(runtime_info, Exception) else _fallback_runtime(),
        "metrics": metrics_data if not isinstance(metrics_data, Exception) else _fallback_metrics(),
        "costs": costs_data if not isinstance(costs_data, Exception) else {"total_usd": 0.0, "total_tokens": 0},
        "dlq": dlq_data if not isinstance(dlq_data, Exception) else {"failed": [], "count": 0},
        "alerts": alerts_data if not isinstance(alerts_data, Exception) else {"notifications": []},
        "status": "ready",
    }


# ── Dashboard sub-resolvers (used by asyncio.gather) ──────────────────


async def _get_services_status() -> dict:
    q_host, q_port = settings.QDRANT_HOST, settings.QDRANT_PORT
    ollama_base = settings.OLLAMA_BASE_URL.rstrip("/")
    results = await asyncio.gather(
        _check_postgres(),
        _check("qdrant", f"http://{q_host}:{q_port}/"),
        _check("ollama", f"{ollama_base}/api/tags"),
        _check("n8n", "http://n8n:5678/healthz"),
        _check("grafana", "http://grafana:3000/api/health"),
        _check("prometheus", "http://prometheus:9090/-/ready"),
        return_exceptions=True,
    )
    names = ["postgres", "qdrant", "ollama", "n8n", "grafana", "prometheus"]
    return {
        "backend": True,
        **{name: (r is True) for name, r in zip(names, results)},
    }


async def _get_runtime_info() -> dict:
    import psutil

    cpu = psutil.cpu_percent(interval=None) or 0.0
    mem = psutil.virtual_memory()
    ram_used = round(mem.used / (1024**3), 2)
    ram_total = round(mem.total / (1024**3), 2)

    # Active model from provider config
    from app.setup.provider_config import get_active_provider_config
    config = get_active_provider_config()
    active_model = config.get("model", "")

    # VRAM (null when no GPU)
    vram = await _read_vram()

    # Average LLM latency from global metrics
    avg_latency = 0.0
    try:
        from app.llm.metrics import ProviderMetrics
        summary = ProviderMetrics.global_summary()
        avg_latency = summary.get("avg_latency_ms", 0.0)
    except Exception:
        pass

    return {
        "activeModel": active_model or "No model installed",
        "latency": avg_latency,
        "cpu": cpu,
        "ram": {"used": ram_used, "total": ram_total},
        "vram": vram,
    }


async def _read_vram() -> dict:
    import subprocess
    import shutil

    nvidia_smi = shutil.which("nvidia-smi")
    if not nvidia_smi:
        return {"used": None, "total": None}

    try:
        res = subprocess.run(
            [nvidia_smi, "--query-gpu=memory.used,memory.total", "--format=csv,noheader,nounits"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, check=True, timeout=1,
        )
        parts = res.stdout.strip().split(",")
        if len(parts) >= 2:
            return {
                "used": round(float(parts[0].strip()) / 1024.0, 2),
                "total": round(float(parts[1].strip()) / 1024.0, 2),
            }
    except Exception:
        pass
    return {"used": None, "total": None}


async def _get_metrics_data() -> dict:
    # Vector count from Qdrant
    vector_count = 0
    try:
        import httpx
        q_host, q_port = settings.QDRANT_HOST, settings.QDRANT_PORT
        async with httpx.AsyncClient(timeout=3) as c:
            r = await c.post(
                f"http://{q_host}:{q_port}/collections/kaos/points/count",
                json={},
            )
            if r.is_success:
                vector_count = r.json().get("result", {}).get("count", 0)
    except Exception:
        pass

    # Token rate from ProviderMetrics
    token_rate = 0.0
    try:
        from app.llm.metrics import ProviderMetrics
        token_rate = ProviderMetrics.global_token_rate()
    except Exception:
        pass

    return {
        "vectorCount": vector_count,
        "tokenRate": token_rate,
    }


async def _get_costs_data() -> dict:
    # Use the in-memory cost tracker (sync, no DB dependency)
    try:
        from app.observability.cost_tracker import CostTracker
        from app.observability.event_bus import EventBus
        trackers = [s for s in EventBus._subscribers.get("llm_response", []) if isinstance(s, CostTracker)]
        if not trackers:
            trackers = [s for s in EventBus._subscribers.get("workflow_completed", []) if isinstance(s, CostTracker)]
        if trackers:
            summary = trackers[0].summary()
            return {
                "total_usd": summary.get("total_cost", 0.0),
                "total_tokens": 0,
            }
    except Exception:
        pass
    return {"total_usd": 0.0, "total_tokens": 0}


async def _get_dlq_data() -> dict:
    try:
        from app.orchestrator.dead_letter_queue import DeadLetterQueue
        failed = DeadLetterQueue.list_all()
        return {
            "failed": [
                {
                    "id": str(f.execution_id),
                    "workflow_name": f.workflow,
                    "status": "failed",
                    "error": f.error[:200] if f.error else "",
                    "created_at": f.timestamp.isoformat(),
                }
                for f in failed
            ],
            "count": len(failed),
        }
    except Exception:
        return {"failed": [], "count": 0}


async def _get_alerts_data() -> dict:
    try:
        from app.notifications.service import NotificationService
        notifications = NotificationService.list(unread_only=True, limit=10)
        return {
            "notifications": [
                {
                    "id": str(n.id),
                    "level": n.level.value,
                    "title": n.title,
                    "message": n.message,
                    "source": n.source,
                    "created_at": n.created_at.isoformat(),
                    "read": n.read,
                }
                for n in notifications
            ]
        }
    except Exception:
        return {"notifications": []}


# ── Fallback helpers (returned when asyncio.gather catches an Exception) ──


def _fallback_services() -> dict:
    return {
        "backend": True,
        "postgres": False, "qdrant": False, "ollama": False,
        "n8n": False, "grafana": False, "prometheus": False,
    }


def _fallback_runtime() -> dict:
    return {
        "activeModel": "Unknown",
        "latency": 0.0,
        "cpu": 0.0,
        "ram": {"used": 0.0, "total": 0.0},
        "vram": {"used": None, "total": None},
    }


def _fallback_metrics() -> dict:
    return {"vectorCount": 0, "tokenRate": 0.0}
