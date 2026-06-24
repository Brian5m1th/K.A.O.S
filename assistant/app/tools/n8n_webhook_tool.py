"""
N8N WebhookTool — LangChain tool for invoking N8N workflows via webhook.

Registers as 'n8n_webhook' in the LangGraph TOOL_REGISTRY.
"""

import httpx
from langchain_core.tools import tool
from loguru import logger

from app.config.settings import settings


@tool
async def n8n_webhook(flow_name: str, payload: dict = {}) -> str:
    """Invoca um flow N8N via webhook.

    Use esta ferramenta quando o usuário solicitar automação externa,
    como backup, notificação, ou integração com sistemas terceiros.

    Args:
        flow_name: Nome do flow N8N a ser invocado (ex: 'backup-vault')
        payload: Dados opcionais a serem enviados para o flow
    """
    if not settings.N8N_API_URL:
        logger.warning("[n8n_webhook] N8N_API_URL not configured")
        return '{"success": false, "error": "n8n_not_configured"}'

    url = f"{settings.N8N_API_URL.rstrip('/')}/webhook/{flow_name}"
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(url, json=payload)
            resp.raise_for_status()
            logger.info(
                "[n8n_webhook] invoked flow='{}' status={}", flow_name, resp.status_code
            )
            return f'{{"success": true, "status": {resp.status_code}}}'
    except httpx.ConnectError:
        logger.warning("[n8n_webhook] N8N unavailable: {}", url)
        return '{"success": false, "error": "n8n_unavailable"}'
    except httpx.HTTPStatusError as exc:
        logger.warning("[n8n_webhook] flow='{}' error: {}", flow_name, exc)
        return f'{{"success": false, "error": "flow_error", "status": {exc.response.status_code}}}'
    except Exception as exc:
        logger.error("[n8n_webhook] unexpected error: {}", exc)
        return f'{{"success": false, "error": "unexpected", "detail": "{exc}"}}'


def register_n8n_webhook() -> None:
    """Register the n8n_webhook tool in the global TOOL_REGISTRY."""
    from app.agent.nodes.executor import TOOL_REGISTRY

    TOOL_REGISTRY["n8n_webhook"] = n8n_webhook
    logger.info("[n8n_webhook] registered in TOOL_REGISTRY")
