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


@tool
def receive_whatsapp(limit: int = 10) -> list[dict]:
    """Recupera mensagens WhatsApp recebidas recentemente.

    Args:
        limit: Numero maximo de mensagens a recuperar (padrao: 10).

    Returns:
        Lista de mensagens recebidas com id, from, text, timestamp.
    """
    provider = WhatsAppProvider()
    if not provider.is_configured():
        return [
            {
                "status": "error",
                "message": "WhatsApp nao configurado (defina WHATSAPP_API_URL e WHATSAPP_API_KEY no .env)",
            }
        ]

    import asyncio

    loop = asyncio.new_event_loop()
    try:
        messages = loop.run_until_complete(provider.receive_messages(limit=limit))
        return [msg.to_dict() for msg in messages]
    finally:
        loop.close()


def register_whatsapp_tools() -> None:
    """Registra as ferramentas WhatsApp no TOOL_REGISTRY global."""
    from app.agent.nodes.executor import TOOL_REGISTRY

    TOOL_REGISTRY["send_whatsapp"] = send_whatsapp
    TOOL_REGISTRY["receive_whatsapp"] = receive_whatsapp
    logger.info("[whatsapp] tools registered")
