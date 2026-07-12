# assistant\app\audit\drift_subscriber.py

## Símbolos

- [[assistant_app_audit_drift_subscriber]] — code: drift_subscriber.py
- [[assistant_app_audit_drift_subscriber_driftsubscriber]] — code: DriftSubscriber
- [[assistant_app_audit_drift_subscriber_driftsubscriber_on_event]] — code: .on_event()
- [[assistant_app_audit_drift_subscriber_driftsubscriber_emit_alert]] — code: ._emit_alert()
- [[assistant_app_audit_drift_subscriber_auditscheduler]] — code: AuditScheduler
- [[assistant_app_audit_drift_subscriber_auditscheduler_run_periodic_audit]] — code: .run_periodic_audit()
- [[assistant_app_audit_drift_subscriber_auditscheduler_set_interval]] — code: .set_interval()

## Dependências

- [[assistant_app_audit_drift_subscriber_auditscheduler]] → `uses` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber]] → `uses` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber_on_event]] → `calls` → [[assistant_app_ai_vault_analyzer_analyzer_engine_analyzerengine_analyze_async]]
- [[assistant_app_audit_drift_subscriber_auditscheduler]] → `uses` → [[assistant_app_audit_audit_engine_auditengine]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber]] → `uses` → [[assistant_app_audit_audit_engine_auditengine]]
- [[assistant_app_audit_drift_subscriber_auditscheduler_run_periodic_audit]] → `calls` → [[assistant_app_audit_audit_engine_auditengine_run_audit]]
- [[assistant_app_audit_drift_subscriber]] → `contains` → [[assistant_app_audit_drift_subscriber_auditscheduler]]
- [[assistant_app_audit_drift_subscriber]] → `contains` → [[assistant_app_audit_drift_subscriber_driftsubscriber]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber]] → `method` → [[assistant_app_audit_drift_subscriber_driftsubscriber_emit_alert]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber]] → `method` → [[assistant_app_audit_drift_subscriber_driftsubscriber_on_event]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber]] → `uses` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber]] → `uses` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber]] → `uses` → [[assistant_app_observability_event_bus_eventbus]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber]] → `uses` → [[assistant_app_observability_event_bus_eventsubscriber]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber_on_event]] → `calls` → [[assistant_app_audit_drift_subscriber_driftsubscriber_emit_alert]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber_on_event]] → `calls` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_build_snapshot]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber_on_event]] → `references` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_audit_drift_subscriber_driftsubscriber_emit_alert]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_audit_drift_subscriber_auditscheduler]] → `method` → [[assistant_app_audit_drift_subscriber_auditscheduler_run_periodic_audit]]
- [[assistant_app_audit_drift_subscriber_auditscheduler]] → `method` → [[assistant_app_audit_drift_subscriber_auditscheduler_set_interval]]
- [[assistant_app_audit_drift_subscriber_auditscheduler]] → `uses` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]]
- [[assistant_app_audit_drift_subscriber_auditscheduler]] → `uses` → [[assistant_app_observability_event_bus_event]]
- [[assistant_app_audit_drift_subscriber_auditscheduler]] → `uses` → [[assistant_app_observability_event_bus_eventbus]]
- [[assistant_app_audit_drift_subscriber_auditscheduler]] → `uses` → [[assistant_app_observability_event_bus_eventsubscriber]]
- [[assistant_app_audit_drift_subscriber_auditscheduler_run_periodic_audit]] → `calls` → [[assistant_app_observability_event_bus_event]]