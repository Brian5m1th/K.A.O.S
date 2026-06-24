import asyncio
import re
from typing import AsyncIterator
from uuid import UUID

from loguru import logger
from fastapi import APIRouter
from fastapi.responses import StreamingResponse, PlainTextResponse

from app.domain.chat import ChatRequest
from app.router.intent_classifier import IntentClassifier
from app.router.fast_router import fast_route
from app.router.memory_router import MemoryRouter
from app.router.smart_router import SmartRouter
from app.router.cache import ResponseCache
from app.domain.workflow import WorkflowType
from app.setup.provider_config import get_config_version
from app.repositories.conversation_repository import (
    ConversationRepository,
    ConversationTurn,
)

router = APIRouter(prefix="/api/chat", tags=["Chat"])

_classifier: IntentClassifier | None = None
_classifier_version: int = -1
_cache = ResponseCache()
_smart_router = SmartRouter()


def _get_classifier() -> IntentClassifier:
    global _classifier, _classifier_version
    version = get_config_version()
    if _classifier is None or _classifier_version != version:
        _classifier = IntentClassifier()
        _classifier_version = version
    return _classifier


def _extract_source_path(message: str) -> str | None:
    match = re.search(
        r"(?:source|fonte|documento|arquivo)\s+([\w\-./]+\.\w+)", message, re.IGNORECASE
    )
    if match:
        return match.group(1)
    words = message.strip().split()
    last = words[-1] if words else ""
    if "." in last and not last.endswith("."):
        return last
    return None


# ── Persistência de conversas (fire-and-forget) ─────────────────────


async def _persist_turn(
    db_session_factory,
    session_id: str,
    user_id: str,
    role: str,
    content: str,
    workflow_type: str | None = None,
    tokens_used: int = 0,
    model_used: str | None = None,
    provider: str | None = None,
) -> None:
    """Salva um turno de conversa no PostgreSQL. Fire-and-forget friendly."""
    try:
        async with db_session_factory() as session:
            repo = ConversationRepository(session)
            await repo.save(
                ConversationTurn(
                    session_id=UUID(session_id),
                    user_id=user_id or "anonymous",
                    role=role,
                    content=content,
                    workflow_type=workflow_type,
                    tokens_used=tokens_used,
                    model_used=model_used,
                    provider=provider,
                )
            )
    except Exception as exc:
        logger.debug("[conversation] falha ao persistir turno: {}", exc)


async def _persist_conversation(
    request: ChatRequest,
    user_msg: str,
    assistant_msg: str,
    workflow_type: str | None,
    model_used: str | None = None,
    provider: str | None = None,
) -> None:
    """Dispara persistência do turno user + assistant em background."""
    from app.database import async_session_factory

    factory = async_session_factory()
    uid = request.user_id or "anonymous"
    sid = request.session_id
    user_tokens = len(user_msg.split()) * 1.3  # estimativa simples
    assistant_tokens = len(assistant_msg.split()) * 1.3
    total_tokens = int(user_tokens + assistant_tokens)

    # Salvar user turn
    asyncio.create_task(
        _persist_turn(
            factory,
            sid,
            uid,
            "user",
            user_msg,
            workflow_type=workflow_type,
        )
    )
    # Salvar assistant turn
    asyncio.create_task(
        _persist_turn(
            factory,
            sid,
            uid,
            "assistant",
            assistant_msg,
            workflow_type=workflow_type,
            tokens_used=total_tokens,
            model_used=model_used,
            provider=provider,
        )
    )
    logger.debug("[conversation] persist triggered: session={}", sid)


def _wrap_stream_with_persist(
    gen: AsyncIterator[str],
    request: ChatRequest,
    workflow_type: str,
) -> AsyncIterator[str]:
    """Wrapper que coleta tokens do generator e persiste ao final."""

    async def wrapper():
        collected = ""
        async for token in gen:
            collected += token
            yield token
        # Ao final do stream, salvar a conversa
        asyncio.create_task(
            _persist_conversation(
                request=request,
                user_msg=request.message,
                assistant_msg=collected,
                workflow_type=workflow_type,
            )
        )

    return wrapper()


# ── Endpoint ─────────────────────────────────────────────────────────


@router.post("/message")
async def send_message(
    request: ChatRequest,
) -> StreamingResponse:
    logger.info(f"[start] chat - send_message [user={request.user_id or 'anonymous'}]")

    cached = _cache.get(request.message)
    if cached is not None:
        logger.info("[info] chat - cache hit")
        return PlainTextResponse(cached)

    intent = await _get_classifier().classify(request.message)
    wf = intent.workflow.value
    logger.info(f"[info] chat - intent={wf}")

    if intent.workflow == WorkflowType.CHAT:
        result = await fast_route(request.message)
        if result:
            _cache.set(request.message, result)
            # Persist fire-and-forget
            asyncio.create_task(
                _persist_conversation(
                    request=request,
                    user_msg=request.message,
                    assistant_msg=result,
                    workflow_type="FAST",
                )
            )
            logger.debug("[finish] chat - send_message (CHAT)")
            return PlainTextResponse(result)

    elif intent.workflow == WorkflowType.RAG:
        router = MemoryRouter()

        async def memory_generator():
            async for token in router.stream(request.message, user_id=request.user_id):
                yield token

        logger.debug("[finish] chat - send_message (RAG)")
        return StreamingResponse(
            _wrap_stream_with_persist(memory_generator(), request, "MEMORY"),
            media_type="text/plain",
        )

    elif intent.workflow == WorkflowType.INGEST:
        source_path = _extract_source_path(request.message)
        logger.info(f"[info] chat - INGEST source_path={source_path}")

        async def ingest_stream():
            async for token in _smart_router.stream(
                session_id=request.session_id,
                user_message=request.message,
                user_id=request.user_id,
                username=request.username,
                role=request.role,
                ingest_source_path=source_path,
            ):
                yield token

        return StreamingResponse(
            _wrap_stream_with_persist(ingest_stream(), request, "AGENT"),
            media_type="text/plain",
        )

    logger.info("[sending] chat - mensagem para smart_router (LangGraph)")

    async def token_generator():
        async for token in _smart_router.stream(
            session_id=request.session_id,
            user_message=request.message,
            user_id=request.user_id,
            username=request.username,
            role=request.role,
        ):
            yield token

    logger.debug("[finish] chat - send_message (AGENT)")
    return StreamingResponse(
        _wrap_stream_with_persist(token_generator(), request, "AGENT"),
        media_type="text/plain",
    )
