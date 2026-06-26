from uuid import uuid4
from fastapi import APIRouter, Request
from loguru import logger
from sqlalchemy import select

from app.database import async_session_factory
from app.models.automation_registry import AutomationWorkflow, AutomationExecution

router = APIRouter(prefix="/api/webhooks", tags=["Webhooks"])


@router.post("/n8n/callback")
async def n8n_callback(request: Request) -> dict:
    """Callback triggered by n8n to report execution results (success/failure/durations)."""
    try:
        body = await request.json()
    except Exception:
        return {"status": "error", "message": "Invalid JSON payload"}

    n8n_wf_id = body.get("workflow_id")
    n8n_exec_id = body.get("execution_id")
    status = body.get("status", "success")  # "success"|"failed"|"running"
    event_name = body.get("event")
    payload = body.get("payload")
    response_data = body.get("response")
    duration_ms = body.get("duration")

    logger.info(
        f"[webhook] n8n callback - workflow_id={n8n_wf_id} exec_id={n8n_exec_id} status={status}"
    )

    if not n8n_wf_id or not n8n_exec_id:
        return {
            "status": "error",
            "message": "workflow_id and execution_id are required",
        }

    factory = async_session_factory()
    async with factory() as session:
        # Find local workflow
        stmt = select(AutomationWorkflow).where(
            AutomationWorkflow.n8n_workflow_id == n8n_wf_id
        )
        result = await session.execute(stmt)
        wf = result.scalar_one_or_none()
        if not wf:
            logger.warning(
                f"[webhook] n8n callback received for unregistered workflow {n8n_wf_id}"
            )
            return {"status": "error", "message": "Workflow not registered."}

        # Check if execution already logged
        exec_stmt = select(AutomationExecution).where(
            AutomationExecution.n8n_execution_id == n8n_exec_id
        )
        exec_res = await session.execute(exec_stmt)
        execution = exec_res.scalar_one_or_none()

        if not execution:
            execution = AutomationExecution(
                workflow_id=wf.id,
                n8n_execution_id=n8n_exec_id,
                status=status,
                trigger_event=event_name,
                payload=payload,
                response=response_data,
                duration_ms=duration_ms,
            )
            session.add(execution)
        else:
            execution.status = status
            if response_data:
                execution.response = response_data
            if duration_ms:
                execution.duration_ms = duration_ms

        await session.commit()
    return {"status": "processed", "n8n_execution_id": n8n_exec_id}


@router.post("/n8n")
async def n8n_webhook(request: Request) -> dict:
    body = await request.json()
    event = body.get("event", "unknown")
    logger.info(f"[webhook] n8n - evento={event}")
    return {"status": "received", "event": event}


@router.post("/n8n/chat")
async def n8n_chat_webhook(request: Request) -> dict:
    body = await request.json()
    message = body.get("message", "")
    session_id = body.get("session_id", str(uuid4()))
    logger.info(f"[webhook] n8n/chat - message={message[:100]}")
    return {"status": "forwarded", "session_id": session_id, "message": message}


@router.post("/n8n/memory")
async def n8n_memory_webhook(request: Request) -> dict:
    body = await request.json()
    action = body.get("action", "save")
    tags = body.get("tags", [])
    logger.info(f"[webhook] n8n/memory - action={action} tags={tags}")
    return {"status": "received", "action": action}


@router.post("/n8n/agent")
async def n8n_agent_webhook(request: Request) -> dict:
    body = await request.json()
    workflow = body.get("workflow", "")
    logger.info(f"[webhook] n8n/agent - workflow={workflow}")
    return {"status": "received", "workflow": workflow}


@router.post("/n8n/webhook-register")
async def n8n_register_webhook(request: Request) -> dict:
    body = await request.json()
    webhook_url = body.get("url", "")
    events = body.get("events", ["*"])
    logger.info(f"[webhook] n8n/register - url={webhook_url} events={events}")
    return {"status": "registered", "url": webhook_url, "events": events}


@router.get("/n8n")
async def n8n_webhook_info() -> dict:
    return {
        "service": "n8n-webhook",
        "endpoints": {
            "receive": "POST /api/webhooks/n8n",
            "chat": "POST /api/webhooks/n8n/chat",
            "memory": "POST /api/webhooks/n8n/memory",
            "agent": "POST /api/webhooks/n8n/agent",
            "register": "POST /api/webhooks/n8n/webhook-register",
        },
    }
