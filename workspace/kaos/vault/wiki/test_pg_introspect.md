# graphify\tests\test_pg_introspect.py

## Símbolos

- [[graphify_tests_test_pg_introspect]] — code: test_pg_introspect.py
- [[graphify_tests_test_pg_introspect_make_mock_psycopg]] — code: _make_mock_psycopg()
- [[graphify_tests_test_pg_introspect_q]] — code: _q()
- [[graphify_tests_test_pg_introspect_test_pg_introspect_success]] — code: test_pg_introspect_success()
- [[graphify_tests_test_pg_introspect_test_pg_introspect_quoted_identifiers]] — code: test_pg_introspect_quoted_identifiers()
- [[graphify_tests_test_pg_introspect_test_pg_introspect_composite_fk]] — code: test_pg_introspect_composite_fk()
- [[graphify_tests_test_pg_introspect_test_pg_introspect_fk_query_avoids_privilege_filtered_view]] — code: test_pg_introspect_fk_query_avoids_privilege_filtered_view()
- [[graphify_tests_test_pg_introspect_test_pg_introspect_connection_error]] — code: test_pg_introspect_connection_error()
- [[graphify_tests_test_pg_introspect_test_pg_introspect_import_error]] — code: test_pg_introspect_import_error()
- [[graphify_tests_test_pg_introspect_test_pg_introspect_uri_forward_slashes]] — code: test_pg_introspect_uri_forward_slashes()
- [[graphify_tests_test_pg_introspect_rationale_19]] — code: Return a mock psycopg module wired to the provided catalog data.      ``routin
- [[graphify_tests_test_pg_introspect_rationale_90]] — code: Return the label form that tree-sitter produces for a quoted identifier.
- [[graphify_tests_test_pg_introspect_rationale_104]] — code: Baseline: tables, views, routines, and a single-column FK all survive.
- [[graphify_tests_test_pg_introspect_rationale_164]] — code: Reserved-word and special-character table names must survive DDL round-trip.
- [[graphify_tests_test_pg_introspect_rationale_203]] — code: A 2-column composite FK must produce exactly ONE references edge, not two.
- [[graphify_tests_test_pg_introspect_rationale_252]] — code: #1746: information_schema.referential_constraints only shows constraints     wh
- [[graphify_tests_test_pg_introspect_rationale_287]] — code: A psycopg.OperationalError must be re-raised as ConnectionError with a     sani
- [[graphify_tests_test_pg_introspect_rationale_314]] — code: If psycopg is missing, introspect_postgres raises ImportError.
- [[graphify_tests_test_pg_introspect_rationale_321]] — code: Assert that the virtual path in postgresql introspection output uses forward sla

## Dependências

- [[graphify_tests_test_pg_introspect]] → `imports_from` → [[graphify_graphify_pg_introspect]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_composite_fk]] → `calls` → [[graphify_graphify_pg_introspect_introspect_postgres]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_connection_error]] → `calls` → [[graphify_graphify_pg_introspect_introspect_postgres]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_fk_query_avoids_privilege_filtered_view]] → `calls` → [[graphify_graphify_pg_introspect_introspect_postgres]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_import_error]] → `calls` → [[graphify_graphify_pg_introspect_introspect_postgres]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_quoted_identifiers]] → `calls` → [[graphify_graphify_pg_introspect_introspect_postgres]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_success]] → `calls` → [[graphify_graphify_pg_introspect_introspect_postgres]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_uri_forward_slashes]] → `calls` → [[graphify_graphify_pg_introspect_introspect_postgres]]
- [[graphify_tests_test_pg_introspect]] → `imports_from` → [[graphify_graphify_validate]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_composite_fk]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_quoted_identifiers]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_success]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_pg_introspect]] → `contains` → [[graphify_tests_test_pg_introspect_make_mock_psycopg]]
- [[graphify_tests_test_pg_introspect]] → `contains` → [[graphify_tests_test_pg_introspect_q]]
- [[graphify_tests_test_pg_introspect]] → `contains` → [[graphify_tests_test_pg_introspect_test_pg_introspect_composite_fk]]
- [[graphify_tests_test_pg_introspect]] → `contains` → [[graphify_tests_test_pg_introspect_test_pg_introspect_connection_error]]
- [[graphify_tests_test_pg_introspect]] → `contains` → [[graphify_tests_test_pg_introspect_test_pg_introspect_fk_query_avoids_privilege_filtered_view]]
- [[graphify_tests_test_pg_introspect]] → `contains` → [[graphify_tests_test_pg_introspect_test_pg_introspect_import_error]]
- [[graphify_tests_test_pg_introspect]] → `contains` → [[graphify_tests_test_pg_introspect_test_pg_introspect_quoted_identifiers]]
- [[graphify_tests_test_pg_introspect]] → `contains` → [[graphify_tests_test_pg_introspect_test_pg_introspect_success]]
- [[graphify_tests_test_pg_introspect]] → `contains` → [[graphify_tests_test_pg_introspect_test_pg_introspect_uri_forward_slashes]]
- [[graphify_tests_test_pg_introspect_rationale_19]] → `rationale_for` → [[graphify_tests_test_pg_introspect_make_mock_psycopg]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_composite_fk]] → `calls` → [[graphify_tests_test_pg_introspect_make_mock_psycopg]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_connection_error]] → `calls` → [[graphify_tests_test_pg_introspect_make_mock_psycopg]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_fk_query_avoids_privilege_filtered_view]] → `calls` → [[graphify_tests_test_pg_introspect_make_mock_psycopg]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_quoted_identifiers]] → `calls` → [[graphify_tests_test_pg_introspect_make_mock_psycopg]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_success]] → `calls` → [[graphify_tests_test_pg_introspect_make_mock_psycopg]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_uri_forward_slashes]] → `calls` → [[graphify_tests_test_pg_introspect_make_mock_psycopg]]
- [[graphify_tests_test_pg_introspect_rationale_90]] → `rationale_for` → [[graphify_tests_test_pg_introspect_q]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_composite_fk]] → `calls` → [[graphify_tests_test_pg_introspect_q]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_quoted_identifiers]] → `calls` → [[graphify_tests_test_pg_introspect_q]]
- [[graphify_tests_test_pg_introspect_test_pg_introspect_success]] → `calls` → [[graphify_tests_test_pg_introspect_q]]
- [[graphify_tests_test_pg_introspect_rationale_104]] → `rationale_for` → [[graphify_tests_test_pg_introspect_test_pg_introspect_success]]
- [[graphify_tests_test_pg_introspect_rationale_164]] → `rationale_for` → [[graphify_tests_test_pg_introspect_test_pg_introspect_quoted_identifiers]]
- [[graphify_tests_test_pg_introspect_rationale_203]] → `rationale_for` → [[graphify_tests_test_pg_introspect_test_pg_introspect_composite_fk]]
- [[graphify_tests_test_pg_introspect_rationale_252]] → `rationale_for` → [[graphify_tests_test_pg_introspect_test_pg_introspect_fk_query_avoids_privilege_filtered_view]]
- [[graphify_tests_test_pg_introspect_rationale_287]] → `rationale_for` → [[graphify_tests_test_pg_introspect_test_pg_introspect_connection_error]]
- [[graphify_tests_test_pg_introspect_rationale_314]] → `rationale_for` → [[graphify_tests_test_pg_introspect_test_pg_introspect_import_error]]
- [[graphify_tests_test_pg_introspect_rationale_321]] → `rationale_for` → [[graphify_tests_test_pg_introspect_test_pg_introspect_uri_forward_slashes]]