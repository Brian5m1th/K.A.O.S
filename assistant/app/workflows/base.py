from abc import ABC, abstractmethod
from typing import AsyncIterator

from app.domain.chat import ChatRequest
from app.domain.execution_plan import ExecutionPlan


class BaseWorkflow(ABC):
    name: str = ""
    version: str = "1.0"

    @property
    @abstractmethod
    def required_capabilities(self) -> list[str]: ...

    @abstractmethod
    async def execute(
        self, plan: ExecutionPlan, request: ChatRequest
    ) -> AsyncIterator[str]: ...

    @abstractmethod
    async def healthcheck(self) -> bool: ...
