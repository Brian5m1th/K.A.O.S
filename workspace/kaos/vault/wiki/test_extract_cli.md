# graphify\tests\test_extract_cli.py

## Símbolos

- [[graphify_tests_test_extract_cli]] — code: test_extract_cli.py
- [[graphify_tests_test_extract_cli_make_corpus]] — code: _make_corpus()
- [[graphify_tests_test_extract_cli_test_extract_exits_nonzero_when_all_semantic_chunks_fail]] — code: test_extract_exits_nonzero_when_all_semantic_chunks_fail()
- [[graphify_tests_test_extract_cli_test_extract_succeeds_when_at_least_one_chunk_completes]] — code: test_extract_succeeds_when_at_least_one_chunk_completes()
- [[graphify_tests_test_extract_cli_code_only_corpus]] — code: _code_only_corpus()
- [[graphify_tests_test_extract_cli_clear_backend_keys]] — code: _clear_backend_keys()
- [[graphify_tests_test_extract_cli_test_extract_codeonly_succeeds_without_api_key]] — code: test_extract_codeonly_succeeds_without_api_key()
- [[graphify_tests_test_extract_cli_test_extract_out_keeps_project_root_clean]] — code: test_extract_out_keeps_project_root_clean()
- [[graphify_tests_test_extract_cli_test_extract_without_key_still_errors_when_docs_present]] — code: test_extract_without_key_still_errors_when_docs_present()
- [[graphify_tests_test_extract_cli_test_extract_timing_flag_emits_stage_timings]] — code: test_extract_timing_flag_emits_stage_timings()
- [[graphify_tests_test_extract_cli_rationale_1]] — code: Tests for `graphify extract` CLI dispatch path in graphify.__main__.
- [[graphify_tests_test_extract_cli_rationale_10]] — code: Minimal corpus: one Go code file + one Markdown doc.      Both file types are
- [[graphify_tests_test_extract_cli_rationale_23]] — code: When every semantic chunk errors (e.g. backend SDK not installed),     the CLI
- [[graphify_tests_test_extract_cli_rationale_84]] — code: Sanity counter-test: a successful chunk run keeps exit 0. Confirms the     new
- [[graphify_tests_test_extract_cli_rationale_127]] — code: A corpus with only code — no docs/papers/images.
- [[graphify_tests_test_extract_cli_rationale_136]] — code: Clear every env var that detect_backend() or _get_backend_api_key() reads.
- [[graphify_tests_test_extract_cli_rationale_149]] — code: A code-only corpus must run with no LLM API key.      Regression: graphify ext
- [[graphify_tests_test_extract_cli_rationale_176]] — code: `extract --out DIR` routes every artifact to DIR/graphify-out/ and the     scan
- [[graphify_tests_test_extract_cli_rationale_215]] — code: Key requirement still fires when semantic work is needed.      A corpus with a
- [[graphify_tests_test_extract_cli_rationale_241]] — code: --timing prints per-stage `[graphify timing]` lines to stderr (#1490); omitting

## Dependências

- [[graphify_tests_test_extract_cli]] → `imports` → [[graphify_graphify_main]]
- [[graphify_tests_test_extract_cli]] → `contains` → [[graphify_tests_test_extract_cli_clear_backend_keys]]
- [[graphify_tests_test_extract_cli]] → `contains` → [[graphify_tests_test_extract_cli_code_only_corpus]]
- [[graphify_tests_test_extract_cli]] → `contains` → [[graphify_tests_test_extract_cli_make_corpus]]
- [[graphify_tests_test_extract_cli]] → `contains` → [[graphify_tests_test_extract_cli_test_extract_codeonly_succeeds_without_api_key]]
- [[graphify_tests_test_extract_cli]] → `contains` → [[graphify_tests_test_extract_cli_test_extract_exits_nonzero_when_all_semantic_chunks_fail]]
- [[graphify_tests_test_extract_cli]] → `contains` → [[graphify_tests_test_extract_cli_test_extract_out_keeps_project_root_clean]]
- [[graphify_tests_test_extract_cli]] → `contains` → [[graphify_tests_test_extract_cli_test_extract_succeeds_when_at_least_one_chunk_completes]]
- [[graphify_tests_test_extract_cli]] → `contains` → [[graphify_tests_test_extract_cli_test_extract_timing_flag_emits_stage_timings]]
- [[graphify_tests_test_extract_cli]] → `contains` → [[graphify_tests_test_extract_cli_test_extract_without_key_still_errors_when_docs_present]]
- [[graphify_tests_test_extract_cli_rationale_1]] → `rationale_for` → [[graphify_tests_test_extract_cli]]
- [[graphify_tests_test_extract_cli_rationale_10]] → `rationale_for` → [[graphify_tests_test_extract_cli_make_corpus]]
- [[graphify_tests_test_extract_cli_test_extract_exits_nonzero_when_all_semantic_chunks_fail]] → `calls` → [[graphify_tests_test_extract_cli_make_corpus]]
- [[graphify_tests_test_extract_cli_test_extract_succeeds_when_at_least_one_chunk_completes]] → `calls` → [[graphify_tests_test_extract_cli_make_corpus]]
- [[graphify_tests_test_extract_cli_test_extract_without_key_still_errors_when_docs_present]] → `calls` → [[graphify_tests_test_extract_cli_make_corpus]]
- [[graphify_tests_test_extract_cli_rationale_23]] → `rationale_for` → [[graphify_tests_test_extract_cli_test_extract_exits_nonzero_when_all_semantic_chunks_fail]]
- [[graphify_tests_test_extract_cli_rationale_84]] → `rationale_for` → [[graphify_tests_test_extract_cli_test_extract_succeeds_when_at_least_one_chunk_completes]]
- [[graphify_tests_test_extract_cli_rationale_127]] → `rationale_for` → [[graphify_tests_test_extract_cli_code_only_corpus]]
- [[graphify_tests_test_extract_cli_test_extract_codeonly_succeeds_without_api_key]] → `calls` → [[graphify_tests_test_extract_cli_code_only_corpus]]
- [[graphify_tests_test_extract_cli_test_extract_out_keeps_project_root_clean]] → `calls` → [[graphify_tests_test_extract_cli_code_only_corpus]]
- [[graphify_tests_test_extract_cli_rationale_136]] → `rationale_for` → [[graphify_tests_test_extract_cli_clear_backend_keys]]
- [[graphify_tests_test_extract_cli_test_extract_codeonly_succeeds_without_api_key]] → `calls` → [[graphify_tests_test_extract_cli_clear_backend_keys]]
- [[graphify_tests_test_extract_cli_test_extract_out_keeps_project_root_clean]] → `calls` → [[graphify_tests_test_extract_cli_clear_backend_keys]]
- [[graphify_tests_test_extract_cli_test_extract_without_key_still_errors_when_docs_present]] → `calls` → [[graphify_tests_test_extract_cli_clear_backend_keys]]
- [[graphify_tests_test_extract_cli_rationale_149]] → `rationale_for` → [[graphify_tests_test_extract_cli_test_extract_codeonly_succeeds_without_api_key]]
- [[graphify_tests_test_extract_cli_rationale_176]] → `rationale_for` → [[graphify_tests_test_extract_cli_test_extract_out_keeps_project_root_clean]]
- [[graphify_tests_test_extract_cli_rationale_215]] → `rationale_for` → [[graphify_tests_test_extract_cli_test_extract_without_key_still_errors_when_docs_present]]
- [[graphify_tests_test_extract_cli_rationale_241]] → `rationale_for` → [[graphify_tests_test_extract_cli_test_extract_timing_flag_emits_stage_timings]]