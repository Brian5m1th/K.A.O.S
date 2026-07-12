# assistant\tests\unit\obsidian\test_obsidian_service.py

## Símbolos

- [[assistant_tests_unit_obsidian_test_obsidian_service]] — code: test_obsidian_service.py
- [[assistant_tests_unit_obsidian_test_obsidian_service_vault]] — code: vault()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_create_and_read_note]] — code: test_create_and_read_note()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_create_note_duplicate_raises]] — code: test_create_note_duplicate_raises()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_read_nonexistent_raises]] — code: test_read_nonexistent_raises()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_update_note_overwrite]] — code: test_update_note_overwrite()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_update_note_append]] — code: test_update_note_append()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_delete_note]] — code: test_delete_note()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_delete_nonexistent_raises]] — code: test_delete_nonexistent_raises()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_list_notes]] — code: test_list_notes()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_list_notes_empty_folder]] — code: test_list_notes_empty_folder()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_search_finds_keyword]] — code: test_search_finds_keyword()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_search_no_match]] — code: test_search_no_match()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_search_max_results]] — code: test_search_max_results()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_path_traversal_protection]] — code: test_path_traversal_protection()
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_special_chars_in_title]] — code: test_special_chars_in_title()

## Dependências

- [[assistant_tests_unit_obsidian_test_obsidian_service_test_create_and_read_note]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_create_note_duplicate_raises]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_delete_nonexistent_raises]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_delete_note]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_list_notes]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_list_notes_empty_folder]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_path_traversal_protection]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_read_nonexistent_raises]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_search_finds_keyword]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_search_max_results]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_search_no_match]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_special_chars_in_title]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_update_note_append]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_update_note_overwrite]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_create_and_read_note]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_create_note_duplicate_raises]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_delete_nonexistent_raises]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_delete_note]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_list_notes]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_list_notes_empty_folder]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_path_traversal_protection]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_read_nonexistent_raises]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_search_finds_keyword]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_search_max_results]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_search_no_match]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_special_chars_in_title]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_update_note_append]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_test_update_note_overwrite]]
- [[assistant_tests_unit_obsidian_test_obsidian_service]] → `contains` → [[assistant_tests_unit_obsidian_test_obsidian_service_vault]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_vault]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_create_and_read_note]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_create_note_duplicate_raises]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_delete_nonexistent_raises]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_delete_note]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_list_notes]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_list_notes_empty_folder]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_path_traversal_protection]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_read_nonexistent_raises]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_search_finds_keyword]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_search_max_results]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_search_no_match]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_special_chars_in_title]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_update_note_append]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]
- [[assistant_tests_unit_obsidian_test_obsidian_service_test_update_note_overwrite]] → `references` → [[assistant_tests_unit_obsidian_test_obsidian_service_py_path]]