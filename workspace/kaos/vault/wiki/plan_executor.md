# assistant\app\orchestrator\plan_executor.py

## Símbolos

- [[assistant_app_orchestrator_plan_executor]] — code: plan_executor.py
- [[assistant_app_orchestrator_plan_executor_planexecutor]] — code: PlanExecutor
- [[assistant_app_orchestrator_plan_executor_planexecutor_init]] — code: .__init__()
- [[assistant_app_orchestrator_plan_executor_planexecutor_execute]] — code: .execute()
- [[assistant_app_orchestrator_plan_executor_planexecutor_try_half_open]] — code: ._try_half_open()
- [[assistant_app_orchestrator_plan_executor_planexecutor_add_to_dlq]] — code: ._add_to_dlq()

## Dependências

- [[assistant_app_orchestrator_plan_executor_planexecutor]] → `uses` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_orchestrator_plan_executor_planexecutor_execute]] → `references` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_orchestrator_plan_executor_planexecutor]] → `uses` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_orchestrator_plan_executor_planexecutor_add_to_dlq]] → `references` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_orchestrator_plan_executor_planexecutor_execute]] → `references` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_orchestrator_plan_executor_planexecutor]] → `uses` → [[assistant_app_orchestrator_circuit_breaker_circuitstate]]
- [[assistant_app_orchestrator_plan_executor_planexecutor]] → `uses` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]]
- [[assistant_app_orchestrator_plan_executor_planexecutor_init]] → `references` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]]
- [[assistant_app_orchestrator_plan_executor_planexecutor]] → `uses` → [[assistant_app_orchestrator_dead_letter_queue_failedexecution]]
- [[assistant_app_orchestrator_plan_executor_planexecutor_add_to_dlq]] → `calls` → [[assistant_app_orchestrator_dead_letter_queue_failedexecution]]
- [[assistant_app_orchestrator_plan_executor_planexecutor]] → `uses` → [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue]]
- [[assistant_app_orchestrator_plan_executor_planexecutor_add_to_dlq]] → `calls` → [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_add]]
- [[assistant_app_orchestrator_plan_executor_planexecutor]] → `uses` → [[assistant_app_orchestrator_health_cache_providerhealthcache]]
- [[assistant_app_orchestrator_plan_executor_planexecutor_init]] → `references` → [[assistant_app_orchestrator_health_cache_providerhealthcache]]
- [[assistant_app_orchestrator_plan_executor]] → `contains` → [[assistant_app_orchestrator_plan_executor_planexecutor]]
- [[assistant_app_orchestrator_plan_executor_planexecutor]] → `method` → [[assistant_app_orchestrator_plan_executor_planexecutor_add_to_dlq]]
- [[assistant_app_orchestrator_plan_executor_planexecutor]] → `method` → [[assistant_app_orchestrator_plan_executor_planexecutor_execute]]
- [[assistant_app_orchestrator_plan_executor_planexecutor]] → `method` → [[assistant_app_orchestrator_plan_executor_planexecutor_init]]
- [[assistant_app_orchestrator_plan_executor_planexecutor]] → `method` → [[assistant_app_orchestrator_plan_executor_planexecutor_try_half_open]]
- [[assistant_app_orchestrator_plan_executor_planexecutor]] → `uses` → [[assistant_app_registry_service_registry_serviceregistry]]
- [[assistant_app_orchestrator_plan_executor_planexecutor_execute]] → `calls` → [[assistant_app_orchestrator_plan_executor_planexecutor_add_to_dlq]]
- [[assistant_app_orchestrator_plan_executor_planexecutor_execute]] → `calls` → [[assistant_app_orchestrator_plan_executor_planexecutor_try_half_open]]
- [[assistant_app_orchestrator_plan_executor_planexecutor_execute]] → `calls` → [[assistant_app_registry_service_registry_serviceregistry_get_workflow]]
- [[assistant_app_orchestrator_plan_executor_planexecutor_add_to_dlq]] → `references` → [[assistant_app_orchestrator_plan_executor_py_any]]