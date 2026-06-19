from unittest.mock import MagicMock, patch

from app.agent.state import AgentState


def _make_state(raw_path: str) -> AgentState:
    return AgentState(messages=[], ingest_source_path=raw_path)


class TestIngestSource:
    @patch("app.agent.nodes.ingest._get_provider")
    @patch("app.agent.nodes.ingest.create_entity")
    @patch("app.agent.nodes.ingest.create_concept")
    @patch("app.agent.nodes.ingest.create_source")
    @patch("app.agent.nodes.ingest.VaultIndexer")
    def test_ingest_full_flow(
        self,
        MockIndexer,
        MockCreateSource,
        MockCreateConcept,
        MockCreateEntity,
        MockGetProvider,
        tmp_path,
        monkeypatch,
    ) -> None:
        vault = tmp_path / "vault"
        vault.mkdir()
        raw_dir = vault / "raw"
        raw_dir.mkdir()
        doc = raw_dir / "test-source.md"
        doc.write_text("# Doc\n\nSome content.", encoding="utf-8")
        monkeypatch.setattr(
            "app.agent.nodes.ingest.settings.OBSIDIAN_VAULT_PATH", str(vault)
        )

        mock_provider = MagicMock()
        mock_response = MagicMock()
        mock_response.content = """{
            "title": "Test Doc",
            "summary": "A summary.",
            "entities": [{"name": "FastAPI", "summary": "Web framework", "tags": ["python"]}],
            "concepts": [{"name": "RAG", "summary": "Retrieval", "tags": ["ai"]}],
            "tags": ["test"]
        }"""
        mock_provider.invoke.return_value = mock_response
        MockGetProvider.return_value = mock_provider

        MockCreateSource.invoke.return_value = "sources/test-doc.md"

        MockCreateEntity.invoke.return_value = "entities/fastapi.md"
        MockCreateConcept.invoke.return_value = "concepts/rag.md"

        from app.agent.nodes.ingest import ingest_source

        result = ingest_source(_make_state("test-source.md"))

        assert "messages" in result
        msg = result["messages"][0].content
        assert "Test Doc" in msg
        assert "sources/test-doc.md" in msg
        assert "entities/fastapi.md" in msg
        assert "concepts/rag.md" in msg

        MockCreateSource.invoke.assert_called_once()
        MockCreateEntity.invoke.assert_called_once()
        MockCreateConcept.invoke.assert_called_once()
        MockIndexer.return_value.index_file.assert_called_once()

    def test_ingest_missing_path(self) -> None:
        from app.agent.nodes.ingest import ingest_source

        result = ingest_source(AgentState(messages=[], ingest_source_path=""))
        msg = result["messages"][0].content
        assert "caminho" in msg

    @patch("app.agent.nodes.ingest.settings")
    def test_ingest_file_not_found(self, MockSettings) -> None:
        MockSettings.OBSIDIAN_VAULT_PATH = "C:\\nonexistent"
        from app.agent.nodes.ingest import ingest_source

        result = ingest_source(_make_state("missing.md"))
        msg = result["messages"][0].content
        assert "nao encontrado" in msg

    @patch("app.agent.nodes.ingest._get_provider")
    def test_ingest_invalid_json_response(
        self, MockGetProvider, tmp_path, monkeypatch
    ) -> None:
        vault = tmp_path / "vault"
        vault.mkdir()
        raw_dir = vault / "raw"
        raw_dir.mkdir()
        (raw_dir / "bad.md").write_text("content", encoding="utf-8")
        monkeypatch.setattr(
            "app.agent.nodes.ingest.settings.OBSIDIAN_VAULT_PATH", str(vault)
        )

        mock_provider = MagicMock()
        mock_response = MagicMock()
        mock_response.content = "Not JSON at all"
        mock_provider.invoke.return_value = mock_response
        MockGetProvider.return_value = mock_provider

        from app.agent.nodes.ingest import ingest_source

        result = ingest_source(_make_state("bad.md"))
        msg = result["messages"][0].content
        assert "invalida" in msg
