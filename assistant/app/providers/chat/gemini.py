from typing import AsyncIterator

from loguru import logger

from app.providers.base.chat import BaseChatProvider
from app.domain.chat import Message

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models"


class GeminiChatProvider(BaseChatProvider):
    provider_name = "gemini"

    def __init__(self, api_key: str = "", model: str = "gemini-2.0-flash"):
        self._api_key = api_key
        self._model = model

    def _convert_messages(self, messages: list[Message]) -> list[dict]:
        gemini_msgs = []
        system = None
        for m in messages:
            if m.role == "system":
                system = m.content
            else:
                role = "user" if m.role == "user" else "model"
                gemini_msgs.append({"role": role, "parts": [{"text": m.content}]})
        return gemini_msgs, system

    async def chat(self, messages: list[Message], **kwargs) -> str:
        logger.info("[start] GeminiChatProvider - chat")

        import httpx

        gemini_msgs, system = self._convert_messages(messages)
        payload = {"contents": gemini_msgs}
        if system:
            payload["system_instruction"] = {"parts": [{"text": system}]}

        url = f"{GEMINI_API_URL}/{self._model}:generateContent?key={self._api_key}"
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            data = response.json()

        logger.debug("[finish] GeminiChatProvider - chat")
        return data["candidates"][0]["content"]["parts"][0]["text"]

    async def stream(self, messages: list[Message], **kwargs) -> AsyncIterator[str]:
        logger.info("[start] GeminiChatProvider - stream")

        import httpx
        import json as json_module

        gemini_msgs, system = self._convert_messages(messages)
        payload = {"contents": gemini_msgs}
        if system:
            payload["system_instruction"] = {"parts": [{"text": system}]}

        url = f"{GEMINI_API_URL}/{self._model}:streamGenerateContent?key={self._api_key}&alt=sse"
        async with httpx.AsyncClient(timeout=120.0) as client:
            async with client.stream("POST", url, json=payload) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        chunk_data = line[6:]
                        if chunk_data == "[DONE]":
                            break
                        chunk = json_module.loads(chunk_data)
                        candidates = chunk.get("candidates", [])
                        if candidates:
                            parts = candidates[0].get("content", {}).get("parts", [])
                            for part in parts:
                                text = part.get("text", "")
                                if text:
                                    yield text

        logger.debug("[finish] GeminiChatProvider - stream")

    async def models(self) -> list[str]:
        return [self._model]

    async def healthcheck(self) -> bool:
        import httpx

        try:
            url = f"{GEMINI_API_URL}?key={self._api_key}"
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(url)
                return response.status_code == 200
        except httpx.RequestError:
            return False
