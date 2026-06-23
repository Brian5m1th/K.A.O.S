import json
from pathlib import Path

import httpx
from fastapi import APIRouter
from loguru import logger

router = APIRouter(prefix="/api/integrations", tags=["Integrations"])

CONFIG_PATH = Path("data/integrations.json")

DEFAULT_INTEGRATIONS = {
    "github": {
        "name": "GitHub",
        "connected": False,
        "configurable": True,
        "token": "",
        "webhookUrl": "",
    },
    "discord": {
        "name": "Discord",
        "connected": False,
        "configurable": True,
        "webhookUrl": "",
        "botToken": "",
    },
    "telegram": {
        "name": "Telegram",
        "connected": False,
        "configurable": True,
        "botToken": "",
    },
    "whatsapp": {
        "name": "WhatsApp",
        "connected": False,
        "configurable": True,
        "apiKey": "",
    },
    "n8n": {
        "name": "N8N",
        "connected": False,
        "configurable": True,
        "webhookUrl": "",
        "apiUrl": "http://n8n:5678",
        "enabled": False,
    },
    "prometheus": {
        "name": "Prometheus",
        "connected": False,
        "configurable": False,
        "url": "http://prometheus:9090",
    },
    "loki": {
        "name": "Loki",
        "connected": False,
        "configurable": False,
        "url": "http://loki:3100",
    },
    "qdrant": {
        "name": "Qdrant",
        "connected": False,
        "configurable": False,
        "url": "http://qdrant:6333",
    },
    "obsidian": {
        "name": "Obsidian",
        "connected": False,
        "configurable": True,
        "vaultPath": "",
    },
}


def _load() -> dict:
    if not CONFIG_PATH.exists():
        return dict(DEFAULT_INTEGRATIONS)
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        merged = dict(DEFAULT_INTEGRATIONS)
        merged.update(data)
        return merged
    except Exception:
        return dict(DEFAULT_INTEGRATIONS)


def _save(data: dict) -> None:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )


@router.get("")
async def list_integrations():
    config = _load()
    return {"integrations": [{"id": k, **v} for k, v in config.items()]}


@router.get("/{integration_id}")
async def get_integration(integration_id: str):
    config = _load()
    entry = config.get(integration_id)
    if not entry:
        return {"error": "Integration not found"}
    return {"id": integration_id, **entry}


@router.put("/{integration_id}")
async def save_integration(integration_id: str, body: dict):
    config = _load()
    if integration_id not in config:
        return {"error": "Integration not found"}
    config[integration_id].update(body)
    _save(config)
    logger.info("[integrations] {} updated", integration_id)
    return {
        "status": "saved",
        "integration": {"id": integration_id, **config[integration_id]},
    }


@router.post("/{integration_id}/test")
async def test_integration(integration_id: str):
    config = _load()
    entry = config.get(integration_id)
    if not entry:
        return {"status": "error", "message": "Integration not found"}

    url = entry.get("url") or entry.get("webhookUrl") or ""
    if not url:
        return {"status": "error", "message": "No URL configured"}

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            resp = await client.get(url)
            if resp.is_success:
                config[integration_id]["connected"] = True
                _save(config)
                return {"status": "connected"}
            return {"status": "error", "message": f"HTTP {resp.status_code}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
