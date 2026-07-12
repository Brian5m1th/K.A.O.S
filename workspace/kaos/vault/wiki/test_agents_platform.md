# graphify\tests\test_agents_platform.py

## Símbolos

- [[graphify_tests_test_agents_platform]] — code: test_agents_platform.py
- [[graphify_tests_test_agents_platform_test_agents_user_destination_is_user_global_dot_agents]] — code: test_agents_user_destination_is_user_global_dot_agents()
- [[graphify_tests_test_agents_platform_test_agents_project_destination_is_dot_agents]] — code: test_agents_project_destination_is_dot_agents()
- [[graphify_tests_test_agents_platform_test_skills_alias_resolves_to_agents]] — code: test_skills_alias_resolves_to_agents()
- [[graphify_tests_test_agents_platform_run]] — code: _run()
- [[graphify_tests_test_agents_platform_test_install_platform_agents_writes_user_global_skill_only]] — code: test_install_platform_agents_writes_user_global_skill_only()
- [[graphify_tests_test_agents_platform_test_uninstall_platform_agents_removes_user_global_skill]] — code: test_uninstall_platform_agents_removes_user_global_skill()
- [[graphify_tests_test_agents_platform_test_uninstall_platform_flag_global_removes_skill]] — code: test_uninstall_platform_flag_global_removes_skill()
- [[graphify_tests_test_agents_platform_test_project_uninstall_all_removes_agents_skill]] — code: test_project_uninstall_all_removes_agents_skill()
- [[graphify_tests_test_agents_platform_test_install_platform_agents_project_writes_dot_agents]] — code: test_install_platform_agents_project_writes_dot_agents()
- [[graphify_tests_test_agents_platform_test_agents_subcommand_install_also_wires_agents_md]] — code: test_agents_subcommand_install_also_wires_agents_md()
- [[graphify_tests_test_agents_platform_test_agents_subcommand_install_is_idempotent]] — code: test_agents_subcommand_install_is_idempotent()
- [[graphify_tests_test_agents_platform_test_skills_subcommand_is_the_agents_subcommand]] — code: test_skills_subcommand_is_the_agents_subcommand()
- [[graphify_tests_test_agents_platform_test_bare_install_does_not_touch_dot_agents]] — code: test_bare_install_does_not_touch_dot_agents()
- [[graphify_tests_test_agents_platform_rationale_1]] — code: Tests for the generic `agents` platform and its `skills` alias (#1432).  `grap
- [[graphify_tests_test_agents_platform_rationale_26]] — code: Global agents skill lands at ~/.agents/skills (the spec's user-global dir),
- [[graphify_tests_test_agents_platform_rationale_34]] — code: Project agents skill lands at ./.agents/skills.
- [[graphify_tests_test_agents_platform_rationale_53]] — code: Drive main() with argv, cwd at tmp_path, and Path.home redirected.
- [[graphify_tests_test_agents_platform_rationale_66]] — code: `graphify install --platform agents|skills` writes ~/.agents/skills/...     SKI
- [[graphify_tests_test_agents_platform_rationale_85]] — code: Bare `graphify uninstall` clears the ~/.agents/skills skill the AGENTS.md and
- [[graphify_tests_test_agents_platform_rationale_104]] — code: `graphify uninstall --platform agents|skills` (global) clears ~/.agents/skills.
- [[graphify_tests_test_agents_platform_rationale_124]] — code: `graphify uninstall --project` (no platform) removes the agents project skill
- [[graphify_tests_test_agents_platform_rationale_141]] — code: `graphify install --project --platform agents` writes ./.agents/skills and
- [[graphify_tests_test_agents_platform_rationale_164]] — code: `graphify agents install` is the amp-twin: skill at ~/.agents/skills PLUS a
- [[graphify_tests_test_agents_platform_rationale_188]] — code: Running `graphify agents install` twice leaves a single AGENTS.md section.
- [[graphify_tests_test_agents_platform_rationale_202]] — code: `graphify skills install`/`uninstall` behaves exactly like the agents form:
- [[graphify_tests_test_agents_platform_rationale_227]] — code: `graphify install` (no platform) stays single-platform claude/windows and     n

## Dependências

- [[graphify_tests_test_agents_platform]] → `imports` → [[graphify_graphify_main]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_run]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_test_agents_project_destination_is_dot_agents]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_test_agents_subcommand_install_also_wires_agents_md]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_test_agents_subcommand_install_is_idempotent]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_test_agents_user_destination_is_user_global_dot_agents]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_test_bare_install_does_not_touch_dot_agents]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_test_install_platform_agents_project_writes_dot_agents]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_test_install_platform_agents_writes_user_global_skill_only]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_test_project_uninstall_all_removes_agents_skill]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_test_skills_alias_resolves_to_agents]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_test_skills_subcommand_is_the_agents_subcommand]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_test_uninstall_platform_agents_removes_user_global_skill]]
- [[graphify_tests_test_agents_platform]] → `contains` → [[graphify_tests_test_agents_platform_test_uninstall_platform_flag_global_removes_skill]]
- [[graphify_tests_test_agents_platform_rationale_1]] → `rationale_for` → [[graphify_tests_test_agents_platform]]
- [[graphify_tests_test_agents_platform_rationale_26]] → `rationale_for` → [[graphify_tests_test_agents_platform_test_agents_user_destination_is_user_global_dot_agents]]
- [[graphify_tests_test_agents_platform_rationale_34]] → `rationale_for` → [[graphify_tests_test_agents_platform_test_agents_project_destination_is_dot_agents]]
- [[graphify_tests_test_agents_platform_rationale_53]] → `rationale_for` → [[graphify_tests_test_agents_platform_run]]
- [[graphify_tests_test_agents_platform_test_agents_subcommand_install_also_wires_agents_md]] → `calls` → [[graphify_tests_test_agents_platform_run]]
- [[graphify_tests_test_agents_platform_test_agents_subcommand_install_is_idempotent]] → `calls` → [[graphify_tests_test_agents_platform_run]]
- [[graphify_tests_test_agents_platform_test_bare_install_does_not_touch_dot_agents]] → `calls` → [[graphify_tests_test_agents_platform_run]]
- [[graphify_tests_test_agents_platform_test_install_platform_agents_project_writes_dot_agents]] → `calls` → [[graphify_tests_test_agents_platform_run]]
- [[graphify_tests_test_agents_platform_test_install_platform_agents_writes_user_global_skill_only]] → `calls` → [[graphify_tests_test_agents_platform_run]]
- [[graphify_tests_test_agents_platform_test_project_uninstall_all_removes_agents_skill]] → `calls` → [[graphify_tests_test_agents_platform_run]]
- [[graphify_tests_test_agents_platform_test_skills_subcommand_is_the_agents_subcommand]] → `calls` → [[graphify_tests_test_agents_platform_run]]
- [[graphify_tests_test_agents_platform_test_uninstall_platform_agents_removes_user_global_skill]] → `calls` → [[graphify_tests_test_agents_platform_run]]
- [[graphify_tests_test_agents_platform_test_uninstall_platform_flag_global_removes_skill]] → `calls` → [[graphify_tests_test_agents_platform_run]]
- [[graphify_tests_test_agents_platform_rationale_66]] → `rationale_for` → [[graphify_tests_test_agents_platform_test_install_platform_agents_writes_user_global_skill_only]]
- [[graphify_tests_test_agents_platform_rationale_85]] → `rationale_for` → [[graphify_tests_test_agents_platform_test_uninstall_platform_agents_removes_user_global_skill]]
- [[graphify_tests_test_agents_platform_rationale_104]] → `rationale_for` → [[graphify_tests_test_agents_platform_test_uninstall_platform_flag_global_removes_skill]]
- [[graphify_tests_test_agents_platform_rationale_124]] → `rationale_for` → [[graphify_tests_test_agents_platform_test_project_uninstall_all_removes_agents_skill]]
- [[graphify_tests_test_agents_platform_rationale_141]] → `rationale_for` → [[graphify_tests_test_agents_platform_test_install_platform_agents_project_writes_dot_agents]]
- [[graphify_tests_test_agents_platform_rationale_164]] → `rationale_for` → [[graphify_tests_test_agents_platform_test_agents_subcommand_install_also_wires_agents_md]]
- [[graphify_tests_test_agents_platform_rationale_188]] → `rationale_for` → [[graphify_tests_test_agents_platform_test_agents_subcommand_install_is_idempotent]]
- [[graphify_tests_test_agents_platform_rationale_202]] → `rationale_for` → [[graphify_tests_test_agents_platform_test_skills_subcommand_is_the_agents_subcommand]]
- [[graphify_tests_test_agents_platform_rationale_227]] → `rationale_for` → [[graphify_tests_test_agents_platform_test_bare_install_does_not_touch_dot_agents]]