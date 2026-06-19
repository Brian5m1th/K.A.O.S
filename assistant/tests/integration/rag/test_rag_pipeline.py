from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from app.domain.document import SearchResult


@pytest.fixture
def test_vault(tmp_path: Path) -> Path:
    vault = tmp_path / "test_vault"
    vault.mkdir()
    (vault / "nota1.md").write_text("# Nota 1\n\nEste é um documento sobre Python e FastAPI.", encoding="utf-8")
    (vault / "nota2.md").write_text("# Nota 2\n\nEste documento fala sobre arquitetura de software.", encoding="utf-8")
    (vault / "nota3.md").write_text("# Nota 3\n\nPython é uma linguagem de programação versátil.", encoding="utf-8")
    return vault


class TestRAGPipeline:
    @patch("app.rag.indexer.vault_indexer.QdrantClient")
    @patch("app.rag.indexer.vault_indexer.get_embedder")
    def test_index_and_retrieve_flow(
        self, MockGetEmbedder, MockQdrantClient, test_vault, monkeypatch
    ) -> None:
        monkeypatch.setattr("app.config.settings.settings.OBSIDIAN_VAULT_PATH", str(test_vault))

        mock_embedder = MagicMock()
        mock_embedder.dimension = 1024
        mock_embedder.embed.return_value = [[0.1] * 1024, [0.2] * 1024]
        MockGetEmbedder.return_value = mock_embedder

        mock_client = MagicMock()
        mock_client.get_collections.return_value = MagicMock(collections=[])
        MockQdrantClient.return_value = mock_client

        from app.rag.indexer.vault_indexer import VaultIndexer
        VaultIndexer()

        mock_hit = MagicMock()
        mock_hit.score = 0.92
        mock_hit.payload = {
            "path": "nota1.md",
            "content": "Este é um documento sobre Python e FastAPI. " * 10,
        }
        mock_client.search.return_value = [mock_hit]

        from app.rag.retriever.semantic_retriever import SemanticRetriever
        with patch("app.rag.retriever.semantic_retriever.QdrantClient", return_value=mock_client):
            with patch("app.rag.retriever.semantic_retriever.get_embedder") as MockRetEmbedder:
                mock_ret_embedder = MagicMock()
                mock_ret_embedder.embed_single.return_value = [0.1] * 1024
                MockRetEmbedder.return_value = mock_ret_embedder

                retriever = SemanticRetriever()
                results = retriever.search("Python", limit=5)

        assert len(results) == 1
        assert isinstance(results[0], SearchResult)
        assert results[0].score == 0.92
        assert "Python" in results[0].excerpt

    @pytest.mark.xfail(reason="MarkdownSplitter does not split long paragraphs within chunk_size bounds")
    def test_chunking_produces_valid_chunks(self) -> None:
        from app.rag.chunking.text_splitter import MarkdownSplitter, TextChunk

        splitter = MarkdownSplitter(chunk_size=800, overlap=150)
        text = "# Titulo\n\n" + "Conteudo. " * 200
        chunks = splitter.split(text, "nota.md")

        assert len(chunks) >= 1
        for chunk in chunks:
            assert isinstance(chunk, TextChunk)
            assert chunk.source_path == "nota.md"
            assert len(chunk.content) <= 800 + 150

    @patch("app.rag.retriever.semantic_retriever.QdrantClient")
    @patch("app.rag.retriever.semantic_retriever.get_embedder")
    def test_retriever_empty_results(
        self, MockGetEmbedder, MockQdrantClient
    ) -> None:
        mock_embedder = MagicMock()
        mock_embedder.embed_single.return_value = [0.1, 0.2, 0.3]
        MockGetEmbedder.return_value = mock_embedder

        mock_client = MagicMock()
        mock_client.search.return_value = []
        MockQdrantClient.return_value = mock_client

        from app.rag.retriever.semantic_retriever import SemanticRetriever
        retriever = SemanticRetriever()
        results = retriever.search("consulta sem resultados")

        assert results == []
