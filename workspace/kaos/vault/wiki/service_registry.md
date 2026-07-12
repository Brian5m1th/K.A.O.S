# assistant\app\registry\service_registry.py

## Símbolos

- [[assistant_app_registry_service_registry]] — code: service_registry.py
- [[assistant_app_registry_service_registry_serviceregistry]] — code: ServiceRegistry
- [[assistant_app_registry_service_registry_serviceregistry_register_workflow]] — code: .register_workflow()
- [[assistant_app_registry_service_registry_serviceregistry_register_chat_provider]] — code: .register_chat_provider()
- [[assistant_app_registry_service_registry_serviceregistry_register_embedding_provider]] — code: .register_embedding_provider()
- [[assistant_app_registry_service_registry_serviceregistry_register_vector_store]] — code: .register_vector_store()
- [[assistant_app_registry_service_registry_serviceregistry_register_memory_provider]] — code: .register_memory_provider()
- [[assistant_app_registry_service_registry_serviceregistry_get_workflow]] — code: .get_workflow()
- [[assistant_app_registry_service_registry_serviceregistry_get_chat_provider]] — code: .get_chat_provider()
- [[assistant_app_registry_service_registry_serviceregistry_get_embedding_provider]] — code: .get_embedding_provider()
- [[assistant_app_registry_service_registry_serviceregistry_get_vector_store]] — code: .get_vector_store()
- [[assistant_app_registry_service_registry_serviceregistry_get_memory_provider]] — code: .get_memory_provider()
- [[assistant_app_registry_service_registry_serviceregistry_list_workflows]] — code: .list_workflows()
- [[assistant_app_registry_service_registry_serviceregistry_list_chat_providers]] — code: .list_chat_providers()
- [[assistant_app_registry_service_registry_serviceregistry_list_embedding_providers]] — code: .list_embedding_providers()
- [[assistant_app_registry_service_registry_serviceregistry_list_vector_stores]] — code: .list_vector_stores()
- [[assistant_app_registry_service_registry_serviceregistry_list_memory_providers]] — code: .list_memory_providers()

## Dependências

- [[assistant_app_registry_service_registry_serviceregistry_get_chat_provider]] → `references` → [[assistant_app_providers_base_chat_basechatprovider]]
- [[assistant_app_registry_service_registry_serviceregistry_register_chat_provider]] → `references` → [[assistant_app_providers_base_chat_basechatprovider]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `uses` → [[assistant_app_providers_base_embedding_baseembeddingprovider]]
- [[assistant_app_registry_service_registry_serviceregistry_get_embedding_provider]] → `references` → [[assistant_app_providers_base_embedding_baseembeddingprovider]]
- [[assistant_app_registry_service_registry_serviceregistry_register_embedding_provider]] → `references` → [[assistant_app_providers_base_embedding_baseembeddingprovider]]
- [[assistant_app_registry_service_registry_serviceregistry_get_memory_provider]] → `references` → [[assistant_app_providers_base_memory_basememoryprovider]]
- [[assistant_app_registry_service_registry_serviceregistry_register_memory_provider]] → `references` → [[assistant_app_providers_base_memory_basememoryprovider]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `uses` → [[assistant_app_providers_base_vector_store_basevectorstore]]
- [[assistant_app_registry_service_registry_serviceregistry_get_vector_store]] → `references` → [[assistant_app_providers_base_vector_store_basevectorstore]]
- [[assistant_app_registry_service_registry_serviceregistry_register_vector_store]] → `references` → [[assistant_app_providers_base_vector_store_basevectorstore]]
- [[assistant_app_registry_service_registry]] → `contains` → [[assistant_app_registry_service_registry_serviceregistry]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_get_chat_provider]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_get_embedding_provider]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_get_memory_provider]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_get_vector_store]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_get_workflow]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_list_chat_providers]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_list_embedding_providers]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_list_memory_providers]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_list_vector_stores]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_list_workflows]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_register_chat_provider]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_register_embedding_provider]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_register_memory_provider]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_register_vector_store]]
- [[assistant_app_registry_service_registry_serviceregistry]] → `method` → [[assistant_app_registry_service_registry_serviceregistry_register_workflow]]
- [[assistant_app_registry_service_registry_serviceregistry_register_workflow]] → `references` → [[assistant_app_workflows_base_baseworkflow]]
- [[assistant_app_registry_service_registry_serviceregistry_get_workflow]] → `references` → [[assistant_app_workflows_base_baseworkflow]]
- [[assistant_app_registry_service_registry_serviceregistry_get_chat_provider]] → `references` → [[assistant_app_registry_service_registry_py_any]]
- [[assistant_app_registry_service_registry_serviceregistry_get_embedding_provider]] → `references` → [[assistant_app_registry_service_registry_py_any]]
- [[assistant_app_registry_service_registry_serviceregistry_get_memory_provider]] → `references` → [[assistant_app_registry_service_registry_py_any]]
- [[assistant_app_registry_service_registry_serviceregistry_get_vector_store]] → `references` → [[assistant_app_registry_service_registry_py_any]]