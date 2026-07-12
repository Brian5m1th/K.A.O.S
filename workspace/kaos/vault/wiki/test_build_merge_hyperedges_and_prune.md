# graphify\tests\test_build_merge_hyperedges_and_prune.py

## Símbolos

- [[graphify_tests_test_build_merge_hyperedges_and_prune]] — code: test_build_merge_hyperedges_and_prune.py
- [[graphify_tests_test_build_merge_hyperedges_and_prune_write_graph]] — code: _write_graph()
- [[graphify_tests_test_build_merge_hyperedges_and_prune_he_ids]] — code: _he_ids()
- [[graphify_tests_test_build_merge_hyperedges_and_prune_seed_two_file_graph]] — code: _seed_two_file_graph()
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_update_preserves_hyperedges_of_unchanged_files]] — code: test_update_preserves_hyperedges_of_unchanged_files()
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_update_without_root_still_preserves_hyperedges]] — code: test_update_without_root_still_preserves_hyperedges()
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_deleted_file_hyperedges_are_pruned]] — code: test_deleted_file_hyperedges_are_pruned()
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_without_root_removes_ghost_nodes_via_grandparent_fallback]] — code: test_prune_without_root_removes_ghost_nodes_via_grandparent_fallback()
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_without_root_uses_graphify_root_marker]] — code: test_prune_without_root_uses_graphify_root_marker()
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_matches_across_symlinked_root]] — code: test_prune_matches_across_symlinked_root()
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_reextracted_file_in_prune_sources_is_not_deleted]] — code: test_reextracted_file_in_prune_sources_is_not_deleted()
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_genuine_deletion_still_prunes]] — code: test_genuine_deletion_still_prunes()
- [[graphify_tests_test_build_merge_hyperedges_and_prune_rationale_1]] — code: Incremental --update: hyperedge preservation (#1574) and root-less prune (#1571)
- [[graphify_tests_test_build_merge_hyperedges_and_prune_rationale_25]] — code: Write a graph.json in the shape to_json emits (top-level hyperedges).
- [[graphify_tests_test_build_merge_hyperedges_and_prune_rationale_72]] — code: The runbook omits root; the fallback root must not break preservation.
- [[graphify_tests_test_build_merge_hyperedges_and_prune_rationale_134]] — code: A symlinked scan root (macOS /var -> /private/var, symlinked home/worktree)
- [[graphify_tests_test_build_merge_hyperedges_and_prune_rationale_155]] — code: #1796: a file present in BOTH new_chunks (re-extracted) and prune_sources     m
- [[graphify_tests_test_build_merge_hyperedges_and_prune_rationale_185]] — code: #1796 guard must not break real deletions: a file in prune_sources but NOT

## Dependências

- [[graphify_tests_test_build_merge_hyperedges_and_prune]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_without_root_uses_graphify_root_marker]] → `calls` → [[graphify_graphify_build_infer_merge_root]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_deleted_file_hyperedges_are_pruned]] → `calls` → [[graphify_graphify_build_build_merge]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_genuine_deletion_still_prunes]] → `calls` → [[graphify_graphify_build_build_merge]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_matches_across_symlinked_root]] → `calls` → [[graphify_graphify_build_build_merge]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_without_root_removes_ghost_nodes_via_grandparent_fallback]] → `calls` → [[graphify_graphify_build_build_merge]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_without_root_uses_graphify_root_marker]] → `calls` → [[graphify_graphify_build_build_merge]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_reextracted_file_in_prune_sources_is_not_deleted]] → `calls` → [[graphify_graphify_build_build_merge]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_update_preserves_hyperedges_of_unchanged_files]] → `calls` → [[graphify_graphify_build_build_merge]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_update_without_root_still_preserves_hyperedges]] → `calls` → [[graphify_graphify_build_build_merge]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune]] → `contains` → [[graphify_tests_test_build_merge_hyperedges_and_prune_he_ids]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune]] → `contains` → [[graphify_tests_test_build_merge_hyperedges_and_prune_seed_two_file_graph]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune]] → `contains` → [[graphify_tests_test_build_merge_hyperedges_and_prune_test_deleted_file_hyperedges_are_pruned]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune]] → `contains` → [[graphify_tests_test_build_merge_hyperedges_and_prune_test_genuine_deletion_still_prunes]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune]] → `contains` → [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_matches_across_symlinked_root]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune]] → `contains` → [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_without_root_removes_ghost_nodes_via_grandparent_fallback]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune]] → `contains` → [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_without_root_uses_graphify_root_marker]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune]] → `contains` → [[graphify_tests_test_build_merge_hyperedges_and_prune_test_reextracted_file_in_prune_sources_is_not_deleted]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune]] → `contains` → [[graphify_tests_test_build_merge_hyperedges_and_prune_test_update_preserves_hyperedges_of_unchanged_files]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune]] → `contains` → [[graphify_tests_test_build_merge_hyperedges_and_prune_test_update_without_root_still_preserves_hyperedges]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune]] → `contains` → [[graphify_tests_test_build_merge_hyperedges_and_prune_write_graph]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_rationale_1]] → `rationale_for` → [[graphify_tests_test_build_merge_hyperedges_and_prune]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_rationale_25]] → `rationale_for` → [[graphify_tests_test_build_merge_hyperedges_and_prune_write_graph]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_seed_two_file_graph]] → `calls` → [[graphify_tests_test_build_merge_hyperedges_and_prune_write_graph]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_genuine_deletion_still_prunes]] → `calls` → [[graphify_tests_test_build_merge_hyperedges_and_prune_write_graph]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_matches_across_symlinked_root]] → `calls` → [[graphify_tests_test_build_merge_hyperedges_and_prune_write_graph]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_without_root_removes_ghost_nodes_via_grandparent_fallback]] → `calls` → [[graphify_tests_test_build_merge_hyperedges_and_prune_write_graph]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_without_root_uses_graphify_root_marker]] → `calls` → [[graphify_tests_test_build_merge_hyperedges_and_prune_write_graph]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_reextracted_file_in_prune_sources_is_not_deleted]] → `calls` → [[graphify_tests_test_build_merge_hyperedges_and_prune_write_graph]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_write_graph]] → `references` → [[graphify_tests_test_build_merge_hyperedges_and_prune_py_path]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_deleted_file_hyperedges_are_pruned]] → `calls` → [[graphify_tests_test_build_merge_hyperedges_and_prune_he_ids]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_update_preserves_hyperedges_of_unchanged_files]] → `calls` → [[graphify_tests_test_build_merge_hyperedges_and_prune_he_ids]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_update_without_root_still_preserves_hyperedges]] → `calls` → [[graphify_tests_test_build_merge_hyperedges_and_prune_he_ids]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_deleted_file_hyperedges_are_pruned]] → `calls` → [[graphify_tests_test_build_merge_hyperedges_and_prune_seed_two_file_graph]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_update_preserves_hyperedges_of_unchanged_files]] → `calls` → [[graphify_tests_test_build_merge_hyperedges_and_prune_seed_two_file_graph]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_test_update_without_root_still_preserves_hyperedges]] → `calls` → [[graphify_tests_test_build_merge_hyperedges_and_prune_seed_two_file_graph]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_rationale_72]] → `rationale_for` → [[graphify_tests_test_build_merge_hyperedges_and_prune_test_update_without_root_still_preserves_hyperedges]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_rationale_134]] → `rationale_for` → [[graphify_tests_test_build_merge_hyperedges_and_prune_test_prune_matches_across_symlinked_root]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_rationale_155]] → `rationale_for` → [[graphify_tests_test_build_merge_hyperedges_and_prune_test_reextracted_file_in_prune_sources_is_not_deleted]]
- [[graphify_tests_test_build_merge_hyperedges_and_prune_rationale_185]] → `rationale_for` → [[graphify_tests_test_build_merge_hyperedges_and_prune_test_genuine_deletion_still_prunes]]