# graphify\tests\test_indirect_dispatch_assign_return.py

## Símbolos

- [[graphify_tests_test_indirect_dispatch_assign_return]] — code: test_indirect_dispatch_assign_return.py
- [[graphify_tests_test_indirect_dispatch_assign_return_extract]] — code: _extract()
- [[graphify_tests_test_indirect_dispatch_assign_return_ind]] — code: _ind()
- [[graphify_tests_test_indirect_dispatch_assign_return_test_assignment_and_return_emit_indirect_call]] — code: test_assignment_and_return_emit_indirect_call()
- [[graphify_tests_test_indirect_dispatch_assign_return_test_multiple_assignment_emits_for_each]] — code: test_multiple_assignment_emits_for_each()
- [[graphify_tests_test_indirect_dispatch_assign_return_test_module_level_assignment_emits_indirect_call]] — code: test_module_level_assignment_emits_indirect_call()
- [[graphify_tests_test_indirect_dispatch_assign_return_test_assignment_feeds_affected]] — code: test_assignment_feeds_affected()
- [[graphify_tests_test_indirect_dispatch_assign_return_test_param_shadow_emits_nothing]] — code: test_param_shadow_emits_nothing()
- [[graphify_tests_test_indirect_dispatch_assign_return_test_local_shadow_emits_nothing]] — code: test_local_shadow_emits_nothing()
- [[graphify_tests_test_indirect_dispatch_assign_return_test_non_callable_value_emits_nothing]] — code: test_non_callable_value_emits_nothing()
- [[graphify_tests_test_indirect_dispatch_assign_return_rationale_1]] — code: Indirect dispatch via assignment + return references — #1566 slice 2.  A funct

## Dependências

- [[graphify_tests_test_indirect_dispatch_assign_return]] → `imports_from` → [[graphify_graphify_affected]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_assignment_feeds_affected]] → `calls` → [[graphify_graphify_affected_affected_nodes]]
- [[graphify_tests_test_indirect_dispatch_assign_return]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_indirect_dispatch_assign_return_extract]] → `calls` → [[graphify_graphify_extract_extract_python]]
- [[graphify_tests_test_indirect_dispatch_assign_return]] → `contains` → [[graphify_tests_test_indirect_dispatch_assign_return_extract]]
- [[graphify_tests_test_indirect_dispatch_assign_return]] → `contains` → [[graphify_tests_test_indirect_dispatch_assign_return_ind]]
- [[graphify_tests_test_indirect_dispatch_assign_return]] → `contains` → [[graphify_tests_test_indirect_dispatch_assign_return_test_assignment_and_return_emit_indirect_call]]
- [[graphify_tests_test_indirect_dispatch_assign_return]] → `contains` → [[graphify_tests_test_indirect_dispatch_assign_return_test_assignment_feeds_affected]]
- [[graphify_tests_test_indirect_dispatch_assign_return]] → `contains` → [[graphify_tests_test_indirect_dispatch_assign_return_test_local_shadow_emits_nothing]]
- [[graphify_tests_test_indirect_dispatch_assign_return]] → `contains` → [[graphify_tests_test_indirect_dispatch_assign_return_test_module_level_assignment_emits_indirect_call]]
- [[graphify_tests_test_indirect_dispatch_assign_return]] → `contains` → [[graphify_tests_test_indirect_dispatch_assign_return_test_multiple_assignment_emits_for_each]]
- [[graphify_tests_test_indirect_dispatch_assign_return]] → `contains` → [[graphify_tests_test_indirect_dispatch_assign_return_test_non_callable_value_emits_nothing]]
- [[graphify_tests_test_indirect_dispatch_assign_return]] → `contains` → [[graphify_tests_test_indirect_dispatch_assign_return_test_param_shadow_emits_nothing]]
- [[graphify_tests_test_indirect_dispatch_assign_return_rationale_1]] → `rationale_for` → [[graphify_tests_test_indirect_dispatch_assign_return]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_assignment_and_return_emit_indirect_call]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_extract]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_assignment_feeds_affected]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_extract]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_local_shadow_emits_nothing]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_extract]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_module_level_assignment_emits_indirect_call]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_extract]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_multiple_assignment_emits_for_each]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_extract]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_non_callable_value_emits_nothing]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_extract]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_param_shadow_emits_nothing]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_extract]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_assignment_and_return_emit_indirect_call]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_ind]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_local_shadow_emits_nothing]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_ind]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_module_level_assignment_emits_indirect_call]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_ind]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_multiple_assignment_emits_for_each]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_ind]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_non_callable_value_emits_nothing]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_ind]]
- [[graphify_tests_test_indirect_dispatch_assign_return_test_param_shadow_emits_nothing]] → `calls` → [[graphify_tests_test_indirect_dispatch_assign_return_ind]]