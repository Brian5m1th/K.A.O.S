import re
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
    logger.info(f"[info] chat - intent={intent.workflow.value}")

    if intent.workflow == WorkflowType.CHAT:
        result = await fast_route(request.message)
        if result:
            _cache.set(request.message, result)
            logger.debug("[finish] chat - send_message (CHAT)")
            return PlainTextResponse(result)

    elif intent.workflow == WorkflowType.RAG:
        router = MemoryRouter()

        async def memory_generator():
            async for token in router.stream(request.message, user_id=request.user_id):
                yield token

        logger.debug("[finish] chat - send_message (RAG)")
        return StreamingResponse(memory_generator(), media_type="text/plain")

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

        return StreamingResponse(ingest_stream(), media_type="text/plain")

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
    return StreamingResponse(token_generator(), media_type="text/plain")
