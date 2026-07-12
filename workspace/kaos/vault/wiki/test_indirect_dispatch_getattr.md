# graphify\tests\test_indirect_dispatch_getattr.py

## Símbolos

- [[graphify_tests_test_indirect_dispatch_getattr]] — code: test_indirect_dispatch_getattr.py
- [[graphify_tests_test_indirect_dispatch_getattr_extract]] — code: _extract()
- [[graphify_tests_test_indirect_dispatch_getattr_ind]] — code: _ind()
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_string_literal_emits_indirect_call]] — code: test_getattr_string_literal_emits_indirect_call()
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_with_default_emits]] — code: test_getattr_with_default_emits()
- [[graphify_tests_test_indirect_dispatch_getattr_test_module_level_getattr_emits]] — code: test_module_level_getattr_emits()
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_feeds_affected]] — code: test_getattr_feeds_affected()
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_string_not_shadowed_by_param]] — code: test_getattr_string_not_shadowed_by_param()
- [[graphify_tests_test_indirect_dispatch_getattr_test_dynamic_getattr_names_emit_nothing]] — code: test_dynamic_getattr_names_emit_nothing()
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_non_callable_name_emits_nothing]] — code: test_getattr_non_callable_name_emits_nothing()
- [[graphify_tests_test_indirect_dispatch_getattr_test_method_named_getattr_is_not_the_builtin]] — code: test_method_named_getattr_is_not_the_builtin()
- [[graphify_tests_test_indirect_dispatch_getattr_rationale_1]] — code: Reflective dispatch via getattr string literals — #1566 slice 3.  ``getattr(ob

## Dependências

- [[graphify_tests_test_indirect_dispatch_getattr]] → `imports_from` → [[graphify_graphify_affected]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_feeds_affected]] → `calls` → [[graphify_graphify_affected_affected_nodes]]
- [[graphify_tests_test_indirect_dispatch_getattr]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_indirect_dispatch_getattr_extract]] → `calls` → [[graphify_graphify_extract_extract_python]]
- [[graphify_tests_test_indirect_dispatch_getattr]] → `contains` → [[graphify_tests_test_indirect_dispatch_getattr_extract]]
- [[graphify_tests_test_indirect_dispatch_getattr]] → `contains` → [[graphify_tests_test_indirect_dispatch_getattr_ind]]
- [[graphify_tests_test_indirect_dispatch_getattr]] → `contains` → [[graphify_tests_test_indirect_dispatch_getattr_test_dynamic_getattr_names_emit_nothing]]
- [[graphify_tests_test_indirect_dispatch_getattr]] → `contains` → [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_feeds_affected]]
- [[graphify_tests_test_indirect_dispatch_getattr]] → `contains` → [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_non_callable_name_emits_nothing]]
- [[graphify_tests_test_indirect_dispatch_getattr]] → `contains` → [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_string_literal_emits_indirect_call]]
- [[graphify_tests_test_indirect_dispatch_getattr]] → `contains` → [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_string_not_shadowed_by_param]]
- [[graphify_tests_test_indirect_dispatch_getattr]] → `contains` → [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_with_default_emits]]
- [[graphify_tests_test_indirect_dispatch_getattr]] → `contains` → [[graphify_tests_test_indirect_dispatch_getattr_test_method_named_getattr_is_not_the_builtin]]
- [[graphify_tests_test_indirect_dispatch_getattr]] → `contains` → [[graphify_tests_test_indirect_dispatch_getattr_test_module_level_getattr_emits]]
- [[graphify_tests_test_indirect_dispatch_getattr_rationale_1]] → `rationale_for` → [[graphify_tests_test_indirect_dispatch_getattr]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_dynamic_getattr_names_emit_nothing]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_extract]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_feeds_affected]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_extract]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_non_callable_name_emits_nothing]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_extract]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_string_literal_emits_indirect_call]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_extract]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_string_not_shadowed_by_param]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_extract]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_with_default_emits]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_extract]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_method_named_getattr_is_not_the_builtin]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_extract]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_module_level_getattr_emits]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_extract]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_dynamic_getattr_names_emit_nothing]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_ind]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_non_callable_name_emits_nothing]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_ind]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_string_literal_emits_indirect_call]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_ind]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_getattr_with_default_emits]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_ind]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_method_named_getattr_is_not_the_builtin]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_ind]]
- [[graphify_tests_test_indirect_dispatch_getattr_test_module_level_getattr_emits]] → `calls` → [[graphify_tests_test_indirect_dispatch_getattr_ind]]