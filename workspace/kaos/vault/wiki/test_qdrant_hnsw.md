# assistant\tests\unit\test_qdrant_hnsw.py

## Símbolos

- [[assistant_tests_unit_test_qdrant_hnsw]] — code: test_qdrant_hnsw.py
- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig]] — code: TestHNSWConfig
- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_qdrant_provider_uses_hnsw_config]] — code: .test_qdrant_provider_uses_hnsw_config()
- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_vault_indexer_uses_hnsw_config]] — code: .test_vault_indexer_uses_hnsw_config()
- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_hnsw_config_default_values]] — code: .test_hnsw_config_default_values()
- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_hnsw_config_accepts_different_values]] — code: .test_hnsw_config_accepts_different_values()
- [[assistant_tests_unit_test_qdrant_hnsw_rationale_1]] — code: Testes da configuracao HNSW no Qdrant.  Verifica que os parametros HNSW (m=32,
- [[assistant_tests_unit_test_qdrant_hnsw_rationale_14]] — code: Testa que o HNSW config eh aplicado corretamente.
- [[assistant_tests_unit_test_qdrant_hnsw_rationale_19]] — code: Verifica que QdrantVectorStore cria colecao com HNSW config.
- [[assistant_tests_unit_test_qdrant_hnsw_rationale_47]] — code: Verifica que VaultIndexer cria colecao com HNSW config.
- [[assistant_tests_unit_test_qdrant_hnsw_rationale_75]] — code: Verifica os valores padrao do HNSW config.
- [[assistant_tests_unit_test_qdrant_hnsw_rationale_82]] — code: Verifica que HNSW aceita valores customizados.

## Dependências

- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig]] → `uses` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore]]
- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_qdrant_provider_uses_hnsw_config]] → `calls` → [[assistant_app_providers_vector_qdrant_qdrantvectorstore]]
- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig]] → `uses` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer]]
- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_vault_indexer_uses_hnsw_config]] → `calls` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer]]
- [[assistant_tests_unit_test_qdrant_hnsw]] → `contains` → [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig]]
- [[assistant_tests_unit_test_qdrant_hnsw_rationale_1]] → `rationale_for` → [[assistant_tests_unit_test_qdrant_hnsw]]
- [[assistant_tests_unit_test_qdrant_hnsw_rationale_14]] → `rationale_for` → [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig]]
- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig]] → `method` → [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_hnsw_config_accepts_different_values]]
- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig]] → `method` → [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_hnsw_config_default_values]]
- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig]] → `method` → [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_qdrant_provider_uses_hnsw_config]]
- [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig]] → `method` → [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_vault_indexer_uses_hnsw_config]]
- [[assistant_tests_unit_test_qdrant_hnsw_rationale_19]] → `rationale_for` → [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_qdrant_provider_uses_hnsw_config]]
- [[assistant_tests_unit_test_qdrant_hnsw_rationale_47]] → `rationale_for` → [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_vault_indexer_uses_hnsw_config]]
- [[assistant_tests_unit_test_qdrant_hnsw_rationale_75]] → `rationale_for` → [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_hnsw_config_default_values]]
- [[assistant_tests_unit_test_qdrant_hnsw_rationale_82]] → `rationale_for` → [[assistant_tests_unit_test_qdrant_hnsw_testhnswconfig_test_hnsw_config_accepts_different_values]]