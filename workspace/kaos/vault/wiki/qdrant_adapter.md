# assistant\app\providers\retrieval\qdrant_adapter.py

## Símbolos

- [[assistant_app_providers_retrieval_qdrant_adapter]] — code: qdrant_adapter.py
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]] — code: QdrantAdapter
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_init]] — code: .__init__()
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_provider_name]] — code: .provider_name()
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_search]] — code: .search()
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_index]] — code: .index()
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_count]] — code: .count()
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_health]] — code: .health()
- [[assistant_app_providers_retrieval_qdrant_adapter_rationale_1]] — code: QdrantAdapter — RetrievalPort implementation backed by Qdrant.  Provides semanti
- [[assistant_app_providers_retrieval_qdrant_adapter_rationale_16]] — code: Vector search adapter backed by Qdrant.
- [[assistant_app_providers_retrieval_qdrant_adapter_rationale_28]] — code: Search Qdrant by keywords (full vector search via Qdrant client).
- [[assistant_app_providers_retrieval_qdrant_adapter_rationale_59]] — code: Index documents in Qdrant (stub — uses existing RAG pipeline).
- [[assistant_app_providers_retrieval_qdrant_adapter_rationale_64]] — code: Count vectors in Qdrant collection.

## Dependências

- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]] → `uses` → [[assistant_app_domain_ports_retrieval_port_retrievalquery]]
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_search]] → `references` → [[assistant_app_domain_ports_retrieval_port_retrievalquery]]
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]] → `uses` → [[assistant_app_domain_ports_retrieval_port_retrievalresult]]
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_search]] → `references` → [[assistant_app_domain_ports_retrieval_port_retrievalresult]]
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]] → `uses` → [[assistant_app_domain_ports_retrieval_port_retrievalport]]
- [[assistant_app_providers_retrieval_qdrant_adapter]] → `contains` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]]
- [[assistant_app_providers_retrieval_qdrant_adapter_rationale_1]] → `rationale_for` → [[assistant_app_providers_retrieval_qdrant_adapter]]
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]] → `method` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_count]]
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]] → `method` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_health]]
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]] → `method` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_index]]
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]] → `method` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_init]]
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]] → `method` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_provider_name]]
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]] → `method` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_search]]
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]] → `uses` → [[assistant_app_rag_embeddings_embedder_embedder]]
- [[assistant_app_providers_retrieval_qdrant_adapter_rationale_16]] → `rationale_for` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]]
- [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_search]] → `calls` → [[assistant_app_rag_embeddings_embedder_embedder]]
- [[assistant_app_providers_retrieval_qdrant_adapter_rationale_28]] → `rationale_for` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_search]]
- [[assistant_app_providers_retrieval_qdrant_adapter_rationale_59]] → `rationale_for` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_index]]
- [[assistant_app_providers_retrieval_qdrant_adapter_rationale_64]] → `rationale_for` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter_count]]