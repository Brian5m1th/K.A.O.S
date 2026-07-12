# assistant\app\api\orchestrator.py

## Símbolos

- [[assistant_app_api_orchestrator]] — code: orchestrator.py
- [[assistant_app_api_orchestrator_get_orchestrator]] — code: _get_orchestrator()
- [[assistant_app_api_orchestrator_execute_workflow]] — code: execute_workflow()
- [[assistant_app_api_orchestrator_list_dlq]] — code: list_dlq()
- [[assistant_app_api_orchestrator_clear_dlq]] — code: clear_dlq()

## Dependências

- [[assistant_app_api_orchestrator]] → `contains` → [[assistant_app_api_orchestrator_clear_dlq]]
- [[assistant_app_api_orchestrator]] → `contains` → [[assistant_app_api_orchestrator_execute_workflow]]
- [[assistant_app_api_orchestrator]] → `contains` → [[assistant_app_api_orchestrator_get_orchestrator]]
- [[assistant_app_api_orchestrator]] → `contains` → [[assistant_app_api_orchestrator_list_dlq]]
- [[assistant_app_api_orchestrator]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_orchestrator_execute_workflow]] → `calls` → [[assistant_app_api_orchestrator_get_orchestrator]]
- [[assistant_app_api_orchestrator_get_orchestrator]] → `references` → [[assistant_app_orchestrator_universal_orchestrator_universalorchestrator]]
- [[assistant_app_api_orchestrator_get_orchestrator]] → `calls` → [[assistant_app_providers_register_all_register_all_providers]]
- [[assistant_app_api_orchestrator_get_orchestrator]] → `calls` → [[assistant_app_workflows_impl_registry_register_workflows]]
- [[assistant_app_api_orchestrator_execute_workflow]] → `references` → [[assistant_app_api_orchestrator_py_streamingresponse]]
- [[assistant_app_api_orchestrator_execute_workflow]] → `references` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_api_orchestrator_list_dlq]] → `calls` → [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_count]]
- [[assistant_app_api_orchestrator_list_dlq]] → `calls` → [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_list_all]]
- [[assistant_app_api_orchestrator_clear_dlq]] → `calls` → [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_clear]]