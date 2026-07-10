"""Email Reader — Leitura e triagem de mensagens via IMAP."""

from __future__ import annotations

import imaplib
import email
from email.header import decode_header
from email.message import Message
from dataclasses import dataclass

from loguru import logger

from app.config.settings import settings


@dataclass
class EmailMessage:
    """Representa uma mensagem de email."""

    uid: str
    subject: str
    sender: str
    date: str
    body: str
    snippet: str = ""


class EmailReader:
    """Leitor de email via protocolo IMAP.

    Responsavel por conectar ao servidor IMAP, listar mensagens
    da caixa de entrada e extrair conteudo.
    """

    def __init__(
        self,
        host: str | None = None,
        port: int | None = None,
        username: str | None = None,
        password: str | None = None,
    ) -> None:
        self._host = host or settings.EMAIL_HOST or ""
        self._port = port or settings.EMAIL_PORT or 993
        self._username = username or settings.EMAIL_USER or ""
        self._password = password or settings.EMAIL_PASS or ""
        self._connected = False

    def _decode_mime_header(self, header_value: str | None) -> str:
        """Decodifica cabecalho MIME para string legivel."""
        if not header_value:
            return ""
        decoded_parts = decode_header(header_value)
        result = []
        for part, charset in decoded_parts:
            if isinstance(part, bytes):
                try:
                    result.append(part.decode(charset or "utf-8", errors="replace"))
                except (LookupError, UnicodeDecodeError):
                    result.append(part.decode("utf-8", errors="replace"))
            else:
                result.append(str(part))
        return "".join(result)

    def _get_email_body(self, msg: Message) -> str:
        """Extrai o corpo do email (text/plain优先)."""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    payload = part.get_payload(decode=True)
                    if payload:
                        return payload.decode("utf-8", errors="replace")
                elif content_type == "text/html":
                    payload = part.get_payload(decode=True)
                    if payload:
                        return payload.decode("utf-8", errors="replace")
        else:
            payload = msg.get_payload(decode=True)
            if payload:
                return payload.decode("utf-8", errors="replace")
        return ""

    def fetch_inbox(self, limit: int = 10) -> list[EmailMessage]:
        """Busca os emails mais recentes da caixa de entrada.

        Args:
            limit: Numero maximo de mensagens a retornar.

        Returns:
            Lista de EmailMessage ordenada por data (mais recente primeiro).
        """
        if not self._host:
            logger.warning("[email] EMAIL_HOST nao configurado")
            return []

        messages: list[EmailMessage] = []
        try:
            mail = imaplib.IMAP4_SSL(self._host, self._port)
            mail.login(self._username, self._password)
            mail.select("INBOX")

            _, data = mail.search(None, "ALL")
            uids = data[0].split() if data[0] else []
            # Pegar os mais recentes
            for uid in uids[-limit:]:
                _, msg_data = mail.fetch(uid, "(RFC822)")
                if msg_data[0] is None:
                    continue
                raw_email = msg_data[0][1]
                msg = email.message_from_bytes(raw_email)

                subject = self._decode_mime_header(msg.get("Subject", ""))
                sender = self._decode_mime_header(msg.get("From", ""))
                date = msg.get("Date", "")
                body = self._get_email_body(msg)

                messages.append(
                    EmailMessage(
                        uid=uid.decode() if isinstance(uid, bytes) else str(uid),
                        subject=subject,
                        sender=sender,
                        date=date,
                        body=body,
                        snippet=body[:200].strip(),
                    )
                )

            mail.logout()
            self._connected = True
            logger.info("[email] fetched {} messages from INBOX", len(messages))

        except imaplib.IMAP4.error as e:
            logger.error("[email] IMAP error: {}", e)
        except Exception as e:
            logger.error("[email] failed to fetch emails: {}", e)

        return messages

    def is_configured(self) -> bool:
        """Verifica se o servico de email esta configurado."""
        return bool(self._host and self._username and self._password)
