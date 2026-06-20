import json
from pathlib import Path

from loguru import logger

from app.config.settings import settings

PROVIDER_CONFIG_PATH = Path("data/provider_config.json")

DEFAULT_ACTIVE_PROVIDER = "ollama"

DEFAULT_CONFIG = {
    "ollama": {
        "url": "http://localhost:11434",
        "apiKey": "",
        "model": "qwen3:14b",
        "fastModel": "",
    },
    "openai": {
        "url": "https://api.openai.com/v1",
        "apiKey": "",
        "model": "gpt-4o",
        "fastModel": "",
    },
    "anthropic": {
        "url": "https://api.anthropic.com",
        "apiKey": "",
        "model": "claude-sonnet-4-20250514",
        "fastModel": "",
    },
    "gemini": {
        "url": "https://generativelanguage.googleapis.com",
        "apiKey": "",
        "model": "gemini-2.0-flash",
        "fastModel": "",
    },
}

_config_version: int = 0


def get_config_version() -> int:
    return _config_version


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


def _bump_version() -> None:
    global _config_version
    _config_version += 1


def _load_from_disk() -> dict:
    if not PROVIDER_CONFIG_PATH.exists():
        return {}
    try:
        raw = PROVIDER_CONFIG_PATH.read_text(encoding="utf-8")
        return json.loads(raw)
    except Exception:
        logger.opt(exception=True).warning("Failed to load provider config from disk")
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
    merged["_activeProvider"] = saved.get("_activeProvider", DEFAULT_ACTIVE_PROVIDER)
    return merged


def save_config(config: dict) -> dict:
    merged = {}
    for provider, defaults in DEFAULT_CONFIG.items():
        provided = config.get(provider, {})
        merged[provider] = {k: provided.get(k, defaults[k]) for k in defaults}

    active = config.get("_activeProvider", DEFAULT_ACTIVE_PROVIDER)
    save_payload = {**merged, "_activeProvider": active}

    _save_to_disk(save_payload)
    _patch_settings(merged)
    _bump_version()

    return {**merged, "_activeProvider": active}


def get_active_provider_config() -> dict:
    saved = _load_from_disk()
    active = saved.get("_activeProvider", DEFAULT_ACTIVE_PROVIDER)

    if active not in DEFAULT_CONFIG:
        logger.warning(
            "[provider] activeProvider '%s' desconhecido, usando 'ollama'", active
        )
        active = DEFAULT_ACTIVE_PROVIDER

    defaults = DEFAULT_CONFIG[active]
    saved_fields = saved.get(active, {})
    merged = {**defaults, **saved_fields}

    if active != "ollama" and not merged.get("apiKey"):
        logger.warning(
            "[provider] activeProvider='%s' sem apiKey, fallback para 'ollama'", active
        )
        active = DEFAULT_ACTIVE_PROVIDER
        defaults = DEFAULT_CONFIG[active]
        saved_fields = saved.get(active, {})
        merged = {**defaults, **saved_fields}

    fast_model = merged.get("fastModel", "")
    return {
        "provider": active,
        "model": merged.get("model", DEFAULT_CONFIG[active]["model"]),
        "fastModel": fast_model if fast_model else merged.get("model", DEFAULT_CONFIG[active]["model"]),
        "url": merged.get("url", DEFAULT_CONFIG[active]["url"]),
        "apiKey": merged.get("apiKey", ""),
    }
