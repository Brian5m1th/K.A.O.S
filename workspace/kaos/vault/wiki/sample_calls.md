# graphify\tests\fixtures\sample_calls.py

## Símbolos

- [[graphify_tests_fixtures_sample_calls]] — code: sample_calls.py
- [[graphify_tests_fixtures_sample_calls_compute_score]] — code: compute_score()
- [[graphify_tests_fixtures_sample_calls_normalize]] — code: normalize()
- [[graphify_tests_fixtures_sample_calls_run_analysis]] — code: run_analysis()
- [[graphify_tests_fixtures_sample_calls_analyzer]] — code: Analyzer
- [[graphify_tests_fixtures_sample_calls_analyzer_process]] — code: .process()
- [[graphify_tests_fixtures_sample_calls_analyzer_score]] — code: .score()
- [[graphify_tests_fixtures_sample_calls_analyzer_full_pipeline]] — code: .full_pipeline()
- [[graphify_tests_fixtures_sample_calls_rationale_1]] — code: Fixture: functions and methods that call each other - for call-graph extraction

## Dependências

- [[graphify_tests_fixtures_sample_calls]] → `contains` → [[graphify_tests_fixtures_sample_calls_analyzer]]
- [[graphify_tests_fixtures_sample_calls]] → `contains` → [[graphify_tests_fixtures_sample_calls_compute_score]]
- [[graphify_tests_fixtures_sample_calls]] → `contains` → [[graphify_tests_fixtures_sample_calls_normalize]]
- [[graphify_tests_fixtures_sample_calls]] → `contains` → [[graphify_tests_fixtures_sample_calls_run_analysis]]
- [[graphify_tests_fixtures_sample_calls_rationale_1]] → `rationale_for` → [[graphify_tests_fixtures_sample_calls]]
- [[graphify_tests_fixtures_sample_calls_analyzer_score]] → `calls` → [[graphify_tests_fixtures_sample_calls_compute_score]]
- [[graphify_tests_fixtures_sample_calls_run_analysis]] → `calls` → [[graphify_tests_fixtures_sample_calls_compute_score]]
- [[graphify_tests_fixtures_sample_calls_analyzer_full_pipeline]] → `calls` → [[graphify_tests_fixtures_sample_calls_normalize]]
- [[graphify_tests_fixtures_sample_calls_run_analysis]] → `calls` → [[graphify_tests_fixtures_sample_calls_normalize]]
- [[graphify_tests_fixtures_sample_calls_analyzer_process]] → `calls` → [[graphify_tests_fixtures_sample_calls_run_analysis]]
- [[graphify_tests_fixtures_sample_calls_analyzer]] → `method` → [[graphify_tests_fixtures_sample_calls_analyzer_full_pipeline]]
- [[graphify_tests_fixtures_sample_calls_analyzer]] → `method` → [[graphify_tests_fixtures_sample_calls_analyzer_process]]
- [[graphify_tests_fixtures_sample_calls_analyzer]] → `method` → [[graphify_tests_fixtures_sample_calls_analyzer_score]]
- [[graphify_tests_fixtures_sample_calls_analyzer_full_pipeline]] → `calls` → [[graphify_tests_fixtures_sample_calls_analyzer_score]]