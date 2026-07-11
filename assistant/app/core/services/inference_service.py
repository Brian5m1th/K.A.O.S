"""
InferenceService — LLM inference orchestrator.

Routes inference requests to the appropriate provider (Ollama, AirLLM,
OpenAI, Gemini, Claude) through the ProviderRegistry.
"""

from typing import AsyncIterator
from app.core.provider_registry import ProviderRegistry
from app.domain.ports.inference_port import InferencePort, InferenceRequest, InferenceResult


class InferenceService:
    """Service for LLM model inference across multiple providers."""

    def __init__(self):
        self.registry = ProviderRegistry[InferencePort]("inference")

    async def invoke(self, request: InferenceRequest) -> InferenceResult:
        provider = self._resolve_provider(request.provider)
        return await provider.invoke(request)

    async def stream(self, request: InferenceRequest) -> AsyncIterator[str]:
        provider = self._resolve_provider(request.provider)
        async for chunk in provider.stream(request):
            yield chunk

    async def list_models(self) -> dict[str, list[str]]:
        models = {}
        for key in self.registry.list_providers():
            try:
                self.registry.activate(key)
                models[key] = await self.registry.active.list_models()
            except Exception:
                models[key] = []
        return models

    async def health(self) -> dict:
        provider = self.registry.active_key or "none"
        ok = await self.registry.active.health()
        return {
            "service": "inference",
            "healthy": ok,
            "active_provider": provider,
            "available_providers": self.registry.list_providers(),
        }

    def _resolve_provider(self, provider_key: str) -> InferencePort:
        if provider_key in self.registry:
            self.registry.activate(provider_key)
        return self.registry.active
