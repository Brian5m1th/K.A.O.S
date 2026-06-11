from unittest.mock import MagicMock, patch

import pytest

from app.agent.nodes.executor import TOOL_REGISTRY


class TestExecutor:
    def test_tool_registry_has_expected_tools(self) -> None:
        expected = {
            "create_note",
            "read_note",
            "update_note",
            "delete_note",
            "search_notes",
        }
        assert set(TOOL_REGISTRY.keys()) == expected

    def test_tool_registry_tools_have_invoke(self) -> None:
        for name, tool in TOOL_REGISTRY.items():
            assert hasattr(tool, "invoke"), f"{name} não tem invoke"
