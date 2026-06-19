import json
import logging
from pathlib import Path

from app.config.settings import settings

logger = logging.getLogger(__name__)

PROVIDER_CONFIG_PATH = Path("data/provider_config.json")

DEFAULT_CONFIG = {
    "ollama": {
        "url": "http://localhost:11434",
        "apiKey": "",
        "model": "qwen3:14b",
    },
    "openai": {
        "url": "https://api.openai.com/v1",
        "apiKey": "",
        "model": "gpt-4o",
    },
    "anthropic": {
        "url": "https://api.anthropic.com",
        "apiKey": "",
        "model": "claude-sonnet-4-20250514",
    },
    "gemini": {
        "url": "https://generativelanguage.googleapis.com",
        "apiKey": "",
        "model": "gemini-2.0-flash",
    },
}

SETTINGS_KEY_MAP = {
    "ollama": {"url": "OLLAMA_BASE_URL", "apiKey": None, "model": "OLLAMA_MODEL"},
    "openai": {"url": None, "apiKey": "OPENAI_API_KEY", "model": None},
    "anthropic": {"url": None, "apiKey": "ANTHROPIC_API_KEY", "model": None},
    "gemini": {"url": None, "apiKey": "GEMINI_API_KEY", "model": None},
}


def _patch_settings(config: dict) -> None:
    for provider, fields in config.items():
        mapping = SETTINGS_KEY_MAP.get(provider)
        if not mapping:
            continue
        for field_key, setting_name in mapping.items():
            if setting_name is None:
                continue
            value = fields.get(field_key)
            if value:
                setattr(settings, setting_name, value)


def _invalidate_caches() -> None:
    import app.api.openai
    import app.agent.nodes.planner
    import app.router.intent_classifier

    app.api.openai._factory = None
    app.agent.nodes.planner._factory = None

    classifier = app.router.intent_classifier._classifier
    if classifier is not None:
        classifier._factory = None


def _load_from_disk() -> dict:
    if not PROVIDER_CONFIG_PATH.exists():
        return {}
    try:
        raw = PROVIDER_CONFIG_PATH.read_text(encoding="utf-8")
        return json.loads(raw)
    except Exception:
        logger.warning("Failed to load provider config from disk", exc_info=True)
        return {}


def _save_to_disk(config: dict) -> None:
    PROVIDER_CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    PROVIDER_CONFIG_PATH.write_text(
        json.dumps(config, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def get_config() -> dict:
    saved = _load_from_disk()
    merged = {}
    for provider, defaults in DEFAULT_CONFIG.items():
        saved_fields = saved.get(provider, {})
        merged[provider] = {**defaults, **saved_fields}
    return merged


def save_config(config: dict) -> dict:
    merged = {}
    for provider, defaults in DEFAULT_CONFIG.items():
        provided = config.get(provider, {})
        merged[provider] = {k: provided.get(k, defaults[k]) for k in defaults}

    _save_to_disk(merged)
    _patch_settings(merged)
    _invalidate_caches()

    return merged
