# graphify\tests\test_charmap_encoding.py

## Símbolos

- [[graphify_tests_test_charmap_encoding]] — code: test_charmap_encoding.py
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding]] — code: TestSubprocessEncoding
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding_make_completed]] — code: ._make_completed()
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_subprocess_called_with_utf8_encoding]] — code: .test_subprocess_called_with_utf8_encoding()
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_subprocess_does_not_use_text_true_without_encoding]] — code: .test_subprocess_does_not_use_text_true_without_encoding()
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_unicode_chars_survive_subprocess_roundtrip]] — code: .test_unicode_chars_survive_subprocess_roundtrip()
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_call_llm_claude_cli_subprocess_encoding]] — code: .test_call_llm_claude_cli_subprocess_encoding()
- [[graphify_tests_test_charmap_encoding_testloudchunkfailure]] — code: TestLoudChunkFailure
- [[graphify_tests_test_charmap_encoding_testloudchunkfailure_test_failure_count_in_merged_result]] — code: .test_failure_count_in_merged_result()
- [[graphify_tests_test_charmap_encoding_testloudchunkfailure_test_summary_printed_when_chunks_fail]] — code: .test_summary_printed_when_chunks_fail()
- [[graphify_tests_test_charmap_encoding_testloudchunkfailure_test_no_false_alarm_when_all_chunks_succeed]] — code: .test_no_false_alarm_when_all_chunks_succeed()
- [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation]] — code: TestSubstitutionValidation
- [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation_test_read_files_produces_utf8_safe_prompt]] — code: .test_read_files_produces_utf8_safe_prompt()
- [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation_test_cp1252_would_fail_but_utf8_succeeds]] — code: .test_cp1252_would_fail_but_utf8_succeeds()
- [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation_test_subprocess_encoding_kwarg_in_extract_files_direct]] — code: .test_subprocess_encoding_kwarg_in_extract_files_direct()
- [[graphify_tests_test_charmap_encoding_rationale_1]] — code: Regression tests for UnicodeEncodeError on Windows cp1252 console.  On Windows
- [[graphify_tests_test_charmap_encoding_rationale_58]] — code: _call_claude_cli must pass encoding="utf-8" to subprocess.run so that     non-A
- [[graphify_tests_test_charmap_encoding_rationale_64]] — code: Build a mock CompletedProcess with a valid JSON envelope.
- [[graphify_tests_test_charmap_encoding_rationale_68]] — code: subprocess.run must be invoked with encoding='utf-8'.
- [[graphify_tests_test_charmap_encoding_rationale_81]] — code: text=True without encoding= relies on the locale codec (cp1252 on Windows).
- [[graphify_tests_test_charmap_encoding_rationale_106]] — code: Writing a file with → ✅ ≥ then passing its content through         _call_claude
- [[graphify_tests_test_charmap_encoding_rationale_123]] — code: _call_llm with backend='claude-cli' must also use encoding='utf-8'.
- [[graphify_tests_test_charmap_encoding_rationale_142]] — code: extract_corpus_parallel must surface chunk failures loudly — either via     non
- [[graphify_tests_test_charmap_encoding_rationale_148]] — code: When chunks fail, extract_corpus_parallel must record failed_chunks > 0
- [[graphify_tests_test_charmap_encoding_rationale_170]] — code: A summary line must appear on stderr when ≥1 chunk fails.
- [[graphify_tests_test_charmap_encoding_rationale_192]] — code: When all chunks succeed, failed_chunks must be 0 and no failure         summary
- [[graphify_tests_test_charmap_encoding_rationale_221]] — code: Exercises the same code path as the rsl-siege-manager reproduction     without
- [[graphify_tests_test_charmap_encoding_rationale_239]] — code: _read_files must return a string that encodes cleanly to UTF-8.
- [[graphify_tests_test_charmap_encoding_rationale_251]] — code: Demonstrate the exact failure mode that is now fixed.          The prompt stri
- [[graphify_tests_test_charmap_encoding_rationale_285]] — code: End-to-end path: write unicode file → extract_files_direct → subprocess.

