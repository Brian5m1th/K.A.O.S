"""
SQLAlchemy models for K.A.O.S automation workflows and executions.
"""

from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Integer, String, Text, func, JSON, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class AutomationWorkflow(Base):
    __tablename__ = "automation_workflows"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    n8n_workflow_id: Mapped[str | None] = mapped_column(
        String(100), unique=True, nullable=True, index=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    json_data: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False)
    version: Mapped[int] = mapped_column(Integer, default=1)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    executions: Mapped[list["AutomationExecution"]] = relationship(
        "AutomationExecution", back_populates="workflow", cascade="all, delete-orphan"
    )


class AutomationExecution(Base):
    __tablename__ = "automation_executions"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    workflow_id: Mapped[UUID] = mapped_column(
        ForeignKey("automation_workflows.id", ondelete="CASCADE"), index=True
    )
    n8n_execution_id: Mapped[str | None] = mapped_column(
        String(100), nullable=True, index=True
    )
    status: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # "success" | "failed" | "running"
    trigger_event: Mapped[str | None] = mapped_column(String(100), nullable=True)
    payload: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    response: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    duration_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )

    workflow: Mapped[AutomationWorkflow] = relationship(
        "AutomationWorkflow", back_populates="executions"
    )
