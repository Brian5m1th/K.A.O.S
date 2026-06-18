from unittest.mock import MagicMock, patch

import pytest

from app.agent.nodes.executor import TOOL_REGISTRY


class TestExecutor:
    def test_tool_registry_has_wiki_tools(self) -> None:
        wiki_tools = {
            "create_entity", "update_entity",
            "create_concept", "update_concept",
            "create_source", "create_synthesis",
            "file_synthesis_page",
            "append_log", "update_index",
            "approve_draft", "reject_draft", "list_drafts",
            "read_wiki_page", "lint_wiki",
        }
        assert wiki_tools.issubset(set(TOOL_REGISTRY.keys()))

    def test_tool_registry_has_core_tools(self) -> None:
        core = {
            "create_note", "read_note", "update_note",
            "delete_note", "search_notes", "list_notes",
            "list_projects", "save_conversation",
        }
        assert core.issubset(set(TOOL_REGISTRY.keys()))

    def test_tool_registry_tools_have_invoke(self) -> None:
        for name, tool in TOOL_REGISTRY.items():
            assert hasattr(tool, "invoke"), f"{name} não tem invoke"
