import json
import time
import uuid
from typing import AsyncIterator

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse, JSONResponse, Response
from loguru import logger
from pydantic import BaseModel, Field, ConfigDict

from app.config.settings import settings
from app.llm.factory import LLMFactory
from app.service.agent_service import AgentService
from app.router.intent_classifier import IntentClassifier
from app.router.workflow_router import WorkflowRouter
from app.router.memory_workflow import MemoryWorkflow
from app.router.fast_router import fast_route
from app.router.memory_router import MemoryRouter
from app.router.cache import ResponseCache
from app.setup.provider_config import get_config_version
from app.domain.workflow import WorkflowType
from app.domain.context import RequestContext
from app.domain.identity import WorkspaceIdentity, UserIdentity
from app.domain.chat import Message

SSE_HEADERS = {
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "X-Accel-Buffering": "no",
}

_classifier: IntentClassifier | None = None
_classifier_version: int = -1
_factory: LLMFactory | None = None
_factory_version: int = -1
_cache = ResponseCache()
_router = WorkflowRouter()


def _get_classifier() -> IntentClassifier:
    global _classifier, _classifier_version
    version = get_config_version()
    if _classifier is None or _classifier_version != version:
        _classifier = IntentClassifier()
        _classifier_version = version
    return _classifier


def _get_factory() -> LLMFactory:
    global _factory, _factory_version
    version = get_config_version()
    if _factory is None or _factory_version != version:
        _factory = LLMFactory()
        _factory_version = version
    return _factory


router = APIRouter(prefix="/v1", tags=["OpenAI"])
legacy_router = APIRouter(tags=["Legacy"])


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

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
    return _models_response()


def _json_response(
    stream_id: str, created: int, model: str, content: str
) -> JSONResponse:
    return JSONResponse(
        {
            "id": stream_id,
            "object": "chat.completion",
            "created": created,
            "model": model,
            "choices": [
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": content},
                    "finish_reason": "stop",
                }
            ],
            "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
        }
    )


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


async def _collect_stream(stream: AsyncIterator[str]) -> str:
    parts = []
    async for token in stream:
        parts.append(token)
    return "".join(parts)


async def _respond(
    stream_id: str,
    created: int,
    model: str,
    token_stream: AsyncIterator[str],
    do_stream: bool,
) -> Response:
    if do_stream:
        return StreamingResponse(
            _sse_stream_generator(stream_id, created, model, token_stream),
            media_type="text/event-stream",
            headers=SSE_HEADERS,
        )
    content = await _collect_stream(token_stream)
    return JSONResponse(
        {
            "id": stream_id,
            "object": "chat.completion",
            "created": created,
            "model": model,
            "choices": [
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": content},
                    "finish_reason": "stop",
                }
            ],
            "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
        }
    )


def _resolve_model(api_model: str) -> str:
    config = _get_factory()._resolve_model_config(api_model)
    return config["model"]


def _build_context(
    body: ChatCompletionRequest, http_request: Request, session_id: str
) -> RequestContext:
    trace_id = uuid.uuid4()
    execution_id = uuid.uuid4()
    user_id_str = body.user_id or http_request.state.user_id or str(uuid.uuid4())
    uid = uuid.uuid5(uuid.NAMESPACE_DNS, user_id_str)
    ws_id = uuid.uuid5(uuid.NAMESPACE_DNS, "kaos-workspace")
    slug = body.username or http_request.state.username or "kaos"
    history = [Message(role=m.role, content=m.content) for m in body.messages]
    return RequestContext(
        execution_id=execution_id,
        trace_id=trace_id,
        workspace=WorkspaceIdentity(workspace_id=ws_id, owner_user_id=uid, slug="kaos"),
        user=UserIdentity(user_id=uid, workspace_id=ws_id, slug=slug),
        api_key_id=None,
        session_id=uuid.uuid5(uuid.NAMESPACE_DNS, session_id),
        history=history,
        workflow="",
        metadata={},
    )


