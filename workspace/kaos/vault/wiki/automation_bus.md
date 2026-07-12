# assistant\app\core\automation_bus.py

## Símbolos

- [[assistant_app_core_automation_bus]] — code: automation_bus.py
- [[assistant_app_core_automation_bus_automationbus]] — code: AutomationBus
- [[assistant_app_core_automation_bus_automationbus_get_provider]] — code: .get_provider()
- [[assistant_app_core_automation_bus_automationbus_auto_import_workflows]] — code: .auto_import_workflows()
- [[assistant_app_core_automation_bus_automationbus_publish]] — code: .publish()
- [[assistant_app_core_automation_bus_automationbus_start_worker]] — code: .start_worker()
- [[assistant_app_core_automation_bus_automationbus_stop_worker]] — code: .stop_worker()
- [[assistant_app_core_automation_bus_automationbus_consume_queue]] — code: ._consume_queue()
- [[assistant_app_core_automation_bus_automationbus_resolve_webhook_path]] — code: ._resolve_webhook_path()
- [[assistant_app_core_automation_bus_rationale_23]] — code: Resolves the configured automation workflow provider.
- [[assistant_app_core_automation_bus_rationale_32]] — code: Polls n8n health status, scans data/workflows/ JSON templates,         and auto
- [[assistant_app_core_automation_bus_rationale_128]] — code: Publishes an event to the automation queue.         Enforces cascading loop lim
- [[assistant_app_core_automation_bus_rationale_158]] — code: Starts the background worker queue consumer.
- [[assistant_app_core_automation_bus_rationale_167]] — code: Stops the background worker consumer.
- [[assistant_app_core_automation_bus_rationale_179]] — code: Worker consumption loop.
- [[assistant_app_core_automation_bus_rationale_219]] — code: Maps EventBus event names to n8n webhook trigger URL path keys.

## Dependências

- [[assistant_app_core_automation_bus]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_core_automation_bus]] → `contains` → [[assistant_app_core_automation_bus_automationbus]]
- [[assistant_app_core_automation_bus_automationbus]] → `method` → [[assistant_app_core_automation_bus_automationbus_auto_import_workflows]]
- [[assistant_app_core_automation_bus_automationbus]] → `method` → [[assistant_app_core_automation_bus_automationbus_consume_queue]]
- [[assistant_app_core_automation_bus_automationbus]] → `method` → [[assistant_app_core_automation_bus_automationbus_get_provider]]
- [[assistant_app_core_automation_bus_automationbus]] → `method` → [[assistant_app_core_automation_bus_automationbus_publish]]
- [[assistant_app_core_automation_bus_automationbus]] → `method` → [[assistant_app_core_automation_bus_automationbus_resolve_webhook_path]]
- [[assistant_app_core_automation_bus_automationbus]] → `method` → [[assistant_app_core_automation_bus_automationbus_start_worker]]
- [[assistant_app_core_automation_bus_automationbus]] → `method` → [[assistant_app_core_automation_bus_automationbus_stop_worker]]
- [[assistant_app_core_automation_bus_automationbus]] → `uses` → [[assistant_app_models_automation_registry_automationworkflow]]
- [[assistant_app_core_automation_bus_automationbus]] → `uses` → [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider]]
- [[assistant_app_core_automation_bus_automationbus]] → `uses` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider]]
- [[assistant_app_core_automation_bus_automationbus_auto_import_workflows]] → `calls` → [[assistant_app_core_automation_bus_automationbus_get_provider]]
- [[assistant_app_core_automation_bus_automationbus_consume_queue]] → `calls` → [[assistant_app_core_automation_bus_automationbus_get_provider]]
- [[assistant_app_core_automation_bus_automationbus_get_provider]] → `references` → [[assistant_app_providers_automation_base_workflow_provider_baseworkflowprovider]]
- [[assistant_app_core_automation_bus_automationbus_get_provider]] → `calls` → [[assistant_app_providers_automation_n8n_workflow_provider_n8nworkflowprovider]]
- [[assistant_app_core_automation_bus_rationale_23]] → `rationale_for` → [[assistant_app_core_automation_bus_automationbus_get_provider]]
- [[assistant_app_core_automation_bus_automationbus_auto_import_workflows]] → `indirect_call` → [[assistant_app_models_automation_registry_automationworkflow]]
- [[assistant_app_core_automation_bus_rationale_32]] → `rationale_for` → [[assistant_app_core_automation_bus_automationbus_auto_import_workflows]]
- [[assistant_app_core_automation_bus_automationbus_publish]] → `references` → [[assistant_app_core_automation_bus_py_any]]
- [[assistant_app_core_automation_bus_rationale_128]] → `rationale_for` → [[assistant_app_core_automation_bus_automationbus_publish]]
- [[assistant_app_core_automation_bus_automationbus_start_worker]] → `calls` → [[assistant_app_core_automation_bus_automationbus_consume_queue]]
- [[assistant_app_core_automation_bus_rationale_158]] → `rationale_for` → [[assistant_app_core_automation_bus_automationbus_start_worker]]
- [[assistant_app_core_automation_bus_rationale_167]] → `rationale_for` → [[assistant_app_core_automation_bus_automationbus_stop_worker]]
- [[assistant_app_core_automation_bus_automationbus_consume_queue]] → `calls` → [[assistant_app_core_automation_bus_automationbus_resolve_webhook_path]]
- [[assistant_app_core_automation_bus_rationale_179]] → `rationale_for` → [[assistant_app_core_automation_bus_automationbus_consume_queue]]
- [[assistant_app_core_automation_bus_rationale_219]] → `rationale_for` → [[assistant_app_core_automation_bus_automationbus_resolve_webhook_path]]