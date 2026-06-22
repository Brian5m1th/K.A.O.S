import httpx
from enum import Enum
from dataclasses import dataclass, field

from fastapi import APIRouter
from loguru import logger

from app.setup.provider_config import get_config, get_active_provider_config

router = APIRouter(prefix="/api", tags=["Providers"])


class ProviderSourceType(str, Enum):
    """How models are discovered for a given provider."""

    API = "api"  # Consult external endpoint (e.g. Ollama /api/tags, OpenAI /models)
    CATALOG = "catalog"  # Static list maintained by backend


@dataclass
class ProviderSource:
    """Configuration for how to discover a provider's models."""

    type: ProviderSourceType
    endpoint: str = ""
    catalog: list[str] = field(default_factory=list)
    auth_type: str = "none"  # "header" | "query" | "none"
    api_key_field: str = ""


# Registry of all known providers and how to discover their models
# Extensible: just add a new entry and the endpoint handles it
PROVIDER_SOURCES: dict[str, ProviderSource] = {
    "openai": ProviderSource(
        type=ProviderSourceType.API,
        endpoint="/models",
        auth_type="header",
        api_key_field="Authorization",
    ),
    "anthropic": ProviderSource(
        type=ProviderSourceType.CATALOG,
        catalog=[
            "claude-sonnet-4-20250514",
            "claude-3-5-sonnet-20241022",
            "claude-3-5-haiku-20241022",
        ],
        auth_type="header",
        api_key_field="x-api-key",
    ),
    "gemini": ProviderSource(
        type=ProviderSourceType.CATALOG,
        catalog=[
            "gemini-2.0-flash",
            "gemini-2.0-flash-lite",
            "gemini-1.5-pro",
        ],
        auth_type="query",
        api_key_field="key",
    ),
    "ollama": ProviderSource(
        type=ProviderSourceType.API,
        endpoint="/api/tags",
        auth_type="none",
    ),
    "openrouter": ProviderSource(
        type=ProviderSourceType.API,
        endpoint="/models",
        auth_type="header",
        api_key_field="Authorization",
    ),
    "openCode": ProviderSource(
        type=ProviderSourceType.CATALOG,
        catalog=["kaos", "kaos-rag", "kaos-fast"],
        auth_type="none",
    ),
}

# Static display names and base URLs
PROVIDER_META = {
    "openai": {
        "name": "OpenAI",
        "base_url": "https://api.openai.com/v1",
        "editable_url": False,
    },
    "anthropic": {
        "name": "Anthropic",
        "base_url": "https://api.anthropic.com",
        "editable_url": False,
    },
    "gemini": {
        "name": "Google Gemini",
        "base_url": "https://generativelanguage.googleapis.com",
        "editable_url": False,
    },
    "ollama": {
        "name": "Ollama",
        "base_url": "http://localhost:11434",
        "editable_url": True,
    },
    "openrouter": {
        "name": "OpenRouter",
        "base_url": "https://openrouter.ai/api/v1",
        "editable_url": False,
    },
    "openCode": {"name": "OpenCode", "base_url": "", "editable_url": False},
}


def _get_configured_providers() -> set[str]:
    """Return set of provider IDs that are usable (API key present or not required)."""
    config = get_config()
    configured = set()
    for provider_id in PROVIDER_SOURCES:
        if provider_id in ("ollama", "openCode"):
            configured.add(provider_id)
            continue
        provider_config = config.get(provider_id, {})
        if provider_config.get("apiKey"):
            configured.add(provider_id)
    return configured


def _get_active_provider() -> str:
    config = get_active_provider_config()
    return config.get("provider", "ollama")


async def _fetch_models_from_api(
    provider_id: str,
    base_url: str,
    source: ProviderSource,
) -> list[str]:
    """Fetch models from an external API endpoint."""
    try:
        url = f"{base_url.rstrip('/')}{source.endpoint}"
        headers = {}
        params = {}

        if source.auth_type == "header" and source.api_key_field:
            config = get_config().get(provider_id, {})
            api_key = config.get("apiKey", "")
            if api_key:
                headers[source.api_key_field] = (
                    f"Bearer {api_key}"
                    if source.api_key_field == "Authorization"
                    else api_key
                )

        if source.auth_type == "query" and source.api_key_field:
            config = get_config().get(provider_id, {})
            api_key = config.get("apiKey", "")
            if api_key:
                params[source.api_key_field] = api_key

        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(url, headers=headers, params=params)
            if not resp.is_success:
                logger.warning(
                    "[providers] {} API returned HTTP {}", provider_id, resp.status_code
                )
                return []

            data = resp.json()
            models: list[str] = []

            # Ollama: {"models": [{"name": "qwen3:14b"}, ...]}
            if provider_id == "ollama":
                for m in data.get("models", []):
                    name = m.get("name", "")
                    if name:
                        models.append(name)

            # OpenAI / OpenRouter: {"data": [{"id": "gpt-5"}, ...]}
            elif provider_id in ("openai", "openrouter"):
                for m in data.get("data", []):
                    mid = m.get("id", "")
                    if mid:
                        models.append(mid)

            return models

    except Exception as e:
        logger.warning("[providers] failed to fetch models from {}: {}", provider_id, e)
        return []


@router.get("/providers")
async def list_providers():
    """List all configured providers with their available models."""
    configured_providers = _get_configured_providers()
    config = get_config()

    active_provider = config.get("_activeProvider", "ollama")
    fallback_chain = config.get("_fallbackChain", [])
    embedding_model = config.get("_embeddingModel", "")

    result_providers = []
    for provider_id, source in PROVIDER_SOURCES.items():
        meta = PROVIDER_META.get(provider_id, {})
        provider_config = config.get(provider_id, {})

        is_configured = provider_id in configured_providers
        saved_url = provider_config.get("url", "")
        base_url = saved_url or meta.get("base_url", "")

        if source.type == ProviderSourceType.API and is_configured:
            models = await _fetch_models_from_api(provider_id, base_url, source)
        else:
            models = list(source.catalog)

        result_providers.append(
            {
                "id": provider_id,
                "name": meta.get("name", provider_id),
                "base_url": base_url,
                "editable_url": meta.get("editable_url", False),
                "configured": is_configured,
                "models": models,
                "default_model": provider_config.get("model", ""),
                "fast_model": provider_config.get("fastModel", ""),
            }
        )

    return {
        "providers": result_providers,
        "activeProvider": active_provider,
        "fallbackChain": fallback_chain,
        "embeddingModel": embedding_model,
    }
