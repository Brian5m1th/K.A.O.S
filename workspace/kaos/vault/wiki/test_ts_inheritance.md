# graphify\tests\test_ts_inheritance.py

## Símbolos

- [[graphify_tests_test_ts_inheritance]] — code: test_ts_inheritance.py
- [[graphify_tests_test_ts_inheritance_write]] — code: _write()
- [[graphify_tests_test_ts_inheritance_has_inherits]] — code: _has_inherits()
- [[graphify_tests_test_ts_inheritance_test_interface_extends_same_file]] — code: test_interface_extends_same_file()
- [[graphify_tests_test_ts_inheritance_test_interface_extends_multiple_same_file]] — code: test_interface_extends_multiple_same_file()
- [[graphify_tests_test_ts_inheritance_test_class_extends_same_file]] — code: test_class_extends_same_file()
- [[graphify_tests_test_ts_inheritance_test_interface_extends_generic_base_same_file]] — code: test_interface_extends_generic_base_same_file()
- [[graphify_tests_test_ts_inheritance_test_interface_extends_imported]] — code: test_interface_extends_imported()
- [[graphify_tests_test_ts_inheritance_test_imported_class_extends_still_works]] — code: test_imported_class_extends_still_works()
- [[graphify_tests_test_ts_inheritance_test_class_implements_same_file_interface]] — code: test_class_implements_same_file_interface()
- [[graphify_tests_test_ts_inheritance_rationale_1]] — code: Regression tests for issue #1095: TypeScript inheritance capture.  Two gaps on
- [[graphify_tests_test_ts_inheritance_rationale_77]] — code: Regression guard: the originally-working imported-class case must stay.

## Dependências

- [[graphify_tests_test_ts_inheritance]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_ts_inheritance_test_class_extends_same_file]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_inheritance_test_class_implements_same_file_interface]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_inheritance_test_imported_class_extends_still_works]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_inheritance_test_interface_extends_generic_base_same_file]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_inheritance_test_interface_extends_imported]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_inheritance_test_interface_extends_multiple_same_file]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_inheritance_test_interface_extends_same_file]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_ts_inheritance_has_inherits]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_tests_test_ts_inheritance]] → `contains` → [[graphify_tests_test_ts_inheritance_has_inherits]]
- [[graphify_tests_test_ts_inheritance]] → `contains` → [[graphify_tests_test_ts_inheritance_test_class_extends_same_file]]
- [[graphify_tests_test_ts_inheritance]] → `contains` → [[graphify_tests_test_ts_inheritance_test_class_implements_same_file_interface]]
- [[graphify_tests_test_ts_inheritance]] → `contains` → [[graphify_tests_test_ts_inheritance_test_imported_class_extends_still_works]]
- [[graphify_tests_test_ts_inheritance]] → `contains` → [[graphify_tests_test_ts_inheritance_test_interface_extends_generic_base_same_file]]
- [[graphify_tests_test_ts_inheritance]] → `contains` → [[graphify_tests_test_ts_inheritance_test_interface_extends_imported]]
- [[graphify_tests_test_ts_inheritance]] → `contains` → [[graphify_tests_test_ts_inheritance_test_interface_extends_multiple_same_file]]
- [[graphify_tests_test_ts_inheritance]] → `contains` → [[graphify_tests_test_ts_inheritance_test_interface_extends_same_file]]
- [[graphify_tests_test_ts_inheritance]] → `contains` → [[graphify_tests_test_ts_inheritance_write]]
- [[graphify_tests_test_ts_inheritance_rationale_1]] → `rationale_for` → [[graphify_tests_test_ts_inheritance]]
- [[graphify_tests_test_ts_inheritance_test_class_extends_same_file]] → `calls` → [[graphify_tests_test_ts_inheritance_write]]
- [[graphify_tests_test_ts_inheritance_test_class_implements_same_file_interface]] → `calls` → [[graphify_tests_test_ts_inheritance_write]]
- [[graphify_tests_test_ts_inheritance_test_imported_class_extends_still_works]] → `calls` → [[graphify_tests_test_ts_inheritance_write]]
- [[graphify_tests_test_ts_inheritance_test_interface_extends_generic_base_same_file]] → `calls` → [[graphify_tests_test_ts_inheritance_write]]
- [[graphify_tests_test_ts_inheritance_test_interface_extends_imported]] → `calls` → [[graphify_tests_test_ts_inheritance_write]]
- [[graphify_tests_test_ts_inheritance_test_interface_extends_multiple_same_file]] → `calls` → [[graphify_tests_test_ts_inheritance_write]]
- [[graphify_tests_test_ts_inheritance_test_interface_extends_same_file]] → `calls` → [[graphify_tests_test_ts_inheritance_write]]
- [[graphify_tests_test_ts_inheritance_write]] → `references` → [[graphify_tests_test_ts_inheritance_py_path]]
- [[graphify_tests_test_ts_inheritance_has_inherits]] → `calls` → [[graphify_tests_test_ts_inheritance_py_path]]
- [[graphify_tests_test_ts_inheritance_test_class_extends_same_file]] → `calls` → [[graphify_tests_test_ts_inheritance_has_inherits]]
- [[graphify_tests_test_ts_inheritance_test_class_implements_same_file_interface]] → `calls` → [[graphify_tests_test_ts_inheritance_has_inherits]]
- [[graphify_tests_test_ts_inheritance_test_imported_class_extends_still_works]] → `calls` → [[graphify_tests_test_ts_inheritance_has_inherits]]
- [[graphify_tests_test_ts_inheritance_test_interface_extends_generic_base_same_file]] → `calls` → [[graphify_tests_test_ts_inheritance_has_inherits]]
- [[graphify_tests_test_ts_inheritance_test_interface_extends_imported]] → `calls` → [[graphify_tests_test_ts_inheritance_has_inherits]]
- [[graphify_tests_test_ts_inheritance_test_interface_extends_multiple_same_file]] → `calls` → [[graphify_tests_test_ts_inheritance_has_inherits]]
- [[graphify_tests_test_ts_inheritance_test_interface_extends_same_file]] → `calls` → [[graphify_tests_test_ts_inheritance_has_inherits]]
- [[graphify_tests_test_ts_inheritance_rationale_77]] → `rationale_for` → [[graphify_tests_test_ts_inheritance_test_imported_class_extends_still_works]]