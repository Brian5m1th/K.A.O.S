# graphify\tests\test_builtin_global_type_refs.py

## Símbolos

- [[graphify_tests_test_builtin_global_type_refs]] — code: test_builtin_global_type_refs.py
- [[graphify_tests_test_builtin_global_type_refs_labels_by_id]] — code: _labels_by_id()
- [[graphify_tests_test_builtin_global_type_refs_test_builtin_date_type_ref_does_not_bind_to_user_date]] — code: test_builtin_date_type_ref_does_not_bind_to_user_DATE()
- [[graphify_tests_test_builtin_global_type_refs_test_nonbuiltin_receiver_type_still_resolves]] — code: test_nonbuiltin_receiver_type_still_resolves()
- [[graphify_tests_test_builtin_global_type_refs_test_builtin_static_call_does_not_bind_to_user_symbol]] — code: test_builtin_static_call_does_not_bind_to_user_symbol()
- [[graphify_tests_test_builtin_global_type_refs_rationale_1]] — code: Builtin-global receiver types must not resolve to same-named user symbols.  #1

## Dependências

- [[graphify_tests_test_builtin_global_type_refs]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_builtin_global_type_refs_test_builtin_date_type_ref_does_not_bind_to_user_date]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_builtin_global_type_refs_test_builtin_static_call_does_not_bind_to_user_symbol]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_builtin_global_type_refs_test_nonbuiltin_receiver_type_still_resolves]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_builtin_global_type_refs]] → `contains` → [[graphify_tests_test_builtin_global_type_refs_labels_by_id]]
- [[graphify_tests_test_builtin_global_type_refs]] → `contains` → [[graphify_tests_test_builtin_global_type_refs_test_builtin_date_type_ref_does_not_bind_to_user_date]]
- [[graphify_tests_test_builtin_global_type_refs]] → `contains` → [[graphify_tests_test_builtin_global_type_refs_test_builtin_static_call_does_not_bind_to_user_symbol]]
- [[graphify_tests_test_builtin_global_type_refs]] → `contains` → [[graphify_tests_test_builtin_global_type_refs_test_nonbuiltin_receiver_type_still_resolves]]
- [[graphify_tests_test_builtin_global_type_refs_rationale_1]] → `rationale_for` → [[graphify_tests_test_builtin_global_type_refs]]
- [[graphify_tests_test_builtin_global_type_refs_test_builtin_date_type_ref_does_not_bind_to_user_date]] → `calls` → [[graphify_tests_test_builtin_global_type_refs_labels_by_id]]
- [[graphify_tests_test_builtin_global_type_refs_test_builtin_static_call_does_not_bind_to_user_symbol]] → `calls` → [[graphify_tests_test_builtin_global_type_refs_labels_by_id]]
- [[graphify_tests_test_builtin_global_type_refs_test_nonbuiltin_receiver_type_still_resolves]] → `calls` → [[graphify_tests_test_builtin_global_type_refs_labels_by_id]]