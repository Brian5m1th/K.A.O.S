import pytest
from unittest.mock import MagicMock, patch
from app.runtime.runtime_selector import RuntimeSelector


class TestRuntimeSelector:
    @patch("app.llm.factory.LLMFactory")
    def test_select_by_objectives(self, MockFactory) -> None:
        # Mock LLMFactory build method to avoid actual provider initialization
        mock_factory = MagicMock()
        mock_factory.build.return_value = MagicMock()
        MockFactory.return_value = mock_factory

        selector = RuntimeSelector()

        # Test selecting offline/privacidade -> should select local runtime (ollama)
        run_offline = selector.select("privacidade")
        assert run_offline.type == "local"
        assert run_offline.capabilities["offline"] is True

        # Test selecting raciocinio/qualidade -> should select cloud (openai or gemini because of reasoning = True)
        run_quality = selector.select("raciocinio")
        assert run_quality.type == "cloud"
        assert run_quality.capabilities["reasoning"] is True
