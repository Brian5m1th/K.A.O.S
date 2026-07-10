"""WhatsApp Tools — Ferramentas LangChain para integracao WhatsApp."""

from __future__ import annotations

from langchain_core.tools import tool
from loguru import logger

from app.providers.whatsapp.whatsapp_provider import WhatsAppProvider


@tool
def send_whatsapp(to: str, message: str) -> dict:
    """Envia uma mensagem WhatsApp.

    Args:
        to: Numero de telefone do destinatario (formato internacional, ex: 5511999999999).
        message: Texto da mensagem a ser enviada.

    Returns:
        Dict com status da operacao.
    """
    provider = WhatsAppProvider()
    if not provider.is_configured():
        return {
            "status": "error",
            "message": "WhatsApp nao configurado (defina WHATSAPP_API_URL e WHATSAPP_API_KEY no .env)",
        }

    import asyncio

    loop = asyncio.new_event_loop()
    try:
        result = loop.run_until_complete(provider.send_message(to, message))
        return result
    finally:
        loop.close()


def register_whatsapp_tools() -> None:
    """Registra as ferramentas WhatsApp no TOOL_REGISTRY global."""
    from app.agent.nodes.executor import TOOL_REGISTRY

    TOOL_REGISTRY["send_whatsapp"] = send_whatsapp
    logger.info("[whatsapp] tools registered")
