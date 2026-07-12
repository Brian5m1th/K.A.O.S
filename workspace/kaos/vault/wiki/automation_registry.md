# assistant\app\models\automation_registry.py

## Símbolos

- [[assistant_app_models_automation_registry]] — code: automation_registry.py
- [[assistant_app_models_automation_registry_automationworkflow]] — code: AutomationWorkflow
- [[assistant_app_models_automation_registry_automationexecution]] — code: AutomationExecution
- [[assistant_app_models_automation_registry_rationale_1]] — code: SQLAlchemy models for K.A.O.S automation workflows and executions.

## Dependências

- [[assistant_app_models_automation_registry]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_models_automation_registry_automationexecution]] → `uses` → [[assistant_app_database_base]]
- [[assistant_app_models_automation_registry_automationworkflow]] → `uses` → [[assistant_app_database_base]]
- [[assistant_app_models_automation_registry]] → `contains` → [[assistant_app_models_automation_registry_automationexecution]]
- [[assistant_app_models_automation_registry]] → `contains` → [[assistant_app_models_automation_registry_automationworkflow]]
- [[assistant_app_models_automation_registry_rationale_1]] → `rationale_for` → [[assistant_app_models_automation_registry]]
- [[assistant_app_models_automation_registry_automationworkflow]] → `inherits` → [[assistant_app_models_automation_registry_py_base]]
- [[assistant_app_models_automation_registry_automationexecution]] → `inherits` → [[assistant_app_models_automation_registry_py_base]]