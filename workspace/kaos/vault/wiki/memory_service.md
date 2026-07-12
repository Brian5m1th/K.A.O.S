# assistant\app\memory\memory_service.py

## Símbolos

- [[assistant_app_memory_memory_service]] — code: memory_service.py
- [[assistant_app_memory_memory_service_memoryservice]] — code: MemoryService
- [[assistant_app_memory_memory_service_memoryservice_init]] — code: .__init__()
- [[assistant_app_memory_memory_service_memoryservice_resolve_uid]] — code: ._resolve_uid()
- [[assistant_app_memory_memory_service_memoryservice_user_dir]] — code: ._user_dir()
- [[assistant_app_memory_memory_service_memoryservice_default_user]] — code: ._default_user()
- [[assistant_app_memory_memory_service_memoryservice_get_postgres_repo]] — code: ._get_postgres_repo()
- [[assistant_app_memory_memory_service_memoryservice_run_async]] — code: ._run_async()
- [[assistant_app_memory_memory_service_memoryservice_save_conversation]] — code: .save_conversation()
- [[assistant_app_memory_memory_service_memoryservice_save_snapshot]] — code: .save_snapshot()
- [[assistant_app_memory_memory_service_memoryservice_save_preference]] — code: .save_preference()
- [[assistant_app_memory_memory_service_memoryservice_get_preferences]] — code: .get_preferences()
- [[assistant_app_memory_memory_service_memoryservice_list_recent_conversations]] — code: .list_recent_conversations()
- [[assistant_app_memory_memory_service_rationale_46]] — code: Run async coroutine in thread pool to avoid blocking sync code.

## Dependências

- [[assistant_app_memory_memory_service]] → `contains` → [[assistant_app_memory_memory_service_memoryservice]]
- [[assistant_app_memory_memory_service_memoryservice]] → `method` → [[assistant_app_memory_memory_service_memoryservice_default_user]]
- [[assistant_app_memory_memory_service_memoryservice]] → `method` → [[assistant_app_memory_memory_service_memoryservice_get_postgres_repo]]
- [[assistant_app_memory_memory_service_memoryservice]] → `method` → [[assistant_app_memory_memory_service_memoryservice_get_preferences]]
- [[assistant_app_memory_memory_service_memoryservice]] → `method` → [[assistant_app_memory_memory_service_memoryservice_init]]
- [[assistant_app_memory_memory_service_memoryservice]] → `method` → [[assistant_app_memory_memory_service_memoryservice_list_recent_conversations]]
- [[assistant_app_memory_memory_service_memoryservice]] → `method` → [[assistant_app_memory_memory_service_memoryservice_resolve_uid]]
- [[assistant_app_memory_memory_service_memoryservice]] → `method` → [[assistant_app_memory_memory_service_memoryservice_run_async]]
- [[assistant_app_memory_memory_service_memoryservice]] → `method` → [[assistant_app_memory_memory_service_memoryservice_save_conversation]]
- [[assistant_app_memory_memory_service_memoryservice]] → `method` → [[assistant_app_memory_memory_service_memoryservice_save_preference]]
- [[assistant_app_memory_memory_service_memoryservice]] → `method` → [[assistant_app_memory_memory_service_memoryservice_save_snapshot]]
- [[assistant_app_memory_memory_service_memoryservice]] → `method` → [[assistant_app_memory_memory_service_memoryservice_user_dir]]
- [[assistant_app_memory_memory_service_memoryservice]] → `uses` → [[assistant_app_memory_storage_postgres_storage_postgresstorage]]
- [[assistant_app_memory_memory_service_memoryservice_init]] → `calls` → [[assistant_app_memory_memory_service_py_path]]
- [[assistant_app_memory_memory_service_memoryservice_get_preferences]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_resolve_uid]]
- [[assistant_app_memory_memory_service_memoryservice_list_recent_conversations]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_resolve_uid]]
- [[assistant_app_memory_memory_service_memoryservice_resolve_uid]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_default_user]]
- [[assistant_app_memory_memory_service_memoryservice_save_conversation]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_resolve_uid]]
- [[assistant_app_memory_memory_service_memoryservice_save_preference]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_resolve_uid]]
- [[assistant_app_memory_memory_service_memoryservice_save_snapshot]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_resolve_uid]]
- [[assistant_app_memory_memory_service_memoryservice_user_dir]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_resolve_uid]]
- [[assistant_app_memory_memory_service_memoryservice_get_preferences]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_user_dir]]
- [[assistant_app_memory_memory_service_memoryservice_list_recent_conversations]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_user_dir]]
- [[assistant_app_memory_memory_service_memoryservice_save_conversation]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_user_dir]]
- [[assistant_app_memory_memory_service_memoryservice_save_preference]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_user_dir]]
- [[assistant_app_memory_memory_service_memoryservice_user_dir]] → `references` → [[assistant_app_memory_memory_service_py_path]]
- [[assistant_app_memory_memory_service_memoryservice_get_postgres_repo]] → `calls` → [[assistant_app_memory_postgres_repository_get_postgres_repository]]
- [[assistant_app_memory_memory_service_memoryservice_save_conversation]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_get_postgres_repo]]
- [[assistant_app_memory_memory_service_memoryservice_save_conversation]] → `calls` → [[assistant_app_memory_memory_service_memoryservice_run_async]]
- [[assistant_app_memory_memory_service_rationale_46]] → `rationale_for` → [[assistant_app_memory_memory_service_memoryservice_run_async]]
- [[assistant_app_memory_memory_service_memoryservice_save_snapshot]] → `calls` → [[assistant_app_memory_storage_postgres_storage_postgresstorage]]