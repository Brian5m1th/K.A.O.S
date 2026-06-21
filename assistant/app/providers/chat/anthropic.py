from typing import AsyncIterator

from loguru import logger

from app.providers.base.chat import BaseChatProvider
from app.domain.chat import Message

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"


class AnthropicChatProvider(BaseChatProvider):
    provider_name = "anthropic"

    def __init__(self, api_key: str = "", model: str = "claude-sonnet-4-20250514"):
        self._api_key = api_key
        self._model = model

    async def chat(self, messages: list[Message], **kwargs) -> str:
        logger.info("[start] AnthropicChatProvider - chat")

        import httpx
        system = None
        chat_messages = []
        for m in messages:
            if m.role == "system":
                system = m.content
            else:
                chat_messages.append({"role": m.role, "content": m.content})

        payload = {
            "model": self._model,
            "messages": chat_messages,
            "max_tokens": kwargs.pop("max_tokens", 4096),
            **kwargs,
        }
        if system:
            payload["system"] = system

        headers = {
            "x-api-key": self._api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                ANTHROPIC_API_URL, json=payload, headers=headers
            )
            response.raise_for_status()
            data = response.json()

        logger.debug("[finish] AnthropicChatProvider - chat")
        return data["content"][0]["text"]

    async def stream(self, messages: list[Message], **kwargs) -> AsyncIterator[str]:
        logger.info("[start] AnthropicChatProvider - stream")

        import httpx
        import json as json_module
        system = None
        chat_messages = []
        for m in messages:
            if m.role == "system":
                system = m.content
            else:
                chat_messages.append({"role": m.role, "content": m.content})

        payload = {
            "model": self._model,
            "messages": chat_messages,
            "max_tokens": kwargs.pop("max_tokens", 4096),
            "stream": True,
            **kwargs,
        }
        if system:
            payload["system"] = system

        headers = {
            "x-api-key": self._api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        }
        async with httpx.AsyncClient(timeout=120.0) as client:
            async with client.stream(
                "POST", ANTHROPIC_API_URL, json=payload, headers=headers
            ) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        chunk_data = line[6:]
                        chunk = json_module.loads(chunk_data)
                        if chunk.get("type") == "content_block_delta":
                            delta = chunk.get("delta", {})
                            text = delta.get("text", "")
                            if text:
                                yield text

        logger.debug("[finish] AnthropicChatProvider - stream")

    async def models(self) -> list[str]:
        return [self._model]

    async def healthcheck(self) -> bool:
        import httpx
        try:
            headers = {
                "x-api-key": self._api_key,
                "anthropic-version": "2023-06-01",
            }
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(
                    "https://api.anthropic.com/v1/messages",
                    headers=headers,
                )
                return response.status_code in (200, 400)
        except httpx.RequestError:
            return False
