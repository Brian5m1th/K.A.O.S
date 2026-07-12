# graphify\tests\test_merge_graphs_cli.py

## Símbolos

- [[graphify_tests_test_merge_graphs_cli]] — code: test_merge_graphs_cli.py
- [[graphify_tests_test_merge_graphs_cli_run]] — code: _run()
- [[graphify_tests_test_merge_graphs_cli_write]] — code: _write()
- [[graphify_tests_test_merge_graphs_cli_test_merge_graphs_mixed_directed_and_multigraph]] — code: test_merge_graphs_mixed_directed_and_multigraph()
- [[graphify_tests_test_merge_graphs_cli_test_merge_graphs_same_named_repo_dirs_do_not_collapse]] — code: test_merge_graphs_same_named_repo_dirs_do_not_collapse()
- [[graphify_tests_test_merge_graphs_cli_test_distinct_repo_tags_unit]] — code: test_distinct_repo_tags_unit()
- [[graphify_tests_test_merge_graphs_cli_rationale_1]] — code: `graphify merge-graphs` tolerates inputs that disagree on graph type (#1606).

## Dependências

- [[graphify_tests_test_merge_graphs_cli_test_distinct_repo_tags_unit]] → `calls` → [[graphify_graphify_build_distinct_repo_tags]]
- [[graphify_tests_test_merge_graphs_cli]] → `contains` → [[graphify_tests_test_merge_graphs_cli_run]]
- [[graphify_tests_test_merge_graphs_cli]] → `contains` → [[graphify_tests_test_merge_graphs_cli_test_distinct_repo_tags_unit]]
- [[graphify_tests_test_merge_graphs_cli]] → `contains` → [[graphify_tests_test_merge_graphs_cli_test_merge_graphs_mixed_directed_and_multigraph]]
- [[graphify_tests_test_merge_graphs_cli]] → `contains` → [[graphify_tests_test_merge_graphs_cli_test_merge_graphs_same_named_repo_dirs_do_not_collapse]]
- [[graphify_tests_test_merge_graphs_cli]] → `contains` → [[graphify_tests_test_merge_graphs_cli_write]]
- [[graphify_tests_test_merge_graphs_cli_rationale_1]] → `rationale_for` → [[graphify_tests_test_merge_graphs_cli]]
- [[graphify_tests_test_merge_graphs_cli_test_merge_graphs_mixed_directed_and_multigraph]] → `calls` → [[graphify_tests_test_merge_graphs_cli_run]]
- [[graphify_tests_test_merge_graphs_cli_test_merge_graphs_same_named_repo_dirs_do_not_collapse]] → `calls` → [[graphify_tests_test_merge_graphs_cli_run]]
- [[graphify_tests_test_merge_graphs_cli_test_merge_graphs_mixed_directed_and_multigraph]] → `calls` → [[graphify_tests_test_merge_graphs_cli_write]]
- [[graphify_tests_test_merge_graphs_cli_write]] → `references` → [[graphify_tests_test_merge_graphs_cli_py_path]]
- [[graphify_tests_test_merge_graphs_cli_test_distinct_repo_tags_unit]] → `calls` → [[graphify_tests_test_merge_graphs_cli_py_path]]