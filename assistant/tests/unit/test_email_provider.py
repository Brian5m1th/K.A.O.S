"""Testes do provedor de Email."""
from unittest.mock import patch, MagicMock

from app.providers.email.email_reader import EmailReader
from app.providers.email.email_sender import EmailSender
from app.providers.email.email_tool import read_emails, send_email


class TestEmailReader:
    def test_not_configured(self) -> None:
        reader = EmailReader(host="", username="", password="")
        assert reader.is_configured() is False
        messages = reader.fetch_inbox()
        assert messages == []

    @patch("app.providers.email.email_reader.imaplib.IMAP4_SSL")
    def test_fetch_inbox(self, mock_imap) -> None:
        reader = EmailReader(host="imap.test.com", username="user", password="pass")

        mock_conn = MagicMock()
        mock_imap.return_value = mock_conn
        mock_conn.search.return_value = ("OK", [b"1 2 3"])

        # Mock fetch to return email-like data
        def mock_fetch(uid, part):
            raw_email = (
                b"From: sender@test.com\r\n"
                b"Subject: Test Subject\r\n"
                b"Date: Mon, 01 Jan 2026 12:00:00 +0000\r\n"
                b"Content-Type: text/plain\r\n"
                b"\r\n"
                b"Hello, this is a test email."
            )
            return ("OK", [(b"1", raw_email)])

        mock_conn.fetch.side_effect = mock_fetch

        messages = reader.fetch_inbox(limit=1)
        assert len(messages) == 1
        assert messages[0].subject == "Test Subject"

    def test_decode_mime_header(self) -> None:
        reader = EmailReader(host="", username="", password="")
        result = reader._decode_mime_header("=?utf-8?B?w4bDpcOj?=")
        assert result  # nao vazio

    def test_decode_mime_header_none(self) -> None:
        reader = EmailReader(host="", username="", password="")
        assert reader._decode_mime_header(None) == ""


class TestEmailSender:
    def test_not_configured(self) -> None:
        sender = EmailSender(host="", username="", password="")
        assert sender.is_configured() is False
        result = sender.send("test@test.com", "Subject", "Body")
        assert result["status"] == "error"

    @patch("app.providers.email.email_sender.smtplib.SMTP")
    def test_send_success(self, mock_smtp) -> None:
        sender = EmailSender(
            host="smtp.test.com",
            port=587,
            username="user@test.com",
            password="pass",
            from_addr="user@test.com",
        )

        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server

        result = sender.send(to="recipient@test.com", subject="Hello", body="World")
        assert result["status"] == "sent"
        mock_server.sendmail.assert_called_once()


class TestEmailTools:
    def test_read_emails_not_configured(self) -> None:
        with patch("app.providers.email.email_tool.EmailReader.is_configured", return_value=False):
            result = read_emails.invoke({"limit": 5})
            assert result["status"] == "error"

    def test_send_email_not_configured(self) -> None:
        with patch("app.providers.email.email_tool.EmailSender.is_configured", return_value=False):
            result = send_email.invoke({"to": "a@b.com", "subject": "S", "body": "B"})
            assert result["status"] == "error"
