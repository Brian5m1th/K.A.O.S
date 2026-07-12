# assistant\tests\unit\test_cost_tracker.py

## Símbolos

- [[assistant_tests_unit_test_cost_tracker]] — code: test_cost_tracker.py
- [[assistant_tests_unit_test_cost_tracker_tracker]] — code: tracker()
- [[assistant_tests_unit_test_cost_tracker_test_tracks_llm_request]] — code: test_tracks_llm_request()
- [[assistant_tests_unit_test_cost_tracker_test_tracks_workflow_started]] — code: test_tracks_workflow_started()
- [[assistant_tests_unit_test_cost_tracker_test_ollama_cost_is_zero]] — code: test_ollama_cost_is_zero()
- [[assistant_tests_unit_test_cost_tracker_test_openai_cost_accumulates]] — code: test_openai_cost_accumulates()
- [[assistant_tests_unit_test_cost_tracker_test_summary_format]] — code: test_summary_format()
- [[assistant_tests_unit_test_cost_tracker_test_reset_clears_all]] — code: test_reset_clears_all()

## Dependências

- [[assistant_tests_unit_test_cost_tracker_tracker]] → `calls` → [[assistant_app_observability_cost_tracker_costtracker]]
- [[assistant_tests_unit_test_cost_tracker_test_ollama_cost_is_zero]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_cost_tracker_test_openai_cost_accumulates]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_cost_tracker_test_reset_clears_all]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_cost_tracker_test_summary_format]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_cost_tracker_test_tracks_llm_request]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_cost_tracker_test_tracks_workflow_started]] → `calls` → [[assistant_app_observability_event_bus_event]]
- [[assistant_tests_unit_test_cost_tracker]] → `contains` → [[assistant_tests_unit_test_cost_tracker_test_ollama_cost_is_zero]]
- [[assistant_tests_unit_test_cost_tracker]] → `contains` → [[assistant_tests_unit_test_cost_tracker_test_openai_cost_accumulates]]
- [[assistant_tests_unit_test_cost_tracker]] → `contains` → [[assistant_tests_unit_test_cost_tracker_test_reset_clears_all]]
- [[assistant_tests_unit_test_cost_tracker]] → `contains` → [[assistant_tests_unit_test_cost_tracker_test_summary_format]]
- [[assistant_tests_unit_test_cost_tracker]] → `contains` → [[assistant_tests_unit_test_cost_tracker_test_tracks_llm_request]]
- [[assistant_tests_unit_test_cost_tracker]] → `contains` → [[assistant_tests_unit_test_cost_tracker_test_tracks_workflow_started]]
- [[assistant_tests_unit_test_cost_tracker]] → `contains` → [[assistant_tests_unit_test_cost_tracker_tracker]]