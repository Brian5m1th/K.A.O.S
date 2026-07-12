# graphify\tests\test_office_limits.py

## Símbolos

- [[graphify_tests_test_office_limits]] — code: test_office_limits.py
- [[graphify_tests_test_office_limits_write_zip]] — code: _write_zip()
- [[graphify_tests_test_office_limits_test_file_within_size_cap]] — code: test_file_within_size_cap()
- [[graphify_tests_test_office_limits_test_zip_ratio_bomb_rejected]] — code: test_zip_ratio_bomb_rejected()
- [[graphify_tests_test_office_limits_test_legit_zip_passes]] — code: test_legit_zip_passes()
- [[graphify_tests_test_office_limits_test_non_zip_rejected]] — code: test_non_zip_rejected()
- [[graphify_tests_test_office_limits_test_converters_return_empty_for_bomb]] — code: test_converters_return_empty_for_bomb()
- [[graphify_tests_test_office_limits_test_legit_multi_member_passes_streaming]] — code: test_legit_multi_member_passes_streaming()
- [[graphify_tests_test_office_limits_test_streaming_ceiling_rejects_oversized_actual]] — code: test_streaming_ceiling_rejects_oversized_actual()
- [[graphify_tests_test_office_limits_test_pdf_over_cap_returns_empty]] — code: test_pdf_over_cap_returns_empty()
- [[graphify_tests_test_office_limits_rationale_1]] — code: Resource-cap guards for parsing untrusted office/PDF files (F2).  .docx/.xlsx
- [[graphify_tests_test_office_limits_rationale_26]] — code: A tiny file that expands far past the ratio threshold is rejected.
- [[graphify_tests_test_office_limits_rationale_46]] — code: The live converters bail out (return "") on a bomb before parsing.
- [[graphify_tests_test_office_limits_rationale_55]] — code: A normal multi-member office zip passes the streaming-ceiling pass.
- [[graphify_tests_test_office_limits_rationale_65]] — code: With a low decompressed cap, content whose actual bytes exceed it is rejected.
- [[graphify_tests_test_office_limits_rationale_82]] — code: A PDF larger than the raw cap is skipped before pypdf opens it.

## Dependências

- [[graphify_tests_test_office_limits_test_pdf_over_cap_returns_empty]] → `indirect_call` → [[graphify_graphify_detect_detect]]
- [[graphify_tests_test_office_limits_test_streaming_ceiling_rejects_oversized_actual]] → `indirect_call` → [[graphify_graphify_detect_detect]]
- [[graphify_tests_test_office_limits]] → `contains` → [[graphify_tests_test_office_limits_test_converters_return_empty_for_bomb]]
- [[graphify_tests_test_office_limits]] → `contains` → [[graphify_tests_test_office_limits_test_file_within_size_cap]]
- [[graphify_tests_test_office_limits]] → `contains` → [[graphify_tests_test_office_limits_test_legit_multi_member_passes_streaming]]
- [[graphify_tests_test_office_limits]] → `contains` → [[graphify_tests_test_office_limits_test_legit_zip_passes]]
- [[graphify_tests_test_office_limits]] → `contains` → [[graphify_tests_test_office_limits_test_non_zip_rejected]]
- [[graphify_tests_test_office_limits]] → `contains` → [[graphify_tests_test_office_limits_test_pdf_over_cap_returns_empty]]
- [[graphify_tests_test_office_limits]] → `contains` → [[graphify_tests_test_office_limits_test_streaming_ceiling_rejects_oversized_actual]]
- [[graphify_tests_test_office_limits]] → `contains` → [[graphify_tests_test_office_limits_test_zip_ratio_bomb_rejected]]
- [[graphify_tests_test_office_limits]] → `contains` → [[graphify_tests_test_office_limits_write_zip]]
- [[graphify_tests_test_office_limits_rationale_1]] → `rationale_for` → [[graphify_tests_test_office_limits]]
- [[graphify_tests_test_office_limits_test_converters_return_empty_for_bomb]] → `calls` → [[graphify_tests_test_office_limits_write_zip]]
- [[graphify_tests_test_office_limits_test_legit_zip_passes]] → `calls` → [[graphify_tests_test_office_limits_write_zip]]
- [[graphify_tests_test_office_limits_test_zip_ratio_bomb_rejected]] → `calls` → [[graphify_tests_test_office_limits_write_zip]]
- [[graphify_tests_test_office_limits_rationale_26]] → `rationale_for` → [[graphify_tests_test_office_limits_test_zip_ratio_bomb_rejected]]
- [[graphify_tests_test_office_limits_rationale_46]] → `rationale_for` → [[graphify_tests_test_office_limits_test_converters_return_empty_for_bomb]]
- [[graphify_tests_test_office_limits_rationale_55]] → `rationale_for` → [[graphify_tests_test_office_limits_test_legit_multi_member_passes_streaming]]
- [[graphify_tests_test_office_limits_rationale_65]] → `rationale_for` → [[graphify_tests_test_office_limits_test_streaming_ceiling_rejects_oversized_actual]]
- [[graphify_tests_test_office_limits_rationale_82]] → `rationale_for` → [[graphify_tests_test_office_limits_test_pdf_over_cap_returns_empty]]