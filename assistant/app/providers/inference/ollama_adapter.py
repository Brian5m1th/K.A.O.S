"""
OllamaAdapter — Wraps OllamaProvider for InferencePort.

Provides local LLM inference via Ollama.
"""

from typing import AsyncIterator

from langchain_core.messages import HumanMessage, SystemMessage
from app.domain.ports.inference_port import (
    InferencePort,
    InferenceRequest,
    InferenceResult,
)
from app.config.settings import settings


class OllamaAdapter(InferencePort):
    """Local Ollama inference adapter."""

    @property
    def provider_name(self) -> str:
        return "ollama"

    async def invoke(self, request: InferenceRequest) -> InferenceResult:
        from app.llm.providers.ollama_provider import OllamaProvider

        provider = OllamaProvider(
            model=request.model or settings.OLLAMA_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
        )
        messages = self._to_langchain(request.messages)
        result = await provider.ainvoke(messages)
        return InferenceResult(
            content=result.content,
            provider="ollama",
            model=provider.model_name,
        )

    async def stream(self, request: InferenceRequest) -> AsyncIterator[str]:
        from app.llm.providers.ollama_provider import OllamaProvider

        provider = OllamaProvider(
            model=request.model or settings.OLLAMA_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
        )
        messages = self._to_langchain(request.messages)
        async for chunk in provider.astream(messages):
            yield chunk.content

    async def health(self) -> bool:
        import httpx

        try:
            ollama_url = settings.OLLAMA_BASE_URL.rstrip("/")
            async with httpx.AsyncClient(timeout=3) as c:
                r = await c.get(f"{ollama_url}/api/tags")
                return r.is_success
        except Exception:
            return False

    async def list_models(self) -> list[str]:
        import httpx

        try:
            ollama_url = settings.OLLAMA_BASE_URL.rstrip("/")
            async with httpx.AsyncClient(timeout=3) as c:
                r = await c.get(f"{ollama_url}/api/tags")
                if r.is_success:
                    return [m["name"] for m in r.json().get("models", [])]
        except Exception:
            pass
        return [settings.OLLAMA_MODEL]

    @staticmethod
    def _to_langchain(messages: list[dict]) -> list:
        result = []
        for m in messages:
            role = m.get("role", "user")
            content = m.get("content", "")
            if role == "system":
                result.append(SystemMessage(content=content))
            else:
                result.append(HumanMessage(content=content))
        return result
