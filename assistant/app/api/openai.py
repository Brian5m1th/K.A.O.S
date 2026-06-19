import json
import time
import uuid
from typing import AsyncIterator

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse, JSONResponse
from loguru import logger
from pydantic import BaseModel, Field

from app.config.settings import settings
from app.llm.factory import LLMFactory
from app.service.agent_service import AgentService
from app.router.intent_classifier import IntentClassifier, IntentType
from app.router.fast_router import fast_route
from app.router.memory_router import MemoryRouter
from app.router.cache import ResponseCache


# Lazy-loaded classifier
_classifier: IntentClassifier | None = None
_factory: LLMFactory | None = None
_cache = ResponseCache()


def _get_classifier() -> IntentClassifier:
    global _classifier
    if _classifier is None:
        _classifier = IntentClassifier()
    return _classifier


def _get_factory() -> LLMFactory:
    global _factory
    if _factory is None:
        _factory = LLMFactory()
    return _factory


router = APIRouter(prefix="/v1", tags=["OpenAI"])
legacy_router = APIRouter(tags=["Legacy"])


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str = Field(default=settings.API_MODEL_ID)
    messages: list[ChatMessage]
    stream: bool = Field(default=True)
    max_tokens: int = Field(default=4096, ge=1, le=32768)
    user_id: str = Field(default="", description="ID do usuário (opcional)")
    username: str = Field(default="", description="Nome do usuário (opcional)")
    role: str = Field(default="user", description="Papel do usuário (opcional)")


def _get_agent() -> AgentService:
    return AgentService()


def _models():
    return [
        {
            "id": settings.API_MODEL_ID,
            "object": "model",
            "created": 0,
            "owned_by": "kaos",
        },
        {
            "id": settings.FAST_MODEL_ID,
            "object": "model",
            "created": 0,
            "owned_by": "kaos",
        },
        {
            "id": settings.DEFAULT_MODEL_ID,
            "object": "model",
            "created": 0,
            "owned_by": "kaos",
        },
    ]


def _models_response():
    return JSONResponse(
        content={
            "object": "list",
            "data": _models(),
        }
    )


@legacy_router.get("/models")
async def list_models_legacy():
    logger.info("[start] openai - list_models_legacy")
    logger.debug("[finish] openai - list_models_legacy")
    return _models_response()


@legacy_router.post("/chat/completions")
async def chat_completions_legacy(
    body: ChatCompletionRequest,
    http_request: Request,
) -> StreamingResponse:
    uid = body.user_id or http_request.state.user_id
    logger.info(f"[start] openai - chat_completions_legacy [user={uid or 'anonymous'}]")
    return await chat_completions(body, http_request)


@router.get("/models")
async def list_models():
    logger.info("[start] openai - list_models")
    logger.debug("[finish] openai - list_models")
    return _models_response()


# Removed module-level classifier - now lazy-loaded via _get_classifier()
_cache = ResponseCache()


async def _sse_stream_generator(
    stream_id: str,
    created: int,
    model: str,
    stream: AsyncIterator[str],
) -> AsyncIterator[str]:
    async for token in stream:
        chunk = {
            "id": stream_id,
            "object": "chat.completion.chunk",
            "created": created,
            "model": model,
            "choices": [
                {
                    "index": 0,
                    "delta": {"content": token},
                    "finish_reason": None,
                }
            ],
        }
        yield f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n"
    final = {
        "id": stream_id,
        "object": "chat.completion.chunk",
        "created": created,
        "model": model,
        "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}],
    }
    yield f"data: {json.dumps(final, ensure_ascii=False)}\n\n"
    yield "data: [DONE]\n\n"


def _resolve_model(api_model: str) -> str:
    """Map API model ID to a model key for the LLMFactory."""
    config = _get_factory()._resolve_model_config(api_model)
    return config["model"]


@router.post("/chat/completions")
async def chat_completions(
    body: ChatCompletionRequest,
    http_request: Request,
) -> StreamingResponse:
    user_id = body.user_id or http_request.state.user_id
    username = body.username or http_request.state.username
    role = body.role or http_request.state.role
    logger.info(f"[start] openai - chat_completions [user={user_id or 'anonymous'}]")
    stream_id = f"chatcmpl-{uuid.uuid4().hex[:12]}"
    created = int(__import__("time").time())
    session_id = stream_id

    user_message = next(
        (m.content for m in reversed(body.messages) if m.role == "user"),
        body.messages[-1].content if body.messages else "",
    )

    cached = _cache.get(user_message)
    if cached is not None:
        logger.info("[info] openai - cache hit")

        async def _cached_stream():
            yield cached

        return StreamingResponse(
            _sse_stream_generator(stream_id, created, body.model, _cached_stream()),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )

    if body.model == settings.FAST_MODEL_ID:
        intent = IntentType.FAST
        logger.info(f"[info] openai - model={body.model} -> forced FAST")
    else:
        intent = await _get_classifier().classify(user_message)
        logger.info(f"[info] openai - intent={intent.value}")

    if intent == IntentType.FAST:
        start = time.perf_counter()
        result = await fast_route(user_message)
        if result:
            _cache.set(user_message, result)

            async def _fast_stream():
                yield result

            elapsed = (time.perf_counter() - start) * 1000
            logger.info(
                f"[audit] generation | route=FAST | user={user_id or 'anonymous'} | "
                f"latency_ms={elapsed:.0f}"
            )
            return StreamingResponse(
                _sse_stream_generator(stream_id, created, body.model, _fast_stream()),
                media_type="text/event-stream",
                headers={
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "X-Accel-Buffering": "no",
                },
            )

        # FAST intent mas sem tool: resposta simples
        async def _simple_stream():
            yield "Olá! Como posso ajudar você hoje?"

        elapsed = (time.perf_counter() - start) * 1000
        logger.info(
            f"[audit] generation | route=FAST | user={user_id or 'anonymous'} | "
            f"latency_ms={elapsed:.0f}"
        )
        return StreamingResponse(
            _sse_stream_generator(stream_id, created, body.model, _simple_stream()),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )

    elif intent == IntentType.MEMORY:
        start = time.perf_counter()
        model_key = _resolve_model(body.model)
        router = MemoryRouter(model=model_key)

        return StreamingResponse(
            _sse_stream_generator(
                stream_id,
                created,
                body.model,
                router.stream(user_message, user_id=user_id),
            ),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )

    # SMART route (LangGraph)
    agent = _get_agent()
    logger.info("[sending] openai - streaming via LangGraph Agent (SMART)")
    model_key = _resolve_model(body.model)

    return StreamingResponse(
        _sse_stream_generator(
            stream_id,
            created,
            body.model,
            agent.stream_message(
                session_id=session_id,
                user_message=user_message,
                user_id=user_id,
                username=username,
                role=role,
                model=model_key,
            ),
        ),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
