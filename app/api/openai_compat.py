import time
import uuid
from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.service.agent_service import AgentService

router = APIRouter(prefix="/v1", tags=["OpenAI"])


class OpenAIMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str


class OpenAIRequest(BaseModel):
    model: str = Field(default="qwen3:14b")
    messages: list[OpenAIMessage]
    stream: bool = Field(default=False)


class ChoiceMessage(BaseModel):
    role: Literal["assistant"]
    content: str


class Choice(BaseModel):
    index: int = 0
    message: ChoiceMessage
    finish_reason: str = "stop"


class Usage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class OpenAIResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: list[Choice]
    usage: Usage


@router.post("/chat/completions")
async def chat_completions(request: OpenAIRequest) -> OpenAIResponse:
    last_user_msg = next(
        (m for m in reversed(request.messages) if m.role == "user"), None
    )
    if not last_user_msg:
        return OpenAIResponse(
            id=f"chatcmpl-{uuid.uuid4().hex[:12]}",
            created=int(time.time()),
            model=request.model,
            choices=[
                Choice(
                    message=ChoiceMessage(
                        role="assistant",
                        content="Envie uma mensagem para começar.",
                    )
                )
            ],
            usage=Usage(),
        )

    agent = AgentService()
    response_text = await agent.process_message(
        session_id=f"openai-{uuid.uuid4().hex[:8]}",
        user_message=last_user_msg.content,
    )

    return OpenAIResponse(
        id=f"chatcmpl-{uuid.uuid4().hex[:12]}",
        created=int(time.time()),
        model=request.model,
        choices=[
            Choice(
                message=ChoiceMessage(role="assistant", content=response_text)
            )
        ],
        usage=Usage(),
    )
