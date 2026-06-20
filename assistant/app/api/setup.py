import logging

import httpx
from fastapi import APIRouter

from app.setup.provider_config import get_config, save_config

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/setup", tags=["setup"])


@router.get("/provider")
async def get_provider_config():
    return get_config()


@router.post("/provider")
async def set_provider_config(config: dict):
    merged = save_config(config)
    return {"status": "ok", "config": merged}


@router.post("/provider/test")
async def test_provider(payload: dict):
    provider = payload.get("provider", "")
    url = payload.get("url", "")
    api_key = payload.get("apiKey", "")

    if not url:
        return {"status": "error", "message": "URL is required"}

    endpoints = {
        "ollama": f"{url.rstrip('/')}/api/tags",
        "openai": f"{url.rstrip('/')}/models",
        "anthropic": url.rstrip("/"),
        "google": f"{url.rstrip('/')}/models",
    }

    endpoint = endpoints.get(provider, url.rstrip("/"))
    headers = {}
    if api_key:
        if provider == "openai":
            headers["Authorization"] = f"Bearer {api_key}"
        elif provider == "anthropic":
            headers["x-api-key"] = api_key
            headers["anthropic-version"] = "2023-06-01"
        elif provider == "google":
            sep = "&" if "?" in endpoint else "?"
            endpoint = f"{endpoint}{sep}key={api_key}"

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(endpoint, headers=headers)
            if resp.is_success or resp.status_code in (401, 403):
                return {"status": "connected"}
            return {"status": "error", "message": f"HTTP {resp.status_code}"}
    except httpx.RequestError as e:
        return {"status": "error", "message": f"Connection failed: {e}"}
