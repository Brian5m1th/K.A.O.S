# assistant\app\observability\cost_tracker.py

## Símbolos

- [[assistant_app_observability_cost_tracker]] — code: cost_tracker.py
- [[assistant_app_observability_cost_tracker_costtracker]] — code: CostTracker
- [[assistant_app_observability_cost_tracker_costtracker_init]] — code: .__init__()
- [[assistant_app_observability_cost_tracker_costtracker_on_event]] — code: .on_event()
- [[assistant_app_observability_cost_tracker_costtracker_estimate_cost]] — code: ._estimate_cost()
- [[assistant_app_observability_cost_tracker_costtracker_persist_cost_event]] — code: ._persist_cost_event()
- [[assistant_app_observability_cost_tracker_costtracker_summary]] — code: .summary()
- [[assistant_app_observability_cost_tracker_costtracker_reset]] — code: .reset()
- [[assistant_app_observability_cost_tracker_rationale_120]] — code: Salva evento de custo no PostgreSQL. Fire-and-forget friendly.

## Dependências

- [[assistant_app_observability_cost_tracker]] → `contains` → [[assistant_app_observability_cost_tracker_costtracker]]
- [[assistant_app_observability_cost_tracker]] → `imports_from` → [[assistant_app_observability_cost_tracker_py_uuid]]
- [[assistant_app_observability_cost_tracker_costtracker]] → `method` → [[assistant_app_observability_cost_tracker_costtracker_estimate_cost]]
- [[assistant_app_observability_cost_tracker_costtracker]] → `method` → [[assistant_app_observability_cost_tracker_costtracker_init]]
- [[assistant_app_observability_cost_tracker_costtracker]] → `method` → [[assistant_app_observability_cost_tracker_costtracker_on_event]]
- [[assistant_app_observability_cost_tracker_costtracker]] → `method` → [[assistant_app_observability_cost_tracker_costtracker_persist_cost_event]]
- [[assistant_app_observability_cost_tracker_costtracker]] → `method` → [[assistant_app_observability_cost_tracker_costtracker_reset]]
- [[assistant_app_observability_cost_tracker_costtracker]] → `method` → [[assistant_app_observability_cost_tracker_costtracker_summary]]
- [[assistant_app_observability_cost_tracker_costtracker]] → `uses` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_observability_cost_tracker_costtracker]] → `uses` → [[assistant_app_observability_event_bus_eventsubscriber]]
- [[assistant_app_observability_cost_tracker_costtracker]] → `uses` → [[assistant_app_repositories_cost_repository_costeventdata]]
- [[assistant_app_observability_cost_tracker_costtracker]] → `uses` → [[assistant_app_repositories_cost_repository_costrepository]]
- [[assistant_app_observability_cost_tracker_costtracker_on_event]] → `calls` → [[assistant_app_observability_cost_tracker_costtracker_estimate_cost]]
- [[assistant_app_observability_cost_tracker_costtracker_on_event]] → `calls` → [[assistant_app_observability_cost_tracker_costtracker_persist_cost_event]]
- [[assistant_app_observability_cost_tracker_costtracker_on_event]] → `references` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_observability_cost_tracker_costtracker_persist_cost_event]] → `references` → [[assistant_app_observability_cost_tracker_py_uuid]]
- [[assistant_app_observability_cost_tracker_costtracker_persist_cost_event]] → `calls` → [[assistant_app_repositories_cost_repository_costeventdata]]
- [[assistant_app_observability_cost_tracker_costtracker_persist_cost_event]] → `calls` → [[assistant_app_repositories_cost_repository_costrepository]]
- [[assistant_app_observability_cost_tracker_rationale_120]] → `rationale_for` → [[assistant_app_observability_cost_tracker_costtracker_persist_cost_event]]
- [[assistant_app_observability_cost_tracker_costtracker_summary]] → `references` → [[assistant_app_observability_cost_tracker_py_any]]