# assistant\app\rag\embeddings\embedder.py

## Símbolos

- [[assistant_app_rag_embeddings_embedder]] — code: embedder.py
- [[assistant_app_rag_embeddings_embedder_embedder]] — code: Embedder
- [[assistant_app_rag_embeddings_embedder_embedder_init]] — code: .__init__()
- [[assistant_app_rag_embeddings_embedder_embedder_get_device]] — code: ._get_device()
- [[assistant_app_rag_embeddings_embedder_embedder_dimension]] — code: .dimension()
- [[assistant_app_rag_embeddings_embedder_embedder_model_key]] — code: .model_key()
- [[assistant_app_rag_embeddings_embedder_embedder_embed]] — code: .embed()
- [[assistant_app_rag_embeddings_embedder_embedder_embed_single]] — code: .embed_single()
- [[assistant_app_rag_embeddings_embedder_embedder_embed_batch]] — code: .embed_batch()
- [[assistant_app_rag_embeddings_embedder_get_embedder]] — code: get_embedder()
- [[assistant_app_rag_embeddings_embedder_warmup_embedder]] — code: warmup_embedder()

## Dependências

- [[assistant_app_rag_embeddings_embedder_embedder_init]] → `calls` → [[assistant_app_api_auth_login]]
- [[assistant_app_rag_embeddings_embedder_embedder]] → `uses` → [[assistant_app_rag_embeddings_cache_embeddingcache]]
- [[assistant_app_rag_embeddings_embedder_embedder_embed]] → `calls` → [[assistant_app_rag_embeddings_cache_embeddingcache]]
- [[assistant_app_rag_embeddings_embedder]] → `contains` → [[assistant_app_rag_embeddings_embedder_embedder]]
- [[assistant_app_rag_embeddings_embedder]] → `contains` → [[assistant_app_rag_embeddings_embedder_get_embedder]]
- [[assistant_app_rag_embeddings_embedder]] → `contains` → [[assistant_app_rag_embeddings_embedder_warmup_embedder]]
- [[assistant_app_rag_embeddings_embedder_embedder]] → `method` → [[assistant_app_rag_embeddings_embedder_embedder_dimension]]
- [[assistant_app_rag_embeddings_embedder_embedder]] → `method` → [[assistant_app_rag_embeddings_embedder_embedder_embed]]
- [[assistant_app_rag_embeddings_embedder_embedder]] → `method` → [[assistant_app_rag_embeddings_embedder_embedder_embed_batch]]
- [[assistant_app_rag_embeddings_embedder_embedder]] → `method` → [[assistant_app_rag_embeddings_embedder_embedder_embed_single]]
- [[assistant_app_rag_embeddings_embedder_embedder]] → `method` → [[assistant_app_rag_embeddings_embedder_embedder_get_device]]
- [[assistant_app_rag_embeddings_embedder_embedder]] → `method` → [[assistant_app_rag_embeddings_embedder_embedder_init]]
- [[assistant_app_rag_embeddings_embedder_embedder]] → `method` → [[assistant_app_rag_embeddings_embedder_embedder_model_key]]
- [[assistant_app_rag_embeddings_embedder_get_embedder]] → `references` → [[assistant_app_rag_embeddings_embedder_embedder]]
- [[assistant_app_rag_embeddings_embedder_embedder_init]] → `calls` → [[assistant_app_rag_embeddings_embedder_embedder_get_device]]
- [[assistant_app_rag_embeddings_embedder_embedder_embed_batch]] → `calls` → [[assistant_app_rag_embeddings_embedder_embedder_embed]]
- [[assistant_app_rag_embeddings_embedder_embedder_embed_single]] → `calls` → [[assistant_app_rag_embeddings_embedder_embedder_embed]]
- [[assistant_app_rag_embeddings_embedder_warmup_embedder]] → `calls` → [[assistant_app_rag_embeddings_embedder_embedder_embed_single]]
- [[assistant_app_rag_embeddings_embedder_warmup_embedder]] → `calls` → [[assistant_app_rag_embeddings_embedder_get_embedder]]