# assistant\app\core\automation_sdk.py

## Símbolos

- [[assistant_app_core_automation_sdk]] — code: automation_sdk.py
- [[assistant_app_core_automation_sdk_automationservice]] — code: AutomationService
- [[assistant_app_core_automation_sdk_automationservice_trigger]] — code: .trigger()
- [[assistant_app_core_automation_sdk_automationservice_emit]] — code: .emit()
- [[assistant_app_core_automation_sdk_automationservice_wait_for]] — code: .wait_for()
- [[assistant_app_core_automation_sdk_rationale_1]] — code: K.A.O.S Internal Automation SDK. Exposes standard hooks for agent nodes, manage
- [[assistant_app_core_automation_sdk_rationale_23]] — code: Triggers a workflow run via the active provider.         Returns a dict: {"succ
- [[assistant_app_core_automation_sdk_rationale_46]] — code: Publishes an event to the Automation Bus queue.         This is non-blocking.
- [[assistant_app_core_automation_sdk_rationale_56]] — code: Blocks and waits until the execution is completed (success or failed) in the dat

## Dependências

- [[assistant_app_core_automation_sdk_automationservice]] → `uses` → [[assistant_app_core_automation_bus_automationbus]]
- [[assistant_app_core_automation_sdk_automationservice_trigger]] → `calls` → [[assistant_app_core_automation_bus_automationbus_get_provider]]
- [[assistant_app_core_automation_sdk_automationservice_emit]] → `calls` → [[assistant_app_core_automation_bus_automationbus_publish]]
- [[assistant_app_core_automation_sdk]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_core_automation_sdk]] → `contains` → [[assistant_app_core_automation_sdk_automationservice]]
- [[assistant_app_core_automation_sdk_rationale_1]] → `rationale_for` → [[assistant_app_core_automation_sdk]]
- [[assistant_app_core_automation_sdk_automationservice]] → `method` → [[assistant_app_core_automation_sdk_automationservice_emit]]
- [[assistant_app_core_automation_sdk_automationservice]] → `method` → [[assistant_app_core_automation_sdk_automationservice_trigger]]
- [[assistant_app_core_automation_sdk_automationservice]] → `method` → [[assistant_app_core_automation_sdk_automationservice_wait_for]]
- [[assistant_app_core_automation_sdk_automationservice]] → `uses` → [[assistant_app_models_automation_registry_automationexecution]]
- [[assistant_app_core_automation_sdk_automationservice_trigger]] → `references` → [[assistant_app_core_automation_sdk_py_any]]
- [[assistant_app_core_automation_sdk_rationale_23]] → `rationale_for` → [[assistant_app_core_automation_sdk_automationservice_trigger]]
- [[assistant_app_core_automation_sdk_automationservice_emit]] → `references` → [[assistant_app_core_automation_sdk_py_any]]
- [[assistant_app_core_automation_sdk_automationservice_wait_for]] → `references` → [[assistant_app_core_automation_sdk_py_any]]
- [[assistant_app_core_automation_sdk_rationale_46]] → `rationale_for` → [[assistant_app_core_automation_sdk_automationservice_emit]]
- [[assistant_app_core_automation_sdk_automationservice_wait_for]] → `indirect_call` → [[assistant_app_models_automation_registry_automationexecution]]
- [[assistant_app_core_automation_sdk_rationale_56]] → `rationale_for` → [[assistant_app_core_automation_sdk_automationservice_wait_for]]