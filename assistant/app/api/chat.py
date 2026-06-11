from loguru import logger
from fastapi import APIRouter
from fastapi.responses import StreamingResponse, PlainTextResponse

from app.domain.chat import ChatRequest
from app.router.intent_classifier import IntentClassifier, IntentType
from app.router.fast_router import fast_route
from app.router.memory_router import MemoryRouter
from app.router.smart_router import SmartRouter
from app.router.cache import ResponseCache

router = APIRouter(prefix="/api/chat", tags=["Chat"])

_classifier = IntentClassifier()
_cache = ResponseCache()
_smart_router = SmartRouter()


@router.post("/message")
async def send_message(
    request: ChatRequest,
) -> StreamingResponse:
    logger.info(f"[start] chat - send_message [user={request.user_id or 'anonymous'}]")

    cached = _cache.get(request.message)
    if cached is not None:
        logger.info("[info] chat - cache hit")
        return PlainTextResponse(cached)

    intent = await _classifier.classify(request.message)
    logger.info(f"[info] chat - intent={intent.value}")

    if intent == IntentType.FAST:
        result = await fast_route(request.message)
        if result:
            _cache.set(request.message, result)
            logger.debug("[finish] chat - send_message (FAST)")
            return PlainTextResponse(result)

    elif intent == IntentType.MEMORY:
        router = MemoryRouter()

        async def memory_generator():
            async for token in router.stream(request.message, user_id=request.user_id):
                yield token

        logger.debug("[finish] chat - send_message (MEMORY)")
        return StreamingResponse(memory_generator(), media_type="text/plain")

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

    logger.debug("[finish] chat - send_message (SMART)")
    return StreamingResponse(token_generator(), media_type="text/plain")
