"""WhatsApp Provider — Envio e recebimento de mensagens via Evolution API."""

from __future__ import annotations

from typing import Any
from datetime import datetime, timezone

import httpx
from loguru import logger

from app.config.settings import settings


class WhatsAppMessage:
    """Represents a received WhatsApp message."""

    def __init__(
        self,
        message_id: str,
        from_number: str,
        text: str,
        timestamp: datetime,
        chat_name: str = "",
    ) -> None:
        self.id = message_id
        self.from_number = from_number
        self.text = text
        self.timestamp = timestamp
        self.chat_name = chat_name

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "from": self.from_number,
            "text": self.text,
            "timestamp": self.timestamp.isoformat(),
            "chat_name": self.chat_name,
        }


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

    async def receive_messages(
        self, limit: int = 10, instance: str = "default"
    ) -> list[WhatsAppMessage]:
        """Recupera mensagens recebidas da fila do Evolution API.

        Args:
            limit: Numero maximo de mensagens a recuperar.
            instance: Nome da instancia Evolution API.

        Returns:
            Lista de mensagens recebidas.
        """
        if not self._enabled:
            logger.warning("[whatsapp] receive: not configured")
            return []

        try:
            async with httpx.AsyncClient(timeout=15) as client:
                resp = await client.get(
                    f"{self._api_url}/chat/fetchMessages/{instance}",
                    params={"limit": limit},
                    headers={
                        "Authorization": f"Bearer {self._api_key}",
                        "Content-Type": "application/json",
                    },
                )

                if resp.is_success:
                    data = resp.json()
                    messages = []
                    for item in (
                        data if isinstance(data, list) else data.get("messages", [])
                    ):
                        msg = WhatsAppMessage(
                            message_id=item.get("key", {}).get("id", ""),
                            from_number=(
                                item.get("key", {}).get("remoteJid", "")
                                or item.get("from", "")
                            ),
                            text=item.get("message", {}).get("conversation", "")
                            or item.get("text", ""),
                            timestamp=datetime.fromtimestamp(
                                item.get("messageTimestamp", 0), tz=timezone.utc
                            )
                            if item.get("messageTimestamp")
                            else datetime.now(timezone.utc),
                            chat_name=item.get("chatName", ""),
                        )
                        messages.append(msg)

                    logger.info("[whatsapp] received {} messages", len(messages))
                    return messages
                else:
                    logger.warning(
                        "[whatsapp] receive HTTP {}: {}", resp.status_code, resp.text
                    )
                    return []

        except httpx.RequestError as e:
            logger.error("[whatsapp] receive failed: {}", e)
            return []

    async def register_webhook(
        self, webhook_url: str, instance: str = "default"
    ) -> dict[str, Any]:
        """Registra um webhook para receber mensagens em tempo real.

        Args:
            webhook_url: URL publica para onde as mensagens serao enviadas.
            instance: Nome da instancia Evolution API.

        Returns:
            Dict com resultado do registro.
        """
        if not self._enabled:
            return {"status": "error", "message": "WhatsApp nao configurado"}

        try:
            async with httpx.AsyncClient(timeout=15) as client:
                resp = await client.post(
                    f"{self._api_url}/webhook/set/{instance}",
                    json={"webhookUrl": webhook_url},
                    headers={
                        "Authorization": f"Bearer {self._api_key}",
                        "Content-Type": "application/json",
                    },
                )

                if resp.is_success:
                    logger.info(
                        "[whatsapp] webhook registered: {} → {}", webhook_url, instance
                    )
                    return {"status": "registered", "webhook_url": webhook_url}
                else:
                    logger.warning(
                        "[whatsapp] webhook HTTP {}: {}", resp.status_code, resp.text
                    )
                    return {
                        "status": "error",
                        "message": f"HTTP {resp.status_code}: {resp.text[:200]}",
                    }

        except httpx.RequestError as e:
            logger.error("[whatsapp] webhook failed: {}", e)
            return {"status": "error", "message": str(e)}

    @staticmethod
    def process_webhook_payload(payload: dict) -> WhatsAppMessage | None:
        """Processa um payload de webhook recebido do Evolution API.

        Args:
            payload: JSON recebido no webhook.

        Returns:
            WhatsAppMessage estruturado ou None se invalido.
        """
        try:
            data = payload.get("data", payload)
            msg_data = data.get("message", data)

            return WhatsAppMessage(
                message_id=msg_data.get("key", {}).get("id", ""),
                from_number=(
                    msg_data.get("key", {}).get("remoteJid", "") or data.get("from", "")
                ),
                text=(
                    msg_data.get("message", {}).get("conversation", "")
                    or msg_data.get("text", "")
                    or data.get("text", "")
                ),
                timestamp=datetime.now(timezone.utc),
                chat_name=data.get("chatName", ""),
            )
        except Exception as exc:
            logger.warning("[whatsapp] failed to process webhook payload: {}", exc)
            return None

    def is_configured(self) -> bool:
        return self._enabled
