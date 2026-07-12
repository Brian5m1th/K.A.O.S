"""
Inference adapters — Wrap existing LLM providers as InferencePort implementations.

Each adapter wraps an existing provider (Ollama, AirLLM, OpenAI, Gemini, Claude)
and exposes it through the InferencePort interface.
"""

from app.providers.inference.ollama_adapter import OllamaAdapter
from app.providers.inference.airllm_adapter import AirLLMAdapter
from app.providers.inference.openai_adapter import OpenAIAdapter
from app.providers.inference.openai_adapter import GeminiAdapter
from app.providers.inference.openai_adapter import ClaudeAdapter

__all__ = [
    "OllamaAdapter",
    "AirLLMAdapter",
    "OpenAIAdapter",
    "GeminiAdapter",
    "ClaudeAdapter",
]
