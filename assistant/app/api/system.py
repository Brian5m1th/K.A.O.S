import httpx
from fastapi import APIRouter
from loguru import logger

from app.config.settings import settings

router = APIRouter(prefix="/api/system", tags=["System"])

# Timeout for each service health check (seconds)
SERVICE_TIMEOUT = 5


async def _check_service(name: str, url: str, method: str = "GET") -> bool:
    """Check if a service is responsive by making an HTTP request."""
    try:
        async with httpx.AsyncClient(timeout=SERVICE_TIMEOUT) as client:
            resp = await client.request(method, url)
            return resp.is_success
    except Exception as e:
        logger.debug("[system] service '{}' at {} unreachable: {}", name, url, e)
        return False


@router.get("/status")
async def system_status():
    """Return the health status of all services in the K.A.O.S platform.

    Each service is checked independently with a short timeout.
    Services that don't respond are reported as `false`.
    """
    backend_ok = True  # If we're here, the backend is running

    # Qdrant
    qdrant_host = settings.QDRANT_HOST
    qdrant_port = settings.QDRANT_PORT
    qdrant_ok = await _check_service(
        "qdrant", f"http://{qdrant_host}:{qdrant_port}/health"
    )

    # Ollama
    ollama_base = settings.OLLAMA_BASE_URL.rstrip("/")
    ollama_ok = await _check_service("ollama", f"{ollama_base}/api/tags")

    # PostgreSQL
    postgres_ok = await _check_postgres()

    # N8N
    n8n_ok = await _check_service("n8n", "http://n8n:5678/healthz")

    # Grafana
    grafana_ok = await _check_service("grafana", "http://grafana:3001/api/health")

    # Prometheus
    prometheus_ok = await _check_service("prometheus", "http://prometheus:9090/-/ready")

    return {
        "backend": backend_ok,
        "qdrant": qdrant_ok,
        "ollama": ollama_ok,
        "postgres": postgres_ok,
        "n8n": n8n_ok,
        "grafana": grafana_ok,
        "prometheus": prometheus_ok,
    }


async def _check_postgres() -> bool:
    """Check PostgreSQL connectivity via a simple query."""
    try:
        from sqlalchemy import text
        from app.database import async_session_factory

        async with async_session_factory() as session:
            result = await session.execute(text("SELECT 1"))
            return result.scalar() == 1
    except Exception as e:
        logger.debug("[system] postgres check failed: {}", e)
        return False
