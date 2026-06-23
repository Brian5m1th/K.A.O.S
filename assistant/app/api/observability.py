import httpx
from fastapi import APIRouter

router = APIRouter(prefix="/api/observability", tags=["Observability"])


@router.get("/health")
async def observability_health():
    services = {"prometheus": False, "loki": False, "grafana": False}
    for name, url in [
        ("prometheus", "http://prometheus:9090/-/ready"),
        ("loki", "http://loki:3100/ready"),
        ("grafana", "http://grafana:3001/api/health"),
    ]:
        try:
            async with httpx.AsyncClient(timeout=2) as c:
                r = await c.get(url)
                services[name] = r.is_success
        except Exception:
            pass
    return services
