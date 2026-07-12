# graphify\tests\test_swift_cross_file_calls.py

## Símbolos

- [[graphify_tests_test_swift_cross_file_calls]] — code: test_swift_cross_file_calls.py
- [[graphify_tests_test_swift_cross_file_calls_write]] — code: _write()
- [[graphify_tests_test_swift_cross_file_calls_label]] — code: _label()
- [[graphify_tests_test_swift_cross_file_calls_edge_labels]] — code: _edge_labels()
- [[graphify_tests_test_swift_cross_file_calls_issue_fixture]] — code: _issue_fixture()
- [[graphify_tests_test_swift_cross_file_calls_test_swift_cross_file_member_calls_resolve]] — code: test_swift_cross_file_member_calls_resolve()
- [[graphify_tests_test_swift_cross_file_calls_test_swift_cross_file_member_calls_have_correct_confidence_and_resolve]] — code: test_swift_cross_file_member_calls_have_correct_confidence_and_resolve()
- [[graphify_tests_test_swift_cross_file_calls_test_swift_ambiguous_type_does_not_over_connect]] — code: test_swift_ambiguous_type_does_not_over_connect()
- [[graphify_tests_test_swift_cross_file_calls_test_swift_unknown_receiver_emits_no_edge]] — code: test_swift_unknown_receiver_emits_no_edge()
- [[graphify_tests_test_swift_cross_file_calls_test_deferred_singleton_local_var_resolves]] — code: test_deferred_singleton_local_var_resolves()
- [[graphify_tests_test_swift_cross_file_calls_rationale_23]] — code: Return {(source_label, relation, target_label)} for the given relations.
- [[graphify_tests_test_swift_cross_file_calls_rationale_32]] — code: The three cross-file patterns from #1356, plus a constructor-in-initializer.
- [[graphify_tests_test_swift_cross_file_calls_rationale_158]] — code: #1604: `let x = Type.shared` cached into a local var, then `x.method()` on a

## Dependências

- [[graphify_tests_test_swift_cross_file_calls]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_tests_test_swift_cross_file_calls]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_swift_cross_file_calls_test_deferred_singleton_local_var_resolves]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_ambiguous_type_does_not_over_connect]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_cross_file_member_calls_have_correct_confidence_and_resolve]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_cross_file_member_calls_resolve]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_unknown_receiver_emits_no_edge]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_swift_cross_file_calls]] → `contains` → [[graphify_tests_test_swift_cross_file_calls_edge_labels]]
- [[graphify_tests_test_swift_cross_file_calls]] → `contains` → [[graphify_tests_test_swift_cross_file_calls_issue_fixture]]
- [[graphify_tests_test_swift_cross_file_calls]] → `contains` → [[graphify_tests_test_swift_cross_file_calls_label]]
- [[graphify_tests_test_swift_cross_file_calls]] → `contains` → [[graphify_tests_test_swift_cross_file_calls_test_deferred_singleton_local_var_resolves]]
- [[graphify_tests_test_swift_cross_file_calls]] → `contains` → [[graphify_tests_test_swift_cross_file_calls_test_swift_ambiguous_type_does_not_over_connect]]
- [[graphify_tests_test_swift_cross_file_calls]] → `contains` → [[graphify_tests_test_swift_cross_file_calls_test_swift_cross_file_member_calls_have_correct_confidence_and_resolve]]
- [[graphify_tests_test_swift_cross_file_calls]] → `contains` → [[graphify_tests_test_swift_cross_file_calls_test_swift_cross_file_member_calls_resolve]]
- [[graphify_tests_test_swift_cross_file_calls]] → `contains` → [[graphify_tests_test_swift_cross_file_calls_test_swift_unknown_receiver_emits_no_edge]]
- [[graphify_tests_test_swift_cross_file_calls]] → `contains` → [[graphify_tests_test_swift_cross_file_calls_write]]
- [[graphify_tests_test_swift_cross_file_calls_issue_fixture]] → `calls` → [[graphify_tests_test_swift_cross_file_calls_write]]
- [[graphify_tests_test_swift_cross_file_calls_test_deferred_singleton_local_var_resolves]] → `calls` → [[graphify_tests_test_swift_cross_file_calls_write]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_ambiguous_type_does_not_over_connect]] → `calls` → [[graphify_tests_test_swift_cross_file_calls_write]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_unknown_receiver_emits_no_edge]] → `calls` → [[graphify_tests_test_swift_cross_file_calls_write]]
- [[graphify_tests_test_swift_cross_file_calls_write]] → `references` → [[graphify_tests_test_swift_cross_file_calls_py_path]]
- [[graphify_tests_test_swift_cross_file_calls_issue_fixture]] → `references` → [[graphify_tests_test_swift_cross_file_calls_py_path]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_ambiguous_type_does_not_over_connect]] → `references` → [[graphify_tests_test_swift_cross_file_calls_py_path]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_cross_file_member_calls_have_correct_confidence_and_resolve]] → `references` → [[graphify_tests_test_swift_cross_file_calls_py_path]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_cross_file_member_calls_resolve]] → `references` → [[graphify_tests_test_swift_cross_file_calls_py_path]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_unknown_receiver_emits_no_edge]] → `references` → [[graphify_tests_test_swift_cross_file_calls_py_path]]
- [[graphify_tests_test_swift_cross_file_calls_edge_labels]] → `calls` → [[graphify_tests_test_swift_cross_file_calls_label]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_cross_file_member_calls_have_correct_confidence_and_resolve]] → `calls` → [[graphify_tests_test_swift_cross_file_calls_label]]
- [[graphify_tests_test_swift_cross_file_calls_rationale_23]] → `rationale_for` → [[graphify_tests_test_swift_cross_file_calls_edge_labels]]
- [[graphify_tests_test_swift_cross_file_calls_test_deferred_singleton_local_var_resolves]] → `calls` → [[graphify_tests_test_swift_cross_file_calls_edge_labels]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_cross_file_member_calls_resolve]] → `calls` → [[graphify_tests_test_swift_cross_file_calls_edge_labels]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_unknown_receiver_emits_no_edge]] → `calls` → [[graphify_tests_test_swift_cross_file_calls_edge_labels]]
- [[graphify_tests_test_swift_cross_file_calls_rationale_32]] → `rationale_for` → [[graphify_tests_test_swift_cross_file_calls_issue_fixture]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_cross_file_member_calls_have_correct_confidence_and_resolve]] → `calls` → [[graphify_tests_test_swift_cross_file_calls_issue_fixture]]
- [[graphify_tests_test_swift_cross_file_calls_test_swift_cross_file_member_calls_resolve]] → `calls` → [[graphify_tests_test_swift_cross_file_calls_issue_fixture]]
- [[graphify_tests_test_swift_cross_file_calls_rationale_158]] → `rationale_for` → [[graphify_tests_test_swift_cross_file_calls_test_deferred_singleton_local_var_resolves]]