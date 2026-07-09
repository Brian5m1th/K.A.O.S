import os
import pytest
from app.rag.embeddings.cache import EmbeddingCache


class TestEmbeddingCache:
    @pytest.fixture
    def cache(self, tmp_path) -> EmbeddingCache:
        db_file = tmp_path / "test_cache.db"
        return EmbeddingCache(db_path=str(db_file))

    def test_cache_set_and_get(self, cache: EmbeddingCache) -> None:
        text = "Este é um texto de teste para cache."
        model = "test-model"
        vector = [0.1, 0.2, 0.3, -0.4, 0.5]

        # Get missing value
        assert cache.get(text, model) is None

        # Set value
        cache.set(text, model, vector)

        # Get cached value
        cached_vec = cache.get(text, model)
        assert cached_vec == vector

    def test_cache_miss_with_different_model(self, cache: EmbeddingCache) -> None:
        text = "Texto de teste"
        model1 = "model-1"
        model2 = "model-2"
        vector = [0.9, 0.8, 0.7]

        cache.set(text, model1, vector)

        assert cache.get(text, model1) == vector
        assert cache.get(text, model2) is None
