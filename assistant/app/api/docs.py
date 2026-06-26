"""
Docs API — Auto-documentation generation from conversation history.

SDD-DOCS-001: POST /api/docs/generate — synthesizes a conversation into an
              SDD, guide, or general Markdown note saved under docs/.
"""

import re
from datetime import datetime
from pathlib import Path
from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from loguru import logger
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.conversation_repository import ConversationRepository

router = APIRouter(prefix="/api/docs", tags=["Docs"])

# ── Constants ──────────────────────────────────────────────────────────
DOCS_ROOT = Path("docs")

DOC_PROMPTS: dict[str, str] = {
    "sdd": (
        "You are a senior software architect. "
        "Based on the conversation below, extract and write a formal Software Design Document (SDD) in Markdown. "
        "Include sections: ## Overview, ## Architecture, ## Key Design Decisions, ## Open Questions, ## Diagrams (text). "
        "Be concise but technically precise. Use bullet lists and code blocks where appropriate.\n\n"
        "--- Conversation History ---\n{history}"
    ),
    "guide": (
        "You are a technical writer. "
        "Based on the conversation below, write a detailed step-by-step setup/installation guide in Markdown. "
        "Include sections: ## Prerequisites, ## Installation Steps, ## Environment Variables, ## Troubleshooting. "
        "Use numbered lists and code blocks for commands.\n\n"
        "--- Conversation History ---\n{history}"
    ),
    "general": (
        "You are a documentation specialist. "
        "Based on the conversation below, write a clear and concise Markdown note capturing the key topics, "
        "decisions, and takeaways. Include a ## Summary section followed by ## Key Points.\n\n"
        "--- Conversation History ---\n{history}"
    ),
}

# ── Pydantic models ────────────────────────────────────────────────────


class GenerateDocRequest(BaseModel):
    session_id: str
    user_id: str
    document_type: str = "sdd"  # "sdd" | "guide" | "general"
    title: str = ""


class GenerateDocResponse(BaseModel):
    doc_path: str
    title: str
    document_type: str
    turns_processed: int
    status: str  # "queued" | "done" | "error"


# ── Helpers ────────────────────────────────────────────────────────────


def _slugify(text: str) -> str:
    """Convert a title to a filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:64]


def _build_history_text(turns) -> str:
    lines = []
    for t in turns:
        emoji = "👤 User" if t.role == "user" else "🤖 Assistant"
        lines.append(f"**{emoji}**: {t.content}\n")
    return "\n".join(lines)


def _resolve_doc_path(doc_type: str, slug: str) -> Path:
    """Return the absolute path where the doc will be written."""
    sub = {"sdd": "sdd", "guide": "guides", "general": "notes"}.get(doc_type, "notes")
    return DOCS_ROOT / sub / f"{slug}.md"


async def _generate_and_save(
    turns,
    doc_type: str,
    title: str,
    doc_path: Path,
) -> None:
    """Run LLM generation and persist the Markdown file (background task)."""
    from app.llm.factory import LLMFactory

    factory = LLMFactory()
    history_text = _build_history_text(turns)
    prompt_template = DOC_PROMPTS.get(doc_type, DOC_PROMPTS["general"])
    prompt = prompt_template.format(history=history_text)

    system_msg = {"role": "system", "content": prompt}
    messages = [system_msg]

    try:
        content = await factory.ainvoke_with_fallback(
            model_key="default",
            messages=messages,
        )
    except Exception as exc:
        logger.error("[docs] LLM generation failed: {}", exc)
        return

    # Build front-matter + body
    now = datetime.now().isoformat(timespec="seconds")
    frontmatter = (
        "---\n"
        f"type: {doc_type}\n"
        f'title: "{title}"\n'
        f"created_at: {now}\n"
        f"turns: {len(turns)}\n"
        "---\n\n"
    )
    full_doc = frontmatter + f"# {title}\n\n" + content

    doc_path.parent.mkdir(parents=True, exist_ok=True)
    doc_path.write_text(full_doc, encoding="utf-8")
    logger.info("[docs] document saved → {}", doc_path)

    # Optionally index in Qdrant (best-effort)
    try:
        from app.rag.indexing.incremental_indexer import IncrementalIndexer

        indexer = IncrementalIndexer()
        await indexer.index_file(doc_path)
        logger.info("[docs] document indexed in Qdrant: {}", doc_path)
    except Exception as exc:
        logger.warning("[docs] Qdrant indexing skipped: {}", exc)


# ── Endpoint ───────────────────────────────────────────────────────────


@router.post("/generate", response_model=GenerateDocResponse)
async def generate_doc(
    req: GenerateDocRequest,
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_session),
):
    """SDD-DOCS-001: Generate a Markdown document from a conversation session."""
    if not req.user_id:
        raise HTTPException(status_code=400, detail="user_id is required")
    if req.document_type not in DOC_PROMPTS:
        raise HTTPException(
            status_code=400,
            detail=f"document_type must be one of: {list(DOC_PROMPTS.keys())}",
        )

    repo = ConversationRepository(session)
    try:
        sid = UUID(req.session_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid session_id format")

    turns = await repo.get_by_session(session_id=sid, user_id=req.user_id, limit=500)
    if not turns:
        raise HTTPException(status_code=404, detail="Session not found or empty")

    # Determine title and slug
    title = (
        req.title.strip()
        if req.title.strip()
        else f"{req.document_type.upper()} — {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )
    slug = (
        _slugify(title)
        or f"{req.document_type}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    )
    doc_path = _resolve_doc_path(req.document_type, slug)

    logger.info(
        "[docs] queuing generation: type={} session={} path={}",
        req.document_type,
        req.session_id,
        doc_path,
    )

    background_tasks.add_task(
        _generate_and_save,
        turns=turns,
        doc_type=req.document_type,
        title=title,
        doc_path=doc_path,
    )

    return GenerateDocResponse(
        doc_path=str(doc_path),
        title=title,
        document_type=req.document_type,
        turns_processed=len(turns),
        status="queued",
    )


@router.get("/list")
async def list_docs():
    """List all generated documents under docs/."""
    result = []
    for doc_type, sub in [("sdd", "sdd"), ("guide", "guides"), ("general", "notes")]:
        folder = DOCS_ROOT / sub
        if folder.exists():
            for f in sorted(
                folder.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True
            ):
                result.append(
                    {
                        "path": str(f),
                        "name": f.stem,
                        "type": doc_type,
                        "size_bytes": f.stat().st_size,
                        "modified_at": datetime.fromtimestamp(
                            f.stat().st_mtime
                        ).isoformat(),
                    }
                )
    return {"docs": result, "total": len(result)}
