"""Testes da configuracao HNSW no Qdrant.

Verifica que os parametros HNSW (m=32, ef_construct=200)
estao sendo aplicados na criacao das colecoes.
"""
import pytest
from unittest.mock import patch, MagicMock, call

from qdrant_client.models import HnswConfigDiff


class TestHNSWConfig:
    """Testa que o HNSW config eh aplicado corretamente."""

    @pytest.mark.asyncio
    @patch("app.providers.vector.qdrant.QdrantClient")
    async def test_qdrant_provider_uses_hnsw_config(self, mock_client_class) -> None:
        """Verifica que QdrantVectorStore cria colecao com HNSW config."""
        from app.providers.vector.qdrant import QdrantVectorStore

        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        # Simular colecao inexistente
        mock_client.get_collections.return_value.collections = []

        # Embedder mock
        mock_embedder = MagicMock()
        mock_embedder.dimension = 1024

        store = QdrantVectorStore()
        with patch.object(store, "_get_embedder", return_value=mock_embedder):
            await store._ensure_collection()

        # Verificar que create_collection foi chamado com HnswConfigDiff
        mock_client.create_collection.assert_called_once()
        call_kwargs = mock_client.create_collection.call_args.kwargs

        assert "hnsw_config" in call_kwargs
        hnsw = call_kwargs["hnsw_config"]
        assert isinstance(hnsw, HnswConfigDiff)
        assert hnsw.m == 32
        assert hnsw.ef_construct == 200
        assert hnsw.full_scan_threshold == 10000

    def test_vault_indexer_uses_hnsw_config(self) -> None:
        """Verifica que VaultIndexer cria colecao com HNSW config."""
        from app.rag.indexer.vault_indexer import VaultIndexer

        # Mock QdrantClient a nivel de classe para evitar init real
        with patch("app.rag.indexer.vault_indexer.QdrantClient") as mock_client_class:
            mock_client = MagicMock()
            mock_client_class.return_value = mock_client
            # Simular colecao inexistente
            mock_client.get_collections.return_value.collections = []

            with patch("app.rag.indexer.vault_indexer.get_embedder") as mock_get_emb:
                mock_embedder = MagicMock()
                mock_embedder.dimension = 1024
                mock_get_emb.return_value = mock_embedder

                indexer = VaultIndexer()

        # Verificar que create_collection foi chamado com HnswConfigDiff
        mock_client.create_collection.assert_called_once()
        call_kwargs = mock_client.create_collection.call_args.kwargs

        assert "hnsw_config" in call_kwargs
        hnsw = call_kwargs["hnsw_config"]
        assert isinstance(hnsw, HnswConfigDiff)
        assert hnsw.m == 32
        assert hnsw.ef_construct == 200

    def test_hnsw_config_default_values(self) -> None:
        """Verifica os valores padrao do HNSW config."""
        config = HnswConfigDiff(m=32, ef_construct=200, full_scan_threshold=10000)
        assert config.m == 32
        assert config.ef_construct == 200
        assert config.full_scan_threshold == 10000

    def test_hnsw_config_accepts_different_values(self) -> None:
        """Verifica que HNSW aceita valores customizados."""
        config = HnswConfigDiff(m=16, ef_construct=100)
        assert config.m == 16
        assert config.ef_construct == 100
