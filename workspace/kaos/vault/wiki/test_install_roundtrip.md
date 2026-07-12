# graphify\tests\test_install_roundtrip.py

## Símbolos

- [[graphify_tests_test_install_roundtrip]] — code: test_install_roundtrip.py
- [[graphify_tests_test_install_roundtrip_has_real_bundle]] — code: _has_real_bundle()
- [[graphify_tests_test_install_roundtrip_test_skill_roundtrip_at_real_destination]] — code: test_skill_roundtrip_at_real_destination()
- [[graphify_tests_test_install_roundtrip_test_amp_user_install_at_corrected_agents_path]] — code: test_amp_user_install_at_corrected_agents_path()
- [[graphify_tests_test_install_roundtrip_test_amp_project_install_at_agents_path]] — code: test_amp_project_install_at_agents_path()
- [[graphify_tests_test_install_roundtrip_test_vscode_install_uninstall_roundtrip]] — code: test_vscode_install_uninstall_roundtrip()
- [[graphify_tests_test_install_roundtrip_install_via_entrypoint]] — code: _install_via_entrypoint()
- [[graphify_tests_test_install_roundtrip_copy_in_tmp]] — code: _copy_in_tmp()
- [[graphify_tests_test_install_roundtrip_test_install_entrypoint_roundtrip_for_progressive_and_monolith]] — code: test_install_entrypoint_roundtrip_for_progressive_and_monolith()
- [[graphify_tests_test_install_roundtrip_fake_progressive_bundle]] — code: fake_progressive_bundle()
- [[graphify_tests_test_install_roundtrip_test_monolith_to_progressive_upgrade]] — code: test_monolith_to_progressive_upgrade()
- [[graphify_tests_test_install_roundtrip_test_progressive_to_monolith_downgrade_clears_references]] — code: test_progressive_to_monolith_downgrade_clears_references()
- [[graphify_tests_test_install_roundtrip_test_interrupted_references_staging_self_heals]] — code: test_interrupted_references_staging_self_heals()
- [[graphify_tests_test_install_roundtrip_test_failed_copytree_leaves_no_partial_references]] — code: test_failed_copytree_leaves_no_partial_references()
- [[graphify_tests_test_install_roundtrip_rationale_1]] — code: Full per-platform install + uninstall round-trip suite.  Every platform graphi
- [[graphify_tests_test_install_roundtrip_rationale_39]] — code: True if this platform's references bundle ships in the package right now.
- [[graphify_tests_test_install_roundtrip_rationale_49]] — code: Install then uninstall every platform's SKILL.md at its real destination.
- [[graphify_tests_test_install_roundtrip_rationale_98]] — code: amp's user-scope skill lands under ~/.config/agents/skills (the fix), not ~/.amp
- [[graphify_tests_test_install_roundtrip_rationale_113]] — code: amp's project-scope skill lands under .agents/skills, an Amp search root.
- [[graphify_tests_test_install_roundtrip_rationale_126]] — code: VS Code Copilot Chat round trip at ~/.copilot/skills/graphify + instructions fil
- [[graphify_tests_test_install_roundtrip_rationale_151]] — code: Drive the high-level install() entry point with home + cwd in tmp_path.
- [[graphify_tests_test_install_roundtrip_rationale_162]] — code: Run _copy_skill_file with home + cwd redirected into tmp_path, restoring cwd.
- [[graphify_tests_test_install_roundtrip_rationale_173]] — code: The public install() entry point round-trips a progressive and a monolith host.
- [[graphify_tests_test_install_roundtrip_rationale_200]] — code: Stage a controllable references bundle in claude's slot.      Lets a test flip
- [[graphify_tests_test_install_roundtrip_rationale_234]] — code: A pre-progressive install (SKILL.md, no references/) gains references/ on upgrad
- [[graphify_tests_test_install_roundtrip_rationale_255]] — code: If a host loses its bundle, the next install clears the orphan references/.
- [[graphify_tests_test_install_roundtrip_rationale_275]] — code: A leftover references.tmp from a crashed install is cleared on the next install.
- [[graphify_tests_test_install_roundtrip_rationale_297]] — code: If copytree blows up mid-stage, no half-written references/ is left visible.

