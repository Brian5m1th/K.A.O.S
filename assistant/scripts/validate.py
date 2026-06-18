#!/usr/bin/env python3
"""Final validation script"""
from app.rag.retriever.semantic_retriever import SemanticRetriever
from app.rag.indexer.vault_indexer import VaultIndexer
from app.config import settings

print("=== FINAL VALIDATION ===")
print()
print("1. Server imports: OK")

r = SemanticRetriever()
results = r.search('teste', limit=3)
print(f'2. Semantic search: {len(results)} results, top_score={results[0].score:.4f}')

idx = VaultIndexer()
stats = idx._doc_cache.stats()
print(f'3. Document cache: {stats["entries"]} entries, {stats["size_mb"]} MB')

info = idx._client.get_collection(settings.QDRANT_COLLECTION)
print(f'4. Collection dim: {info.config.params.vectors.size}')

print()
print("=== ALL CHECKS PASSED ===")
