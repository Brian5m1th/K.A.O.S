# assistant\app\observability\event_bus.py

## Símbolos

- [[assistant_app_observability_event_bus]] — code: event_bus.py
- [[assistant_app_observability_event_bus_event]] — code: Event
- [[assistant_app_observability_event_bus_eventsubscriber]] — code: EventSubscriber
- [[assistant_app_observability_event_bus_eventsubscriber_on_event]] — code: .on_event()
- [[assistant_app_observability_event_bus_eventbus]] — code: EventBus
- [[assistant_app_observability_event_bus_eventbus_subscribe]] — code: .subscribe()
- [[assistant_app_observability_event_bus_eventbus_unsubscribe]] — code: .unsubscribe()
- [[assistant_app_observability_event_bus_eventbus_publish]] — code: .publish()
- [[assistant_app_observability_event_bus_eventbus_clear]] — code: .clear()

## Dependências

- [[assistant_app_observability_event_bus]] → `contains` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_observability_event_bus]] → `contains` → [[assistant_app_observability_event_bus_eventbus]]
- [[assistant_app_observability_event_bus]] → `contains` → [[assistant_app_observability_event_bus_eventsubscriber]]
- [[assistant_app_observability_event_bus]] → `imports_from` → [[assistant_app_observability_event_bus_py_abc]]
- [[assistant_app_observability_event_bus_eventbus_publish]] → `references` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_observability_event_bus_eventsubscriber_on_event]] → `references` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_observability_event_bus_eventbus_subscribe]] → `references` → [[assistant_app_observability_event_bus_eventsubscriber]]
- [[assistant_app_observability_event_bus_eventbus_unsubscribe]] → `references` → [[assistant_app_observability_event_bus_eventsubscriber]]
- [[assistant_app_observability_event_bus_eventsubscriber]] → `method` → [[assistant_app_observability_event_bus_eventsubscriber_on_event]]
- [[assistant_app_observability_event_bus_eventsubscriber]] → `inherits` → [[assistant_app_observability_event_bus_py_abc]]
- [[assistant_app_observability_event_bus_eventbus_publish]] → `calls` → [[assistant_app_observability_event_bus_eventsubscriber_on_event]]
- [[assistant_app_observability_event_bus_eventbus]] → `method` → [[assistant_app_observability_event_bus_eventbus_clear]]
- [[assistant_app_observability_event_bus_eventbus]] → `method` → [[assistant_app_observability_event_bus_eventbus_publish]]
- [[assistant_app_observability_event_bus_eventbus]] → `method` → [[assistant_app_observability_event_bus_eventbus_subscribe]]
- [[assistant_app_observability_event_bus_eventbus]] → `method` → [[assistant_app_observability_event_bus_eventbus_unsubscribe]]