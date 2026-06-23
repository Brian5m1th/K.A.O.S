import json
from pathlib import Path

from fastapi import APIRouter
from loguru import logger

router = APIRouter(prefix="/api/settings", tags=["Settings"])

SETTINGS_PATH = Path("data/settings.json")
DEFAULT_SETTINGS = {
    "theme": "dark",
    "accent_color": "#3B82F6",
    "language": "pt-BR",
    "telemetry": True,
}


def _load() -> dict:
    if not SETTINGS_PATH.exists():
        return dict(DEFAULT_SETTINGS)
    try:
        return json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
    except Exception:
        return dict(DEFAULT_SETTINGS)


def _save(data: dict) -> None:
    SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    SETTINGS_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )


@router.get("")
async def get_settings():
    return _load()


@router.put("")
async def save_settings(body: dict):
    current = _load()
    current.update(body)
    _save(current)
    logger.info("[settings] settings updated")
    return {"status": "saved", "settings": current}
