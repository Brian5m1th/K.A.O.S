from typing import Protocol


class MemoryRepository(Protocol):

    def get_preferences(self, user_id: str) -> str:
        ...

    def save_preference(self, user_id: str, key: str, value: str) -> None:
        ...

    def save_conversation(
        self, user_id: str, session_id: str, summary: str, user_message: str, assistant_response: str
    ) -> str:
        ...

    def list_recent_conversations(self, user_id: str, limit: int = 5) -> list[str]:
        ...
