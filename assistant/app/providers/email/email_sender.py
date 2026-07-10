"""Email Sender — Envio de mensagens via SMTP."""

from __future__ import annotations

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Any

from loguru import logger

from app.config.settings import settings


class EmailSender:
    """Envio de email via protocolo SMTP.

    Responsavel por enviar mensagens de email utilizando o servidor SMTP
    configurado no .env.
    """

    def __init__(
        self,
        host: str | None = None,
        port: int | None = None,
        username: str | None = None,
        password: str | None = None,
        from_addr: str | None = None,
    ) -> None:
        self._host = host or settings.EMAIL_HOST or ""
        self._port = port or settings.EMAIL_SMTP_PORT or 587
        self._username = username or settings.EMAIL_USER or ""
        self._password = password or settings.EMAIL_PASS or ""
        self._from = from_addr or settings.EMAIL_FROM or self._username

    def send(
        self,
        to: str,
        subject: str,
        body: str,
        html: str | None = None,
    ) -> dict[str, Any]:
        """Envia um email.

        Args:
            to: Endereco de email do destinatario.
            subject: Assunto do email.
            body: Corpo do email em texto puro.
            html: Corpo opcional em HTML (sobrescreve body se fornecido).

        Returns:
            Dict com status da operacao.
        """
        if not self._host:
            return {"status": "error", "message": "EMAIL_HOST nao configurado"}

        try:
            msg = MIMEMultipart("alternative")
            msg["From"] = self._from
            msg["To"] = to
            msg["Subject"] = subject

            msg.attach(MIMEText(body, "plain", "utf-8"))
            if html:
                msg.attach(MIMEText(html, "html", "utf-8"))

            with smtplib.SMTP(self._host, self._port) as server:
                server.starttls()
                server.login(self._username, self._password)
                server.sendmail(self._from, [to], msg.as_string())

            logger.info("[email] sent to {}: '{}'", to, subject)
            return {"status": "sent", "to": to, "subject": subject}

        except smtplib.SMTPException as e:
            logger.error("[email] SMTP error: {}", e)
            return {"status": "error", "message": str(e)}
        except Exception as e:
            logger.error("[email] failed to send: {}", e)
            return {"status": "error", "message": str(e)}

    def is_configured(self) -> bool:
        return bool(self._host and self._username and self._password)
