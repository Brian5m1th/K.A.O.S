# assistant\app\domain\ports\retrieval_port.py

## Símbolos

- [[assistant_app_domain_ports_retrieval_port]] — code: retrieval_port.py
- [[assistant_app_domain_ports_retrieval_port_retrievalquery]] — code: RetrievalQuery
- [[assistant_app_domain_ports_retrieval_port_retrievalresult]] — code: RetrievalResult
- [[assistant_app_domain_ports_retrieval_port_retrievalport]] — code: RetrievalPort
- [[assistant_app_domain_ports_retrieval_port_retrievalport_provider_name]] — code: .provider_name()
- [[assistant_app_domain_ports_retrieval_port_retrievalport_search]] — code: .search()
- [[assistant_app_domain_ports_retrieval_port_retrievalport_index]] — code: .index()
- [[assistant_app_domain_ports_retrieval_port_retrievalport_count]] — code: .count()
- [[assistant_app_domain_ports_retrieval_port_retrievalport_health]] — code: .health()
- [[assistant_app_domain_ports_retrieval_port_rationale_1]] — code: RetrievalPort — Semantic search and vector retrieval capability.  Searches acros
- [[assistant_app_domain_ports_retrieval_port_rationale_17]] — code: Semantic search query.
- [[assistant_app_domain_ports_retrieval_port_rationale_27]] — code: Retrieved document chunk with score.
- [[assistant_app_domain_ports_retrieval_port_rationale_36]] — code: Interface for semantic search and vector retrieval.      Concrete implementation
- [[assistant_app_domain_ports_retrieval_port_rationale_51]] — code: Search for semantically similar documents.
- [[assistant_app_domain_ports_retrieval_port_rationale_56]] — code: Index documents into the vector store. Returns count indexed.
- [[assistant_app_domain_ports_retrieval_port_rationale_61]] — code: Return the number of indexed vectors.

## Dependências

- [[assistant_app_domain_ports_retrieval_port]] → `imports_from` → [[assistant_app_domain_ports_retrieval_port_py_abc]]
- [[assistant_app_domain_ports_retrieval_port]] → `contains` → [[assistant_app_domain_ports_retrieval_port_retrievalport]]
- [[assistant_app_domain_ports_retrieval_port]] → `contains` → [[assistant_app_domain_ports_retrieval_port_retrievalquery]]
- [[assistant_app_domain_ports_retrieval_port]] → `contains` → [[assistant_app_domain_ports_retrieval_port_retrievalresult]]
- [[assistant_app_domain_ports_retrieval_port_rationale_1]] → `rationale_for` → [[assistant_app_domain_ports_retrieval_port]]
- [[assistant_app_domain_ports_retrieval_port_rationale_17]] → `rationale_for` → [[assistant_app_domain_ports_retrieval_port_retrievalquery]]
- [[assistant_app_domain_ports_retrieval_port_retrievalport_search]] → `references` → [[assistant_app_domain_ports_retrieval_port_retrievalquery]]
- [[assistant_app_domain_ports_retrieval_port_rationale_27]] → `rationale_for` → [[assistant_app_domain_ports_retrieval_port_retrievalresult]]
- [[assistant_app_domain_ports_retrieval_port_retrievalport_search]] → `references` → [[assistant_app_domain_ports_retrieval_port_retrievalresult]]
- [[assistant_app_domain_ports_retrieval_port_rationale_36]] → `rationale_for` → [[assistant_app_domain_ports_retrieval_port_retrievalport]]
- [[assistant_app_domain_ports_retrieval_port_retrievalport]] → `inherits` → [[assistant_app_domain_ports_retrieval_port_py_abc]]
- [[assistant_app_domain_ports_retrieval_port_retrievalport]] → `method` → [[assistant_app_domain_ports_retrieval_port_retrievalport_count]]
- [[assistant_app_domain_ports_retrieval_port_retrievalport]] → `method` → [[assistant_app_domain_ports_retrieval_port_retrievalport_health]]
- [[assistant_app_domain_ports_retrieval_port_retrievalport]] → `method` → [[assistant_app_domain_ports_retrieval_port_retrievalport_index]]
- [[assistant_app_domain_ports_retrieval_port_retrievalport]] → `method` → [[assistant_app_domain_ports_retrieval_port_retrievalport_provider_name]]
- [[assistant_app_domain_ports_retrieval_port_retrievalport]] → `method` → [[assistant_app_domain_ports_retrieval_port_retrievalport_search]]
- [[assistant_app_domain_ports_retrieval_port_rationale_51]] → `rationale_for` → [[assistant_app_domain_ports_retrieval_port_retrievalport_search]]
- [[assistant_app_domain_ports_retrieval_port_rationale_56]] → `rationale_for` → [[assistant_app_domain_ports_retrieval_port_retrievalport_index]]
- [[assistant_app_domain_ports_retrieval_port_rationale_61]] → `rationale_for` → [[assistant_app_domain_ports_retrieval_port_retrievalport_count]]