# assistant\app\api\observability.py

## Símbolos

- [[assistant_app_api_observability]] — code: observability.py
- [[assistant_app_api_observability_log_sink]] — code: log_sink()
- [[assistant_app_api_observability_sseeventsubscriber]] — code: SSEEventSubscriber
- [[assistant_app_api_observability_sseeventsubscriber_on_event]] — code: .on_event()
- [[assistant_app_api_observability_costbreakdownresponse]] — code: CostBreakdownResponse
- [[assistant_app_api_observability_costsresponse]] — code: CostsResponse
- [[assistant_app_api_observability_costsummaryresponse]] — code: CostSummaryResponse
- [[assistant_app_api_observability_observability_health]] — code: observability_health()
- [[assistant_app_api_observability_get_costs]] — code: get_costs()
- [[assistant_app_api_observability_get_costs_summary]] — code: get_costs_summary()
- [[assistant_app_api_observability_stream_logs]] — code: stream_logs()
- [[assistant_app_api_observability_stream_events]] — code: stream_events()
- [[assistant_app_api_observability_rationale_162]] — code: RF-F01: Breakdown de custos por provider e workflow.
- [[assistant_app_api_observability_rationale_192]] — code: RF-F02: Total de custos para o período especificado.
- [[assistant_app_api_observability_rationale_220]] — code: SSE endpoint to stream real-time system log records.
- [[assistant_app_api_observability_rationale_245]] — code: SSE endpoint to stream real-time EventBus events.

## Dependências

- [[assistant_app_api_observability]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_api_observability]] → `contains` → [[assistant_app_api_observability_costbreakdownresponse]]
- [[assistant_app_api_observability]] → `contains` → [[assistant_app_api_observability_costsresponse]]
- [[assistant_app_api_observability]] → `contains` → [[assistant_app_api_observability_costsummaryresponse]]
- [[assistant_app_api_observability]] → `contains` → [[assistant_app_api_observability_get_costs]]
- [[assistant_app_api_observability]] → `contains` → [[assistant_app_api_observability_get_costs_summary]]
- [[assistant_app_api_observability]] → `contains` → [[assistant_app_api_observability_log_sink]]
- [[assistant_app_api_observability]] → `contains` → [[assistant_app_api_observability_observability_health]]
- [[assistant_app_api_observability]] → `contains` → [[assistant_app_api_observability_sseeventsubscriber]]
- [[assistant_app_api_observability]] → `contains` → [[assistant_app_api_observability_stream_events]]
- [[assistant_app_api_observability]] → `contains` → [[assistant_app_api_observability_stream_logs]]
- [[assistant_app_api_observability]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_observability_sseeventsubscriber]] → `method` → [[assistant_app_api_observability_sseeventsubscriber_on_event]]
- [[assistant_app_api_observability_sseeventsubscriber]] → `uses` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_api_observability_sseeventsubscriber]] → `uses` → [[assistant_app_observability_event_bus_eventbus]]
- [[assistant_app_api_observability_sseeventsubscriber]] → `uses` → [[assistant_app_observability_event_bus_eventsubscriber]]
- [[assistant_app_api_observability_sseeventsubscriber]] → `uses` → [[assistant_app_repositories_cost_repository_costrepository]]
- [[assistant_app_api_observability_sseeventsubscriber_on_event]] → `references` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_api_observability_costbreakdownresponse]] → `inherits` → [[assistant_app_api_observability_py_basemodel]]
- [[assistant_app_api_observability_costbreakdownresponse]] → `uses` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_api_observability_costbreakdownresponse]] → `uses` → [[assistant_app_observability_event_bus_eventbus]]
- [[assistant_app_api_observability_costbreakdownresponse]] → `uses` → [[assistant_app_observability_event_bus_eventsubscriber]]
- [[assistant_app_api_observability_costbreakdownresponse]] → `uses` → [[assistant_app_repositories_cost_repository_costrepository]]
- [[assistant_app_api_observability_get_costs]] → `calls` → [[assistant_app_api_observability_costbreakdownresponse]]
- [[assistant_app_api_observability_get_costs_summary]] → `calls` → [[assistant_app_api_observability_costbreakdownresponse]]
- [[assistant_app_api_observability_costsresponse]] → `inherits` → [[assistant_app_api_observability_py_basemodel]]
- [[assistant_app_api_observability_costsummaryresponse]] → `inherits` → [[assistant_app_api_observability_py_basemodel]]
- [[assistant_app_api_observability_costsresponse]] → `uses` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_api_observability_costsresponse]] → `uses` → [[assistant_app_observability_event_bus_eventbus]]
- [[assistant_app_api_observability_costsresponse]] → `uses` → [[assistant_app_observability_event_bus_eventsubscriber]]
- [[assistant_app_api_observability_costsresponse]] → `uses` → [[assistant_app_repositories_cost_repository_costrepository]]
- [[assistant_app_api_observability_get_costs]] → `calls` → [[assistant_app_api_observability_costsresponse]]
- [[assistant_app_api_observability_costsummaryresponse]] → `uses` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_api_observability_costsummaryresponse]] → `uses` → [[assistant_app_observability_event_bus_eventbus]]
- [[assistant_app_api_observability_costsummaryresponse]] → `uses` → [[assistant_app_observability_event_bus_eventsubscriber]]
- [[assistant_app_api_observability_costsummaryresponse]] → `uses` → [[assistant_app_repositories_cost_repository_costrepository]]
- [[assistant_app_api_observability_get_costs_summary]] → `calls` → [[assistant_app_api_observability_costsummaryresponse]]
- [[assistant_app_api_observability_get_costs]] → `references` → [[assistant_app_api_observability_py_asyncsession]]
- [[assistant_app_api_observability_get_costs]] → `calls` → [[assistant_app_repositories_cost_repository_costrepository]]
- [[assistant_app_api_observability_rationale_162]] → `rationale_for` → [[assistant_app_api_observability_get_costs]]
- [[assistant_app_api_observability_get_costs_summary]] → `references` → [[assistant_app_api_observability_py_asyncsession]]
- [[assistant_app_api_observability_get_costs_summary]] → `calls` → [[assistant_app_repositories_cost_repository_costrepository]]
- [[assistant_app_api_observability_rationale_192]] → `rationale_for` → [[assistant_app_api_observability_get_costs_summary]]
- [[assistant_app_api_observability_rationale_220]] → `rationale_for` → [[assistant_app_api_observability_stream_logs]]
- [[assistant_app_api_observability_rationale_245]] → `rationale_for` → [[assistant_app_api_observability_stream_events]]