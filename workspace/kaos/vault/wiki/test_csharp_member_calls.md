# graphify\tests\test_csharp_member_calls.py

## Símbolos

- [[graphify_tests_test_csharp_member_calls]] — code: test_csharp_member_calls.py
- [[graphify_tests_test_csharp_member_calls_calls]] — code: _calls()
- [[graphify_tests_test_csharp_member_calls_find]] — code: _find()
- [[graphify_tests_test_csharp_member_calls_test_field_receiver_resolves_to_declared_type_not_bare_match]] — code: test_field_receiver_resolves_to_declared_type_not_bare_match()
- [[graphify_tests_test_csharp_member_calls_test_parameter_receiver_resolves]] — code: test_parameter_receiver_resolves()
- [[graphify_tests_test_csharp_member_calls_test_local_var_receiver_resolves]] — code: test_local_var_receiver_resolves()
- [[graphify_tests_test_csharp_member_calls_test_cross_file_receiver_resolves]] — code: test_cross_file_receiver_resolves()
- [[graphify_tests_test_csharp_member_calls_test_this_and_static_receivers]] — code: test_this_and_static_receivers()
- [[graphify_tests_test_csharp_member_calls_test_untyped_receiver_emits_no_edge]] — code: test_untyped_receiver_emits_no_edge()
- [[graphify_tests_test_csharp_member_calls_test_method_absent_on_type_emits_no_edge]] — code: test_method_absent_on_type_emits_no_edge()
- [[graphify_tests_test_csharp_member_calls_test_unqualified_call_still_resolves]] — code: test_unqualified_call_still_resolves()
- [[graphify_tests_test_csharp_member_calls_test_method_chained_off_new_expression_resolves]] — code: test_method_chained_off_new_expression_resolves()
- [[graphify_tests_test_csharp_member_calls_rationale_1]] — code: C# receiver-typed member-call resolution (#1609).  `recv.Method()` where `recv
- [[graphify_tests_test_csharp_member_calls_rationale_147]] — code: #1770: a method invoked directly on a `new X(...)` object-creation     expressi

## Dependências

- [[graphify_tests_test_csharp_member_calls]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_csharp_member_calls_calls]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_csharp_member_calls]] → `contains` → [[graphify_tests_test_csharp_member_calls_calls]]
- [[graphify_tests_test_csharp_member_calls]] → `contains` → [[graphify_tests_test_csharp_member_calls_find]]
- [[graphify_tests_test_csharp_member_calls]] → `contains` → [[graphify_tests_test_csharp_member_calls_test_cross_file_receiver_resolves]]
- [[graphify_tests_test_csharp_member_calls]] → `contains` → [[graphify_tests_test_csharp_member_calls_test_field_receiver_resolves_to_declared_type_not_bare_match]]
- [[graphify_tests_test_csharp_member_calls]] → `contains` → [[graphify_tests_test_csharp_member_calls_test_local_var_receiver_resolves]]
- [[graphify_tests_test_csharp_member_calls]] → `contains` → [[graphify_tests_test_csharp_member_calls_test_method_absent_on_type_emits_no_edge]]
- [[graphify_tests_test_csharp_member_calls]] → `contains` → [[graphify_tests_test_csharp_member_calls_test_method_chained_off_new_expression_resolves]]
- [[graphify_tests_test_csharp_member_calls]] → `contains` → [[graphify_tests_test_csharp_member_calls_test_parameter_receiver_resolves]]
- [[graphify_tests_test_csharp_member_calls]] → `contains` → [[graphify_tests_test_csharp_member_calls_test_this_and_static_receivers]]
- [[graphify_tests_test_csharp_member_calls]] → `contains` → [[graphify_tests_test_csharp_member_calls_test_unqualified_call_still_resolves]]
- [[graphify_tests_test_csharp_member_calls]] → `contains` → [[graphify_tests_test_csharp_member_calls_test_untyped_receiver_emits_no_edge]]
- [[graphify_tests_test_csharp_member_calls_rationale_1]] → `rationale_for` → [[graphify_tests_test_csharp_member_calls]]
- [[graphify_tests_test_csharp_member_calls_test_cross_file_receiver_resolves]] → `calls` → [[graphify_tests_test_csharp_member_calls_calls]]
- [[graphify_tests_test_csharp_member_calls_test_field_receiver_resolves_to_declared_type_not_bare_match]] → `calls` → [[graphify_tests_test_csharp_member_calls_calls]]
- [[graphify_tests_test_csharp_member_calls_test_local_var_receiver_resolves]] → `calls` → [[graphify_tests_test_csharp_member_calls_calls]]
- [[graphify_tests_test_csharp_member_calls_test_method_absent_on_type_emits_no_edge]] → `calls` → [[graphify_tests_test_csharp_member_calls_calls]]
- [[graphify_tests_test_csharp_member_calls_test_method_chained_off_new_expression_resolves]] → `calls` → [[graphify_tests_test_csharp_member_calls_calls]]
- [[graphify_tests_test_csharp_member_calls_test_parameter_receiver_resolves]] → `calls` → [[graphify_tests_test_csharp_member_calls_calls]]
- [[graphify_tests_test_csharp_member_calls_test_this_and_static_receivers]] → `calls` → [[graphify_tests_test_csharp_member_calls_calls]]
- [[graphify_tests_test_csharp_member_calls_test_unqualified_call_still_resolves]] → `calls` → [[graphify_tests_test_csharp_member_calls_calls]]
- [[graphify_tests_test_csharp_member_calls_test_untyped_receiver_emits_no_edge]] → `calls` → [[graphify_tests_test_csharp_member_calls_calls]]
- [[graphify_tests_test_csharp_member_calls_test_field_receiver_resolves_to_declared_type_not_bare_match]] → `calls` → [[graphify_tests_test_csharp_member_calls_find]]
- [[graphify_tests_test_csharp_member_calls_rationale_147]] → `rationale_for` → [[graphify_tests_test_csharp_member_calls_test_method_chained_off_new_expression_resolves]]