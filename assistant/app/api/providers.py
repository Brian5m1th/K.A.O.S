import time

import httpx
from enum import Enum
from dataclasses import dataclass, field
from fastapi import APIRouter
from loguru import logger
from app.setup.provider_config import get_config

router = APIRouter(prefix="/api", tags=["Providers"])


class ProviderSourceType(str, Enum):
    API = "api"
    CATALOG = "catalog"


@dataclass
class ProviderSource:
    type: ProviderSourceType
    endpoint: str = ""
    catalog: list[str] = field(default_factory=list)
    auth_type: str = "none"
    api_key_field: str = ""


PROVIDER_SOURCES = {
    "openai": ProviderSource(
        ProviderSourceType.API,
        "/models",
        auth_type="header",
        api_key_field="Authorization",
    ),
    "anthropic": ProviderSource(
        ProviderSourceType.CATALOG,
        catalog=["claude-sonnet-4-20250514"],
        auth_type="header",
        api_key_field="x-api-key",
    ),
    "gemini": ProviderSource(
        ProviderSourceType.CATALOG,
        catalog=["gemini-2.0-flash"],
        auth_type="query",
        api_key_field="key",
    ),
    "ollama": ProviderSource(ProviderSourceType.API, "/api/tags", auth_type="none"),
    "openrouter": ProviderSource(
        ProviderSourceType.API,
        "/models",
        auth_type="header",
        api_key_field="Authorization",
    ),
    "openCode": ProviderSource(
        ProviderSourceType.CATALOG,
        catalog=["kaos", "kaos-rag", "kaos-fast"],
        auth_type="none",
    ),
    "azure": ProviderSource(
        ProviderSourceType.API,
        "/openai/deployments",
        auth_type="header",
        api_key_field="api-key",
    ),
    "groq": ProviderSource(
        ProviderSourceType.API,
        "/models",
        auth_type="header",
        api_key_field="Authorization",
    ),
    "lmstudio": ProviderSource(ProviderSourceType.API, "/v1/models", auth_type="none"),
    "deepseek": ProviderSource(
        ProviderSourceType.API,
        "/models",
        auth_type="header",
        api_key_field="Authorization",
    ),
    "mistral": ProviderSource(
        ProviderSourceType.API,
        "/models",
        auth_type="header",
        api_key_field="Authorization",
    ),
}

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
    "azure": {"name": "Azure OpenAI", "base_url": "", "editable_url": True},
    "groq": {
        "name": "Groq",
        "base_url": "https://api.groq.com/openai/v1",
        "editable_url": False,
    },
    "lmstudio": {
        "name": "LM Studio",
        "base_url": "http://localhost:1234/v1",
        "editable_url": True,
    },
    "deepseek": {
        "name": "DeepSeek",
        "base_url": "https://api.deepseek.com",
        "editable_url": False,
    },
    "mistral": {
        "name": "Mistral",
        "base_url": "https://api.mistral.ai/v1",
        "editable_url": False,
    },
}


# ---------------------------------------------------------------------------
# Configured detection
# ---------------------------------------------------------------------------


def _get_configured_providers() -> set[str]:
    config = get_config()
    configured = set()
    for pid in PROVIDER_SOURCES:
        if pid in ("ollama", "openCode"):
            configured.add(pid)
            continue
        pc = config.get(pid, {})
        if pc.get("apiKey"):
            configured.add(pid)
    return configured


# ---------------------------------------------------------------------------
# Health check with TTL cache
# ---------------------------------------------------------------------------

HEALTH_CACHE_TTL = 30  # seconds
_health_cache: dict[str, dict] = {}
_health_cache_ts: float = 0.0


