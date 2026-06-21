from abc import ABC, abstractmethod

from app.domain.chat import Message


class BaseMemoryProvider(ABC):
    provider_name: str = ""

    @abstractmethod
    async def save(self, session_id: str, messages: list[Message]) -> None: ...

    @abstractmethod
    async def load(self, session_id: str) -> list[Message]: ...

    @abstractmethod
    async def clear(self, session_id: str) -> None: ...

    @abstractmethod
    async def healthcheck(self) -> bool: ...
