"""
PlannerPort — Task planning and agent orchestration capability.

Decomposes complex user intents into executable steps and orchestrates
their execution through the agent/workflow engine.
Current provider: LangGraph.
Future candidates: Letta (MemGPT), CrewAI, AutoGen.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class PlanStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class PlanStep:
    """A single step in an execution plan."""

    id: str
    action: str  # tool name or workflow node
    inputs: dict = field(default_factory=dict)
    depends_on: list[str] = field(default_factory=list)  # step IDs
    status: PlanStatus = PlanStatus.PENDING
    result: Optional[dict] = None
    error: Optional[str] = None


@dataclass
class PlanRequest:
    """Request to generate an execution plan."""

    intent: str
    context: dict = field(default_factory=dict)
    user_id: Optional[str] = None
    max_steps: int = 10


@dataclass
class PlanResult:
    """Generated execution plan."""

    plan_id: str
    steps: list[PlanStep] = field(default_factory=list)
    status: PlanStatus = PlanStatus.PENDING
    estimated_cost_usd: float = 0.0


class PlannerPort(ABC):
    """
    Interface for task planning and orchestration.

    Concrete implementations:
      - LangGraphAdapter   (current — workflow state machines)
      - LettaAdapter        (future — MemGPT autonomous loops)
      - CrewAIAdapter       (future — role-based agent teams)
    """

    @property
    @abstractmethod
    def provider_name(self) -> str: ...

    @abstractmethod
    async def plan(self, request: PlanRequest) -> PlanResult:
        """Generate an execution plan from an intent."""
        ...

    @abstractmethod
    async def execute(self, plan_id: str) -> PlanResult:
        """Execute a previously generated plan."""
        ...

    @abstractmethod
    async def status(self, plan_id: str) -> PlanResult:
        """Check the status of a plan."""
        ...

    @abstractmethod
    async def health(self) -> bool: ...