## Dependências

- [[graphify_tests_test_charmap_encoding]] → `contains` → [[graphify_tests_test_charmap_encoding_testloudchunkfailure]]
- [[graphify_tests_test_charmap_encoding]] → `contains` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding]]
- [[graphify_tests_test_charmap_encoding]] → `contains` → [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation]]
- [[graphify_tests_test_charmap_encoding_rationale_1]] → `rationale_for` → [[graphify_tests_test_charmap_encoding]]
- [[graphify_tests_test_charmap_encoding_rationale_58]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding]]
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding]] → `method` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_make_completed]]
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding]] → `method` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_call_llm_claude_cli_subprocess_encoding]]
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding]] → `method` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_subprocess_called_with_utf8_encoding]]
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding]] → `method` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_subprocess_does_not_use_text_true_without_encoding]]
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding]] → `method` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_unicode_chars_survive_subprocess_roundtrip]]
- [[graphify_tests_test_charmap_encoding_rationale_64]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_make_completed]]
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_subprocess_called_with_utf8_encoding]] → `calls` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_make_completed]]
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_subprocess_does_not_use_text_true_without_encoding]] → `calls` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_make_completed]]
- [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_unicode_chars_survive_subprocess_roundtrip]] → `calls` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_make_completed]]
- [[graphify_tests_test_charmap_encoding_rationale_68]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_subprocess_called_with_utf8_encoding]]
- [[graphify_tests_test_charmap_encoding_rationale_81]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_subprocess_does_not_use_text_true_without_encoding]]
- [[graphify_tests_test_charmap_encoding_rationale_106]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_unicode_chars_survive_subprocess_roundtrip]]
- [[graphify_tests_test_charmap_encoding_rationale_123]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testsubprocessencoding_test_call_llm_claude_cli_subprocess_encoding]]
- [[graphify_tests_test_charmap_encoding_rationale_142]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testloudchunkfailure]]
- [[graphify_tests_test_charmap_encoding_testloudchunkfailure]] → `method` → [[graphify_tests_test_charmap_encoding_testloudchunkfailure_test_failure_count_in_merged_result]]
- [[graphify_tests_test_charmap_encoding_testloudchunkfailure]] → `method` → [[graphify_tests_test_charmap_encoding_testloudchunkfailure_test_no_false_alarm_when_all_chunks_succeed]]
- [[graphify_tests_test_charmap_encoding_testloudchunkfailure]] → `method` → [[graphify_tests_test_charmap_encoding_testloudchunkfailure_test_summary_printed_when_chunks_fail]]
- [[graphify_tests_test_charmap_encoding_rationale_148]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testloudchunkfailure_test_failure_count_in_merged_result]]
- [[graphify_tests_test_charmap_encoding_rationale_170]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testloudchunkfailure_test_summary_printed_when_chunks_fail]]
- [[graphify_tests_test_charmap_encoding_rationale_192]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testloudchunkfailure_test_no_false_alarm_when_all_chunks_succeed]]
- [[graphify_tests_test_charmap_encoding_rationale_221]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation]]
- [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation]] → `method` → [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation_test_cp1252_would_fail_but_utf8_succeeds]]
- [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation]] → `method` → [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation_test_read_files_produces_utf8_safe_prompt]]
- [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation]] → `method` → [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation_test_subprocess_encoding_kwarg_in_extract_files_direct]]
- [[graphify_tests_test_charmap_encoding_rationale_239]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation_test_read_files_produces_utf8_safe_prompt]]
- [[graphify_tests_test_charmap_encoding_rationale_251]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation_test_cp1252_would_fail_but_utf8_succeeds]]
- [[graphify_tests_test_charmap_encoding_rationale_285]] → `rationale_for` → [[graphify_tests_test_charmap_encoding_testsubstitutionvalidation_test_subprocess_encoding_kwarg_in_extract_files_direct]]