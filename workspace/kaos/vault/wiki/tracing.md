# assistant\app\observability\tracing.py

## Símbolos

- [[assistant_app_observability_tracing]] — code: tracing.py
- [[assistant_app_observability_tracing_setup_tracing]] — code: setup_tracing()
- [[assistant_app_observability_tracing_get_tracer]] — code: get_tracer()
- [[assistant_app_observability_tracing_tracingsubscriber]] — code: TracingSubscriber
- [[assistant_app_observability_tracing_tracingsubscriber_on_event]] — code: .on_event()

## Dependências

- [[assistant_app_observability_tracing_tracingsubscriber]] → `uses` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_observability_tracing_tracingsubscriber_on_event]] → `references` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_observability_tracing_tracingsubscriber]] → `uses` → [[assistant_app_observability_event_bus_eventsubscriber]]
- [[assistant_app_observability_tracing]] → `contains` → [[assistant_app_observability_tracing_get_tracer]]
- [[assistant_app_observability_tracing]] → `contains` → [[assistant_app_observability_tracing_setup_tracing]]
- [[assistant_app_observability_tracing]] → `contains` → [[assistant_app_observability_tracing_tracingsubscriber]]
- [[assistant_app_observability_tracing_setup_tracing]] → `calls` → [[assistant_app_observability_tracing_get_tracer]]
- [[assistant_app_observability_tracing_get_tracer]] → `references` → [[assistant_app_observability_tracing_py_any]]
- [[assistant_app_observability_tracing_tracingsubscriber]] → `method` → [[assistant_app_observability_tracing_tracingsubscriber_on_event]]