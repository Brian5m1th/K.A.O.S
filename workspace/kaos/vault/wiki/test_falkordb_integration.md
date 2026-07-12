# graphify\tests\test_falkordb_integration.py

## Símbolos

- [[graphify_tests_test_falkordb_integration]] — code: test_falkordb_integration.py
- [[graphify_tests_test_falkordb_integration_connect]] — code: _connect()
- [[graphify_tests_test_falkordb_integration_db]] — code: db()
- [[graphify_tests_test_falkordb_integration_test_push_to_falkordb_creates_expected_graph]] — code: test_push_to_falkordb_creates_expected_graph()
- [[graphify_tests_test_falkordb_integration_test_push_to_falkordb_is_idempotent]] — code: test_push_to_falkordb_is_idempotent()
- [[graphify_tests_test_falkordb_integration_rationale_1]] — code: Integration test for push_to_falkordb against a real FalkorDB instance.  Runs
- [[graphify_tests_test_falkordb_integration_rationale_29]] — code: Return a connected FalkorDB client, or skip if none is reachable.
- [[graphify_tests_test_falkordb_integration_rationale_76]] — code: MERGE-based push is safe to re-run - counts must not grow.

## Dependências

- [[graphify_tests_test_falkordb_integration_test_push_to_falkordb_creates_expected_graph]] → `calls` → [[graphify_graphify_exporters_graphdb_push_to_falkordb]]
- [[graphify_tests_test_falkordb_integration_test_push_to_falkordb_is_idempotent]] → `calls` → [[graphify_graphify_exporters_graphdb_push_to_falkordb]]
- [[graphify_tests_test_falkordb_integration]] → `contains` → [[graphify_tests_test_falkordb_integration_connect]]
- [[graphify_tests_test_falkordb_integration]] → `contains` → [[graphify_tests_test_falkordb_integration_db]]
- [[graphify_tests_test_falkordb_integration]] → `contains` → [[graphify_tests_test_falkordb_integration_test_push_to_falkordb_creates_expected_graph]]
- [[graphify_tests_test_falkordb_integration]] → `contains` → [[graphify_tests_test_falkordb_integration_test_push_to_falkordb_is_idempotent]]
- [[graphify_tests_test_falkordb_integration_rationale_1]] → `rationale_for` → [[graphify_tests_test_falkordb_integration]]
- [[graphify_tests_test_falkordb_integration_db]] → `calls` → [[graphify_tests_test_falkordb_integration_connect]]
- [[graphify_tests_test_falkordb_integration_rationale_29]] → `rationale_for` → [[graphify_tests_test_falkordb_integration_connect]]
- [[graphify_tests_test_falkordb_integration_rationale_76]] → `rationale_for` → [[graphify_tests_test_falkordb_integration_test_push_to_falkordb_is_idempotent]]