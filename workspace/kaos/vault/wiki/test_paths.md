# graphify\tests\test_paths.py

## Símbolos

- [[graphify_tests_test_paths]] — code: test_paths.py
- [[graphify_tests_test_paths_test_is_test_path_positive]] — code: test_is_test_path_positive()
- [[graphify_tests_test_paths_test_is_test_path_negative]] — code: test_is_test_path_negative()
- [[graphify_tests_test_paths_test_disambiguate_drops_test_candidate_for_nontest_call_site]] — code: test_disambiguate_drops_test_candidate_for_nontest_call_site()
- [[graphify_tests_test_paths_test_disambiguate_bails_on_two_nontest_candidates]] — code: test_disambiguate_bails_on_two_nontest_candidates()
- [[graphify_tests_test_paths_test_disambiguate_test_call_site_prefers_test_local]] — code: test_disambiguate_test_call_site_prefers_test_local()
- [[graphify_tests_test_paths_test_disambiguate_path_proximity_same_dir]] — code: test_disambiguate_path_proximity_same_dir()
- [[graphify_tests_test_paths_rationale_1]] — code: Tests for graphify.paths — the shared test-path classifier (#1553).

## Dependências

- [[graphify_tests_test_paths]] → `imports_from` → [[graphify_graphify_paths]]
- [[graphify_tests_test_paths_test_is_test_path_negative]] → `calls` → [[graphify_graphify_paths_is_test_path]]
- [[graphify_tests_test_paths_test_is_test_path_positive]] → `calls` → [[graphify_graphify_paths_is_test_path]]
- [[graphify_tests_test_paths_test_disambiguate_bails_on_two_nontest_candidates]] → `calls` → [[graphify_graphify_paths_disambiguate_ambiguous_candidates]]
- [[graphify_tests_test_paths_test_disambiguate_drops_test_candidate_for_nontest_call_site]] → `calls` → [[graphify_graphify_paths_disambiguate_ambiguous_candidates]]
- [[graphify_tests_test_paths_test_disambiguate_path_proximity_same_dir]] → `calls` → [[graphify_graphify_paths_disambiguate_ambiguous_candidates]]
- [[graphify_tests_test_paths_test_disambiguate_test_call_site_prefers_test_local]] → `calls` → [[graphify_graphify_paths_disambiguate_ambiguous_candidates]]
- [[graphify_tests_test_paths]] → `contains` → [[graphify_tests_test_paths_test_disambiguate_bails_on_two_nontest_candidates]]
- [[graphify_tests_test_paths]] → `contains` → [[graphify_tests_test_paths_test_disambiguate_drops_test_candidate_for_nontest_call_site]]
- [[graphify_tests_test_paths]] → `contains` → [[graphify_tests_test_paths_test_disambiguate_path_proximity_same_dir]]
- [[graphify_tests_test_paths]] → `contains` → [[graphify_tests_test_paths_test_disambiguate_test_call_site_prefers_test_local]]
- [[graphify_tests_test_paths]] → `contains` → [[graphify_tests_test_paths_test_is_test_path_negative]]
- [[graphify_tests_test_paths]] → `contains` → [[graphify_tests_test_paths_test_is_test_path_positive]]
- [[graphify_tests_test_paths_rationale_1]] → `rationale_for` → [[graphify_tests_test_paths]]