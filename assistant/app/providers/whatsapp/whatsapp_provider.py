"""WhatsApp Provider — Envio de mensagens via Evolution API / N8N."""

from __future__ import annotations

from typing import Any

import httpx
from loguru import logger

from app.config.settings import settings


class WhatsAppProvider:
    """Provedor de mensagens WhatsApp via Evolution API.

    Utiliza a Evolution API (ou Baileys) para enviar e receber
    mensagens WhatsApp. Pode ser chamado diretamente ou via N8N.
    """

    def __init__(
        self,
        api_url: str | None = None,
        api_key: str | None = None,
    ) -> None:
        self._api_url = (api_url or settings.WHATSAPP_API_URL or "").rstrip("/")
        self._api_key = api_key or settings.WHATSAPP_API_KEY or ""
        self._enabled = bool(self._api_url and self._api_key)

    async def send_message(self, to: str, message: str) -> dict[str, Any]:
        """Envia uma mensagem WhatsApp.

        Args:
            to: Numero de telefone do destinatario (formato internacional).
            message: Texto da mensagem.

        Returns:
            Dict com status da operacao.
        """
        if not self._enabled:
            return {
                "status": "error",
                "message": "WhatsApp nao configurado (WHATSAPP_API_URL e WHATSAPP_API_KEY)",
            }

        try:
            async with httpx.AsyncClient(timeout=15) as client:
                resp = await client.post(
                    f"{self._api_url}/message/send",
                    json={
                        "number": to,
                        "text": message,
                    },
                    headers={
                        "Authorization": f"Bearer {self._api_key}",
                        "Content-Type": "application/json",
                    },
                )

                if resp.is_success:
                    logger.info("[whatsapp] sent to {}: '{}'", to, message[:50])
                    return {"status": "sent", "to": to}
                else:
                    logger.warning(
                        "[whatsapp] HTTP {}: {}", resp.status_code, resp.text
                    )
                    return {
                        "status": "error",
                        "message": f"HTTP {resp.status_code}: {resp.text[:200]}",
                    }

        except httpx.RequestError as e:
            logger.error("[whatsapp] request failed: {}", e)
            return {"status": "error", "message": str(e)}

    def is_configured(self) -> bool:
        return self._enabled
