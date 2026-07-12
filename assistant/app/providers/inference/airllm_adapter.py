"""
AirLLMAdapter — Wraps AirLLMProvider for InferencePort.

Layer-wise inference for large models (70B+) on consumer GPUs.
Best for batch/documentation tasks, not real-time chat.
"""

from typing import AsyncIterator

from langchain_core.messages import HumanMessage, SystemMessage
from app.domain.ports.inference_port import (
    InferencePort,
    InferenceRequest,
    InferenceResult,
)


class AirLLMAdapter(InferencePort):
    """Local AirLLM layer-wise inference adapter."""

    @property
    def provider_name(self) -> str:
        return "airllm"

    async def invoke(self, request: InferenceRequest) -> InferenceResult:
        from app.llm.providers.airllm_provider import AirLLMProvider

        provider = AirLLMProvider(model=request.model or "default")
        messages = self._to_langchain(request.messages)
        result = await provider.ainvoke(messages)
        return InferenceResult(
            content=result.content,
            provider="airllm",
            model=provider.model_name,
        )

    async def stream(self, request: InferenceRequest) -> AsyncIterator[str]:
        from app.llm.providers.airllm_provider import AirLLMProvider

        provider = AirLLMProvider(model=request.model or "default")
        messages = self._to_langchain(request.messages)
        async for chunk in provider.astream(messages):
            yield chunk.content

    async def health(self) -> bool:
        try:
            import importlib

            return importlib.util.find_spec("airllm") is not None
        except Exception:
            return False

    async def list_models(self) -> list[str]:
        return ["airllm-meta-llama/Meta-Llama-3-8B", "airllm-qwen/Qwen-2.5-14B"]

    @staticmethod
    def _to_langchain(messages: list[dict]) -> list:
        return [
            SystemMessage(content=m["content"])
            if m["role"] == "system"
            else HumanMessage(content=m["content"])
            for m in messages
        ]
