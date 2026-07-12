# assistant\app\providers\vector\qdrant.py

## Símbolos

- [[assistant_app_providers_vector_qdrant]] — code: qdrant.py
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore]] — code: QdrantVectorStore
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_init]] — code: .__init__()
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_get_embedder]] — code: ._get_embedder()
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_ensure_collection]] — code: ._ensure_collection()
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_upsert]] — code: .upsert()
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_search]] — code: .search()
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_delete]] — code: .delete()
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_providers_vector_qdrant_qdrantvectorstore]] → `uses` → [[assistant_app_domain_document_searchresult]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_search]] → `references` → [[assistant_app_domain_document_searchresult]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore]] → `uses` → [[assistant_app_providers_base_vector_store_basevectorstore]]
- [[assistant_app_providers_vector_qdrant]] → `contains` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore]] → `method` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore_delete]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore]] → `method` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore_ensure_collection]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore]] → `method` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore_get_embedder]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore]] → `method` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore_healthcheck]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore]] → `method` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore_init]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore]] → `method` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore_search]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore]] → `method` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore_upsert]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_ensure_collection]] → `calls` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore_get_embedder]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_get_embedder]] → `calls` → [[assistant_app_rag_embeddings_embedder_get_embedder]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_delete]] → `calls` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore_ensure_collection]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_search]] → `calls` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore_ensure_collection]]
- [[assistant_app_providers_vector_qdrant_qdrantvectorstore_upsert]] → `calls` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore_ensure_collection]]