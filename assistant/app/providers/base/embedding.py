from abc import ABC, abstractmethod


class BaseEmbeddingProvider(ABC):
    provider_name: str = ""

    @abstractmethod
    async def embed(self, text: str) -> list[float]: ...

    @abstractmethod
    async def embed_batch(self, texts: list[str]) -> list[list[float]]: ...

    @abstractmethod
    async def healthcheck(self) -> bool: ...