## Dependências

- [[graphify_tests_test_install_roundtrip]] → `imports` → [[graphify_graphify_main]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_copy_in_tmp]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_fake_progressive_bundle]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_has_real_bundle]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_install_via_entrypoint]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_test_amp_project_install_at_agents_path]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_test_amp_user_install_at_corrected_agents_path]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_test_failed_copytree_leaves_no_partial_references]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_test_install_entrypoint_roundtrip_for_progressive_and_monolith]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_test_interrupted_references_staging_self_heals]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_test_monolith_to_progressive_upgrade]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_test_progressive_to_monolith_downgrade_clears_references]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_test_skill_roundtrip_at_real_destination]]
- [[graphify_tests_test_install_roundtrip]] → `contains` → [[graphify_tests_test_install_roundtrip_test_vscode_install_uninstall_roundtrip]]
- [[graphify_tests_test_install_roundtrip_rationale_1]] → `rationale_for` → [[graphify_tests_test_install_roundtrip]]
- [[graphify_tests_test_install_roundtrip_rationale_39]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_has_real_bundle]]
- [[graphify_tests_test_install_roundtrip_test_install_entrypoint_roundtrip_for_progressive_and_monolith]] → `calls` → [[graphify_tests_test_install_roundtrip_has_real_bundle]]
- [[graphify_tests_test_install_roundtrip_test_skill_roundtrip_at_real_destination]] → `calls` → [[graphify_tests_test_install_roundtrip_has_real_bundle]]
- [[graphify_tests_test_install_roundtrip_rationale_49]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_test_skill_roundtrip_at_real_destination]]
- [[graphify_tests_test_install_roundtrip_rationale_98]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_test_amp_user_install_at_corrected_agents_path]]
- [[graphify_tests_test_install_roundtrip_rationale_113]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_test_amp_project_install_at_agents_path]]
- [[graphify_tests_test_install_roundtrip_rationale_126]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_test_vscode_install_uninstall_roundtrip]]
- [[graphify_tests_test_install_roundtrip_rationale_151]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_install_via_entrypoint]]
- [[graphify_tests_test_install_roundtrip_test_install_entrypoint_roundtrip_for_progressive_and_monolith]] → `calls` → [[graphify_tests_test_install_roundtrip_install_via_entrypoint]]
- [[graphify_tests_test_install_roundtrip_rationale_162]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_copy_in_tmp]]
- [[graphify_tests_test_install_roundtrip_test_interrupted_references_staging_self_heals]] → `calls` → [[graphify_tests_test_install_roundtrip_copy_in_tmp]]
- [[graphify_tests_test_install_roundtrip_test_monolith_to_progressive_upgrade]] → `calls` → [[graphify_tests_test_install_roundtrip_copy_in_tmp]]
- [[graphify_tests_test_install_roundtrip_test_progressive_to_monolith_downgrade_clears_references]] → `calls` → [[graphify_tests_test_install_roundtrip_copy_in_tmp]]
- [[graphify_tests_test_install_roundtrip_rationale_173]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_test_install_entrypoint_roundtrip_for_progressive_and_monolith]]
- [[graphify_tests_test_install_roundtrip_rationale_200]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_fake_progressive_bundle]]
- [[graphify_tests_test_install_roundtrip_rationale_234]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_test_monolith_to_progressive_upgrade]]
- [[graphify_tests_test_install_roundtrip_rationale_255]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_test_progressive_to_monolith_downgrade_clears_references]]
- [[graphify_tests_test_install_roundtrip_rationale_275]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_test_interrupted_references_staging_self_heals]]
- [[graphify_tests_test_install_roundtrip_rationale_297]] → `rationale_for` → [[graphify_tests_test_install_roundtrip_test_failed_copytree_leaves_no_partial_references]]