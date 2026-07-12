# graphify\tests\test_incremental.py

## Símbolos

- [[graphify_tests_test_incremental]] — code: test_incremental.py
- [[graphify_tests_test_incremental_run]] — code: _run()
- [[graphify_tests_test_incremental_make_docs_corpus]] — code: _make_docs_corpus()
- [[graphify_tests_test_incremental_test_manifest_written_after_extract]] — code: test_manifest_written_after_extract()
- [[graphify_tests_test_incremental_test_incremental_mode_detected_via_manifest]] — code: test_incremental_mode_detected_via_manifest()
- [[graphify_tests_test_incremental_test_no_incremental_without_manifest]] — code: test_no_incremental_without_manifest()
- [[graphify_tests_test_incremental_test_extract_no_cluster_incremental_noop_preserves_existing_graph]] — code: test_extract_no_cluster_incremental_noop_preserves_existing_graph()
- [[graphify_tests_test_incremental_edges]] — code: _edges()
- [[graphify_tests_test_incremental_test_update_prunes_a_removed_imports_edge]] — code: test_update_prunes_a_removed_imports_edge()
- [[graphify_tests_test_incremental_rationale_1]] — code: Integration tests for incremental graphify extract behavior.
- [[graphify_tests_test_incremental_rationale_44]] — code: After a full extract run, manifest.json must exist (or run fails before writing
- [[graphify_tests_test_incremental_rationale_55]] — code: If manifest.json + graph.json exist, incremental mode message is shown.
- [[graphify_tests_test_incremental_rationale_67]] — code: Without manifest.json, full scan message is shown (not incremental).
- [[graphify_tests_test_incremental_rationale_78]] — code: #1347: no-op incremental no-cluster extract must not overwrite graph.json.
- [[graphify_tests_test_incremental_rationale_107]] — code: #1521: when an import is deleted from a file, `graphify update` must prune

## Dependências

- [[graphify_tests_test_incremental]] → `contains` → [[graphify_tests_test_incremental_edges]]
- [[graphify_tests_test_incremental]] → `contains` → [[graphify_tests_test_incremental_make_docs_corpus]]
- [[graphify_tests_test_incremental]] → `contains` → [[graphify_tests_test_incremental_run]]
- [[graphify_tests_test_incremental]] → `contains` → [[graphify_tests_test_incremental_test_extract_no_cluster_incremental_noop_preserves_existing_graph]]
- [[graphify_tests_test_incremental]] → `contains` → [[graphify_tests_test_incremental_test_incremental_mode_detected_via_manifest]]
- [[graphify_tests_test_incremental]] → `contains` → [[graphify_tests_test_incremental_test_manifest_written_after_extract]]
- [[graphify_tests_test_incremental]] → `contains` → [[graphify_tests_test_incremental_test_no_incremental_without_manifest]]
- [[graphify_tests_test_incremental]] → `contains` → [[graphify_tests_test_incremental_test_update_prunes_a_removed_imports_edge]]
- [[graphify_tests_test_incremental_rationale_1]] → `rationale_for` → [[graphify_tests_test_incremental]]
- [[graphify_tests_test_incremental_run]] → `references` → [[graphify_tests_test_incremental_py_completedprocess]]
- [[graphify_tests_test_incremental_run]] → `references` → [[graphify_tests_test_incremental_py_path]]
- [[graphify_tests_test_incremental_test_extract_no_cluster_incremental_noop_preserves_existing_graph]] → `calls` → [[graphify_tests_test_incremental_run]]
- [[graphify_tests_test_incremental_test_incremental_mode_detected_via_manifest]] → `calls` → [[graphify_tests_test_incremental_run]]
- [[graphify_tests_test_incremental_test_manifest_written_after_extract]] → `calls` → [[graphify_tests_test_incremental_run]]
- [[graphify_tests_test_incremental_test_no_incremental_without_manifest]] → `calls` → [[graphify_tests_test_incremental_run]]
- [[graphify_tests_test_incremental_test_update_prunes_a_removed_imports_edge]] → `calls` → [[graphify_tests_test_incremental_run]]
- [[graphify_tests_test_incremental_edges]] → `references` → [[graphify_tests_test_incremental_py_path]]
- [[graphify_tests_test_incremental_make_docs_corpus]] → `references` → [[graphify_tests_test_incremental_py_path]]
- [[graphify_tests_test_incremental_test_incremental_mode_detected_via_manifest]] → `calls` → [[graphify_tests_test_incremental_make_docs_corpus]]
- [[graphify_tests_test_incremental_test_manifest_written_after_extract]] → `calls` → [[graphify_tests_test_incremental_make_docs_corpus]]
- [[graphify_tests_test_incremental_test_no_incremental_without_manifest]] → `calls` → [[graphify_tests_test_incremental_make_docs_corpus]]
- [[graphify_tests_test_incremental_rationale_44]] → `rationale_for` → [[graphify_tests_test_incremental_test_manifest_written_after_extract]]
- [[graphify_tests_test_incremental_rationale_55]] → `rationale_for` → [[graphify_tests_test_incremental_test_incremental_mode_detected_via_manifest]]
- [[graphify_tests_test_incremental_rationale_67]] → `rationale_for` → [[graphify_tests_test_incremental_test_no_incremental_without_manifest]]
- [[graphify_tests_test_incremental_rationale_78]] → `rationale_for` → [[graphify_tests_test_incremental_test_extract_no_cluster_incremental_noop_preserves_existing_graph]]
- [[graphify_tests_test_incremental_test_update_prunes_a_removed_imports_edge]] → `calls` → [[graphify_tests_test_incremental_edges]]
- [[graphify_tests_test_incremental_rationale_107]] → `rationale_for` → [[graphify_tests_test_incremental_test_update_prunes_a_removed_imports_edge]]