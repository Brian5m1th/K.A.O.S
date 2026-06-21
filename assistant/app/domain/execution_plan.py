from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class CapabilityProfile:
    capabilities: list[str] = field(default_factory=list)

    def has(self, capability: str) -> bool:
        return capability in self.capabilities

    def has_any(self, capabilities: list[str]) -> bool:
        return any(c in self.capabilities for c in capabilities)

    def has_all(self, capabilities: list[str]) -> bool:
        return all(c in self.capabilities for c in capabilities)

    def merge(self, other: "CapabilityProfile") -> "CapabilityProfile":
        merged = list(set(self.capabilities + other.capabilities))
        return CapabilityProfile(capabilities=merged)

    def __len__(self) -> int:
        return len(self.capabilities)


@dataclass
class ExecutionPlan:
    execution_id: UUID
    trace_id: UUID
    user_id: UUID
    session_id: UUID
    workflow: str
    selected_model: str
    capabilities: list[str] = field(default_factory=list)
    provider_configs: dict = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        workflow: str,
        selected_model: str,
        user_id: UUID,
        session_id: UUID,
        capabilities: list[str] | None = None,
        provider_configs: dict | None = None,
        execution_id: UUID | None = None,
        trace_id: UUID | None = None,
    ) -> "ExecutionPlan":
        return cls(
            execution_id=execution_id or uuid4(),
            trace_id=trace_id or uuid4(),
            user_id=user_id,
            session_id=session_id,
            workflow=workflow,
            selected_model=selected_model,
            capabilities=capabilities or [],
            provider_configs=provider_configs or {},
        )

    @property
    def capability_profile(self) -> CapabilityProfile:
        return CapabilityProfile(capabilities=self.capabilities)
