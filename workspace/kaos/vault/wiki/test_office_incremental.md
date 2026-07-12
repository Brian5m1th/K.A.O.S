# graphify\tests\test_office_incremental.py

## Símbolos

- [[graphify_tests_test_office_incremental]] — code: test_office_incremental.py
- [[graphify_tests_test_office_incremental_make_docx]] — code: _make_docx()
- [[graphify_tests_test_office_incremental_bump_mtime]] — code: _bump_mtime()
- [[graphify_tests_test_office_incremental_test_modified_docx_reconverts_sidecar]] — code: test_modified_docx_reconverts_sidecar()
- [[graphify_tests_test_office_incremental_test_unchanged_docx_sidecar_not_rewritten]] — code: test_unchanged_docx_sidecar_not_rewritten()
- [[graphify_tests_test_office_incremental_rationale_1]] — code: #1649 — a modified .docx/.xlsx must re-enter --update.  detect_incremental tra
- [[graphify_tests_test_office_incremental_rationale_28]] — code: Set path's mtime relative to now so ordering is deterministic.

## Dependências

- [[graphify_tests_test_office_incremental]] → `contains` → [[graphify_tests_test_office_incremental_bump_mtime]]
- [[graphify_tests_test_office_incremental]] → `contains` → [[graphify_tests_test_office_incremental_make_docx]]
- [[graphify_tests_test_office_incremental]] → `contains` → [[graphify_tests_test_office_incremental_test_modified_docx_reconverts_sidecar]]
- [[graphify_tests_test_office_incremental]] → `contains` → [[graphify_tests_test_office_incremental_test_unchanged_docx_sidecar_not_rewritten]]
- [[graphify_tests_test_office_incremental_rationale_1]] → `rationale_for` → [[graphify_tests_test_office_incremental]]
- [[graphify_tests_test_office_incremental_make_docx]] → `references` → [[graphify_tests_test_office_incremental_py_path]]
- [[graphify_tests_test_office_incremental_test_modified_docx_reconverts_sidecar]] → `calls` → [[graphify_tests_test_office_incremental_make_docx]]
- [[graphify_tests_test_office_incremental_test_unchanged_docx_sidecar_not_rewritten]] → `calls` → [[graphify_tests_test_office_incremental_make_docx]]
- [[graphify_tests_test_office_incremental_bump_mtime]] → `references` → [[graphify_tests_test_office_incremental_py_path]]
- [[graphify_tests_test_office_incremental_test_modified_docx_reconverts_sidecar]] → `references` → [[graphify_tests_test_office_incremental_py_path]]
- [[graphify_tests_test_office_incremental_test_unchanged_docx_sidecar_not_rewritten]] → `references` → [[graphify_tests_test_office_incremental_py_path]]
- [[graphify_tests_test_office_incremental_rationale_28]] → `rationale_for` → [[graphify_tests_test_office_incremental_bump_mtime]]
- [[graphify_tests_test_office_incremental_test_modified_docx_reconverts_sidecar]] → `calls` → [[graphify_tests_test_office_incremental_bump_mtime]]
- [[graphify_tests_test_office_incremental_test_unchanged_docx_sidecar_not_rewritten]] → `calls` → [[graphify_tests_test_office_incremental_bump_mtime]]