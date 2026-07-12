# assistant\app\providers\embedding\bge.py

## Símbolos

- [[assistant_app_providers_embedding_bge]] — code: bge.py
- [[assistant_app_providers_embedding_bge_bgeembeddingprovider]] — code: BgeEmbeddingProvider
- [[assistant_app_providers_embedding_bge_bgeembeddingprovider_init]] — code: .__init__()
- [[assistant_app_providers_embedding_bge_bgeembeddingprovider_embed]] — code: .embed()
- [[assistant_app_providers_embedding_bge_bgeembeddingprovider_embed_batch]] — code: .embed_batch()
- [[assistant_app_providers_embedding_bge_bgeembeddingprovider_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_providers_embedding_bge_bgeembeddingprovider]] → `uses` → [[assistant_app_providers_base_embedding_baseembeddingprovider]]
- [[assistant_app_providers_embedding_bge]] → `contains` → [[assistant_app_providers_embedding_bge_bgeembeddingprovider]]
- [[assistant_app_providers_embedding_bge_bgeembeddingprovider]] → `method` → [[assistant_app_providers_embedding_bge_bgeembeddingprovider_embed]]
- [[assistant_app_providers_embedding_bge_bgeembeddingprovider]] → `method` → [[assistant_app_providers_embedding_bge_bgeembeddingprovider_embed_batch]]
- [[assistant_app_providers_embedding_bge_bgeembeddingprovider]] → `method` → [[assistant_app_providers_embedding_bge_bgeembeddingprovider_healthcheck]]
- [[assistant_app_providers_embedding_bge_bgeembeddingprovider]] → `method` → [[assistant_app_providers_embedding_bge_bgeembeddingprovider_init]]
- [[assistant_app_providers_embedding_bge_bgeembeddingprovider_init]] → `calls` → [[assistant_app_rag_embeddings_embedder_get_embedder]]