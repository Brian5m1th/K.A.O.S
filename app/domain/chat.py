from pydantic import BaseModel, Field
from typing import Literal


class Message(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str


class ChatRequest(BaseModel):
    session_id: str = Field(..., description="ID único da sessão de conversa")
    message: str = Field(..., min_length=1, max_length=8000)
    history: list[Message] = Field(default_factory=list)


class ChatResponse(BaseModel):
    session_id: str
    content: str
    model: str
