import time

import httpx
from fastapi import APIRouter
from loguru import logger

from app.setup.provider_config import (
    get_config,
    get_active_provider_config,
    save_config,
    DEFAULT_CONFIG,
    DEFAULT_ACTIVE_PROVIDER,
)

router = APIRouter(prefix="/api/setup", tags=["setup"])


@router.get("/provider")
async def get_provider_config():
    return get_config()


@router.post("/provider")
async def set_provider_config(config: dict):
    merged = save_config(config)
    return {"status": "ok", "config": merged}


@router.get("/provider/active")
async def get_active_provider():
    config = get_active_provider_config()
    return {
        "activeProvider": config["provider"],
        "model": config["model"],
        "url": config["url"],
        "available": list(DEFAULT_CONFIG.keys()),
    }


@router.post("/provider/active")
async def set_active_provider(payload: dict):
    provider = payload.get("provider", DEFAULT_ACTIVE_PROVIDER)
    current = get_config()
    current["_activeProvider"] = provider
    merged = save_config(current)
    logger.info("[setup] active provider changed to '%s'", provider)
    return {"status": "ok", "activeProvider": provider, "config": merged}


@router.post("/provider/test")
async def test_provider(payload: dict):
    provider = payload.get("provider", "")
    url = payload.get("url", "")
    api_key = payload.get("apiKey", "")

    if not url:
        return {"status": "error", "message": "URL is required"}

    # Reject empty API key (providers that don't need one are handled below)
    if not api_key and provider not in ("ollama", "openCode", "lmstudio"):
        return {
            "status": "error",
            "message": "API key is required for this provider",
        }

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
        t0 = time.monotonic()
        async with httpx.AsyncClient(timeout=5) as client:
            resp = await client.get(endpoint, headers=headers)
        latency_ms = int((time.monotonic() - t0) * 1000)

        if resp.is_success:
            return {"status": "connected", "latency_ms": latency_ms}
        if resp.status_code in (401, 403):
            return {
                "status": "connected",
                "latency_ms": latency_ms,
                "warning": f"HTTP {resp.status_code} (auth may be required)",
            }
        return {
            "status": "error",
            "message": f"HTTP {resp.status_code}",
            "latency_ms": latency_ms,
        }
    except httpx.RequestError as e:
        return {"status": "error", "message": f"Connection failed: {e}"}
    except ValueError as e:
        return {"status": "error", "message": f"Invalid URL: {e}"}


# Secure encrypted setup endpoint

from pydantic import BaseModel
import json


class SecureSetupRequest(BaseModel):
    client_id: str
    encrypted_data: str


@router.post("/provider/secure")
async def set_secure_provider_config(payload: SecureSetupRequest):
    from app.auth.handshake import HandshakeService

    service = HandshakeService()
    try:
        # Descriptografar payload usando o segredo compartilhado derivado do handshake
        decrypted_json = service.decrypt(payload.client_id, payload.encrypted_data)
        config_data = json.loads(decrypted_json)

        merged = save_config(config_data)
        return {"status": "ok", "config": merged}
    except Exception as e:
        logger.error(f"[setup] Secure provider setup failed: {e}")
        return {"status": "error", "message": str(e)}

