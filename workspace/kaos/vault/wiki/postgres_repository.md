# assistant\app\memory\postgres_repository.py

## Símbolos

- [[assistant_app_memory_postgres_repository]] — code: postgres_repository.py
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] — code: PostgresMemoryRepository
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_init]] — code: .__init__()
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_init_db]] — code: .init_db()
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_close]] — code: .close()
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_get_session]] — code: ._get_session()
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_get_preferences]] — code: .get_preferences()
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_save_preference]] — code: .save_preference()
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_save_conversation]] — code: .save_conversation()
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_list_recent_conversations]] — code: .list_recent_conversations()
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_get_conversation_history]] — code: .get_conversation_history()
- [[assistant_app_memory_postgres_repository_get_postgres_repository]] — code: get_postgres_repository()

## Dependências

- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_init]] → `calls` → [[async_sessionmaker]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `uses` → [[assistant_app_memory_models_base]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `uses` → [[assistant_app_memory_models_memorysession]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_list_recent_conversations]] → `indirect_call` → [[assistant_app_memory_models_memorysession]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_save_conversation]] → `indirect_call` → [[assistant_app_memory_models_memorysession]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `uses` → [[assistant_app_memory_models_memorymessage]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_get_conversation_history]] → `indirect_call` → [[assistant_app_memory_models_memorymessage]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_save_conversation]] → `calls` → [[assistant_app_memory_models_memorymessage]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `uses` → [[assistant_app_memory_models_memorysummary]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_save_conversation]] → `indirect_call` → [[assistant_app_memory_models_memorysummary]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `uses` → [[assistant_app_memory_models_userpreference]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_get_preferences]] → `indirect_call` → [[assistant_app_memory_models_userpreference]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_save_preference]] → `indirect_call` → [[assistant_app_memory_models_userpreference]]
- [[assistant_app_memory_postgres_repository]] → `contains` → [[assistant_app_memory_postgres_repository_get_postgres_repository]]
- [[assistant_app_memory_postgres_repository]] → `contains` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository]]
- [[assistant_app_memory_postgres_repository_get_postgres_repository]] → `references` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `method` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository_close]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `method` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository_get_conversation_history]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `method` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository_get_preferences]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `method` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository_get_session]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `method` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository_init]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `method` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository_init_db]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `method` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository_list_recent_conversations]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `method` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository_save_conversation]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `method` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository_save_preference]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository]] → `uses` → [[assistant_app_memory_repository_memoryrepository]]
- [[assistant_app_memory_postgres_repository_get_postgres_repository]] → `calls` → [[assistant_app_memory_postgres_repository_postgresmemoryrepository_init_db]]
- [[assistant_app_memory_postgres_repository_postgresmemoryrepository_get_session]] → `references` → [[assistant_app_memory_postgres_repository_py_asyncsession]]