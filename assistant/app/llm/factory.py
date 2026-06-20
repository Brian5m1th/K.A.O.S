import asyncio

from loguru import logger

from app.config.settings import settings
from app.llm.provider import BaseProvider
from app.llm.metrics import ProviderMetrics
from app.setup.provider_config import get_active_provider_config


class LLMFactory:
    def __init__(self):
        self._cache: dict[str, BaseProvider] = {}
        self._metrics = ProviderMetrics()
        self._fallbacks = self._parse_fallback_chain()

    def _parse_fallback_chain(self) -> list[dict]:
        raw = settings.FALLBACK_CHAIN
        chain = []
        for entry in raw.split(","):
            entry = entry.strip()
            if not entry:
                continue
            parts = entry.split(":")
            provider = parts[0]
            model = ":".join(parts[1:]) if len(parts) > 1 else settings.OLLAMA_MODEL
            if not model:
                model = settings.OLLAMA_MODEL
            chain.append({"provider": provider, "model": model})
        return chain

    def build(self, model_key: str, **kwargs) -> BaseProvider:
        if model_key in self._cache:
            return self._cache[model_key]

        resolved = self._resolve_model_config(model_key)
        provider = self._create_provider(
            provider_name=resolved["provider"],
            model_name=resolved["model"],
            **kwargs,
        )
        self._cache[model_key] = provider
        logger.info(
            f"[info] LLMFactory - built: {resolved['provider']}/{resolved['model']} (key={model_key})"
        )
        return provider

    def _resolve_model_config(self, model_key: str) -> dict:
        active = get_active_provider_config()

        model_map = {
            settings.API_MODEL_ID: {
                "provider": active["provider"],
                "model": active["model"],
            },
            settings.FAST_MODEL_ID: {
                "provider": active["provider"],
                "model": active["fastModel"],
            },
            settings.DEFAULT_MODEL_ID: {
                "provider": active["provider"],
                "model": active["model"],
            },
        }

        if model_key in model_map:
            return model_map[model_key]

        if model_key in settings.MODEL_MAP:
            return settings.MODEL_MAP[model_key]

        return {"provider": active["provider"], "model": model_key}

    def _create_provider(
        self, provider_name: str, model_name: str, **kwargs
    ) -> BaseProvider:
        if provider_name == "ollama":
            from app.llm.providers.ollama_provider import OllamaProvider

            return OllamaProvider(
                model=model_name,
                base_url=kwargs.get("base_url", settings.OLLAMA_BASE_URL),
                **kwargs,
            )
        elif provider_name == "openai":
            from app.llm.providers.openai_provider import OpenAIProvider

            return OpenAIProvider(
                model=model_name, api_key=settings.OPENAI_API_KEY, **kwargs
            )
        elif provider_name == "claude":
            from app.llm.providers.claude_provider import ClaudeProvider

            return ClaudeProvider(
                model=model_name, api_key=settings.ANTHROPIC_API_KEY, **kwargs
            )
        elif provider_name == "gemini":
            from app.llm.providers.gemini_provider import GeminiProvider

            return GeminiProvider(
                model=model_name, api_key=settings.GEMINI_API_KEY, **kwargs
            )
        else:
            logger.warning(
                f"[warn] LLMFactory - provider desconhecido: {provider_name}, fallback Ollama"
            )
            from app.llm.providers.ollama_provider import OllamaProvider

            return OllamaProvider(
                model=model_name, base_url=settings.OLLAMA_BASE_URL, **kwargs
            )

    async def ainvoke_with_fallback(
        self, model_key: str, messages: list, **kwargs
    ) -> str:
        return await self._fallback_invoke(model_key, messages, 0, **kwargs)

    async def _fallback_invoke(
        self, model_key: str, messages: list, index: int, **kwargs
    ) -> str:
        if index >= len(self._fallbacks):
            raise RuntimeError("Todos os providers da fallback chain falharam")

        if self._fallbacks:
            config = self._fallbacks[index]
            provider = self._create_provider(
                config["provider"], config["model"], **kwargs
            )
            logger.info(
                f"[info] LLMFactory - fallback[{index}]: {config['provider']}/{config['model']}"
            )
        else:
            provider = self.build(model_key, **kwargs)

        try:
            return await asyncio.wait_for(
                self._metrics.ainvoke_and_record(provider, messages),
                timeout=30.0,
            )
        except asyncio.TimeoutError:
            logger.warning(f"[warn] LLMFactory - fallback[{index}] timeout")
            return await self._fallback_invoke(model_key, messages, index + 1, **kwargs)
        except Exception as e:
            logger.warning(f"[warn] LLMFactory - fallback[{index}] falhou: {e}")
            return await self._fallback_invoke(model_key, messages, index + 1, **kwargs)

    @property
    def metrics(self) -> ProviderMetrics:
        return self._metrics
