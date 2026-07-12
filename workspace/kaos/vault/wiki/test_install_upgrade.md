# graphify\tests\test_install_upgrade.py

## Símbolos

- [[graphify_tests_test_install_upgrade]] — code: test_install_upgrade.py
- [[graphify_tests_test_install_upgrade_assert_no_report_first]] — code: _assert_no_report_first()
- [[graphify_tests_test_install_upgrade_assert_query_first]] — code: _assert_query_first()
- [[graphify_tests_test_install_upgrade_test_claude_install_upgrades_stale_section]] — code: test_claude_install_upgrades_stale_section()
- [[graphify_tests_test_install_upgrade_test_claude_install_upgrades_stale_hook_payload]] — code: test_claude_install_upgrades_stale_hook_payload()
- [[graphify_tests_test_install_upgrade_test_agents_install_upgrades_stale_section]] — code: test_agents_install_upgrades_stale_section()
- [[graphify_tests_test_install_upgrade_test_gemini_install_upgrades_stale_section]] — code: test_gemini_install_upgrades_stale_section()
- [[graphify_tests_test_install_upgrade_test_vscode_install_upgrades_stale_section]] — code: test_vscode_install_upgrades_stale_section()
- [[graphify_tests_test_install_upgrade_test_cursor_install_upgrades_stale_rule]] — code: test_cursor_install_upgrades_stale_rule()
- [[graphify_tests_test_install_upgrade_test_kiro_install_upgrades_stale_steering]] — code: test_kiro_install_upgrades_stale_steering()
- [[graphify_tests_test_install_upgrade_test_kiro_install_ships_references_sidecar_and_version_stamp]] — code: test_kiro_install_ships_references_sidecar_and_version_stamp()
- [[graphify_tests_test_install_upgrade_rationale_1]] — code: Installer-level regression tests for upgrade-in-place behavior (issue #580).
- [[graphify_tests_test_install_upgrade_rationale_94]] — code: A pre-fix CLAUDE.md gets the new section in place when the user runs     `graph
- [[graphify_tests_test_install_upgrade_rationale_112]] — code: The Claude install must also rewrite a stale .claude/settings.json hook     pay
- [[graphify_tests_test_install_upgrade_rationale_159]] — code: Same upgrade behavior for AGENTS.md (Codex / OpenCode / Aider / Trae).
- [[graphify_tests_test_install_upgrade_rationale_174]] — code: Same upgrade behavior for GEMINI.md.
- [[graphify_tests_test_install_upgrade_rationale_188]] — code: Same upgrade behavior for .github/copilot-instructions.md (VS Code).
- [[graphify_tests_test_install_upgrade_rationale_203]] — code: Same upgrade behavior for .cursor/rules/graphify.mdc.     The Cursor rule file
- [[graphify_tests_test_install_upgrade_rationale_221]] — code: Same upgrade behavior for .kiro/steering/graphify.md (wholly owned).
- [[graphify_tests_test_install_upgrade_rationale_242]] — code: _kiro_install routes through _copy_skill_file so the references/ sidecar     an

## Dependências

- [[graphify_tests_test_install_upgrade]] → `imports` → [[graphify_graphify_main]]
- [[graphify_tests_test_install_upgrade]] → `contains` → [[graphify_tests_test_install_upgrade_assert_no_report_first]]
- [[graphify_tests_test_install_upgrade]] → `contains` → [[graphify_tests_test_install_upgrade_assert_query_first]]
- [[graphify_tests_test_install_upgrade]] → `contains` → [[graphify_tests_test_install_upgrade_test_agents_install_upgrades_stale_section]]
- [[graphify_tests_test_install_upgrade]] → `contains` → [[graphify_tests_test_install_upgrade_test_claude_install_upgrades_stale_hook_payload]]
- [[graphify_tests_test_install_upgrade]] → `contains` → [[graphify_tests_test_install_upgrade_test_claude_install_upgrades_stale_section]]
- [[graphify_tests_test_install_upgrade]] → `contains` → [[graphify_tests_test_install_upgrade_test_cursor_install_upgrades_stale_rule]]
- [[graphify_tests_test_install_upgrade]] → `contains` → [[graphify_tests_test_install_upgrade_test_gemini_install_upgrades_stale_section]]
- [[graphify_tests_test_install_upgrade]] → `contains` → [[graphify_tests_test_install_upgrade_test_kiro_install_ships_references_sidecar_and_version_stamp]]
- [[graphify_tests_test_install_upgrade]] → `contains` → [[graphify_tests_test_install_upgrade_test_kiro_install_upgrades_stale_steering]]
- [[graphify_tests_test_install_upgrade]] → `contains` → [[graphify_tests_test_install_upgrade_test_vscode_install_upgrades_stale_section]]
- [[graphify_tests_test_install_upgrade_rationale_1]] → `rationale_for` → [[graphify_tests_test_install_upgrade]]
- [[graphify_tests_test_install_upgrade_test_agents_install_upgrades_stale_section]] → `calls` → [[graphify_tests_test_install_upgrade_assert_no_report_first]]
- [[graphify_tests_test_install_upgrade_test_claude_install_upgrades_stale_section]] → `calls` → [[graphify_tests_test_install_upgrade_assert_no_report_first]]
- [[graphify_tests_test_install_upgrade_test_gemini_install_upgrades_stale_section]] → `calls` → [[graphify_tests_test_install_upgrade_assert_no_report_first]]
- [[graphify_tests_test_install_upgrade_test_vscode_install_upgrades_stale_section]] → `calls` → [[graphify_tests_test_install_upgrade_assert_no_report_first]]
- [[graphify_tests_test_install_upgrade_test_agents_install_upgrades_stale_section]] → `calls` → [[graphify_tests_test_install_upgrade_assert_query_first]]
- [[graphify_tests_test_install_upgrade_test_claude_install_upgrades_stale_section]] → `calls` → [[graphify_tests_test_install_upgrade_assert_query_first]]
- [[graphify_tests_test_install_upgrade_test_cursor_install_upgrades_stale_rule]] → `calls` → [[graphify_tests_test_install_upgrade_assert_query_first]]
- [[graphify_tests_test_install_upgrade_test_gemini_install_upgrades_stale_section]] → `calls` → [[graphify_tests_test_install_upgrade_assert_query_first]]
- [[graphify_tests_test_install_upgrade_test_kiro_install_upgrades_stale_steering]] → `calls` → [[graphify_tests_test_install_upgrade_assert_query_first]]
- [[graphify_tests_test_install_upgrade_test_vscode_install_upgrades_stale_section]] → `calls` → [[graphify_tests_test_install_upgrade_assert_query_first]]
- [[graphify_tests_test_install_upgrade_rationale_94]] → `rationale_for` → [[graphify_tests_test_install_upgrade_test_claude_install_upgrades_stale_section]]
- [[graphify_tests_test_install_upgrade_rationale_112]] → `rationale_for` → [[graphify_tests_test_install_upgrade_test_claude_install_upgrades_stale_hook_payload]]
- [[graphify_tests_test_install_upgrade_rationale_159]] → `rationale_for` → [[graphify_tests_test_install_upgrade_test_agents_install_upgrades_stale_section]]
- [[graphify_tests_test_install_upgrade_rationale_174]] → `rationale_for` → [[graphify_tests_test_install_upgrade_test_gemini_install_upgrades_stale_section]]
- [[graphify_tests_test_install_upgrade_rationale_188]] → `rationale_for` → [[graphify_tests_test_install_upgrade_test_vscode_install_upgrades_stale_section]]
- [[graphify_tests_test_install_upgrade_rationale_203]] → `rationale_for` → [[graphify_tests_test_install_upgrade_test_cursor_install_upgrades_stale_rule]]
- [[graphify_tests_test_install_upgrade_rationale_221]] → `rationale_for` → [[graphify_tests_test_install_upgrade_test_kiro_install_upgrades_stale_steering]]
- [[graphify_tests_test_install_upgrade_rationale_242]] → `rationale_for` → [[graphify_tests_test_install_upgrade_test_kiro_install_ships_references_sidecar_and_version_stamp]]