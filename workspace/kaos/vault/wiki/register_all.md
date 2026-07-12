# assistant\app\providers\register_all.py

## Símbolos

- [[assistant_app_providers_register_all]] — code: register_all.py
- [[assistant_app_providers_register_all_register_all_providers]] — code: register_all_providers()
- [[assistant_app_providers_register_all_register_all_workflows]] — code: register_all_workflows()

## Dependências

- [[assistant_app_providers_register_all_register_all_providers]] → `calls` → [[assistant_app_providers_chat_registry_register_chat_providers]]
- [[assistant_app_providers_register_all_register_all_providers]] → `calls` → [[assistant_app_providers_embedding_registry_register_embedding_providers]]
- [[assistant_app_providers_register_all_register_all_providers]] → `calls` → [[assistant_app_providers_memory_registry_register_memory_providers]]
- [[assistant_app_providers_register_all]] → `contains` → [[assistant_app_providers_register_all_register_all_providers]]
- [[assistant_app_providers_register_all]] → `contains` → [[assistant_app_providers_register_all_register_all_workflows]]
- [[assistant_app_providers_register_all_register_all_providers]] → `calls` → [[assistant_app_providers_vector_registry_register_vector_stores]]
- [[assistant_app_providers_register_all_register_all_workflows]] → `calls` → [[assistant_app_workflows_impl_registry_register_workflows]]