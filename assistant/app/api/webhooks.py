from uuid import UUID, uuid4, uuid5, NAMESPACE_DNS
from fastapi import APIRouter, Request
from loguru import logger
from app.config.settings import settings

router = APIRouter(prefix="/api/webhooks", tags=["Webhooks"])


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
    content = body.get("content", "")
    tags = body.get("tags", [])
    logger.info(f"[webhook] n8n/memory - action={action} tags={tags}")
    return {"status": "received", "action": action}


@router.post("/n8n/agent")
async def n8n_agent_webhook(request: Request) -> dict:
    body = await request.json()
    workflow = body.get("workflow", "")
    payload = body.get("payload", {})
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
