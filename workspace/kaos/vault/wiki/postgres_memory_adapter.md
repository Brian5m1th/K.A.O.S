# assistant\app\providers\memory\postgres_memory_adapter.py

## Símbolos

- [[assistant_app_providers_memory_postgres_memory_adapter]] — code: postgres_memory_adapter.py
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] — code: PostgresMemoryAdapter
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_init]] — code: .__init__()
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_provider_name]] — code: .provider_name()
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_store]] — code: .store()
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_search]] — code: .search()
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_get]] — code: .get()
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_delete]] — code: .delete()
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_health]] — code: .health()
- [[assistant_app_providers_memory_postgres_memory_adapter_rationale_1]] — code: PostgresMemoryAdapter — MemoryPort implementation backed by PostgreSQL.  Stores
- [[assistant_app_providers_memory_postgres_memory_adapter_rationale_16]] — code: Memory adapter backed by existing PostgreSQL storage.

## Dependências

- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] → `uses` → [[assistant_app_domain_ports_memory_port_memoryentry]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] → `uses` → [[assistant_app_domain_ports_memory_port_memoryquery]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_search]] → `references` → [[assistant_app_domain_ports_memory_port_memoryquery]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] → `uses` → [[assistant_app_domain_ports_memory_port_memoryresult]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_search]] → `references` → [[assistant_app_domain_ports_memory_port_memoryresult]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] → `uses` → [[assistant_app_domain_ports_memory_port_memoryport]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] → `uses` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_store]] → `calls` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository]]
- [[assistant_app_providers_memory_postgres_memory_adapter]] → `contains` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]]
- [[assistant_app_providers_memory_postgres_memory_adapter_rationale_1]] → `rationale_for` → [[assistant_app_providers_memory_postgres_memory_adapter]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] → `method` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_delete]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] → `method` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_get]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] → `method` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_health]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] → `method` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_init]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] → `method` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_provider_name]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] → `method` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_search]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]] → `method` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_store]]
- [[assistant_app_providers_memory_postgres_memory_adapter_rationale_16]] → `rationale_for` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_store]] → `references` → [[assistant_app_providers_memory_postgres_memory_adapter_py_memoryentry]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_get]] → `references` → [[assistant_app_providers_memory_postgres_memory_adapter_py_memoryentry]]
- [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter_health]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]