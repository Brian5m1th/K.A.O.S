from unittest.mock import MagicMock, patch

import numpy as np

from app.rag.embeddings.embedder import Embedder


class TestEmbedder:
    @patch("sentence_transformers.SentenceTransformer")
    def test_embed_returns_float_vectors(self, MockST) -> None:
        mock_model = MagicMock()
        mock_model.encode.return_value = np.array(
            [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
        )
        MockST.return_value = mock_model

        embedder = Embedder(model_key="bge-m3")
        result = embedder.embed(["texto 1", "texto 2"])

        assert len(result) == 2
        assert all(isinstance(v, list) for v in result)
        assert all(isinstance(x, float) for v in result for x in v)

    @patch("sentence_transformers.SentenceTransformer")
    def test_embed_single_returns_single_vector(self, MockST) -> None:
        mock_model = MagicMock()
        mock_model.encode.return_value = np.array([[0.1, 0.2, 0.3]])
        MockST.return_value = mock_model

        embedder = Embedder(model_key="bge-m3")
        result = embedder.embed_single("texto unico")

        assert isinstance(result, list)
        assert len(result) == 3

    @patch("sentence_transformers.SentenceTransformer")
    def test_dimension_property(self, MockST) -> None:
        MockST.return_value = MagicMock()

        embedder = Embedder(model_key="bge-m3")
        assert embedder.dimension == 1024

        embedder2 = Embedder(model_key="nomic-embed-text")
        assert embedder2.dimension == 768
