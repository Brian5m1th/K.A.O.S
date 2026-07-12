# assistant\app\api\memory_api.py

## Símbolos

- [[assistant_app_api_memory_api]] — code: memory_api.py
- [[assistant_app_api_memory_api_storerequest]] — code: StoreRequest
- [[assistant_app_api_memory_api_searchrequest]] — code: SearchRequest
- [[assistant_app_api_memory_api_get_memory_service]] — code: get_memory_service()
- [[assistant_app_api_memory_api_store_memory]] — code: store_memory()
- [[assistant_app_api_memory_api_search_memory]] — code: search_memory()
- [[assistant_app_api_memory_api_get_memory]] — code: get_memory()
- [[assistant_app_api_memory_api_delete_memory]] — code: delete_memory()
- [[assistant_app_api_memory_api_memory_health]] — code: memory_health()
- [[assistant_app_api_memory_api_rationale_1]] — code: Memory REST API — Agent and user memory storage.  Endpoints:   POST   /api/memor
- [[assistant_app_api_memory_api_rationale_50]] — code: Store a memory entry. Returns the assigned ID.
- [[assistant_app_api_memory_api_rationale_68]] — code: Search memories by semantic similarity or metadata.
- [[assistant_app_api_memory_api_rationale_90]] — code: Retrieve a specific memory by ID.
- [[assistant_app_api_memory_api_rationale_102]] — code: Delete a memory entry.

## Dependências

- [[assistant_app_api_memory_api]] → `contains` → [[assistant_app_api_memory_api_delete_memory]]
- [[assistant_app_api_memory_api]] → `contains` → [[assistant_app_api_memory_api_get_memory]]
- [[assistant_app_api_memory_api]] → `contains` → [[assistant_app_api_memory_api_get_memory_service]]
- [[assistant_app_api_memory_api]] → `contains` → [[assistant_app_api_memory_api_memory_health]]
- [[assistant_app_api_memory_api]] → `contains` → [[assistant_app_api_memory_api_search_memory]]
- [[assistant_app_api_memory_api]] → `contains` → [[assistant_app_api_memory_api_searchrequest]]
- [[assistant_app_api_memory_api]] → `contains` → [[assistant_app_api_memory_api_store_memory]]
- [[assistant_app_api_memory_api]] → `contains` → [[assistant_app_api_memory_api_storerequest]]
- [[assistant_app_api_memory_api]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_memory_api_rationale_1]] → `rationale_for` → [[assistant_app_api_memory_api]]
- [[assistant_app_api_memory_api_store_memory]] → `references` → [[assistant_app_api_memory_api_storerequest]]
- [[assistant_app_api_memory_api_storerequest]] → `inherits` → [[assistant_app_api_memory_api_py_basemodel]]
- [[assistant_app_api_memory_api_storerequest]] → `uses` → [[assistant_app_core_services_memory_service_memoryservice]]
- [[assistant_app_api_memory_api_storerequest]] → `uses` → [[assistant_app_domain_ports_memory_port_memoryentry]]
- [[assistant_app_api_memory_api_storerequest]] → `uses` → [[assistant_app_domain_ports_memory_port_memoryquery]]
- [[assistant_app_api_memory_api_storerequest]] → `uses` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]]
- [[assistant_app_api_memory_api_searchrequest]] → `inherits` → [[assistant_app_api_memory_api_py_basemodel]]
- [[assistant_app_api_memory_api_search_memory]] → `references` → [[assistant_app_api_memory_api_searchrequest]]
- [[assistant_app_api_memory_api_searchrequest]] → `uses` → [[assistant_app_core_services_memory_service_memoryservice]]
- [[assistant_app_api_memory_api_searchrequest]] → `uses` → [[assistant_app_domain_ports_memory_port_memoryentry]]
- [[assistant_app_api_memory_api_searchrequest]] → `uses` → [[assistant_app_domain_ports_memory_port_memoryquery]]
- [[assistant_app_api_memory_api_searchrequest]] → `uses` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]]
- [[assistant_app_api_memory_api_get_memory_service]] → `references` → [[assistant_app_api_memory_api_py_memoryservice]]
- [[assistant_app_api_memory_api_get_memory_service]] → `calls` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]]
- [[assistant_app_api_memory_api_delete_memory]] → `references` → [[assistant_app_api_memory_api_py_memoryservice]]
- [[assistant_app_api_memory_api_get_memory]] → `references` → [[assistant_app_api_memory_api_py_memoryservice]]
- [[assistant_app_api_memory_api_memory_health]] → `references` → [[assistant_app_api_memory_api_py_memoryservice]]
- [[assistant_app_api_memory_api_search_memory]] → `references` → [[assistant_app_api_memory_api_py_memoryservice]]
- [[assistant_app_api_memory_api_store_memory]] → `references` → [[assistant_app_api_memory_api_py_memoryservice]]
- [[assistant_app_api_memory_api_rationale_50]] → `rationale_for` → [[assistant_app_api_memory_api_store_memory]]
- [[assistant_app_api_memory_api_store_memory]] → `calls` → [[assistant_app_domain_ports_memory_port_memoryentry]]
- [[assistant_app_api_memory_api_rationale_68]] → `rationale_for` → [[assistant_app_api_memory_api_search_memory]]
- [[assistant_app_api_memory_api_search_memory]] → `calls` → [[assistant_app_domain_ports_memory_port_memoryquery]]
- [[assistant_app_api_memory_api_rationale_90]] → `rationale_for` → [[assistant_app_api_memory_api_get_memory]]
- [[assistant_app_api_memory_api_rationale_102]] → `rationale_for` → [[assistant_app_api_memory_api_delete_memory]]