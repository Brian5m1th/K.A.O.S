from typing import AsyncIterator, Iterator

from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI

from app.llm.provider import BaseProvider


class OpenAIProvider(BaseProvider):
    def __init__(self, model: str, api_key: str, **kwargs):
        self._model = model
        self._llm = ChatOpenAI(model=model, api_key=api_key, **kwargs)

    def invoke(self, messages: list[BaseMessage]) -> BaseMessage:
        return self._llm.invoke(messages)

    async def ainvoke(self, messages: list[BaseMessage]) -> BaseMessage:
        return await self._llm.ainvoke(messages)

    def stream(self, messages: list[BaseMessage]) -> Iterator[BaseMessage]:
        return self._llm.stream(messages)

    async def astream(self, messages: list[BaseMessage]) -> AsyncIterator[BaseMessage]:
        async for chunk in self._llm.astream(messages):
            yield chunk

    @property
    def model_name(self) -> str:
        return self._model

    @property
    def provider_name(self) -> str:
        return "openai"
