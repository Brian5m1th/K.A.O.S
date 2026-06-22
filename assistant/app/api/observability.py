import httpx
from fastapi import APIRouter
from loguru import logger

from app.config.settings import settings

router = APIRouter(prefix="/api/observability", tags=["Observability"])


@router.get("/metrics")
async def get_metrics():
    """Proxy to Prometheus if available, otherwise return empty metrics."""
    try:
        async with httpx.AsyncClient(timeout=3) as client:
            resp = await client.get("http://prometheus:9090/api/v1/query?query=kaos_*")
            if resp.is_success:
                data = resp.json()
                return {"source": "prometheus", "data": data.get("data", {})}
    except Exception as e:
        logger.debug("[observability] Prometheus unavailable: {}", e)

    return {"source": "none", "data": {}, "message": "Prometheus not available"}


@router.get("/health")
async def observability_health():
    """Check which observability services are reachable."""
    services = {"prometheus": False, "loki": False, "grafana": False}

    try:
        async with httpx.AsyncClient(timeout=2) as client:
            r = await client.get("http://prometheus:9090/-/ready")
            services["prometheus"] = r.is_success
    except Exception:
        pass

    try:
        async with httpx.AsyncClient(timeout=2) as client:
            r = await client.get("http://loki:3100/ready")
            services["loki"] = r.is_success
    except Exception:
        pass

    try:
        async with httpx.AsyncClient(timeout=2) as client:
            r = await client.get("http://grafana:3001/api/health")
            services["grafana"] = r.is_success
    except Exception:
        pass

    return services
