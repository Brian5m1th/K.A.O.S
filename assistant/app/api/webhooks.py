from fastapi import APIRouter, Request
from loguru import logger

router = APIRouter(prefix="/api/webhooks", tags=["Webhooks"])


@router.post("/n8n")
async def n8n_webhook(request: Request) -> dict:
    body = await request.json()
    event = body.get("event", "unknown")
    logger.info(f"[webhook] n8n - evento={event}")
    logger.debug(f"[webhook] n8n - payload={str(body)[:500]}")
    return {"status": "received", "event": event}


@router.get("/n8n")
async def n8n_webhook_info() -> dict:
    return {
        "service": "n8n-webhook",
        "endpoints": {
            "receive": "POST /api/webhooks/n8n",
        },
    }
