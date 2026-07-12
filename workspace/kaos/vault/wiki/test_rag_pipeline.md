# assistant\tests\integration\rag\test_rag_pipeline.py

## Símbolos

- [[assistant_tests_integration_rag_test_rag_pipeline]] — code: test_rag_pipeline.py
- [[assistant_tests_integration_rag_test_rag_pipeline_test_vault]] — code: test_vault()
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline]] — code: TestRAGPipeline
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline_test_index_and_retrieve_flow]] — code: .test_index_and_retrieve_flow()
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline_test_chunking_produces_valid_chunks]] — code: .test_chunking_produces_valid_chunks()
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline_test_retriever_empty_results]] — code: .test_retriever_empty_results()

## Dependências

- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline]] → `uses` → [[assistant_app_domain_document_searchresult]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline_test_index_and_retrieve_flow]] → `indirect_call` → [[assistant_app_domain_document_searchresult]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline]] → `uses` → [[assistant_app_rag_chunking_text_splitter_textchunk]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline_test_chunking_produces_valid_chunks]] → `indirect_call` → [[assistant_app_rag_chunking_text_splitter_textchunk]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline]] → `uses` → [[assistant_app_rag_chunking_text_splitter_markdownsplitter]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline_test_chunking_produces_valid_chunks]] → `calls` → [[assistant_app_rag_chunking_text_splitter_markdownsplitter]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline]] → `uses` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline_test_index_and_retrieve_flow]] → `calls` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline]] → `uses` → [[assistant_app_rag_retriever_semantic_retriever_semanticretriever]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline_test_index_and_retrieve_flow]] → `calls` → [[assistant_app_rag_retriever_semantic_retriever_semanticretriever]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline_test_retriever_empty_results]] → `calls` → [[assistant_app_rag_retriever_semantic_retriever_semanticretriever]]
- [[assistant_tests_integration_rag_test_rag_pipeline]] → `contains` → [[assistant_tests_integration_rag_test_rag_pipeline_test_vault]]
- [[assistant_tests_integration_rag_test_rag_pipeline]] → `contains` → [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline]]
- [[assistant_tests_integration_rag_test_rag_pipeline_test_vault]] → `references` → [[assistant_tests_integration_rag_test_rag_pipeline_py_path]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline]] → `method` → [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline_test_chunking_produces_valid_chunks]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline]] → `method` → [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline_test_index_and_retrieve_flow]]
- [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline]] → `method` → [[assistant_tests_integration_rag_test_rag_pipeline_testragpipeline_test_retriever_empty_results]]