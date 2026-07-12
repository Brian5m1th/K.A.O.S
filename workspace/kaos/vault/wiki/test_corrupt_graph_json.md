# graphify\tests\test_corrupt_graph_json.py

## Símbolos

- [[graphify_tests_test_corrupt_graph_json]] — code: test_corrupt_graph_json.py
- [[graphify_tests_test_corrupt_graph_json_corrupt]] — code: _corrupt()
- [[graphify_tests_test_corrupt_graph_json_test_build_merge_corrupt_graph_raises_runtimeerror]] — code: test_build_merge_corrupt_graph_raises_runtimeerror()
- [[graphify_tests_test_corrupt_graph_json_test_affected_load_graph_corrupt_raises_runtimeerror]] — code: test_affected_load_graph_corrupt_raises_runtimeerror()
- [[graphify_tests_test_corrupt_graph_json_test_diagnostics_read_corrupt_raises_runtimeerror]] — code: test_diagnostics_read_corrupt_raises_runtimeerror()
- [[graphify_tests_test_corrupt_graph_json_test_valid_graph_still_loads]] — code: test_valid_graph_still_loads()
- [[graphify_tests_test_corrupt_graph_json_rationale_1]] — code: Corrupt graph.json produces an actionable error, not a raw traceback (#1536/#153
- [[graphify_tests_test_corrupt_graph_json_rationale_44]] — code: Happy path unchanged: a well-formed graph.json loads without raising.

## Dependências

- [[graphify_tests_test_corrupt_graph_json]] → `imports_from` → [[graphify_graphify_affected]]
- [[graphify_tests_test_corrupt_graph_json]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_tests_test_corrupt_graph_json_test_build_merge_corrupt_graph_raises_runtimeerror]] → `calls` → [[graphify_graphify_build_build_merge]]
- [[graphify_tests_test_corrupt_graph_json_test_valid_graph_still_loads]] → `calls` → [[graphify_graphify_build_build_merge]]
- [[graphify_tests_test_corrupt_graph_json]] → `imports_from` → [[graphify_graphify_diagnostics]]
- [[graphify_tests_test_corrupt_graph_json_test_diagnostics_read_corrupt_raises_runtimeerror]] → `calls` → [[graphify_graphify_diagnostics_read_json_file]]
- [[graphify_tests_test_corrupt_graph_json_test_valid_graph_still_loads]] → `calls` → [[graphify_graphify_diagnostics_read_json_file]]
- [[graphify_tests_test_corrupt_graph_json]] → `contains` → [[graphify_tests_test_corrupt_graph_json_corrupt]]
- [[graphify_tests_test_corrupt_graph_json]] → `contains` → [[graphify_tests_test_corrupt_graph_json_test_affected_load_graph_corrupt_raises_runtimeerror]]
- [[graphify_tests_test_corrupt_graph_json]] → `contains` → [[graphify_tests_test_corrupt_graph_json_test_build_merge_corrupt_graph_raises_runtimeerror]]
- [[graphify_tests_test_corrupt_graph_json]] → `contains` → [[graphify_tests_test_corrupt_graph_json_test_diagnostics_read_corrupt_raises_runtimeerror]]
- [[graphify_tests_test_corrupt_graph_json]] → `contains` → [[graphify_tests_test_corrupt_graph_json_test_valid_graph_still_loads]]
- [[graphify_tests_test_corrupt_graph_json_rationale_1]] → `rationale_for` → [[graphify_tests_test_corrupt_graph_json]]
- [[graphify_tests_test_corrupt_graph_json_test_affected_load_graph_corrupt_raises_runtimeerror]] → `calls` → [[graphify_tests_test_corrupt_graph_json_corrupt]]
- [[graphify_tests_test_corrupt_graph_json_test_build_merge_corrupt_graph_raises_runtimeerror]] → `calls` → [[graphify_tests_test_corrupt_graph_json_corrupt]]
- [[graphify_tests_test_corrupt_graph_json_test_diagnostics_read_corrupt_raises_runtimeerror]] → `calls` → [[graphify_tests_test_corrupt_graph_json_corrupt]]
- [[graphify_tests_test_corrupt_graph_json_rationale_44]] → `rationale_for` → [[graphify_tests_test_corrupt_graph_json_test_valid_graph_still_loads]]