# assistant\app\repositories\cost_repository.py

## Símbolos

- [[assistant_app_repositories_cost_repository]] — code: cost_repository.py
- [[assistant_app_repositories_cost_repository_costeventdata]] — code: CostEventData
- [[assistant_app_repositories_cost_repository_costbreakdown]] — code: CostBreakdown
- [[assistant_app_repositories_cost_repository_costsummary]] — code: CostSummary
- [[assistant_app_repositories_cost_repository_costrepository]] — code: CostRepository
- [[assistant_app_repositories_cost_repository_costrepository_init]] — code: .__init__()
- [[assistant_app_repositories_cost_repository_costrepository_save]] — code: .save()
- [[assistant_app_repositories_cost_repository_costrepository_aggregate]] — code: .aggregate()
- [[assistant_app_repositories_cost_repository_costrepository_summary]] — code: .summary()
- [[assistant_app_repositories_cost_repository_rationale_1]] — code: CostRepository — persistence and aggregation for cost tracking.  Uses SQLAlche
- [[assistant_app_repositories_cost_repository_rationale_19]] — code: Input data for recording a cost event.
- [[assistant_app_repositories_cost_repository_rationale_33]] — code: Aggregated cost by provider and workflow.
- [[assistant_app_repositories_cost_repository_rationale_44]] — code: Overall cost summary for a period.
- [[assistant_app_repositories_cost_repository_rationale_52]] — code: Repository for persisting and querying cost events.
- [[assistant_app_repositories_cost_repository_rationale_58]] — code: Persist a cost event and return the ORM object.
- [[assistant_app_repositories_cost_repository_rationale_80]] — code: Return cost breakdown grouped by provider and workflow.
- [[assistant_app_repositories_cost_repository_rationale_116]] — code: Return total cost for the period (day|week|month).

## Dependências

- [[assistant_app_repositories_cost_repository_costbreakdown]] → `uses` → [[assistant_app_models_cost_event_costevent]]
- [[assistant_app_repositories_cost_repository_costeventdata]] → `uses` → [[assistant_app_models_cost_event_costevent]]
- [[assistant_app_repositories_cost_repository_costrepository]] → `uses` → [[assistant_app_models_cost_event_costevent]]
- [[assistant_app_repositories_cost_repository_costrepository_save]] → `references` → [[assistant_app_models_cost_event_costevent]]
- [[assistant_app_repositories_cost_repository_costsummary]] → `uses` → [[assistant_app_models_cost_event_costevent]]
- [[assistant_app_repositories_cost_repository]] → `contains` → [[assistant_app_repositories_cost_repository_costbreakdown]]
- [[assistant_app_repositories_cost_repository]] → `contains` → [[assistant_app_repositories_cost_repository_costeventdata]]
- [[assistant_app_repositories_cost_repository]] → `contains` → [[assistant_app_repositories_cost_repository_costrepository]]
- [[assistant_app_repositories_cost_repository]] → `contains` → [[assistant_app_repositories_cost_repository_costsummary]]
- [[assistant_app_repositories_cost_repository_rationale_1]] → `rationale_for` → [[assistant_app_repositories_cost_repository]]
- [[assistant_app_repositories_cost_repository_costrepository_save]] → `references` → [[assistant_app_repositories_cost_repository_costeventdata]]
- [[assistant_app_repositories_cost_repository_rationale_19]] → `rationale_for` → [[assistant_app_repositories_cost_repository_costeventdata]]
- [[assistant_app_repositories_cost_repository_costrepository_aggregate]] → `references` → [[assistant_app_repositories_cost_repository_costbreakdown]]
- [[assistant_app_repositories_cost_repository_costrepository_summary]] → `calls` → [[assistant_app_repositories_cost_repository_costbreakdown]]
- [[assistant_app_repositories_cost_repository_rationale_33]] → `rationale_for` → [[assistant_app_repositories_cost_repository_costbreakdown]]
- [[assistant_app_repositories_cost_repository_costrepository_summary]] → `references` → [[assistant_app_repositories_cost_repository_costsummary]]
- [[assistant_app_repositories_cost_repository_rationale_44]] → `rationale_for` → [[assistant_app_repositories_cost_repository_costsummary]]
- [[assistant_app_repositories_cost_repository_costrepository]] → `method` → [[assistant_app_repositories_cost_repository_costrepository_aggregate]]
- [[assistant_app_repositories_cost_repository_costrepository]] → `method` → [[assistant_app_repositories_cost_repository_costrepository_init]]
- [[assistant_app_repositories_cost_repository_costrepository]] → `method` → [[assistant_app_repositories_cost_repository_costrepository_save]]
- [[assistant_app_repositories_cost_repository_costrepository]] → `method` → [[assistant_app_repositories_cost_repository_costrepository_summary]]
- [[assistant_app_repositories_cost_repository_rationale_52]] → `rationale_for` → [[assistant_app_repositories_cost_repository_costrepository]]
- [[assistant_app_repositories_cost_repository_costrepository_init]] → `references` → [[assistant_app_repositories_cost_repository_py_asyncsession]]
- [[assistant_app_repositories_cost_repository_rationale_58]] → `rationale_for` → [[assistant_app_repositories_cost_repository_costrepository_save]]
- [[assistant_app_repositories_cost_repository_rationale_80]] → `rationale_for` → [[assistant_app_repositories_cost_repository_costrepository_aggregate]]
- [[assistant_app_repositories_cost_repository_rationale_116]] → `rationale_for` → [[assistant_app_repositories_cost_repository_costrepository_summary]]