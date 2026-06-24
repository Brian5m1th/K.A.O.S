"""
Generic Integrations API.

Manages third-party service connections (GitHub, Discord, N8N, etc.)
using ``ConfigService`` for persistence and secret isolation.
"""

from fastapi import APIRouter
from loguru import logger

from app.core.config_service import ConfigService

router = APIRouter(prefix="/api/integrations", tags=["Integrations"])


@router.get("")
async def list_integrations():
    """Return all configured integrations with their connection status."""
    config = ConfigService.load_config()
    integrations = config.get("integrations", {})
    result = []
    for integ_type, data in integrations.items():
        if isinstance(data, dict):
            result.append(
                {
                    "type": integ_type,
                    "status": data.get("status", "disconnected"),
                    "metadata": {
                        k: v
                        for k, v in data.items()
                        if k
                        not in ("status", "token", "apiKey", "botToken", "webhookUrl")
                    },
                }
            )
    return {"integrations": result}


@router.post("")
async def configure_integration(payload: dict):
    """Configure or update an integration type with credentials.

    Request body::

        {"type": "github", "credentials": {"token": "ghp_..."}}
    """
    integ_type = payload.get("type", "").strip()
    credentials = payload.get("credentials", {})

    if not integ_type:
        return {"status": "error", "message": "Integration type is required"}

    # Load current config
    config = ConfigService.load_config()
    integrations = config.get("integrations", {})

    # Create or update the integration entry
    entry = integrations.get(integ_type, {})
    entry["status"] = "connected"
    entry.update(
        {
            k: v
            for k, v in credentials.items()
            if k not in ("token", "apiKey", "botToken")
        }
    )
    integrations[integ_type] = entry
    config["integrations"] = integrations

    # Persist public config
    ConfigService.save_config(config)

    # Store sensitive credentials in secrets file
    secret_fields = {
        k: v for k, v in credentials.items() if k in ("token", "apiKey", "botToken")
    }
    if secret_fields:
        secrets = ConfigService.load_secrets()
        integ_secrets = secrets.setdefault("integrations", {})
        integ_secrets[integ_type] = secret_fields
        ConfigService.save_secrets(secrets)

    logger.info("[integrations] configured type='{}'", integ_type)
    return {
        "status": "ok",
        "message": f"Integration type {integ_type} connected successfully",
    }
