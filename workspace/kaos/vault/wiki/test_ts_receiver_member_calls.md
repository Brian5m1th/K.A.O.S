# graphify\tests\test_ts_receiver_member_calls.py

## Símbolos

- [[graphify_tests_test_ts_receiver_member_calls]] — code: test_ts_receiver_member_calls.py
- [[graphify_tests_test_ts_receiver_member_calls_calls]] — code: _calls()
- [[graphify_tests_test_ts_receiver_member_calls_test_local_new_binding_receiver]] — code: test_local_new_binding_receiver()
- [[graphify_tests_test_ts_receiver_member_calls_test_closure_over_typed_param_receiver]] — code: test_closure_over_typed_param_receiver()
- [[graphify_tests_test_ts_receiver_member_calls_test_new_binding_resolves_to_correct_class_under_ambiguity]] — code: test_new_binding_resolves_to_correct_class_under_ambiguity()
- [[graphify_tests_test_ts_receiver_member_calls_test_untyped_param_receiver_emits_no_edge]] — code: test_untyped_param_receiver_emits_no_edge()
- [[graphify_tests_test_ts_receiver_member_calls_test_array_typed_receiver_emits_no_edge]] — code: test_array_typed_receiver_emits_no_edge()
- [[graphify_tests_test_ts_receiver_member_calls_rationale_1]] — code: TS/JS receiver-typed member calls beyond `this.field` (#1630).  The #1316 reso

## Dependências

- [[graphify_tests_test_ts_receiver_member_calls]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_ts_receiver_member_calls_calls]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_receiver_member_calls]] → `contains` → [[graphify_tests_test_ts_receiver_member_calls_calls]]
- [[graphify_tests_test_ts_receiver_member_calls]] → `contains` → [[graphify_tests_test_ts_receiver_member_calls_test_array_typed_receiver_emits_no_edge]]
- [[graphify_tests_test_ts_receiver_member_calls]] → `contains` → [[graphify_tests_test_ts_receiver_member_calls_test_closure_over_typed_param_receiver]]
- [[graphify_tests_test_ts_receiver_member_calls]] → `contains` → [[graphify_tests_test_ts_receiver_member_calls_test_local_new_binding_receiver]]
- [[graphify_tests_test_ts_receiver_member_calls]] → `contains` → [[graphify_tests_test_ts_receiver_member_calls_test_new_binding_resolves_to_correct_class_under_ambiguity]]
- [[graphify_tests_test_ts_receiver_member_calls]] → `contains` → [[graphify_tests_test_ts_receiver_member_calls_test_untyped_param_receiver_emits_no_edge]]
- [[graphify_tests_test_ts_receiver_member_calls_rationale_1]] → `rationale_for` → [[graphify_tests_test_ts_receiver_member_calls]]
- [[graphify_tests_test_ts_receiver_member_calls_test_array_typed_receiver_emits_no_edge]] → `calls` → [[graphify_tests_test_ts_receiver_member_calls_calls]]
- [[graphify_tests_test_ts_receiver_member_calls_test_closure_over_typed_param_receiver]] → `calls` → [[graphify_tests_test_ts_receiver_member_calls_calls]]
- [[graphify_tests_test_ts_receiver_member_calls_test_local_new_binding_receiver]] → `calls` → [[graphify_tests_test_ts_receiver_member_calls_calls]]
- [[graphify_tests_test_ts_receiver_member_calls_test_new_binding_resolves_to_correct_class_under_ambiguity]] → `calls` → [[graphify_tests_test_ts_receiver_member_calls_calls]]
- [[graphify_tests_test_ts_receiver_member_calls_test_untyped_param_receiver_emits_no_edge]] → `calls` → [[graphify_tests_test_ts_receiver_member_calls_calls]]