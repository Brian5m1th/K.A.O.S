# assistant\app\repositories\failed_execution_repository.py

## Símbolos

- [[assistant_app_repositories_failed_execution_repository]] — code: failed_execution_repository.py
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrecord]] — code: FailedExecutionRecord
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository]] — code: FailedExecutionRepository
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_init]] — code: .__init__()
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_save]] — code: .save()
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_list_pending]] — code: .list_pending()
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_mark_reprocessed]] — code: .mark_reprocessed()
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_count_pending]] — code: .count_pending()

## Dependências

- [[assistant_app_repositories_failed_execution_repository]] → `contains` → [[assistant_app_repositories_failed_execution_repository_failedexecutionrecord]]
- [[assistant_app_repositories_failed_execution_repository]] → `contains` → [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository]]
- [[assistant_app_repositories_failed_execution_repository]] → `imports_from` → [[assistant_app_repositories_failed_execution_repository_py_uuid]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_list_pending]] → `references` → [[assistant_app_repositories_failed_execution_repository_failedexecutionrecord]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository]] → `method` → [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_count_pending]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository]] → `method` → [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_init]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository]] → `method` → [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_list_pending]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository]] → `method` → [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_mark_reprocessed]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository]] → `method` → [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_save]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_init]] → `references` → [[assistant_app_repositories_failed_execution_repository_py_asyncsession]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_save]] → `references` → [[assistant_app_repositories_failed_execution_repository_py_uuid]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_save]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_mark_reprocessed]] → `references` → [[assistant_app_repositories_failed_execution_repository_py_uuid]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_list_pending]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_mark_reprocessed]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]
- [[assistant_app_repositories_failed_execution_repository_failedexecutionrepository_count_pending]] → `calls` → [[graphify_worked_httpx_raw_models_response_text]]