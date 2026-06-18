from abc import ABC, abstractmethod
from typing import AsyncIterator, Iterator

from langchain_core.messages import BaseMessage


class BaseProvider(ABC):
    @abstractmethod
    def invoke(self, messages: list[BaseMessage]) -> BaseMessage:
        ...

    @abstractmethod
    async def ainvoke(self, messages: list[BaseMessage]) -> BaseMessage:
        ...

    @abstractmethod
    def stream(self, messages: list[BaseMessage]) -> Iterator[BaseMessage]:
        ...

    @abstractmethod
    async def astream(self, messages: list[BaseMessage]) -> AsyncIterator[BaseMessage]:
        ...

    @property
    @abstractmethod
    def model_name(self) -> str:
        ...

    @property
    @abstractmethod
    def provider_name(self) -> str:
        ...