async def _check_provider_health(
    provider_id: str, base_url: str, source: ProviderSource, api_key: str
) -> tuple[str, int]:
    """Ping the provider API and return (status, latency_ms).

    Returns ("healthy", ms) on success, ("unhealthy", ms) on failure,
    or ("unknown", 0) if no URL/api_key available.
    """
    if not base_url or not source.endpoint:
        return "unknown", 0

    url = f"{base_url.rstrip('/')}{source.endpoint}"
    headers = {}
    params = {}

    if source.auth_type == "header" and source.api_key_field and api_key:
        val = (
            f"Bearer {api_key}" if source.api_key_field == "Authorization" else api_key
        )
        headers[source.api_key_field] = val
    elif source.auth_type == "query" and api_key:
        params[source.api_key_field] = api_key

    # Providers with no auth and no api_key can still be checked
    try:
        t0 = time.monotonic()
        async with httpx.AsyncClient(timeout=5) as client:
            resp = await client.get(url, headers=headers, params=params)
        latency_ms = int((time.monotonic() - t0) * 1000)
        if resp.is_success:
            return "healthy", latency_ms
        return "unhealthy", latency_ms
    except Exception:
        return "unhealthy", 0


async def _get_health(
    provider_id: str, base_url: str, source: ProviderSource, api_key: str
) -> tuple[str, int]:
    """Get health with TTL caching."""
    global _health_cache, _health_cache_ts

    now = time.monotonic()
    cache_key = f"{provider_id}:{base_url}:{bool(api_key)}"

    # Return cached value if still fresh
    if now - _health_cache_ts < HEALTH_CACHE_TTL and cache_key in _health_cache:
        return _health_cache[cache_key]

    # Perform real health check
    status, latency = await _check_provider_health(
        provider_id, base_url, source, api_key
    )

    # Update cache
    _health_cache[cache_key] = (status, latency)
    _health_cache_ts = now

    return status, latency


# ---------------------------------------------------------------------------
# Model fetching
# ---------------------------------------------------------------------------


async def _fetch_models_from_api(
    provider_id: str, base_url: str, source: ProviderSource
) -> list[str]:
    try:
        url = f"{base_url.rstrip('/')}{source.endpoint}"
        headers, params = {}, {}
        if source.auth_type == "header" and source.api_key_field:
            api_key = get_config().get(provider_id, {}).get("apiKey", "")
            if api_key:
                val = (
                    f"Bearer {api_key}"
                    if source.api_key_field == "Authorization"
                    else api_key
                )
                headers[source.api_key_field] = val
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(url, headers=headers, params=params)
            if not resp.is_success:
                return []
            data = resp.json()
            if provider_id == "ollama":
                return [
                    m.get("name", "") for m in data.get("models", []) if m.get("name")
                ]
            return [m.get("id", "") for m in data.get("data", []) if m.get("id")]
    except Exception as e:
        logger.warning("[providers] failed {}: {}", provider_id, e)
        return []


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@router.get("/providers")
async def list_providers():
    configured = _get_configured_providers()
    config = get_config()
    active = config.get("_activeProvider", "ollama")
    fallback = config.get("_fallbackChain", [])
    embedding = config.get("_embeddingModel", "")
    result = []
    for pid, src in PROVIDER_SOURCES.items():
        meta = PROVIDER_META.get(pid, {})
        pc = config.get(pid, {})
        is_cfg = pid in configured
        base = pc.get("url", "") or meta.get("base_url", "")
        api_key = pc.get("apiKey", "")

        models = (
            await _fetch_models_from_api(pid, base, src)
            if (src.type == ProviderSourceType.API and is_cfg)
            else list(src.catalog)
        )

        # Health check — skip for providers without API key (except no-auth ones)
        if is_cfg or pid in ("ollama", "openCode", "lmstudio"):
            status, latency = await _get_health(pid, base, src, api_key)
        else:
            status, latency = "unknown", 0

        result.append(
            {
                "id": pid,
                "name": meta.get("name", pid),
                "base_url": base,
                "editable_url": meta.get("editable_url", False),
                "configured": is_cfg,
                "models": models,
                "default_model": pc.get("model", ""),
                "fast_model": pc.get("fastModel", ""),
                "status": status,
                "latency": latency,
            }
        )
    return {
        "providers": result,
        "activeProvider": active,
        "fallbackChain": fallback,
        "embeddingModel": embedding,
    }
