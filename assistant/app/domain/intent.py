from dataclasses import dataclass

from app.domain.workflow import WorkflowType
from app.domain.command import CommandType


@dataclass
class IntentResult:
    workflow: WorkflowType
    command: CommandType | None = None
    confidence: float = 0.0
