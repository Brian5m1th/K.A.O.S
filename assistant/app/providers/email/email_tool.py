"""Email Tools — Ferramentas LangChain para integracao de email."""
from __future__ import annotations

from langchain_core.tools import tool
from loguru import logger

from app.providers.email.email_reader import EmailReader
from app.providers.email.email_sender import EmailSender


@tool
def read_emails(limit: int = 5, folder: str = "INBOX") -> dict:
    """Le os emails mais recentes da caixa de entrada.

    Args:
        limit: Numero maximo de emails a retornar (1-20).
        folder: Pasta do email (padrao: INBOX).

    Returns:
        Dict com lista de emails e metadados.
    """
    reader = EmailReader()
    if not reader.is_configured():
        return {"status": "error", "message": "Email nao configurado (defina EMAIL_HOST, EMAIL_USER, EMAIL_PASS no .env)"}

    messages = reader.fetch_inbox(limit=min(limit, 20))
    return {
        "status": "ok",
        "total": len(messages),
        "messages": [
            {
                "uid": m.uid,
                "subject": m.subject,
                "sender": m.sender,
                "date": m.date,
                "snippet": m.snippet,
            }
            for m in messages
        ],
    }


@tool
def send_email(to: str, subject: str, body: str) -> dict:
    """Envia um email.

    Args:
        to: Endereco de email do destinatario.
        subject: Assunto do email.
        body: Corpo do email em texto puro.

    Returns:
        Dict com status da operacao.
    """
    sender = EmailSender()
    if not sender.is_configured():
        return {"status": "error", "message": "Email nao configurado (defina EMAIL_HOST, EMAIL_USER, EMAIL_PASS no .env)"}

    return sender.send(to=to, subject=subject, body=body)


def register_email_tools() -> None:
    """Registra as ferramentas de email no TOOL_REGISTRY global."""
    from app.agent.nodes.executor import TOOL_REGISTRY

    TOOL_REGISTRY["read_emails"] = read_emails
    TOOL_REGISTRY["send_email"] = send_email
    logger.info("[email] tools registered")
