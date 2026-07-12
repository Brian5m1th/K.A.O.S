# assistant\app\api\indexing.py

## Símbolos

- [[assistant_app_api_indexing]] — code: indexing.py
- [[assistant_app_api_indexing_get_indexer]] — code: _get_indexer()
- [[assistant_app_api_indexing_full_reindex]] — code: full_reindex()
- [[assistant_app_api_indexing_init_vault_folders]] — code: init_vault_folders()

## Dependências

- [[assistant_app_api_indexing]] → `contains` → [[assistant_app_api_indexing_full_reindex]]
- [[assistant_app_api_indexing]] → `contains` → [[assistant_app_api_indexing_get_indexer]]
- [[assistant_app_api_indexing]] → `contains` → [[assistant_app_api_indexing_init_vault_folders]]
- [[assistant_app_api_indexing]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_indexing_full_reindex]] → `calls` → [[assistant_app_api_indexing_get_indexer]]
- [[assistant_app_api_indexing_get_indexer]] → `references` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer]]
- [[assistant_app_api_indexing_init_vault_folders]] → `calls` → [[assistant_app_obsidian_vault_init_create_vault_structure]]