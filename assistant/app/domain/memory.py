from dataclasses import dataclass

from app.domain.chat import Message


@dataclass
class ConversationSnapshot:
    version: str = "1.0"
    history: list[Message] | None = None
    summary: str = ""
    title: str = ""
    tags: list[str] | None = None
    metadata: dict | None = None
