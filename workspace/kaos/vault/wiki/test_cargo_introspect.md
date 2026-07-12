# graphify\tests\test_cargo_introspect.py

## Símbolos

- [[graphify_tests_test_cargo_introspect]] — code: test_cargo_introspect.py
- [[graphify_tests_test_cargo_introspect_write_manifest]] — code: _write_manifest()
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_workspace_internal_dependency_only]] — code: test_cargo_introspect_workspace_internal_dependency_only()
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_malformed_toml_reports_parser_error]] — code: test_cargo_introspect_malformed_toml_reports_parser_error()
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_degenerate_manifests_return_empty_or_skip_bad_deps]] — code: test_cargo_introspect_degenerate_manifests_return_empty_or_skip_bad_deps()
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_old_manifest_keeps_internal_path_dep_and_skips_external]] — code: test_cargo_introspect_old_manifest_keeps_internal_path_dep_and_skips_external()
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_modern_virtual_and_root_package_workspaces]] — code: test_cargo_introspect_modern_virtual_and_root_package_workspaces()
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_large_workspace_dependency_chain]] — code: test_cargo_introspect_large_workspace_dependency_chain()
- [[graphify_tests_test_cargo_introspect_rationale_11]] — code: Real workspace: pin raw graph fields while excluding registry-only deps.
- [[graphify_tests_test_cargo_introspect_rationale_77]] — code: Malformed manifests surface the TOML parser failure, not an arbitrary crash.
- [[graphify_tests_test_cargo_introspect_rationale_94]] — code: Degenerate but parseable manifests should not invent graph data or crash.
- [[graphify_tests_test_cargo_introspect_rationale_148]] — code: Legacy manifests still resolve path deps and ignore bare-string externals.
- [[graphify_tests_test_cargo_introspect_rationale_195]] — code: Modern workspace forms cover virtual roots, workspace deps, and root packages.
- [[graphify_tests_test_cargo_introspect_rationale_307]] — code: Large deterministic workspace proves chain extraction scales by shape, not timin

## Dependências

- [[graphify_tests_test_cargo_introspect]] → `imports_from` → [[graphify_graphify_cargo_introspect]]
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_degenerate_manifests_return_empty_or_skip_bad_deps]] → `calls` → [[graphify_graphify_cargo_introspect_introspect_cargo]]
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_large_workspace_dependency_chain]] → `calls` → [[graphify_graphify_cargo_introspect_introspect_cargo]]
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_malformed_toml_reports_parser_error]] → `calls` → [[graphify_graphify_cargo_introspect_introspect_cargo]]
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_modern_virtual_and_root_package_workspaces]] → `calls` → [[graphify_graphify_cargo_introspect_introspect_cargo]]
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_old_manifest_keeps_internal_path_dep_and_skips_external]] → `calls` → [[graphify_graphify_cargo_introspect_introspect_cargo]]
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_workspace_internal_dependency_only]] → `calls` → [[graphify_graphify_cargo_introspect_introspect_cargo]]
- [[graphify_tests_test_cargo_introspect]] → `contains` → [[graphify_tests_test_cargo_introspect_test_cargo_introspect_degenerate_manifests_return_empty_or_skip_bad_deps]]
- [[graphify_tests_test_cargo_introspect]] → `contains` → [[graphify_tests_test_cargo_introspect_test_cargo_introspect_large_workspace_dependency_chain]]
- [[graphify_tests_test_cargo_introspect]] → `contains` → [[graphify_tests_test_cargo_introspect_test_cargo_introspect_malformed_toml_reports_parser_error]]
- [[graphify_tests_test_cargo_introspect]] → `contains` → [[graphify_tests_test_cargo_introspect_test_cargo_introspect_modern_virtual_and_root_package_workspaces]]
- [[graphify_tests_test_cargo_introspect]] → `contains` → [[graphify_tests_test_cargo_introspect_test_cargo_introspect_old_manifest_keeps_internal_path_dep_and_skips_external]]
- [[graphify_tests_test_cargo_introspect]] → `contains` → [[graphify_tests_test_cargo_introspect_test_cargo_introspect_workspace_internal_dependency_only]]
- [[graphify_tests_test_cargo_introspect]] → `contains` → [[graphify_tests_test_cargo_introspect_write_manifest]]
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_degenerate_manifests_return_empty_or_skip_bad_deps]] → `calls` → [[graphify_tests_test_cargo_introspect_write_manifest]]
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_large_workspace_dependency_chain]] → `calls` → [[graphify_tests_test_cargo_introspect_write_manifest]]
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_malformed_toml_reports_parser_error]] → `calls` → [[graphify_tests_test_cargo_introspect_write_manifest]]
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_modern_virtual_and_root_package_workspaces]] → `calls` → [[graphify_tests_test_cargo_introspect_write_manifest]]
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_old_manifest_keeps_internal_path_dep_and_skips_external]] → `calls` → [[graphify_tests_test_cargo_introspect_write_manifest]]
- [[graphify_tests_test_cargo_introspect_test_cargo_introspect_workspace_internal_dependency_only]] → `calls` → [[graphify_tests_test_cargo_introspect_write_manifest]]
- [[graphify_tests_test_cargo_introspect_rationale_11]] → `rationale_for` → [[graphify_tests_test_cargo_introspect_test_cargo_introspect_workspace_internal_dependency_only]]
- [[graphify_tests_test_cargo_introspect_rationale_77]] → `rationale_for` → [[graphify_tests_test_cargo_introspect_test_cargo_introspect_malformed_toml_reports_parser_error]]
- [[graphify_tests_test_cargo_introspect_rationale_94]] → `rationale_for` → [[graphify_tests_test_cargo_introspect_test_cargo_introspect_degenerate_manifests_return_empty_or_skip_bad_deps]]
- [[graphify_tests_test_cargo_introspect_rationale_148]] → `rationale_for` → [[graphify_tests_test_cargo_introspect_test_cargo_introspect_old_manifest_keeps_internal_path_dep_and_skips_external]]
- [[graphify_tests_test_cargo_introspect_rationale_195]] → `rationale_for` → [[graphify_tests_test_cargo_introspect_test_cargo_introspect_modern_virtual_and_root_package_workspaces]]
- [[graphify_tests_test_cargo_introspect_rationale_307]] → `rationale_for` → [[graphify_tests_test_cargo_introspect_test_cargo_introspect_large_workspace_dependency_chain]]