"""
Conversation SQLAlchemy model.

Persists individual chat turns (user + assistant messages) for session history.
"""

from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    session_id: Mapped[UUID] = mapped_column(index=True, nullable=False)
    user_id: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    role: Mapped[str] = mapped_column(
        String(10), nullable=False
    )  # "user"|"assistant"|"system"
    content: Mapped[str] = mapped_column(Text, nullable=False)
    workflow_type: Mapped[str | None] = mapped_column(
        String(20), nullable=True
    )  # "FAST"|"MEMORY"|"SMART"|"AGENT"
    tokens_used: Mapped[int] = mapped_column(Integer, default=0)
    model_used: Mapped[str | None] = mapped_column(String(100), nullable=True)
    provider: Mapped[str | None] = mapped_column(String(50), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )
