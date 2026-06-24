"""
CostEvent SQLAlchemy model.

Persists cost tracking events for observability and billing.
"""

from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class CostEvent(Base):
    __tablename__ = "cost_events"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    execution_id: Mapped[UUID | None] = mapped_column(index=True, nullable=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    provider: Mapped[str] = mapped_column(String(50), nullable=False)
    workflow: Mapped[str | None] = mapped_column(String(20), nullable=True)
    model: Mapped[str | None] = mapped_column(String(100), nullable=True)
    tokens_in: Mapped[int] = mapped_column(Integer, default=0)
    tokens_out: Mapped[int] = mapped_column(Integer, default=0)
    cost_usd: Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )
