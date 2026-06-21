from abc import ABC, abstractmethod
from typing import AsyncIterator

from app.domain.chat import Message


class BaseChatProvider(ABC):
    provider_name: str = ""

    @abstractmethod
    async def chat(self, messages: list[Message], **kwargs) -> str: ...

    @abstractmethod
    async def stream(self, messages: list[Message], **kwargs) -> AsyncIterator[str]: ...

    @abstractmethod
    async def models(self) -> list[str]: ...

    @abstractmethod
    async def healthcheck(self) -> bool: ...
