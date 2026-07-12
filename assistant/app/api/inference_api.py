"""
Inference REST API — LLM model inference and provider management.

Endpoints:
  POST /api/inference/invoke     — Non-streaming inference
  POST /api/inference/stream     — Streaming inference (SSE)
  GET  /api/inference/models     — List available models per provider
  GET  /api/inference/health     — Health of all providers
"""

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional

from app.core.services.inference_service import InferenceService
from app.domain.ports.inference_port import InferenceRequest
import json

router = APIRouter(prefix="/api/inference", tags=["Inference"])


class InvokeRequest(BaseModel):
    messages: list[dict]
    provider: str = "ollama"
    model: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 2048


def get_inference_service() -> InferenceService:
    from app.providers.inference.ollama_adapter import OllamaAdapter
    from app.providers.inference.airllm_adapter import AirLLMAdapter
    from app.providers.inference.openai_adapter import (
        OpenAIAdapter,
        GeminiAdapter,
        ClaudeAdapter,
    )

    svc = InferenceService()
    svc.registry.register("ollama", OllamaAdapter())
    svc.registry.register("airllm", AirLLMAdapter())
    svc.registry.register("openai", OpenAIAdapter())
    svc.registry.register("gemini", GeminiAdapter())
    svc.registry.register("claude", ClaudeAdapter())
    return svc


@router.post("/invoke")
async def invoke_inference(
    body: InvokeRequest,
    inf: InferenceService = Depends(get_inference_service),
):
    """Non-streaming LLM inference."""
    request = InferenceRequest(
        messages=body.messages,
        provider=body.provider,
        model=body.model,
        temperature=body.temperature,
        max_tokens=body.max_tokens,
    )
    result = await inf.invoke(request)
    return {
        "content": result.content,
        "provider": result.provider,
        "model": result.model,
        "tokens_used": result.tokens_used,
        "latency_ms": result.latency_ms,
    }


@router.post("/stream")
async def stream_inference(
    body: InvokeRequest,
    inf: InferenceService = Depends(get_inference_service),
):
    """Streaming LLM inference via Server-Sent Events."""
    request = InferenceRequest(
        messages=body.messages,
        provider=body.provider,
        model=body.model,
        temperature=body.temperature,
        max_tokens=body.max_tokens,
        stream=True,
    )

    async def generate():
        async for chunk in inf.stream(request):
            yield f"data: {json.dumps({'content': chunk})}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")


@router.get("/models")
async def list_models(inf: InferenceService = Depends(get_inference_service)):
    """List available models grouped by provider."""
    return await inf.list_models()


@router.get("/health")
async def inference_health(inf: InferenceService = Depends(get_inference_service)):
    return await inf.health()
