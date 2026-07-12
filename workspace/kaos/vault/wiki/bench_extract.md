# graphify\tests\bench_extract.py

## Símbolos

- [[graphify_tests_bench_extract]] — code: bench_extract.py
- [[graphify_tests_bench_extract_count_by_ext]] — code: _count_by_ext()
- [[graphify_tests_bench_extract_format_languages]] — code: _format_languages()
- [[graphify_tests_bench_extract_run_extraction]] — code: _run_extraction()
- [[graphify_tests_bench_extract_main]] — code: main()
- [[graphify_tests_bench_extract_rationale_39]] — code: Count files by extension.
- [[graphify_tests_bench_extract_rationale_102]] — code: Run extraction, return (elapsed_seconds, node_count, edge_count).

## Dependências

- [[graphify_tests_bench_extract]] → `imports_from` → [[graphify_graphify_cache]]
- [[graphify_tests_bench_extract_main]] → `calls` → [[graphify_graphify_cache_clear_cache]]
- [[graphify_tests_bench_extract_run_extraction]] → `calls` → [[graphify_graphify_cache_clear_cache]]
- [[graphify_tests_bench_extract]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_bench_extract_run_extraction]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_bench_extract_main]] → `calls` → [[graphify_graphify_extract_collect_files]]
- [[graphify_tests_bench_extract]] → `contains` → [[graphify_tests_bench_extract_count_by_ext]]
- [[graphify_tests_bench_extract]] → `contains` → [[graphify_tests_bench_extract_format_languages]]
- [[graphify_tests_bench_extract]] → `contains` → [[graphify_tests_bench_extract_main]]
- [[graphify_tests_bench_extract]] → `contains` → [[graphify_tests_bench_extract_run_extraction]]
- [[graphify_tests_bench_extract_count_by_ext]] → `references` → [[graphify_tests_bench_extract_py_path]]
- [[graphify_tests_bench_extract_main]] → `calls` → [[graphify_tests_bench_extract_count_by_ext]]
- [[graphify_tests_bench_extract_rationale_39]] → `rationale_for` → [[graphify_tests_bench_extract_count_by_ext]]
- [[graphify_tests_bench_extract_main]] → `calls` → [[graphify_tests_bench_extract_py_path]]
- [[graphify_tests_bench_extract_run_extraction]] → `references` → [[graphify_tests_bench_extract_py_path]]
- [[graphify_tests_bench_extract_main]] → `calls` → [[graphify_tests_bench_extract_format_languages]]
- [[graphify_tests_bench_extract_main]] → `calls` → [[graphify_tests_bench_extract_run_extraction]]
- [[graphify_tests_bench_extract_rationale_102]] → `rationale_for` → [[graphify_tests_bench_extract_run_extraction]]