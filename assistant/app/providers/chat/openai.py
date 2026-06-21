from typing import AsyncIterator

from loguru import logger

from app.providers.base.chat import BaseChatProvider
from app.domain.chat import Message


class OpenAIChatProvider(BaseChatProvider):
    provider_name = "openai"

    def __init__(self, api_key: str = "", model: str = "gpt-4o", base_url: str = ""):
        self._api_key = api_key
        self._model = model
        self._base_url = base_url or "https://api.openai.com/v1"

    async def chat(self, messages: list[Message], **kwargs) -> str:
        logger.info("[start] OpenAIChatProvider - chat")

        import httpx

        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self._model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            **kwargs,
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{self._base_url}/chat/completions",
                json=payload,
                headers=headers,
            )
            response.raise_for_status()
            data = response.json()

        logger.debug("[finish] OpenAIChatProvider - chat")
        return data["choices"][0]["message"]["content"]

    async def stream(self, messages: list[Message], **kwargs) -> AsyncIterator[str]:
        logger.info("[start] OpenAIChatProvider - stream")

        import httpx

        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self._model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "stream": True,
            **kwargs,
        }
        async with httpx.AsyncClient(timeout=120.0) as client:
            async with client.stream(
                "POST",
                f"{self._base_url}/chat/completions",
                json=payload,
                headers=headers,
            ) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        chunk_data = line[6:]
                        if chunk_data.strip() == "[DONE]":
                            break
                        import json as json_module

                        chunk = json_module.loads(chunk_data)
                        delta = chunk.get("choices", [{}])[0].get("delta", {})
                        content = delta.get("content", "")
                        if content:
                            yield content

        logger.debug("[finish] OpenAIChatProvider - stream")

    async def models(self) -> list[str]:
        import httpx

        headers = {"Authorization": f"Bearer {self._api_key}"}
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{self._base_url}/models", headers=headers)
            response.raise_for_status()
            data = response.json()
            return [m["id"] for m in data.get("data", [])]

    async def healthcheck(self) -> bool:
        import httpx

        try:
            headers = {"Authorization": f"Bearer {self._api_key}"}
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(f"{self._base_url}/models", headers=headers)
                return response.status_code == 200
        except httpx.RequestError:
            return False
