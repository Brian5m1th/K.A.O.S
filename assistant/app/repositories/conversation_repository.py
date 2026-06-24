"""
ConversationRepository — CRUD for conversation history.

Uses SQLAlchemy async ORM with the Conversation model.
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from sqlalchemy import func, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.conversation import Conversation


@dataclass
class ConversationTurn:
    """Represents a single turn in a conversation (user or assistant)."""
    session_id: UUID
    user_id: str
    role: str  # "user" | "assistant" | "system"
    content: str
    workflow_type: str | None = None
    tokens_used: int = 0
    model_used: str | None = None
    provider: str | None = None

    def to_orm(self) -> Conversation:
        return Conversation(
            session_id=self.session_id,
            user_id=self.user_id,
            role=self.role,
            content=self.content,
            workflow_type=self.workflow_type,
            tokens_used=self.tokens_used,
            model_used=self.model_used,
            provider=self.provider,
        )


@dataclass
class SessionSummary:
    """Summarized view of a conversation session."""
    session_id: UUID
    user_id: str
    started_at: datetime
    last_message_at: datetime
    message_count: int
    workflow_types: list[str]
    total_tokens: int


class ConversationRepository:
    """Repository for managing conversation history."""

    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, turn: ConversationTurn) -> Conversation:
        """Persist a single turn (user or assistant) and return the ORM object."""
        orm = turn.to_orm()
        self._session.add(orm)
        await self._session.commit()
        return orm

    async def get_by_session(
        self, session_id: str | UUID, user_id: str, limit: int = 100
    ) -> list[Conversation]:
        """Return all turns for a session, ordered by created_at ASC."""
        sid = UUID(session_id) if isinstance(session_id, str) else session_id
        stmt = (
            select(Conversation)
            .where(
                Conversation.session_id == sid,
                Conversation.user_id == user_id,
            )
            .order_by(Conversation.created_at.asc())
            .limit(limit)
        )
        result = await self._session.execute(stmt)
        return list(result.scalars().all())

    async def get_session_count(self, session_id: str | UUID, user_id: str) -> int:
        """Return the number of turns in a session."""
        sid = UUID(session_id) if isinstance(session_id, str) else session_id
        stmt = (
            select(func.count())
            .select_from(Conversation)
            .where(
                Conversation.session_id == sid,
                Conversation.user_id == user_id,
            )
        )
        result = await self._session.execute(stmt)
        return result.scalar() or 0

    async def list_sessions(
        self, user_id: str, page: int = 1, limit: int = 20
    ) -> tuple[list[SessionSummary], int]:
        """Return paginated list of sessions with summary per session.

        Returns:
            Tuple of (list of SessionSummary, total count of sessions).
        """
        # Subquery: aggregate per session_id
        subq = (
            select(
                Conversation.session_id,
                func.min(Conversation.created_at).label("started_at"),
                func.max(Conversation.created_at).label("last_message_at"),
                func.count().label("message_count"),
                func.sum(Conversation.tokens_used).label("total_tokens"),
            )
            .where(Conversation.user_id == user_id)
            .group_by(Conversation.session_id)
            .subquery()
        )

        # Count total sessions
        count_stmt = select(func.count()).select_from(subq)
        total_result = await self._session.execute(count_stmt)
        total = total_result.scalar() or 0

        # Fetch page
        offset = (page - 1) * limit
        stmt = (
            select(subq)
            .order_by(subq.c.last_message_at.desc())
            .offset(offset)
            .limit(limit)
        )
        rows = await self._session.execute(stmt)
        sessions = []
        for row in rows:
            # Collect workflow types for this session
            wf_stmt = (
                select(Conversation.workflow_type)
                .where(
                    Conversation.session_id == row.session_id,
                    Conversation.workflow_type.isnot(None),
                )
                .distinct()
            )
            wf_result = await self._session.execute(wf_stmt)
            workflow_types = [r[0] for r in wf_result if r[0]]

            sessions.append(SessionSummary(
                session_id=row.session_id,
                user_id=user_id,
                started_at=row.started_at,
                last_message_at=row.last_message_at,
                message_count=row.message_count,
                workflow_types=workflow_types,
                total_tokens=row.total_tokens or 0,
            ))

        return sessions, total

    async def delete_session(
        self, session_id: str | UUID, user_id: str
    ) -> int:
        """Remove all turns for a session. Returns count of deleted records."""
        sid = UUID(session_id) if isinstance(session_id, str) else session_id
        stmt = delete(Conversation).where(
            Conversation.session_id == sid,
            Conversation.user_id == user_id,
        )
        result = await self._session.execute(stmt)
        await self._session.commit()
        return result.rowcount