@router.post("/chat/completions")
async def chat_completions(
    body: ChatCompletionRequest,
    http_request: Request,
) -> Response:
    user_id = body.user_id or http_request.state.user_id
    role = body.role or http_request.state.role
    logger.info(f"[start] openai - chat_completions [user={user_id or 'anonymous'}]")
    stream_id = f"chatcmpl-{uuid.uuid4().hex[:12]}"
    created = int(time.time())
    session_id = stream_id

    user_message = next(
        (m.content for m in reversed(body.messages) if m.role == "user"),
        body.messages[-1].content if body.messages else "",
    )

    cached = _cache.get(user_message)
    if cached is not None:

        async def _cached_stream():
            yield cached

        return await _respond(
            stream_id, created, body.model, _cached_stream(), body.stream
        )

    if body.model == settings.FAST_MODEL_ID:
        from app.domain.intent import IntentResult

        intent = IntentResult(workflow=WorkflowType.CHAT, confidence=1.0)
        logger.info(f"[info] openai - model={body.model} -> forced CHAT")
    else:
        intent = await _get_classifier().classify(user_message)
        logger.info(f"[info] openai - intent={intent.workflow.value}")

    context = _build_context(body, http_request, session_id)
    resolved = _router.resolve(intent, context)

    if resolved == WorkflowType.CHAT:
        start = time.perf_counter()
        result = await fast_route(user_message)
        if result:
            _cache.set(user_message, result)

            async def _fast_stream():
                yield result

            elapsed = round((time.perf_counter() - start) * 1000, 2)
            logger.bind(
                event="generation.completed",
                route=resolved.value,
                user_id=str(context.user.user_id),
                trace_id=str(context.trace_id),
                execution_id=str(context.execution_id),
                latency_ms=elapsed,
            ).info(
                f"[audit] generation | route={resolved.value} | latency_ms={elapsed}"
            )
            return await _respond(
                stream_id, created, body.model, _fast_stream(), body.stream
            )

        # Se nenhuma tool foi reconhecida, faz fallback para o AGENT
        logger.info("[info] openai - CHAT/FAST route fallback to AGENT")

    elif resolved == WorkflowType.RAG:
        start = time.perf_counter()
        model_key = _resolve_model(body.model)
        router = MemoryRouter(model=model_key)
        result = await router.process(user_message, user_id=str(context.user.user_id))
        elapsed = round((time.perf_counter() - start) * 1000, 2)
        logger.bind(
            event="generation.completed",
            route=resolved.value,
            user_id=str(context.user.user_id),
            trace_id=str(context.trace_id),
            execution_id=str(context.execution_id),
            latency_ms=elapsed,
        ).info(f"[audit] generation | route={resolved.value} | latency_ms={elapsed}")

        async def _rag_stream():
            yield result

        return await _respond(
            stream_id, created, body.model, _rag_stream(), body.stream
        )

    elif resolved == WorkflowType.MEMORY:
        start = time.perf_counter()
        workflow = MemoryWorkflow()
        result = await workflow.execute(intent.command, context)
        elapsed = round((time.perf_counter() - start) * 1000, 2)
        logger.bind(
            event="generation.completed",
            route=resolved.value,
            user_id=str(context.user.user_id),
            trace_id=str(context.trace_id),
            execution_id=str(context.execution_id),
            latency_ms=elapsed,
        ).info(
            f"[audit] generation | route={resolved.value} | command={intent.command.value if intent.command else 'none'} | latency_ms={elapsed}"
        )

        async def _memory_stream():
            yield result or "Comando de memória executado."

        return await _respond(
            stream_id, created, body.model, _memory_stream(), body.stream
        )

    elif resolved == WorkflowType.INGEST:
        from app.agent.graph import ingest_source

        start = time.perf_counter()
        result = await ingest_source(user_message)
        elapsed = round((time.perf_counter() - start) * 1000, 2)
        logger.bind(
            event="generation.completed",
            route=resolved.value,
            latency_ms=elapsed,
        ).info(f"[audit] generation | route={resolved.value} | latency_ms={elapsed}")

        async def _ingest_stream():
            yield str(result) if result else "Fonte ingerida."

        return await _respond(
            stream_id, created, body.model, _ingest_stream(), body.stream
        )

    # AGENT route (LangGraph)
    agent = _get_agent()
    model_key = _resolve_model(body.model)
    logger.info("[sending] openai - streaming via LangGraph Agent (AGENT)")
    return await _respond(
        stream_id,
        created,
        body.model,
        agent.stream_message(
            session_id=session_id,
            user_message=user_message,
            user_id=str(context.user.user_id),
            username=context.user.slug,
            role=role,
            model=model_key,
        ),
        body.stream,
    )
