# graphify\tests\test_install_strings.py

## Símbolos

- [[graphify_tests_test_install_strings]] — code: test_install_strings.py
- [[graphify_tests_test_install_strings_test_every_install_surface_recommends_graphify_query]] — code: test_every_install_surface_recommends_graphify_query()
- [[graphify_tests_test_install_strings_test_no_install_surface_demands_reading_the_full_report_first]] — code: test_no_install_surface_demands_reading_the_full_report_first()
- [[graphify_tests_test_install_strings_test_report_is_still_referenced_as_fallback]] — code: test_report_is_still_referenced_as_fallback()
- [[graphify_tests_test_install_strings_test_agents_section_does_not_skip_dirty_graph_output]] — code: test_agents_section_does_not_skip_dirty_graph_output()
- [[graphify_tests_test_install_strings_test_agents_section_uses_generic_graphify_instruction]] — code: test_agents_section_uses_generic_graphify_instruction()
- [[graphify_tests_test_install_strings_test_skill_registration_uses_host_generic_instruction]] — code: test_skill_registration_uses_host_generic_instruction()
- [[graphify_tests_test_install_strings_test_how_it_works_clarifies_code_only_semantic_extraction]] — code: test_how_it_works_clarifies_code_only_semantic_extraction()
- [[graphify_tests_test_install_strings_rationale_1]] — code: Regression tests for install-time instruction strings.  These strings live in
- [[graphify_tests_test_install_strings_rationale_51]] — code: All ten install surfaces must point the assistant at `graphify query`     as th
- [[graphify_tests_test_install_strings_rationale_67]] — code: The pre-fix instructions told assistants to read GRAPH_REPORT.md as     their f
- [[graphify_tests_test_install_strings_rationale_100]] — code: The fix demotes GRAPH_REPORT.md, it doesn't delete the reference.     Most inst

## Dependências

- [[graphify_tests_test_install_strings]] → `imports_from` → [[graphify_graphify_main]]
- [[graphify_tests_test_install_strings_test_skill_registration_uses_host_generic_instruction]] → `calls` → [[graphify_graphify_install_skill_registration]]
- [[graphify_tests_test_install_strings]] → `contains` → [[graphify_tests_test_install_strings_test_agents_section_does_not_skip_dirty_graph_output]]
- [[graphify_tests_test_install_strings]] → `contains` → [[graphify_tests_test_install_strings_test_agents_section_uses_generic_graphify_instruction]]
- [[graphify_tests_test_install_strings]] → `contains` → [[graphify_tests_test_install_strings_test_every_install_surface_recommends_graphify_query]]
- [[graphify_tests_test_install_strings]] → `contains` → [[graphify_tests_test_install_strings_test_how_it_works_clarifies_code_only_semantic_extraction]]
- [[graphify_tests_test_install_strings]] → `contains` → [[graphify_tests_test_install_strings_test_no_install_surface_demands_reading_the_full_report_first]]
- [[graphify_tests_test_install_strings]] → `contains` → [[graphify_tests_test_install_strings_test_report_is_still_referenced_as_fallback]]
- [[graphify_tests_test_install_strings]] → `contains` → [[graphify_tests_test_install_strings_test_skill_registration_uses_host_generic_instruction]]
- [[graphify_tests_test_install_strings_rationale_1]] → `rationale_for` → [[graphify_tests_test_install_strings]]
- [[graphify_tests_test_install_strings_rationale_51]] → `rationale_for` → [[graphify_tests_test_install_strings_test_every_install_surface_recommends_graphify_query]]
- [[graphify_tests_test_install_strings_rationale_67]] → `rationale_for` → [[graphify_tests_test_install_strings_test_no_install_surface_demands_reading_the_full_report_first]]
- [[graphify_tests_test_install_strings_rationale_100]] → `rationale_for` → [[graphify_tests_test_install_strings_test_report_is_still_referenced_as_fallback]]