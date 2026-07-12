# graphify\tests\test_affected_cli.py

## Símbolos

- [[graphify_tests_test_affected_cli]] — code: test_affected_cli.py
- [[graphify_tests_test_affected_cli_write_graph]] — code: _write_graph()
- [[graphify_tests_test_affected_cli_test_affected_cli_reverse_traverses_impact_edges]] — code: test_affected_cli_reverse_traverses_impact_edges()
- [[graphify_tests_test_affected_cli_test_affected_cli_relation_filter_limits_reverse_traversal]] — code: test_affected_cli_relation_filter_limits_reverse_traversal()
- [[graphify_tests_test_affected_cli_test_affected_cli_forces_directed_on_undirected_graph]] — code: test_affected_cli_forces_directed_on_undirected_graph()
- [[graphify_tests_test_affected_cli_test_affected_cli_loads_edges_keyed_graph]] — code: test_affected_cli_loads_edges_keyed_graph()
- [[graphify_tests_test_affected_cli_test_resolve_seed_bare_name_matches_callable_label]] — code: test_resolve_seed_bare_name_matches_callable_label()
- [[graphify_tests_test_affected_cli_test_resolve_seed_decorated_query_matches_bare_label]] — code: test_resolve_seed_decorated_query_matches_bare_label()
- [[graphify_tests_test_affected_cli_test_resolve_seed_matches_unicode_normalized_label]] — code: test_resolve_seed_matches_unicode_normalized_label()
- [[graphify_tests_test_affected_cli_test_resolve_seed_preserves_distinct_accents]] — code: test_resolve_seed_preserves_distinct_accents()
- [[graphify_tests_test_affected_cli_test_resolve_seed_bare_name_tie_still_returns_none]] — code: test_resolve_seed_bare_name_tie_still_returns_none()
- [[graphify_tests_test_affected_cli_test_resolve_seed_source_file_path_prefers_file_level_node]] — code: test_resolve_seed_source_file_path_prefers_file_level_node()
- [[graphify_tests_test_affected_cli_test_resolve_seed_source_file_trailing_slash_parity]] — code: test_resolve_seed_source_file_trailing_slash_parity()
- [[graphify_tests_test_affected_cli_test_resolve_seed_source_file_ambiguous_no_file_node_returns_none]] — code: test_resolve_seed_source_file_ambiguous_no_file_node_returns_none()
- [[graphify_tests_test_affected_cli_test_affected_cli_source_file_path_uses_file_level_node]] — code: test_affected_cli_source_file_path_uses_file_level_node()
- [[graphify_tests_test_affected_cli_rationale_64]] — code: A graph persisted with directed=false must still recover caller->callee     dir
- [[graphify_tests_test_affected_cli_rationale_98]] — code: graphify's `extract` writes graph.json with an "edges" key (not networkx's
- [[graphify_tests_test_affected_cli_rationale_201]] — code: A trailing path separator must not change the match (parity with explain's
- [[graphify_tests_test_affected_cli_rationale_214]] — code: Several nodes share a source_file but none is the L1 file node and none's     b

## Dependências

- [[graphify_tests_test_affected_cli]] → `imports` → [[graphify_graphify_main]]
- [[graphify_tests_test_affected_cli_test_resolve_seed_bare_name_matches_callable_label]] → `calls` → [[graphify_graphify_affected_resolve_seed]]
- [[graphify_tests_test_affected_cli_test_resolve_seed_bare_name_tie_still_returns_none]] → `calls` → [[graphify_graphify_affected_resolve_seed]]
- [[graphify_tests_test_affected_cli_test_resolve_seed_decorated_query_matches_bare_label]] → `calls` → [[graphify_graphify_affected_resolve_seed]]
- [[graphify_tests_test_affected_cli_test_resolve_seed_matches_unicode_normalized_label]] → `calls` → [[graphify_graphify_affected_resolve_seed]]
- [[graphify_tests_test_affected_cli_test_resolve_seed_preserves_distinct_accents]] → `calls` → [[graphify_graphify_affected_resolve_seed]]
- [[graphify_tests_test_affected_cli_test_resolve_seed_source_file_ambiguous_no_file_node_returns_none]] → `calls` → [[graphify_graphify_affected_resolve_seed]]
- [[graphify_tests_test_affected_cli_test_resolve_seed_source_file_path_prefers_file_level_node]] → `calls` → [[graphify_graphify_affected_resolve_seed]]
- [[graphify_tests_test_affected_cli_test_resolve_seed_source_file_trailing_slash_parity]] → `calls` → [[graphify_graphify_affected_resolve_seed]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_affected_cli_forces_directed_on_undirected_graph]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_affected_cli_loads_edges_keyed_graph]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_affected_cli_relation_filter_limits_reverse_traversal]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_affected_cli_reverse_traverses_impact_edges]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_affected_cli_source_file_path_uses_file_level_node]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_resolve_seed_bare_name_matches_callable_label]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_resolve_seed_bare_name_tie_still_returns_none]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_resolve_seed_decorated_query_matches_bare_label]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_resolve_seed_matches_unicode_normalized_label]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_resolve_seed_preserves_distinct_accents]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_resolve_seed_source_file_ambiguous_no_file_node_returns_none]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_resolve_seed_source_file_path_prefers_file_level_node]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_test_resolve_seed_source_file_trailing_slash_parity]]
- [[graphify_tests_test_affected_cli]] → `contains` → [[graphify_tests_test_affected_cli_write_graph]]
- [[graphify_tests_test_affected_cli_test_affected_cli_relation_filter_limits_reverse_traversal]] → `calls` → [[graphify_tests_test_affected_cli_write_graph]]
- [[graphify_tests_test_affected_cli_test_affected_cli_reverse_traverses_impact_edges]] → `calls` → [[graphify_tests_test_affected_cli_write_graph]]
- [[graphify_tests_test_affected_cli_rationale_64]] → `rationale_for` → [[graphify_tests_test_affected_cli_test_affected_cli_forces_directed_on_undirected_graph]]
- [[graphify_tests_test_affected_cli_rationale_98]] → `rationale_for` → [[graphify_tests_test_affected_cli_test_affected_cli_loads_edges_keyed_graph]]
- [[graphify_tests_test_affected_cli_rationale_201]] → `rationale_for` → [[graphify_tests_test_affected_cli_test_resolve_seed_source_file_trailing_slash_parity]]
- [[graphify_tests_test_affected_cli_rationale_214]] → `rationale_for` → [[graphify_tests_test_affected_cli_test_resolve_seed_source_file_ambiguous_no_file_node_returns_none]]