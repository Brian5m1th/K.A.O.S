from abc import ABC, abstractmethod
from uuid import UUID


class BaseApp(ABC):
    app_id: UUID
    name: str
    version: str = "1.0.0"
    enabled: bool = True

    @abstractmethod
    async def start(self) -> None: ...

    @abstractmethod
    async def stop(self) -> None: ...

    @abstractmethod
    async def health(self) -> bool: ...

    @abstractmethod
    async def execute(self, action: str, payload: dict) -> dict: ...
