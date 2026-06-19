import sys

sys.path.insert(0, ".")
from app.rag.retriever.semantic_retriever import SemanticRetriever
from app.rag.indexer.vault_indexer import VaultIndexer
from app.config import settings

print("1. Server imports: OK")

r = SemanticRetriever()
results = r.search("teste", limit=3)
print(f"2. Semantic search: {len(results)} results, top_score={results[0].score:.4f}")

idx = VaultIndexer()
stats = idx._doc_cache.stats()
print("3. Document cache: {} entries, {} MB".format(stats["entries"], stats["size_mb"]))

info = idx._client.get_collection(settings.QDRANT_COLLECTION)
print("4. Collection dim: {}".format(info.config.params.vectors.size))

print("=== ALL CHECKS PASSED ===")
