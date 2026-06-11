import json
import uuid
from typing import AsyncIterator

from fastapi import APIRouter
from fastapi.responses import StreamingResponse, JSONResponse
from loguru import logger
from pydantic import BaseModel, Field

from app.config.settings import settings
from app.service.agent_service import AgentService

router = APIRouter(prefix="/v1", tags=["OpenAI"])
legacy_router = APIRouter(tags=["Legacy"])


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str = Field(default=settings.OLLAMA_MODEL)
    messages: list[ChatMessage]
    stream: bool = Field(default=True)
    max_tokens: int = Field(default=4096, ge=1, le=32768)


def _get_agent() -> AgentService:
    return AgentService()


def _models_response():
    return JSONResponse(
        content={
            "object": "list",
            "data": [
                {
                    "id": settings.OLLAMA_MODEL,
                    "object": "model",
                    "created": 0,
                    "owned_by": "kaos",
                }
            ],
        }
    )


@legacy_router.get("/models")
async def list_models_legacy():
    logger.info("[start] openai - list_models_legacy")
    logger.debug("[finish] openai - list_models_legacy")
    return _models_response()


@router.get("/models")
async def list_models():
    logger.info("[start] openai - list_models")
    logger.debug("[finish] openai - list_models")
    return _models_response()


@router.post("/chat/completions")
async def chat_completions(
    request: ChatCompletionRequest,
) -> StreamingResponse:
    logger.info("[start] openai - chat_completions")
    agent = _get_agent()
    stream_id = f"chatcmpl-{uuid.uuid4().hex[:12]}"
    created = int(__import__("time").time())
    session_id = stream_id

    user_message = next(
        (m.content for m in reversed(request.messages) if m.role == "user"),
        request.messages[-1].content if request.messages else "",
    )

    logger.info("[sending] openai - streaming via LangGraph Agent")

    async def token_generator() -> AsyncIterator[str]:
        full_content = ""
        async for token in agent.stream_message(
            session_id=session_id, user_message=user_message
        ):
            full_content += token
            chunk = {
                "id": stream_id,
                "object": "chat.completion.chunk",
                "created": created,
                "model": request.model,
                "choices": [
                    {
                        "index": 0,
                        "delta": {"content": token},
                        "finish_reason": None,
                    }
                ],
            }
            yield f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n"

        final_chunk = {
            "id": stream_id,
            "object": "chat.completion.chunk",
            "created": created,
            "model": request.model,
            "choices": [
                {
                    "index": 0,
                    "delta": {},
                    "finish_reason": "stop",
                }
            ],
        }
        yield f"data: {json.dumps(final_chunk, ensure_ascii=False)}\n\n"
        yield "data: [DONE]\n\n"

    logger.debug("[finish] openai - chat_completions")
    return StreamingResponse(
        token_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
