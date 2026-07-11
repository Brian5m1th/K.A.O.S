"""
OpenAIAdapter / GeminiAdapter / ClaudeAdapter — Cloud LLM adapters.

Each wraps the existing provider implementation through InferencePort.
"""

from typing import AsyncIterator
from langchain_core.messages import HumanMessage, SystemMessage
from app.domain.ports.inference_port import InferencePort, InferenceRequest, InferenceResult
from app.config.settings import settings


def _to_langchain(messages: list[dict]) -> list:
    return [
        SystemMessage(content=m["content"]) if m.get("role") == "system"
        else HumanMessage(content=m["content"])
        for m in messages
    ]


class OpenAIAdapter(InferencePort):
    @property
    def provider_name(self) -> str: return "openai"

    async def invoke(self, request: InferenceRequest) -> InferenceResult:
        from app.llm.providers.openai_provider import OpenAIProvider
        provider = OpenAIProvider(
            model=request.model or settings.API_MODEL_ID,
            api_key=settings.OPENAI_API_KEY,
        )
        result = await provider.ainvoke(_to_langchain(request.messages))
        return InferenceResult(content=result.content, provider="openai", model=provider.model_name)

    async def stream(self, request: InferenceRequest) -> AsyncIterator[str]:
        from app.llm.providers.openai_provider import OpenAIProvider
        provider = OpenAIProvider(model=request.model or settings.API_MODEL_ID, api_key=settings.OPENAI_API_KEY)
        async for chunk in provider.astream(_to_langchain(request.messages)):
            yield chunk.content

    async def health(self) -> bool: return bool(settings.OPENAI_API_KEY)
    async def list_models(self) -> list[str]: return [settings.API_MODEL_ID]


class GeminiAdapter(InferencePort):
    @property
    def provider_name(self) -> str: return "gemini"

    async def invoke(self, request: InferenceRequest) -> InferenceResult:
        from app.llm.providers.gemini_provider import GeminiProvider
        provider = GeminiProvider(model=request.model or "gemini-pro", api_key=settings.GEMINI_API_KEY)
        result = await provider.ainvoke(_to_langchain(request.messages))
        return InferenceResult(content=result.content, provider="gemini", model=provider.model_name)

    async def stream(self, request: InferenceRequest) -> AsyncIterator[str]:
        from app.llm.providers.gemini_provider import GeminiProvider
        provider = GeminiProvider(model=request.model or "gemini-pro", api_key=settings.GEMINI_API_KEY)
        async for chunk in provider.astream(_to_langchain(request.messages)):
            yield chunk.content

    async def health(self) -> bool: return bool(settings.GEMINI_API_KEY)
    async def list_models(self) -> list[str]: return ["gemini-pro"]


class ClaudeAdapter(InferencePort):
    @property
    def provider_name(self) -> str: return "claude"

    async def invoke(self, request: InferenceRequest) -> InferenceResult:
        from app.llm.providers.claude_provider import ClaudeProvider
        provider = ClaudeProvider(model=request.model or "claude-sonnet", api_key=settings.ANTHROPIC_API_KEY)
        result = await provider.ainvoke(_to_langchain(request.messages))
        return InferenceResult(content=result.content, provider="claude", model=provider.model_name)

    async def stream(self, request: InferenceRequest) -> AsyncIterator[str]:
        from app.llm.providers.claude_provider import ClaudeProvider
        provider = ClaudeProvider(model=request.model or "claude-sonnet", api_key=settings.ANTHROPIC_API_KEY)
        async for chunk in provider.astream(_to_langchain(request.messages)):
            yield chunk.content

    async def health(self) -> bool: return bool(settings.ANTHROPIC_API_KEY)
    async def list_models(self) -> list[str]: return ["claude-sonnet", "claude-opus"]
