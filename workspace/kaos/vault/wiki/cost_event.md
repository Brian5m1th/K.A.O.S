# assistant\app\models\cost_event.py

## Símbolos

- [[assistant_app_models_cost_event]] — code: cost_event.py
- [[assistant_app_models_cost_event_costevent]] — code: CostEvent
- [[assistant_app_models_cost_event_rationale_1]] — code: CostEvent SQLAlchemy model.  Persists cost tracking events for observability a

## Dependências

- [[assistant_app_models_cost_event]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_models_cost_event_costevent]] → `uses` → [[assistant_app_database_base]]
- [[assistant_app_models_cost_event]] → `contains` → [[assistant_app_models_cost_event_costevent]]
- [[assistant_app_models_cost_event_rationale_1]] → `rationale_for` → [[assistant_app_models_cost_event]]
- [[assistant_app_models_cost_event_costevent]] → `inherits` → [[assistant_app_models_cost_event_py_base]]