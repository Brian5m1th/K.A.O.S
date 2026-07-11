"""
InferencePort — LLM inference and model routing capability.

Provides a unified interface for text generation across local
and cloud LLM providers. The Desktop selects a model by name;
the backend routes to the appropriate provider (Ollama, AirLLM,
OpenAI, Gemini, Claude) through the ProviderRegistry.

Current providers: Ollama, OpenAI, Gemini, Claude, AirLLM.
Future: LLaMA.cpp, vLLM, Together AI.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, AsyncIterator


@dataclass
class InferenceRequest:
    """Unified inference request."""
    messages: list[dict]  # [{"role": "user", "content": "..."}]
    provider: str = "ollama"  # Provider key in registry
    model: Optional[str] = None  # Override default model
    temperature: float = 0.7
    max_tokens: int = 2048
    stream: bool = False


@dataclass
class InferenceResult:
    """Unified inference result."""
    content: str
    provider: str = ""
    model: str = ""
    tokens_used: int = 0
    latency_ms: float = 0.0
    cost_usd: float = 0.0


class InferencePort(ABC):
    """
    Interface for LLM model inference.

    Concrete implementations:
      - OllamaAdapter         (local — qwen3, llama3)
      - AirLLMAdapter         (local — layer-wise 70B models)
      - OpenAIAdapter         (cloud — GPT-4o)
      - GeminiAdapter         (cloud — Gemini Pro)
      - ClaudeAdapter         (cloud — Claude Sonnet/Opus)
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        ...

    @abstractmethod
    async def invoke(self, request: InferenceRequest) -> InferenceResult:
        """Non-streaming inference call."""
        ...

    @abstractmethod
    async def stream(self, request: InferenceRequest) -> AsyncIterator[str]:
        """Streaming inference call. Yields content chunks."""
        ...

    @abstractmethod
    async def health(self) -> bool:
        """Check if the provider is reachable and models are available."""
        ...

    @abstractmethod
    async def list_models(self) -> list[str]:
        """List available models for this provider."""
        ...
