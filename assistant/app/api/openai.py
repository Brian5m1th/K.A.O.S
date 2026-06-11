import json
import uuid
from typing import AsyncIterator

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel, Field

from app.domain.chat import Message
from app.service.llm_service import LLMService
from app.config.settings import settings
from app.config.prompts import SYSTEM_PROMPT_KAOS

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


def get_llm_service() -> LLMService:
    return LLMService()


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
    return _models_response()


@router.get("/models")
async def list_models():
    return _models_response()


@router.post("/chat/completions")
async def chat_completions(
    request: ChatCompletionRequest,
    llm: LLMService = Depends(get_llm_service),
) -> StreamingResponse:
    messages = [Message(role="system", content=SYSTEM_PROMPT_KAOS)]
    messages += [
        Message(role=m.role, content=m.content)
        for m in request.messages
    ]
    stream_id = f"chatcmpl-{uuid.uuid4().hex[:12]}"
    created = int(__import__("time").time())

    async def token_generator() -> AsyncIterator[str]:
        full_content = ""
        async for token in llm.stream_chat(messages=messages):
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

    return StreamingResponse(
        token_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
