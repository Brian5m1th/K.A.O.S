from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class ExecutionContext:
    execution_id: UUID
    trace_id: UUID
    user_id: UUID
    session_id: UUID
    workflow: str
    model: str
    provider: str
    start_time: float = 0.0
    metadata: dict = field(default_factory=dict)

    @classmethod
    def from_plan(
        cls,
        execution_id: UUID,
        trace_id: UUID,
        user_id: UUID,
        session_id: UUID,
        workflow: str,
        model: str,
        provider: str,
        **metadata,
    ) -> "ExecutionContext":
        return cls(
            execution_id=execution_id,
            trace_id=trace_id,
            user_id=user_id,
            session_id=session_id,
            workflow=workflow,
            model=model,
            provider=provider,
            start_time=0.0,
            metadata=metadata,
        )

    def to_log_dict(self) -> dict:
        return {
            "execution_id": str(self.execution_id),
            "trace_id": str(self.trace_id),
            "user_id": str(self.user_id),
            "session_id": str(self.session_id),
            "workflow": self.workflow,
            "model": self.model,
            "provider": self.provider,
        }
