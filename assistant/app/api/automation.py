"""
FastAPI Router for K.A.O.S Automation Platform.
Handles workflow query, template import, status toggling, and execution logs query.
"""

from typing import Any
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from app.database import get_session
from app.models.automation_registry import AutomationWorkflow, AutomationExecution
from app.core.automation_bus import AutomationBus

router = APIRouter(prefix="/api/automation", tags=["Automation"])


@router.get("/templates")
async def list_templates() -> dict:
    """Lista templates disponiveis no Marketplace (da pasta data/workflows/)."""
    from pathlib import Path
    import json

    templates_dir = Path("data/workflows")
    if not templates_dir.exists():
        return {"templates": []}

    templates = []
    for fpath in sorted(templates_dir.glob("*.json")):
        try:
            data = json.loads(fpath.read_text(encoding="utf-8"))
            templates.append({
                "name": data.get("name", fpath.stem),
                "description": data.get("description", ""),
                "json_name": fpath.name,
                "category": _infer_category(data.get("nodes", [])),
            })
        except Exception as e:
            logger.warning("[marketplace] Erro ao ler template {}: {}", fpath.name, e)
    return {"templates": templates}


def _infer_category(nodes: list) -> str:
    """Infere categoria do workflow baseado nos nodes."""
    names = [n.get("name", "").lower() for n in nodes]
    text = " ".join(names)
    if any(w in text for w in ["whatsapp", "telegram", "chat", "message"]):
        return "Messaging"
    if any(w in text for w in ["github", "pr", "pull request"]):
        return "GitHub"
    if any(w in text for w in ["backup", "s3", "devops"]):
        return "DevOps"
    if any(w in text for w in ["mcp", "health"]):
        return "MCP"
    if any(w in text for w in ["ollama", "cost", "llm", "ai"]):
        return "IA"
    return "IA"


@router.get("/workflows")
async def list_workflows(
    session: AsyncSession = Depends(get_session),
) -> dict[str, Any]:
    """Lists all registered workflows in the K.A.O.S system."""
    stmt = select(AutomationWorkflow).order_by(AutomationWorkflow.created_at.desc())
    result = await session.execute(stmt)
    workflows = result.scalars().all()

    return {
        "workflows": [
            {
                "id": str(w.id),
                "n8n_workflow_id": w.n8n_workflow_id,
                "name": w.name,
                "description": w.description,
                "is_active": w.is_active,
                "version": w.version,
                "json_data": w.json_data,
                "created_at": w.created_at.isoformat() if w.created_at else None,
                "updated_at": w.updated_at.isoformat() if w.updated_at else None,
            }
            for w in workflows
        ]
    }


@router.post("/workflows/import", status_code=status.HTTP_201_CREATED)
async def import_workflow(
    payload: dict[str, Any], session: AsyncSession = Depends(get_session)
) -> dict[str, Any]:
    """
    Imports a new workflow JSON template.
    Saves to n8n first, then registers in K.A.O.S Postgres database.
    """
    name = payload.get("name", "").strip()
    if not name:
        raise HTTPException(status_code=422, detail="Workflow name is required.")

    json_data = payload.get("json_data", {})
    if not json_data:
        raise HTTPException(
            status_code=422, detail="Workflow JSON structure is required."
        )

    description = payload.get("description", "")

    provider = AutomationBus.get_provider()
    try:
        # Import to external engine
        res = await provider.import_workflow(name, json_data)
        remote_id = res.get("remote_id")

        # Save to local DB
        workflow = AutomationWorkflow(
            n8n_workflow_id=remote_id,
            name=name,
            description=description,
            is_active=True,
            json_data=json_data,
            version=1,
        )
        session.add(workflow)
        await session.commit()
        await session.refresh(workflow)

        logger.info(
            f"[AutomationAPI] Workflow '{name}' imported successfully. Remote ID: {remote_id}"
        )
        return {
            "status": "ok",
            "workflow_id": str(workflow.id),
            "n8n_workflow_id": remote_id,
        }
    except Exception as e:
        logger.error(f"[AutomationAPI] Import failed: {e}")
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to import workflow: {e}")


@router.post("/workflows/{workflow_id}/toggle")
async def toggle_workflow(
    workflow_id: UUID,
    payload: dict[str, Any],
    session: AsyncSession = Depends(get_session),
) -> dict[str, Any]:
    """Enables or disables a workflow in both n8n and K.A.O.S Postgres database."""
    is_active = payload.get("is_active")
    if is_active is None:
        raise HTTPException(
            status_code=422, detail="is_active boolean parameter is required."
        )

    stmt = select(AutomationWorkflow).where(AutomationWorkflow.id == workflow_id)
    result = await session.execute(stmt)
    workflow = result.scalar_one_or_none()

    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found.")

    provider = AutomationBus.get_provider()

    # Toggle in n8n
    if workflow.n8n_workflow_id:
        success = await provider.toggle_workflow(workflow.n8n_workflow_id, is_active)
        if not success:
            raise HTTPException(
                status_code=500, detail="Failed to toggle workflow in remote engine."
            )

    # Toggle in database
    workflow.is_active = is_active
    await session.commit()

    logger.info(
        f"[AutomationAPI] Workflow '{workflow.name}' active status set to {is_active}"
    )
    return {"status": "ok", "workflow_id": str(workflow.id), "is_active": is_active}


@router.get("/history")
async def get_execution_history(
    session: AsyncSession = Depends(get_session),
) -> dict[str, Any]:
    """Returns execution logs of all automated runs."""
    stmt = (
        select(AutomationExecution)
        .order_by(AutomationExecution.created_at.desc())
        .limit(100)
    )
    result = await session.execute(stmt)
    executions = result.scalars().all()

    return {
        "history": [
            {
                "id": str(e.id),
                "workflow_id": str(e.workflow_id),
                "n8n_execution_id": e.n8n_execution_id,
                "status": e.status,
                "trigger_event": e.trigger_event,
                "duration_ms": e.duration_ms,
                "created_at": e.created_at.isoformat() if e.created_at else None,
            }
            for e in executions
        ]
    }
