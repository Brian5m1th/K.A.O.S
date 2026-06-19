from unittest.mock import AsyncMock, MagicMock, patch

import pytest


class TestLLMFactory:
    def test_build_ollama_provider(self) -> None:
        from app.llm import LLMFactory

        factory = LLMFactory()
        provider = factory.build("default")
        assert provider.provider_name == "ollama"

    @patch("app.llm.factory.settings")
    def test_resolve_model_config_from_map(self, MockSettings) -> None:
        MockSettings.MODEL_MAP = {
            "phi4": {"provider": "ollama", "model": "phi4:latest"}
        }
        MockSettings.API_MODEL_ID = "default"
        MockSettings.FAST_MODEL_ID = "fast"
        MockSettings.DEFAULT_MODEL_ID = "default"
        MockSettings.OLLAMA_MODEL = "deepseek-r1:14b"
        MockSettings.OLLAMA_FAST_MODEL = "qwen2.5:7b"

        from app.llm import LLMFactory

        factory = LLMFactory()
        config = factory._resolve_model_config("phi4")
        assert config["model"] == "phi4:latest"

    def test_fallback_chain_parse(self, monkeypatch) -> None:
        monkeypatch.setattr(
            "app.llm.factory.settings.FALLBACK_CHAIN",
            "ollama:deepseek-r1:14b,openai:gpt-4o",
        )
        from app.llm import LLMFactory

        factory = LLMFactory()
        assert len(factory._fallbacks) == 2
        assert factory._fallbacks[0] == {
            "provider": "ollama",
            "model": "deepseek-r1:14b",
        }
        assert factory._fallbacks[1] == {"provider": "openai", "model": "gpt-4o"}

    @patch("app.llm.factory.LLMFactory._create_provider")
    def test_async_fallback_kicks_in_on_failure(self, MockCreateProvider) -> None:
        first = MagicMock()
        first.provider_name = "ollama"
        first.model_name = "deepseek-r1:14b"
        first.ainvoke = AsyncMock(side_effect=Exception("Ollama down"))

        second = MagicMock()
        second.provider_name = "openai"
        second.model_name = "gpt-4o"
        mock_response = MagicMock()
        mock_response.content = "Hello from fallback"
        mock_response.usage_metadata = None
        second.ainvoke = AsyncMock(return_value=mock_response)

        MockCreateProvider.side_effect = [first, second]

        monkeypatch = pytest.MonkeyPatch()
        monkeypatch.setattr(
            "app.llm.factory.settings.FALLBACK_CHAIN",
            "ollama:deepseek-r1:14b,openai:gpt-4o",
        )

        import asyncio
        from app.llm import LLMFactory

        factory = LLMFactory()
        result = asyncio.run(factory.ainvoke_with_fallback("default", []))

        assert result == "Hello from fallback"
        first.ainvoke.assert_called_once()
        second.ainvoke.assert_called_once()

    @patch("app.llm.factory.LLMFactory._create_provider")
    def test_all_fallbacks_fail_raises_error(self, MockCreateProvider) -> None:
        first = MagicMock()
        first.ainvoke.side_effect = Exception("fail 1")
        second = MagicMock()
        second.ainvoke.side_effect = Exception("fail 2")

        MockCreateProvider.side_effect = [first, second]

        monkeypatch = pytest.MonkeyPatch()
        monkeypatch.setattr(
            "app.llm.factory.settings.FALLBACK_CHAIN", "ollama:m1,openai:m2"
        )

        import asyncio
        from app.llm import LLMFactory

        factory = LLMFactory()
        with pytest.raises(
            RuntimeError, match="Todos os providers da fallback chain falharam"
        ):
            asyncio.run(factory.ainvoke_with_fallback("default", []))

    def test_metrics_collected_after_invoke(self, monkeypatch) -> None:
        monkeypatch.setattr(
            "app.llm.factory.settings.FALLBACK_CHAIN", "ollama:deepseek-r1:14b"
        )

        mock_provider = MagicMock()
        mock_provider.provider_name = "ollama"
        mock_provider.model_name = "deepseek-r1:14b"
        mock_response = MagicMock()
        mock_response.content = "OK"
        mock_response.usage_metadata = None
        mock_provider.ainvoke = AsyncMock(return_value=mock_response)

        import asyncio
        from app.llm import LLMFactory

        factory = LLMFactory()
        factory._fallbacks = [{"provider": "ollama", "model": "deepseek-r1:14b"}]

        with patch.object(factory, "_create_provider", return_value=mock_provider):
            asyncio.run(factory.ainvoke_with_fallback("default", []))

        summary = factory.metrics.summary()
        assert summary["total_calls"] == 1
        assert summary["total_cost"] == 0.0
