from dataclasses import dataclass
from uuid import UUID


@dataclass
class WorkspaceIdentity:
    workspace_id: UUID
    owner_user_id: UUID
    slug: str


@dataclass
class UserIdentity:
    user_id: UUID
    workspace_id: UUID
    slug: str
