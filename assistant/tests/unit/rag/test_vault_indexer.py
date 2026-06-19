from unittest.mock import MagicMock, patch

from app.rag.indexer.vault_indexer import VaultIndexer


class TestVaultIndexer:
    @patch("app.rag.indexer.vault_indexer.QdrantClient")
    @patch("app.rag.indexer.vault_indexer.get_embedder")
    @patch("app.rag.indexer.vault_indexer.MarkdownSplitter")
    def test_index_file_skips_nonexistent(
        self, MockSplitter, MockGetEmbedder, MockClient
    ) -> None:
        indexer = VaultIndexer()
        result = indexer.index_file("/nonexistent/file.md")
        assert result == 0

    @patch("app.rag.indexer.vault_indexer.QdrantClient")
    @patch("app.rag.indexer.vault_indexer.get_embedder")
    @patch("app.rag.indexer.vault_indexer.MarkdownSplitter")
    def test_index_file_skips_non_md(
        self, MockSplitter, MockGetEmbedder, MockClient
    ) -> None:
        indexer = VaultIndexer()
        result = indexer.index_file("file.txt")
        assert result == 0

    @patch("app.rag.indexer.vault_indexer.QdrantClient")
    @patch("app.rag.indexer.vault_indexer.get_embedder")
    def test_make_point_id_is_deterministic(self, MockGetEmbedder, MockClient) -> None:
        mock_embedder = MagicMock()
        mock_embedder.dimension = 1024
        MockGetEmbedder.return_value = mock_embedder
        indexer = VaultIndexer()

        id1 = indexer._make_point_id("nota.md", 0)
        id2 = indexer._make_point_id("nota.md", 0)
        id3 = indexer._make_point_id("nota.md", 1)

        assert id1 == id2
        assert id1 != id3

    @patch("app.rag.indexer.vault_indexer.QdrantClient")
    @patch("app.rag.indexer.vault_indexer.get_embedder")
    def test_ensure_collection_creates_if_missing(
        self, MockGetEmbedder, MockClient
    ) -> None:
        mock_instance = MagicMock()
        mock_instance.get_collections.return_value.collections = []
        MockClient.return_value = mock_instance
        mock_embedder = MagicMock()
        mock_embedder.dimension = 1024
        MockGetEmbedder.return_value = mock_embedder

        VaultIndexer()

        mock_instance.create_collection.assert_called_once()
        assert (
            mock_instance.create_collection.call_args[1]["vectors_config"].size == 1024
        )

    @patch("app.rag.indexer.vault_indexer.QdrantClient")
    @patch("app.rag.indexer.vault_indexer.get_embedder")
    def test_ensure_collection_skips_if_exists(
        self, MockGetEmbedder, MockClient
    ) -> None:
        mock_instance = MagicMock()
        mock_collection = MagicMock()
        mock_collection.name = "obsidian_memory"
        mock_instance.get_collections.return_value.collections = [mock_collection]
        mock_collection_info = MagicMock()
        mock_collection_info.config.params.vectors.size = 1024
        mock_instance.get_collection.return_value = mock_collection_info
        MockClient.return_value = mock_instance
        mock_embedder = MagicMock()
        mock_embedder.dimension = 1024
        MockGetEmbedder.return_value = mock_embedder

        VaultIndexer()

        mock_instance.create_collection.assert_not_called()
