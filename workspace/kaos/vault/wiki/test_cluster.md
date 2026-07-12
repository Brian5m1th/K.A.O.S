# graphify\tests\test_cluster.py

## Símbolos

- [[graphify_tests_test_cluster]] — code: test_cluster.py
- [[graphify_tests_test_cluster_make_graph]] — code: make_graph()
- [[graphify_tests_test_cluster_test_cluster_returns_dict]] — code: test_cluster_returns_dict()
- [[graphify_tests_test_cluster_test_cluster_covers_all_nodes]] — code: test_cluster_covers_all_nodes()
- [[graphify_tests_test_cluster_test_cohesion_score_complete_graph]] — code: test_cohesion_score_complete_graph()
- [[graphify_tests_test_cluster_test_cohesion_score_single_node]] — code: test_cohesion_score_single_node()
- [[graphify_tests_test_cluster_test_cohesion_score_disconnected]] — code: test_cohesion_score_disconnected()
- [[graphify_tests_test_cluster_test_cohesion_score_range]] — code: test_cohesion_score_range()
- [[graphify_tests_test_cluster_test_score_all_keys_match_communities]] — code: test_score_all_keys_match_communities()
- [[graphify_tests_test_cluster_test_cluster_does_not_write_to_stdout]] — code: test_cluster_does_not_write_to_stdout()
- [[graphify_tests_test_cluster_test_cluster_does_not_write_to_stderr]] — code: test_cluster_does_not_write_to_stderr()
- [[graphify_tests_test_cluster_test_remap_communities_to_previous_reuses_old_ids]] — code: test_remap_communities_to_previous_reuses_old_ids()
- [[graphify_tests_test_cluster_test_remap_communities_to_previous_assigns_deterministic_new_ids]] — code: test_remap_communities_to_previous_assigns_deterministic_new_ids()
- [[graphify_tests_test_cluster_rationale_57]] — code: Clustering should not emit ANSI escape codes or other output.      graspologic
- [[graphify_tests_test_cluster_rationale_70]] — code: Same as above but for stderr — ANSI codes can go to either stream.

## Dependências

- [[graphify_tests_test_cluster]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_tests_test_cluster]] → `imports_from` → [[graphify_graphify_cluster]]
- [[graphify_tests_test_cluster_test_remap_communities_to_previous_assigns_deterministic_new_ids]] → `calls` → [[graphify_graphify_cluster_remap_communities_to_previous]]
- [[graphify_tests_test_cluster_test_remap_communities_to_previous_reuses_old_ids]] → `calls` → [[graphify_graphify_cluster_remap_communities_to_previous]]
- [[graphify_tests_test_cluster]] → `contains` → [[graphify_tests_test_cluster_make_graph]]
- [[graphify_tests_test_cluster]] → `contains` → [[graphify_tests_test_cluster_test_cluster_covers_all_nodes]]
- [[graphify_tests_test_cluster]] → `contains` → [[graphify_tests_test_cluster_test_cluster_does_not_write_to_stderr]]
- [[graphify_tests_test_cluster]] → `contains` → [[graphify_tests_test_cluster_test_cluster_does_not_write_to_stdout]]
- [[graphify_tests_test_cluster]] → `contains` → [[graphify_tests_test_cluster_test_cluster_returns_dict]]
- [[graphify_tests_test_cluster]] → `contains` → [[graphify_tests_test_cluster_test_cohesion_score_complete_graph]]
- [[graphify_tests_test_cluster]] → `contains` → [[graphify_tests_test_cluster_test_cohesion_score_disconnected]]
- [[graphify_tests_test_cluster]] → `contains` → [[graphify_tests_test_cluster_test_cohesion_score_range]]
- [[graphify_tests_test_cluster]] → `contains` → [[graphify_tests_test_cluster_test_cohesion_score_single_node]]
- [[graphify_tests_test_cluster]] → `contains` → [[graphify_tests_test_cluster_test_remap_communities_to_previous_assigns_deterministic_new_ids]]
- [[graphify_tests_test_cluster]] → `contains` → [[graphify_tests_test_cluster_test_remap_communities_to_previous_reuses_old_ids]]
- [[graphify_tests_test_cluster]] → `contains` → [[graphify_tests_test_cluster_test_score_all_keys_match_communities]]
- [[graphify_tests_test_cluster_test_cluster_covers_all_nodes]] → `calls` → [[graphify_tests_test_cluster_make_graph]]
- [[graphify_tests_test_cluster_test_cluster_does_not_write_to_stderr]] → `calls` → [[graphify_tests_test_cluster_make_graph]]
- [[graphify_tests_test_cluster_test_cluster_does_not_write_to_stdout]] → `calls` → [[graphify_tests_test_cluster_make_graph]]
- [[graphify_tests_test_cluster_test_cluster_returns_dict]] → `calls` → [[graphify_tests_test_cluster_make_graph]]
- [[graphify_tests_test_cluster_test_cohesion_score_range]] → `calls` → [[graphify_tests_test_cluster_make_graph]]
- [[graphify_tests_test_cluster_test_score_all_keys_match_communities]] → `calls` → [[graphify_tests_test_cluster_make_graph]]
- [[graphify_tests_test_cluster_rationale_57]] → `rationale_for` → [[graphify_tests_test_cluster_test_cluster_does_not_write_to_stdout]]
- [[graphify_tests_test_cluster_rationale_70]] → `rationale_for` → [[graphify_tests_test_cluster_test_cluster_does_not_write_to_stderr]]