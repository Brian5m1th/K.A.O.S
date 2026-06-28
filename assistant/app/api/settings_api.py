from fastapi import APIRouter
from loguru import logger

from app.core.config_service import ConfigService

router = APIRouter(prefix="/api/settings", tags=["Settings"])

# Fields that belong to the "settings" subset (not providers/integrations)
_SETTINGS_KEYS = {"theme", "accent_color", "language", "telemetry", "schemaVersion"}


@router.get("")
async def get_settings():
    config = ConfigService.load_config()
    # Return only the general settings subset plus schemaVersion
    return {k: config.get(k) for k in _SETTINGS_KEYS if k in config}


@router.put("")
async def save_settings(body: dict):
    config = ConfigService.load_config()
    # Filter the incoming body to only allow updating general settings keys
    filtered_body = {k: v for k, v in body.items() if k in _SETTINGS_KEYS}
    config.update(filtered_body)
    ConfigService.save_config(config)
    logger.info("[settings] settings updated")
    # Return the full settings subset after save
    return {
        "status": "saved",
        "settings": {k: config.get(k) for k in _SETTINGS_KEYS if k in config},
    }
