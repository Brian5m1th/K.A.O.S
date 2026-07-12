# assistant\tests\unit\test_observability_subscribers.py

## Símbolos

- [[assistant_tests_unit_test_observability_subscribers]] — code: test_observability_subscribers.py
- [[assistant_tests_unit_test_observability_subscribers_clear_eventbus]] — code: clear_eventbus()
- [[assistant_tests_unit_test_observability_subscribers_test_logger_subscriber_logs_event]] — code: test_logger_subscriber_logs_event()
- [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_counts_events]] — code: test_metrics_subscriber_counts_events()
- [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_workflow_duration]] — code: test_metrics_subscriber_workflow_duration()
- [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_llm_duration]] — code: test_metrics_subscriber_llm_duration()
- [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_failed_event]] — code: test_metrics_subscriber_failed_event()
- [[assistant_tests_unit_test_observability_subscribers_test_audit_subscriber_logs_event]] — code: test_audit_subscriber_logs_event()
- [[assistant_tests_unit_test_observability_subscribers_test_subscribers_work_with_eventbus]] — code: test_subscribers_work_with_eventbus()
- [[assistant_tests_unit_test_observability_subscribers_test_eventbus_subscriber_error_does_not_break_publish]] — code: test_eventbus_subscriber_error_does_not_break_publish()

## Dependências

- [[assistant_tests_unit_test_observability_subscribers_test_audit_subscriber_logs_event]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_observability_subscribers_test_eventbus_subscriber_error_does_not_break_publish]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_observability_subscribers_test_logger_subscriber_logs_event]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_counts_events]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_failed_event]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_llm_duration]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_workflow_duration]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_observability_subscribers_test_subscribers_work_with_eventbus]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_observability_subscribers_test_audit_subscriber_logs_event]] → `calls` → [[assistant_app_observability_subscribers_audit_subscriber_auditsubscriber]]
- [[assistant_tests_unit_test_observability_subscribers_test_eventbus_subscriber_error_does_not_break_publish]] → `calls` → [[assistant_app_observability_subscribers_logger_subscriber_loggersubscriber]]
- [[assistant_tests_unit_test_observability_subscribers_test_logger_subscriber_logs_event]] → `calls` → [[assistant_app_observability_subscribers_logger_subscriber_loggersubscriber]]
- [[assistant_tests_unit_test_observability_subscribers_test_subscribers_work_with_eventbus]] → `calls` → [[assistant_app_observability_subscribers_logger_subscriber_loggersubscriber]]
- [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_counts_events]] → `calls` → [[assistant_app_observability_subscribers_metrics_subscriber_metricssubscriber]]
- [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_failed_event]] → `calls` → [[assistant_app_observability_subscribers_metrics_subscriber_metricssubscriber]]
- [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_llm_duration]] → `calls` → [[assistant_app_observability_subscribers_metrics_subscriber_metricssubscriber]]
- [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_workflow_duration]] → `calls` → [[assistant_app_observability_subscribers_metrics_subscriber_metricssubscriber]]
- [[assistant_tests_unit_test_observability_subscribers_test_subscribers_work_with_eventbus]] → `calls` → [[assistant_app_observability_subscribers_metrics_subscriber_metricssubscriber]]
- [[assistant_tests_unit_test_observability_subscribers]] → `contains` → [[assistant_tests_unit_test_observability_subscribers_clear_eventbus]]
- [[assistant_tests_unit_test_observability_subscribers]] → `contains` → [[assistant_tests_unit_test_observability_subscribers_test_audit_subscriber_logs_event]]
- [[assistant_tests_unit_test_observability_subscribers]] → `contains` → [[assistant_tests_unit_test_observability_subscribers_test_eventbus_subscriber_error_does_not_break_publish]]
- [[assistant_tests_unit_test_observability_subscribers]] → `contains` → [[assistant_tests_unit_test_observability_subscribers_test_logger_subscriber_logs_event]]
- [[assistant_tests_unit_test_observability_subscribers]] → `contains` → [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_counts_events]]
- [[assistant_tests_unit_test_observability_subscribers]] → `contains` → [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_failed_event]]
- [[assistant_tests_unit_test_observability_subscribers]] → `contains` → [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_llm_duration]]
- [[assistant_tests_unit_test_observability_subscribers]] → `contains` → [[assistant_tests_unit_test_observability_subscribers_test_metrics_subscriber_workflow_duration]]
- [[assistant_tests_unit_test_observability_subscribers]] → `contains` → [[assistant_tests_unit_test_observability_subscribers_test_subscribers_work_with_eventbus]]