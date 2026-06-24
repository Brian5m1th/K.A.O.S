"""
Conversations API — Session History endpoints.

RF-D02: GET /api/conversations — lista sessões paginadas
RF-D03: GET /api/conversations/{session_id} — turnos de uma sessão
RF-D04: POST /api/conversations/{session_id}/summarize — gera resumo
"""

from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from loguru import logger
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.domain.chat import Message
from app.memory.summarizer import ConversationSummarizer
from app.repositories.conversation_repository import (
    ConversationRepository,
    SessionSummary,
    Conversation,
)

router = APIRouter(prefix="/api/conversations", tags=["Conversations"])


# ── Pydantic response models ─────────────────────────────────────────


class SessionSummaryResponse(BaseModel):
    session_id: str
    user_id: str
    started_at: datetime
    last_message_at: datetime
    message_count: int
    workflow_types: list[str]
    total_tokens: int


class ConversationsListResponse(BaseModel):
    total: int
    page: int
    limit: int
    conversations: list[SessionSummaryResponse]


class TurnResponse(BaseModel):
    id: str
    session_id: str
    role: str
    content: str
    workflow_type: str | None = None
    tokens_used: int = 0
    model_used: str | None = None
    provider: str | None = None
    created_at: datetime


class SessionDetailResponse(BaseModel):
    total: int
    turns: list[TurnResponse]


class SummarizeResponse(BaseModel):
    session_id: str
    summary: str
    note_path: str
    tokens_used: int


# ── Helpers ──────────────────────────────────────────────────────────


def _summary_to_response(s: SessionSummary) -> SessionSummaryResponse:
    return SessionSummaryResponse(
        session_id=str(s.session_id),
        user_id=s.user_id,
        started_at=s.started_at,
        last_message_at=s.last_message_at,
        message_count=s.message_count,
        workflow_types=s.workflow_types,
        total_tokens=s.total_tokens,
    )


def _turn_to_response(t: Conversation) -> TurnResponse:
    return TurnResponse(
        id=str(t.id),
        session_id=str(t.session_id),
        role=t.role,
        content=t.content,
        workflow_type=t.workflow_type,
        tokens_used=t.tokens_used,
        model_used=t.model_used,
        provider=t.provider,
        created_at=t.created_at,
    )


# ── Endpoints ────────────────────────────────────────────────────────


@router.get("", response_model=ConversationsListResponse)
async def list_sessions(
    user_id: str = Query(..., description="User ID (obrigatório)"),
    page: int = Query(1, ge=1, description="Número da página"),
    limit: int = Query(20, ge=1, le=100, description="Itens por página"),
    session: AsyncSession = Depends(get_session),
):
    """RF-D02: Lista sessões paginadas por user_id."""
    if not user_id:
        raise HTTPException(status_code=400, detail="user_id is required")

    repo = ConversationRepository(session)
    sessions, total = await repo.list_sessions(user_id=user_id, page=page, limit=limit)

    return ConversationsListResponse(
        total=total,
        page=page,
        limit=limit,
        conversations=[_summary_to_response(s) for s in sessions],
    )


@router.get("/{session_id}", response_model=SessionDetailResponse)
async def get_session(
    session_id: str,
    user_id: str = Query(..., description="User ID (obrigatório)"),
    limit: int = Query(100, ge=1, le=500, description="Máx turnos"),
    session: AsyncSession = Depends(get_session),
):
    """RF-D03: Retorna todos os turnos de uma sessão."""
    if not user_id:
        raise HTTPException(status_code=400, detail="user_id is required")

    repo = ConversationRepository(session)
    try:
        sid = UUID(session_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid session_id format")

    turns = await repo.get_by_session(session_id=sid, user_id=user_id, limit=limit)

    return SessionDetailResponse(
        total=len(turns),
        turns=[_turn_to_response(t) for t in turns],
    )


@router.delete("/{session_id}")
async def delete_session(
    session_id: str,
    user_id: str = Query(..., description="User ID (obrigatório)"),
    session: AsyncSession = Depends(get_session),
):
    """Deleta todos os turnos de uma sessão."""
    if not user_id:
        raise HTTPException(status_code=400, detail="user_id is required")

    repo = ConversationRepository(session)
    try:
        sid = UUID(session_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid session_id format")

    deleted = await repo.delete_session(session_id=sid, user_id=user_id)
    logger.info(
        "[conversations] deleted session={} user={} count={}",
        session_id,
        user_id,
        deleted,
    )
    return {"deleted": deleted, "session_id": session_id}


@router.post("/{session_id}/summarize", response_model=SummarizeResponse)
async def summarize_session(
    session_id: str,
    user_id: str = Query(..., description="User ID (obrigatório)"),
    force: bool = Query(False, description="Sobrescrever resumo existente"),
    session: AsyncSession = Depends(get_session),
):
    """RF-D04: Gera resumo da sessão e salva como nota no Obsidian.

    O resumo é salvo em: Diário/conversas/{date}-{session_id[:8]}.md
    """
    if not user_id:
        raise HTTPException(status_code=400, detail="user_id is required")

    repo = ConversationRepository(session)
    try:
        sid = UUID(session_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid session_id format")

    # Buscar turnos da sessão
    turns = await repo.get_by_session(session_id=sid, user_id=user_id, limit=500)
    if not turns:
        raise HTTPException(status_code=404, detail="Session not found or empty")

    # Converter para Message objects
    history = [Message(role=t.role, content=t.content) for t in turns]

    # Gerar resumo
    summary = ConversationSummarizer.generate(history)
    if not summary:
        summary = f"Conversa em {datetime.now().strftime('%Y-%m-%d %H:%M')}"

    title = ConversationSummarizer.generate_title(history)

    # Salvar no Obsidian
    note_path = ""
    try:
        from app.obsidian.services.obsidian_service import ObsidianService

        obsidian = ObsidianService()
        today = datetime.now().strftime("%Y-%m-%d")
        folder = "Diário/conversas"
        note_content = (
            "---\n"
            f"type: knowledge\n"
            f"domain: conversas\n"
            f"session_id: {session_id}\n"
            f"created_at: {datetime.now().isoformat()}\n"
            "---\n\n"
            f"# {title}\n\n"
            f"{summary}\n\n"
            "---\n\n"
            "## Histórico\n\n"
        )
        for t in turns:
            emoji = "👤" if t.role == "user" else "🤖"
            note_content += f"- {emoji} **{t.role}**: {t.content[:200]}{'...' if len(t.content) > 200 else ''}\n"

        obsidian.create_note(
            title=f"{today}-{session_id[:8]}",
            folder=folder,
            content=note_content,
        )
        note_path = f"{folder}/{today}-{session_id[:8]}.md"
        logger.info("[conversations] summary saved to Obsidian: {}", note_path)
    except (FileExistsError, ValueError) as exc:
        if not force:
            raise HTTPException(
                status_code=409,
                detail=f"Summary already exists. Use ?force=true to overwrite: {exc}",
            )
        logger.info(
            "[conversations] summary already exists (force=true), skipping Obsidian save"
        )
    except Exception as exc:
        logger.warning("[conversations] failed to save summary to Obsidian: {}", exc)
        # Não bloqueia a resposta — retorna resumo mesmo sem salvar

    total_tokens = sum(t.tokens_used for t in turns)

    return SummarizeResponse(
        session_id=session_id,
        summary=summary,
        note_path=note_path,
        tokens_used=total_tokens,
    )
