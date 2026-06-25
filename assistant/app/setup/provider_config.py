from pathlib import Path

from loguru import logger

from app.config.settings import settings
from app.core.config_service import ConfigService

PROVIDER_CONFIG_PATH = Path("data/provider_config.json")

DEFAULT_ACTIVE_PROVIDER = "ollama"

# Static DEFAULT_CONFIG kept for schema compatibility checks if needed
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


def get_default_config() -> dict:
    """Resolve provider default configurations dynamically from environment settings."""
    return {
        "ollama": {
            "url": settings.OLLAMA_BASE_URL or "http://localhost:11434",
            "apiKey": "",
            "model": settings.OLLAMA_MODEL or "qwen3:14b",
            "fastModel": settings.OLLAMA_FAST_MODEL or "",
        },
        "openai": {
            "url": "https://api.openai.com/v1",
            "apiKey": settings.OPENAI_API_KEY or "",
            "model": "gpt-4o",
            "fastModel": "",
        },
        "anthropic": {
            "url": "https://api.anthropic.com",
            "apiKey": settings.ANTHROPIC_API_KEY or "",
            "model": "claude-sonnet-4-20250514",
            "fastModel": "",
        },
        "gemini": {
            "url": "https://generativelanguage.googleapis.com",
            "apiKey": settings.GEMINI_API_KEY or "",
            "model": "gemini-2.0-flash",
            "fastModel": "",
        },
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
    """Load configuration from ConfigService (central settings file)."""
    try:
        config = ConfigService.load_config()
        payload = dict(config.get("providers", {}))
        payload["_activeProvider"] = config.get(
            "_activeProvider", DEFAULT_ACTIVE_PROVIDER
        )
        payload["_fallbackChain"] = config.get("_fallbackChain", [])
        payload["_embeddingModel"] = config.get("_embeddingModel", "")

        # Merge credentials from secrets
        secrets = ConfigService.load_secrets()
        provider_secrets = secrets.get("providers", {})
        for provider_id in payload:
            if isinstance(payload[provider_id], dict):
                p_secrets = provider_secrets.get(provider_id, {})
                for k, v in p_secrets.items():
                    if v:
                        payload[provider_id][k] = v
        return payload
    except Exception as e:
        logger.exception("Failed to load provider config via ConfigService: {}", e)
        return {}


def _save_to_disk(config: dict) -> None:
    """Save configuration to ConfigService (separating public config and secrets)."""
    try:
        db_config = ConfigService.load_config()
        db_secrets = ConfigService.load_secrets()

        providers = {}
        provider_secrets = db_secrets.setdefault("providers", {})

        for k, v in config.items():
            if k in ("_activeProvider", "_fallbackChain", "_embeddingModel"):
                db_config[k] = v
            elif isinstance(v, dict):
                provider_id = k
                provider_data = dict(v)
                p_secrets = provider_secrets.setdefault(provider_id, {})

                # Extract secret API keys or tokens
                for sec_key in ("apiKey", "token", "botToken", "webhookUrl"):
                    if sec_key in provider_data:
                        val = provider_data[sec_key]
                        if val:
                            p_secrets[sec_key] = val
                        provider_data[sec_key] = ""

                providers[provider_id] = provider_data

        db_config["providers"] = providers
        ConfigService.save_config(db_config)
        ConfigService.save_secrets(db_secrets)
    except Exception as e:
        logger.exception("Failed to save provider config via ConfigService: {}", e)


def get_config() -> dict:
    saved = _load_from_disk()
    merged = {}
    default_cfg = get_default_config()
    for provider, defaults in default_cfg.items():
        saved_fields = saved.get(provider, {})
        merged[provider] = {**defaults, **saved_fields}
    merged["_activeProvider"] = saved.get("_activeProvider", DEFAULT_ACTIVE_PROVIDER)
    return merged


def save_config(config: dict) -> dict:
    merged = {}
    default_cfg = get_default_config()
    for provider, defaults in default_cfg.items():
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
    default_cfg = get_default_config()

    if active not in default_cfg:
        logger.warning(
            "[provider] activeProvider '%s' desconhecido, usando 'ollama'", active
        )
        active = DEFAULT_ACTIVE_PROVIDER

    defaults = default_cfg[active]
    saved_fields = saved.get(active, {})
    merged = {**defaults, **saved_fields}

    if active != "ollama" and not merged.get("apiKey"):
        logger.warning(
            "[provider] activeProvider='%s' sem apiKey, fallback para 'ollama'", active
        )
        active = DEFAULT_ACTIVE_PROVIDER
        defaults = default_cfg[active]
        saved_fields = saved.get(active, {})
        merged = {**defaults, **saved_fields}

    fast_model = merged.get("fastModel", "")
    return {
        "provider": active,
        "model": merged.get("model", default_cfg[active]["model"]),
        "fastModel": fast_model
        if fast_model
        else merged.get("model", default_cfg[active]["model"]),
        "url": merged.get("url", default_cfg[active]["url"]),
        "apiKey": merged.get("apiKey", ""),
    }
