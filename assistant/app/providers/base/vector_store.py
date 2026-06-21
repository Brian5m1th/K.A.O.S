from abc import ABC, abstractmethod

from app.domain.document import SearchResult


class BaseVectorStore(ABC):
    store_name: str = ""

    @abstractmethod
    async def upsert(self, collection: str, vectors: list[dict]) -> None: ...

    @abstractmethod
    async def search(
        self, collection: str, query_vector: list[float], limit: int
    ) -> list[SearchResult]: ...

    @abstractmethod
    async def delete(self, collection: str, ids: list[str]) -> None: ...

    @abstractmethod
    async def healthcheck(self) -> bool: ...
