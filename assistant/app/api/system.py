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

        async with async_session_factory() as s:
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
        "qdrant": await _check("qdrant", f"http://{q_host}:{q_port}/health"),
        "ollama": await _check("ollama", f"{ollama_base}/api/tags"),
        "postgres": await _check_postgres(),
        "n8n": await _check("n8n", "http://n8n:5678/healthz"),
        "grafana": await _check("grafana", "http://grafana:3000/api/health"),
        "prometheus": await _check("prometheus", "http://prometheus:9090/-/ready"),
    }
