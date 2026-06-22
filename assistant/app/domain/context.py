from dataclasses import dataclass
from uuid import UUID

from app.domain.identity import UserIdentity, WorkspaceIdentity
from app.domain.chat import Message


@dataclass
class RequestContext:
    execution_id: UUID
    trace_id: UUID
    workspace: WorkspaceIdentity
    user: UserIdentity
    api_key_id: UUID | None
    session_id: UUID
    history: list[Message]
    workflow: str
    metadata: dict
