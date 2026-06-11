from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.domain.chat import ChatRequest
from app.service.agent_service import AgentService

router = APIRouter(prefix="/api/chat", tags=["Chat"])

_agent = AgentService()


@router.post("/message")
async def send_message(
    request: ChatRequest,
) -> StreamingResponse:
    async def token_generator():
        async for token in _agent.stream_message(
            session_id=request.session_id,
            user_message=request.message,
        ):
            yield token

    return StreamingResponse(token_generator(), media_type="text/plain")
