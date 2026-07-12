# assistant\tests\unit\obsidian\test_vault_watcher.py

## Símbolos

- [[assistant_tests_unit_obsidian_test_vault_watcher]] — code: test_vault_watcher.py
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler]] — code: TestVaultEventHandler
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_is_markdown_positive]] — code: .test_is_markdown_positive()
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_is_markdown_negative_extension]] — code: .test_is_markdown_negative_extension()
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_is_markdown_hidden_file]] — code: .test_is_markdown_hidden_file()
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_on_created_triggers_index]] — code: .test_on_created_triggers_index()
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_on_created_skips_directory]] — code: .test_on_created_skips_directory()
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_on_modified_triggers_index]] — code: .test_on_modified_triggers_index()
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_on_deleted_triggers_remove]] — code: .test_on_deleted_triggers_remove()
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher]] — code: TestVaultWatcher
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher_test_start_schedules_observer]] — code: .test_start_schedules_observer()
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher_test_start_skips_when_vault_path_empty]] — code: .test_start_skips_when_vault_path_empty()
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher_test_stop_observer]] — code: .test_stop_observer()

## Dependências

- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_is_markdown_hidden_file]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_is_markdown_negative_extension]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_is_markdown_positive]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_on_created_skips_directory]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_on_created_triggers_index]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_on_deleted_triggers_remove]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_on_modified_triggers_index]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler]] → `uses` → [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher]] → `uses` → [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher_test_start_schedules_observer]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher_test_start_skips_when_vault_path_empty]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher_test_stop_observer]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher]]
- [[assistant_tests_unit_obsidian_test_vault_watcher]] → `contains` → [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler]]
- [[assistant_tests_unit_obsidian_test_vault_watcher]] → `contains` → [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler]] → `method` → [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_is_markdown_hidden_file]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler]] → `method` → [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_is_markdown_negative_extension]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler]] → `method` → [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_is_markdown_positive]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler]] → `method` → [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_on_created_skips_directory]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler]] → `method` → [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_on_created_triggers_index]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler]] → `method` → [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_on_deleted_triggers_remove]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler]] → `method` → [[assistant_tests_unit_obsidian_test_vault_watcher_testvaulteventhandler_test_on_modified_triggers_index]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher]] → `method` → [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher_test_start_schedules_observer]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher]] → `method` → [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher_test_start_skips_when_vault_path_empty]]
- [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher]] → `method` → [[assistant_tests_unit_obsidian_test_vault_watcher_testvaultwatcher_test_stop_observer]]