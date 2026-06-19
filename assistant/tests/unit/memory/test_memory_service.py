from pathlib import Path

import pytest

from app.memory.memory_service import MemoryService


class TestMemoryService:
    @pytest.fixture
    def service(self, tmp_path: Path, monkeypatch) -> MemoryService:
        monkeypatch.setattr("app.config.settings.settings.OBSIDIAN_VAULT_PATH", str(tmp_path))
        return MemoryService()

    def test_save_conversation_creates_file(self, service: MemoryService) -> None:
        path = service.save_conversation(
            user_id="",
            session_id="test-123",
            summary="Conversa sobre Python",
            user_message="O que e Python?",
            assistant_response="Python e uma linguagem.",
        )
        assert path.endswith(".md")
        assert "conversa_" in path

    def test_save_and_get_preferences(self, service: MemoryService) -> None:
        service.save_preference(user_id="", key="lingua", value="portugues")
        prefs = service.get_preferences()
        assert "lingua" in prefs
        assert "portugues" in prefs

    def test_update_preference(self, service: MemoryService) -> None:
        service.save_preference(user_id="", key="lingua", value="portugues")
        service.save_preference(user_id="", key="lingua", value="ingles")
        prefs = service.get_preferences()
        assert "ingles" in prefs

    def test_list_recent_conversations(self, service: MemoryService) -> None:
        service.save_conversation(user_id="", session_id="s1", summary="sum1", user_message="msg1", assistant_response="resp1")
        service.save_conversation(user_id="", session_id="s2", summary="sum2", user_message="msg2", assistant_response="resp2")
        recent = service.list_recent_conversations(limit=5)
        assert len(recent) == 2

    def test_empty_preferences(self, service: MemoryService) -> None:
        prefs = service.get_preferences()
        assert prefs == ""
