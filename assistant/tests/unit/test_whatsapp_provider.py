"""Testes do provedor WhatsApp."""

from unittest.mock import patch, MagicMock, AsyncMock
import pytest

from app.providers.whatsapp.whatsapp_provider import WhatsAppProvider
from app.providers.whatsapp.whatsapp_tool import send_whatsapp


class TestWhatsAppProvider:
    def test_not_configured(self) -> None:
        provider = WhatsAppProvider(api_url="", api_key="")
        assert provider.is_configured() is False

    @pytest.mark.asyncio
    async def test_send_message_not_configured(self) -> None:
        provider = WhatsAppProvider(api_url="", api_key="")
        result = await provider.send_message("5511999999999", "Hello")
        assert result["status"] == "error"

    @pytest.mark.asyncio
    async def test_send_message_success(self) -> None:
        provider = WhatsAppProvider(api_url="https://evo.test.com", api_key="key123")

        mock_response = MagicMock()
        mock_response.is_success = True

        mock_client = AsyncMock()
        mock_client.post = AsyncMock(return_value=mock_response)

        with patch(
            "app.providers.whatsapp.whatsapp_provider.httpx.AsyncClient"
        ) as mock_client_class:
            mock_client_class.return_value.__aenter__.return_value = mock_client

            result = await provider.send_message("5511999999999", "Hello!")
            assert result["status"] == "sent"

    @pytest.mark.asyncio
    async def test_send_message_http_error(self) -> None:
        provider = WhatsAppProvider(api_url="https://evo.test.com", api_key="key123")

        mock_response = MagicMock()
        mock_response.is_success = False
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"

        mock_client = AsyncMock()
        mock_client.post = AsyncMock(return_value=mock_response)

        with patch(
            "app.providers.whatsapp.whatsapp_provider.httpx.AsyncClient"
        ) as mock_client_class:
            mock_client_class.return_value.__aenter__.return_value = mock_client

            result = await provider.send_message("5511999999999", "Hello!")
            assert result["status"] == "error"


class TestWhatsAppTool:
    def test_tool_not_configured(self) -> None:
        with patch(
            "app.providers.whatsapp.whatsapp_tool.WhatsAppProvider.is_configured",
            return_value=False,
        ):
            result = send_whatsapp.invoke({"to": "5511999999999", "message": "Hello"})
            assert result["status"] == "error"
