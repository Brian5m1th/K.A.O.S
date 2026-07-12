# assistant\app\rag\indexer\vault_indexer.py

## Símbolos

- [[assistant_app_rag_indexer_vault_indexer]] — code: vault_indexer.py
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer]] — code: VaultIndexer
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_init]] — code: .__init__()
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_ensure_collection]] — code: ._ensure_collection()
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_make_point_id]] — code: ._make_point_id()
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_index_file]] — code: .index_file()
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_remove_file]] — code: .remove_file()
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_index_vault]] — code: .index_vault()

## Dependências

- [[assistant_app_rag_indexer_vault_indexer_vaultindexer]] → `uses` → [[assistant_app_rag_chunking_text_splitter_markdownsplitter]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_init]] → `calls` → [[assistant_app_rag_chunking_text_splitter_markdownsplitter]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer]] → `uses` → [[assistant_app_rag_embeddings_document_cache_documentembeddingcache]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_init]] → `calls` → [[assistant_app_rag_embeddings_document_cache_documentembeddingcache]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_init]] → `calls` → [[assistant_app_rag_embeddings_embedder_get_embedder]]
- [[assistant_app_rag_indexer_vault_indexer]] → `contains` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer]] → `method` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer_ensure_collection]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer]] → `method` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer_index_file]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer]] → `method` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer_index_vault]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer]] → `method` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer_init]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer]] → `method` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer_make_point_id]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer]] → `method` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer_remove_file]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_init]] → `calls` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer_ensure_collection]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_index_file]] → `calls` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer_make_point_id]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_index_file]] → `calls` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer_remove_file]]
- [[assistant_app_rag_indexer_vault_indexer_vaultindexer_index_vault]] → `calls` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer_index_file]]