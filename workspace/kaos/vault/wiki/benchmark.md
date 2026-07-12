# graphify\graphify\benchmark.py

## Símbolos

- [[graphify_graphify_benchmark]] — code: benchmark.py
- [[graphify_graphify_benchmark_safe]] — code: _safe()
- [[graphify_graphify_benchmark_hr]] — code: _hr()
- [[graphify_graphify_benchmark_estimate_tokens]] — code: _estimate_tokens()
- [[graphify_graphify_benchmark_query_subgraph_tokens]] — code: _query_subgraph_tokens()
- [[graphify_graphify_benchmark_run_benchmark]] — code: run_benchmark()
- [[graphify_graphify_benchmark_print_benchmark]] — code: print_benchmark()
- [[graphify_graphify_benchmark_rationale_1]] — code: Token-reduction benchmark - measures how much context graphify saves vs naive fu
- [[graphify_graphify_benchmark_rationale_18]] — code: Return unicode_char if stdout can encode it, else ascii_fallback.      Windows
- [[graphify_graphify_benchmark_rationale_32]] — code: Horizontal rule that survives non-UTF-8 stdout (e.g. Windows cp1252 console).
- [[graphify_graphify_benchmark_rationale_41]] — code: Run BFS from best-matching nodes and return estimated tokens in the subgraph con
- [[graphify_graphify_benchmark_rationale_93]] — code: Measure token reduction: corpus tokens vs graphify query tokens.      Args:
- [[graphify_graphify_benchmark_rationale_142]] — code: Print a human-readable benchmark report.

## Dependências

- [[graphify_graphify_benchmark]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_graphify_benchmark]] → `contains` → [[graphify_graphify_benchmark_estimate_tokens]]
- [[graphify_graphify_benchmark]] → `contains` → [[graphify_graphify_benchmark_hr]]
- [[graphify_graphify_benchmark]] → `contains` → [[graphify_graphify_benchmark_print_benchmark]]
- [[graphify_graphify_benchmark]] → `contains` → [[graphify_graphify_benchmark_query_subgraph_tokens]]
- [[graphify_graphify_benchmark]] → `contains` → [[graphify_graphify_benchmark_run_benchmark]]
- [[graphify_graphify_benchmark]] → `contains` → [[graphify_graphify_benchmark_safe]]
- [[graphify_graphify_benchmark]] → `imports_from` → [[graphify_graphify_paths]]
- [[graphify_graphify_benchmark]] → `imports_from` → [[graphify_graphify_serve]]
- [[graphify_graphify_benchmark_rationale_1]] → `rationale_for` → [[graphify_graphify_benchmark]]
- [[graphify_graphify_benchmark_hr]] → `calls` → [[graphify_graphify_benchmark_safe]]
- [[graphify_graphify_benchmark_print_benchmark]] → `calls` → [[graphify_graphify_benchmark_safe]]
- [[graphify_graphify_benchmark_rationale_18]] → `rationale_for` → [[graphify_graphify_benchmark_safe]]
- [[graphify_graphify_benchmark_print_benchmark]] → `calls` → [[graphify_graphify_benchmark_hr]]
- [[graphify_graphify_benchmark_rationale_32]] → `rationale_for` → [[graphify_graphify_benchmark_hr]]
- [[graphify_graphify_benchmark_query_subgraph_tokens]] → `calls` → [[graphify_graphify_benchmark_estimate_tokens]]
- [[graphify_graphify_benchmark_query_subgraph_tokens]] → `calls` → [[graphify_graphify_build_edge_data]]
- [[graphify_graphify_benchmark_query_subgraph_tokens]] → `calls` → [[graphify_graphify_serve_query_terms]]
- [[graphify_graphify_benchmark_rationale_41]] → `rationale_for` → [[graphify_graphify_benchmark_query_subgraph_tokens]]
- [[graphify_graphify_benchmark_run_benchmark]] → `calls` → [[graphify_graphify_benchmark_query_subgraph_tokens]]
- [[graphify_graphify_benchmark_rationale_93]] → `rationale_for` → [[graphify_graphify_benchmark_run_benchmark]]
- [[graphify_graphify_benchmark_run_benchmark]] → `calls` → [[graphify_graphify_security_check_graph_file_size_cap]]
- [[graphify_graphify_benchmark_rationale_142]] → `rationale_for` → [[graphify_graphify_benchmark_print_benchmark]]