# graphify\tests\test_manifest_ingest.py

## Símbolos

- [[graphify_tests_test_manifest_ingest]] — code: test_manifest_ingest.py
- [[graphify_tests_test_manifest_ingest_write]] — code: _write()
- [[graphify_tests_test_manifest_ingest_test_manifests_classify_as_code_not_document]] — code: test_manifests_classify_as_code_not_document()
- [[graphify_tests_test_manifest_ingest_pkg_nodes]] — code: _pkg_nodes()
- [[graphify_tests_test_manifest_ingest_test_apm_parses_name_and_deps]] — code: test_apm_parses_name_and_deps()
- [[graphify_tests_test_manifest_ingest_test_pyproject_parses_pep508_deps]] — code: test_pyproject_parses_pep508_deps()
- [[graphify_tests_test_manifest_ingest_test_gomod_parses_module_and_requires]] — code: test_gomod_parses_module_and_requires()
- [[graphify_tests_test_manifest_ingest_test_pom_parses_artifact_and_deps]] — code: test_pom_parses_artifact_and_deps()
- [[graphify_tests_test_manifest_ingest_test_apm_dependency_collapses_to_single_canonical_node]] — code: test_apm_dependency_collapses_to_single_canonical_node()
- [[graphify_tests_test_manifest_ingest_test_external_dependency_edge_pruned_not_orphaned]] — code: test_external_dependency_edge_pruned_not_orphaned()
- [[graphify_tests_test_manifest_ingest_test_malformed_manifest_does_not_crash]] — code: test_malformed_manifest_does_not_crash()

## Dependências

- [[graphify_tests_test_manifest_ingest]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_tests_test_manifest_ingest]] → `imports_from` → [[graphify_graphify_detect]]
- [[graphify_tests_test_manifest_ingest_test_manifests_classify_as_code_not_document]] → `calls` → [[graphify_graphify_detect_classify_file]]
- [[graphify_tests_test_manifest_ingest]] → `imports_from` → [[graphify_graphify_extract]]
- [[graphify_tests_test_manifest_ingest_test_apm_dependency_collapses_to_single_canonical_node]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_manifest_ingest_test_external_dependency_edge_pruned_not_orphaned]] → `calls` → [[graphify_graphify_extract_extract]]
- [[graphify_tests_test_manifest_ingest]] → `imports_from` → [[graphify_graphify_manifest_ingest]]
- [[graphify_tests_test_manifest_ingest_test_manifests_classify_as_code_not_document]] → `calls` → [[graphify_graphify_manifest_ingest_is_package_manifest_path]]
- [[graphify_tests_test_manifest_ingest_test_apm_parses_name_and_deps]] → `calls` → [[graphify_graphify_manifest_ingest_extract_package_manifest]]
- [[graphify_tests_test_manifest_ingest_test_gomod_parses_module_and_requires]] → `calls` → [[graphify_graphify_manifest_ingest_extract_package_manifest]]
- [[graphify_tests_test_manifest_ingest_test_malformed_manifest_does_not_crash]] → `calls` → [[graphify_graphify_manifest_ingest_extract_package_manifest]]
- [[graphify_tests_test_manifest_ingest_test_pom_parses_artifact_and_deps]] → `calls` → [[graphify_graphify_manifest_ingest_extract_package_manifest]]
- [[graphify_tests_test_manifest_ingest_test_pyproject_parses_pep508_deps]] → `calls` → [[graphify_graphify_manifest_ingest_extract_package_manifest]]
- [[graphify_tests_test_manifest_ingest]] → `contains` → [[graphify_tests_test_manifest_ingest_pkg_nodes]]
- [[graphify_tests_test_manifest_ingest]] → `contains` → [[graphify_tests_test_manifest_ingest_test_apm_dependency_collapses_to_single_canonical_node]]
- [[graphify_tests_test_manifest_ingest]] → `contains` → [[graphify_tests_test_manifest_ingest_test_apm_parses_name_and_deps]]
- [[graphify_tests_test_manifest_ingest]] → `contains` → [[graphify_tests_test_manifest_ingest_test_external_dependency_edge_pruned_not_orphaned]]
- [[graphify_tests_test_manifest_ingest]] → `contains` → [[graphify_tests_test_manifest_ingest_test_gomod_parses_module_and_requires]]
- [[graphify_tests_test_manifest_ingest]] → `contains` → [[graphify_tests_test_manifest_ingest_test_malformed_manifest_does_not_crash]]
- [[graphify_tests_test_manifest_ingest]] → `contains` → [[graphify_tests_test_manifest_ingest_test_manifests_classify_as_code_not_document]]
- [[graphify_tests_test_manifest_ingest]] → `contains` → [[graphify_tests_test_manifest_ingest_test_pom_parses_artifact_and_deps]]
- [[graphify_tests_test_manifest_ingest]] → `contains` → [[graphify_tests_test_manifest_ingest_test_pyproject_parses_pep508_deps]]
- [[graphify_tests_test_manifest_ingest]] → `contains` → [[graphify_tests_test_manifest_ingest_write]]
- [[graphify_tests_test_manifest_ingest_test_apm_dependency_collapses_to_single_canonical_node]] → `calls` → [[graphify_tests_test_manifest_ingest_write]]
- [[graphify_tests_test_manifest_ingest_test_apm_parses_name_and_deps]] → `calls` → [[graphify_tests_test_manifest_ingest_write]]
- [[graphify_tests_test_manifest_ingest_test_external_dependency_edge_pruned_not_orphaned]] → `calls` → [[graphify_tests_test_manifest_ingest_write]]
- [[graphify_tests_test_manifest_ingest_test_gomod_parses_module_and_requires]] → `calls` → [[graphify_tests_test_manifest_ingest_write]]
- [[graphify_tests_test_manifest_ingest_test_malformed_manifest_does_not_crash]] → `calls` → [[graphify_tests_test_manifest_ingest_write]]
- [[graphify_tests_test_manifest_ingest_test_manifests_classify_as_code_not_document]] → `calls` → [[graphify_tests_test_manifest_ingest_write]]
- [[graphify_tests_test_manifest_ingest_test_pom_parses_artifact_and_deps]] → `calls` → [[graphify_tests_test_manifest_ingest_write]]
- [[graphify_tests_test_manifest_ingest_test_pyproject_parses_pep508_deps]] → `calls` → [[graphify_tests_test_manifest_ingest_write]]
- [[graphify_tests_test_manifest_ingest_write]] → `references` → [[graphify_tests_test_manifest_ingest_py_path]]
- [[graphify_tests_test_manifest_ingest_test_apm_parses_name_and_deps]] → `calls` → [[graphify_tests_test_manifest_ingest_pkg_nodes]]
- [[graphify_tests_test_manifest_ingest_test_gomod_parses_module_and_requires]] → `calls` → [[graphify_tests_test_manifest_ingest_pkg_nodes]]
- [[graphify_tests_test_manifest_ingest_test_pom_parses_artifact_and_deps]] → `calls` → [[graphify_tests_test_manifest_ingest_pkg_nodes]]
- [[graphify_tests_test_manifest_ingest_test_pyproject_parses_pep508_deps]] → `calls` → [[graphify_tests_test_manifest_ingest_pkg_nodes]]