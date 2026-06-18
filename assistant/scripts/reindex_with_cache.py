#!/usr/bin/env python3
"""
Script de reindexação completa do vault usando DocumentEmbeddingCache
Execute: python scripts/reindex_with_cache.py
"""
import sys
import time
from pathlib import Path
from loguru import logger

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.rag.indexer.vault_indexer import VaultIndexer


def main():
    logger.info("[start] Reindexação completa com cache")
    start_total = time.perf_counter()
    
    indexer = VaultIndexer()
    
    if not indexer._available:
        logger.error("Qdrant indisponível")
        return
    
    logger.info("Limpando coleção existente...")
    # Opcional: limpar coleção antes
    # indexer._client.delete_collection(collection_name=settings.QDRANT_COLLECTION)
    # indexer._ensure_collection()
    
    result = indexer.index_vault()
    
    elapsed = (time.perf_counter() - start_total)
    logger.info(
        f"[finish] Reindexação completa: {result['files']} arquivos, "
        f"{result['chunks']} chunks em {elapsed:.1f}s"
    )
    
    # Mostra stats do cache
    cache_stats = indexer._doc_cache.stats()
    logger.info(f"Cache: {cache_stats['entries']} entradas, {cache_stats['size_mb']} MB")
    
    # Verifica hit rate se possível
    logger.info("Dica: Execute novamente para ver cache hits!")


if __name__ == "__main__":
    main()