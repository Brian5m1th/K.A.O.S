from unittest.mock import MagicMock, patch

from app.domain.document import SearchResult
from app.rag.retriever.semantic_retriever import SemanticRetriever


class TestSemanticRetriever:
    @patch("app.rag.retriever.semantic_retriever.QdrantClient")
    @patch("app.rag.retriever.semantic_retriever.get_embedder")
    def test_search_returns_search_results(
        self, MockGetEmbedder, MockClient
    ) -> None:
        mock_embedder = MagicMock()
        mock_embedder.embed_single.return_value = [0.1, 0.2, 0.3]
        MockGetEmbedder.return_value = mock_embedder

        mock_qdrant = MagicMock()
        mock_hit = MagicMock()
        mock_hit.score = 0.95
        mock_hit.payload = {
            "path": "nota.md",
            "content": "Conteudo da nota com ate 300 caracteres...",
        }
        mock_qdrant.search.return_value = [mock_hit]
        MockClient.return_value = mock_qdrant

        retriever = SemanticRetriever()
        results = retriever.search("consulta teste", limit=3)

        assert len(results) == 1
        assert isinstance(results[0], SearchResult)
        assert results[0].path == "nota.md"
        assert results[0].score == 0.95

    @patch("app.rag.retriever.semantic_retriever.QdrantClient")
    @patch("app.rag.retriever.semantic_retriever.get_embedder")
    def test_search_with_folder_filter(
        self, MockGetEmbedder, MockClient
    ) -> None:
        mock_embedder = MagicMock()
        mock_embedder.embed_single.return_value = [0.1, 0.2, 0.3]
        MockGetEmbedder.return_value = mock_embedder

        mock_qdrant = MagicMock()
        mock_qdrant.search.return_value = []
        MockClient.return_value = mock_qdrant

        retriever = SemanticRetriever()
        results = retriever.search("consulta", folder_filter="Inbox")

        assert results == []
        call_kwargs = mock_qdrant.search.call_args[1]
        assert call_kwargs["query_filter"] is not None

    @patch("app.rag.retriever.semantic_retriever.QdrantClient")
    @patch("app.rag.retriever.semantic_retriever.get_embedder")
    def test_search_without_filter(
        self, MockGetEmbedder, MockClient
    ) -> None:
        mock_embedder = MagicMock()
        mock_embedder.embed_single.return_value = [0.1, 0.2, 0.3]
        MockGetEmbedder.return_value = mock_embedder

        mock_qdrant = MagicMock()
        mock_qdrant.search.return_value = []
        MockClient.return_value = mock_qdrant

        retriever = SemanticRetriever()
        results = retriever.search("consulta")

        assert results == []
        call_kwargs = mock_qdrant.search.call_args[1]
        assert call_kwargs["query_filter"] is None
