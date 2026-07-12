# graphify\tests\test_semantic_fragment_sanitize.py

## Símbolos

- [[graphify_tests_test_semantic_fragment_sanitize]] — code: test_semantic_fragment_sanitize.py
- [[graphify_tests_test_semantic_fragment_sanitize_test_sanitize_drops_non_dict_edge_entries]] — code: test_sanitize_drops_non_dict_edge_entries()
- [[graphify_tests_test_semantic_fragment_sanitize_test_sanitize_coerces_non_list_values_to_empty]] — code: test_sanitize_coerces_non_list_values_to_empty()
- [[graphify_tests_test_semantic_fragment_sanitize_test_parse_llm_json_sanitizes_stray_list_in_edges]] — code: test_parse_llm_json_sanitizes_stray_list_in_edges()
- [[graphify_tests_test_semantic_fragment_sanitize_test_parse_llm_json_fenced_response_is_sanitized]] — code: test_parse_llm_json_fenced_response_is_sanitized()
- [[graphify_tests_test_semantic_fragment_sanitize_test_merge_after_sanitize_does_not_raise_on_source_file_access]] — code: test_merge_after_sanitize_does_not_raise_on_source_file_access()
- [[graphify_tests_test_semantic_fragment_sanitize_rationale_1]] — code: #1631 — a malformed LLM chunk (a stray non-dict entry in edges/nodes) must not

## Dependências

- [[graphify_tests_test_semantic_fragment_sanitize]] → `imports_from` → [[graphify_graphify_llm]]
- [[graphify_tests_test_semantic_fragment_sanitize_test_sanitize_coerces_non_list_values_to_empty]] → `calls` → [[graphify_graphify_llm_sanitize_fragment]]
- [[graphify_tests_test_semantic_fragment_sanitize_test_sanitize_drops_non_dict_edge_entries]] → `calls` → [[graphify_graphify_llm_sanitize_fragment]]
- [[graphify_tests_test_semantic_fragment_sanitize_test_merge_after_sanitize_does_not_raise_on_source_file_access]] → `calls` → [[graphify_graphify_llm_parse_llm_json]]
- [[graphify_tests_test_semantic_fragment_sanitize_test_parse_llm_json_fenced_response_is_sanitized]] → `calls` → [[graphify_graphify_llm_parse_llm_json]]
- [[graphify_tests_test_semantic_fragment_sanitize_test_parse_llm_json_sanitizes_stray_list_in_edges]] → `calls` → [[graphify_graphify_llm_parse_llm_json]]
- [[graphify_tests_test_semantic_fragment_sanitize]] → `contains` → [[graphify_tests_test_semantic_fragment_sanitize_test_merge_after_sanitize_does_not_raise_on_source_file_access]]
- [[graphify_tests_test_semantic_fragment_sanitize]] → `contains` → [[graphify_tests_test_semantic_fragment_sanitize_test_parse_llm_json_fenced_response_is_sanitized]]
- [[graphify_tests_test_semantic_fragment_sanitize]] → `contains` → [[graphify_tests_test_semantic_fragment_sanitize_test_parse_llm_json_sanitizes_stray_list_in_edges]]
- [[graphify_tests_test_semantic_fragment_sanitize]] → `contains` → [[graphify_tests_test_semantic_fragment_sanitize_test_sanitize_coerces_non_list_values_to_empty]]
- [[graphify_tests_test_semantic_fragment_sanitize]] → `contains` → [[graphify_tests_test_semantic_fragment_sanitize_test_sanitize_drops_non_dict_edge_entries]]
- [[graphify_tests_test_semantic_fragment_sanitize_rationale_1]] → `rationale_for` → [[graphify_tests_test_semantic_fragment_sanitize]]