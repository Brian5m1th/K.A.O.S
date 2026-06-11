from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.domain.chat import ChatRequest, Message
from app.service.llm_service import LLMService

router = APIRouter(prefix="/api/chat", tags=["Chat"])


def get_llm_service() -> LLMService:
    return LLMService()


@router.post("/message")
async def send_message(
    request: ChatRequest,
    llm: LLMService = Depends(get_llm_service),
) -> StreamingResponse:
    messages = list(request.history)
    messages.append(Message(role="user", content=request.message))

    async def token_generator():
        async for token in llm.stream_chat(messages=messages):
            yield token

    return StreamingResponse(token_generator(), media_type="text/plain")
