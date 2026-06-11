from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.fixture
def client() -> AsyncClient:
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_openai_chat_completions(client: AsyncClient) -> None:
    mock_agent = MagicMock()
    mock_agent.process_message = AsyncMock(return_value="Resposta do RAG + Ollama")

    with patch("app.api.openai_compat.AgentService", return_value=mock_agent):
        response = await client.post(
            "/v1/chat/completions",
            json={
                "model": "qwen3:14b",
                "messages": [
                    {"role": "user", "content": "O que tem no meu vault?"}
                ],
            },
        )

    assert response.status_code == 200
    data = response.json()
    assert data["object"] == "chat.completion"
    assert len(data["choices"]) == 1
    assert data["choices"][0]["message"]["content"] == "Resposta do RAG + Ollama"


@pytest.mark.asyncio
async def test_openai_chat_completions_no_user_message(
    client: AsyncClient,
) -> None:
    response = await client.post(
        "/v1/chat/completions",
        json={
            "model": "qwen3:14b",
            "messages": [{"role": "assistant", "content": "Olá"}],
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert "Envie uma mensagem" in data["choices"][0]["message"]["content"]


@pytest.mark.asyncio
async def test_openai_chat_completions_empty_body_returns_422(
    client: AsyncClient,
) -> None:
    response = await client.post("/v1/chat/completions", json={})
    assert response.status_code == 422
