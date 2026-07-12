# graphify\tests\test_replace_or_append_section.py

## Símbolos

- [[graphify_tests_test_replace_or_append_section]] — code: test_replace_or_append_section.py
- [[graphify_tests_test_replace_or_append_section_test_inline_reference_to_marker_is_not_treated_as_the_section]] — code: test_inline_reference_to_marker_is_not_treated_as_the_section()
- [[graphify_tests_test_replace_or_append_section_test_real_section_is_replaced_in_place]] — code: test_real_section_is_replaced_in_place()
- [[graphify_tests_test_replace_or_append_section_test_reinstall_is_idempotent]] — code: test_reinstall_is_idempotent()
- [[graphify_tests_test_replace_or_append_section_test_append_when_no_real_heading]] — code: test_append_when_no_real_heading()
- [[graphify_tests_test_replace_or_append_section_test_prefers_last_heading_when_duplicated]] — code: test_prefers_last_heading_when_duplicated()
- [[graphify_tests_test_replace_or_append_section_rationale_1]] — code: #1688 - graphify's shared-file section update must not destroy user content.

## Dependências

- [[graphify_tests_test_replace_or_append_section]] → `imports_from` → [[graphify_graphify_main]]
- [[graphify_tests_test_replace_or_append_section_test_append_when_no_real_heading]] → `calls` → [[graphify_graphify_install_replace_or_append_section]]
- [[graphify_tests_test_replace_or_append_section_test_inline_reference_to_marker_is_not_treated_as_the_section]] → `calls` → [[graphify_graphify_install_replace_or_append_section]]
- [[graphify_tests_test_replace_or_append_section_test_prefers_last_heading_when_duplicated]] → `calls` → [[graphify_graphify_install_replace_or_append_section]]
- [[graphify_tests_test_replace_or_append_section_test_real_section_is_replaced_in_place]] → `calls` → [[graphify_graphify_install_replace_or_append_section]]
- [[graphify_tests_test_replace_or_append_section_test_reinstall_is_idempotent]] → `calls` → [[graphify_graphify_install_replace_or_append_section]]
- [[graphify_tests_test_replace_or_append_section]] → `contains` → [[graphify_tests_test_replace_or_append_section_test_append_when_no_real_heading]]
- [[graphify_tests_test_replace_or_append_section]] → `contains` → [[graphify_tests_test_replace_or_append_section_test_inline_reference_to_marker_is_not_treated_as_the_section]]
- [[graphify_tests_test_replace_or_append_section]] → `contains` → [[graphify_tests_test_replace_or_append_section_test_prefers_last_heading_when_duplicated]]
- [[graphify_tests_test_replace_or_append_section]] → `contains` → [[graphify_tests_test_replace_or_append_section_test_real_section_is_replaced_in_place]]
- [[graphify_tests_test_replace_or_append_section]] → `contains` → [[graphify_tests_test_replace_or_append_section_test_reinstall_is_idempotent]]
- [[graphify_tests_test_replace_or_append_section_rationale_1]] → `rationale_for` → [[graphify_tests_test_replace_or_append_section]]