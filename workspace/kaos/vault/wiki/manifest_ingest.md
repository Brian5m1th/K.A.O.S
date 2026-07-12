# graphify\graphify\manifest_ingest.py

## Símbolos

- [[graphify_graphify_manifest_ingest]] — code: manifest_ingest.py
- [[graphify_graphify_manifest_ingest_is_package_manifest_path]] — code: is_package_manifest_path()
- [[graphify_graphify_manifest_ingest_pkg_id]] — code: _pkg_id()
- [[graphify_graphify_manifest_ingest_extract_package_manifest]] — code: extract_package_manifest()
- [[graphify_graphify_manifest_ingest_coerce_deps]] — code: _coerce_deps()
- [[graphify_graphify_manifest_ingest_parse_apm]] — code: _parse_apm()
- [[graphify_graphify_manifest_ingest_parse_apm_fallback]] — code: _parse_apm_fallback()
- [[graphify_graphify_manifest_ingest_pep508_name]] — code: _pep508_name()
- [[graphify_graphify_manifest_ingest_parse_pyproject]] — code: _parse_pyproject()
- [[graphify_graphify_manifest_ingest_parse_gomod]] — code: _parse_gomod()
- [[graphify_graphify_manifest_ingest_parse_pom]] — code: _parse_pom()
- [[graphify_graphify_manifest_ingest_rationale_1]] — code: Deterministic package-manifest ingestion (#1377).  Package manifests (``apm.ym
- [[graphify_graphify_manifest_ingest_rationale_40]] — code: True if ``path`` is a recognized package manifest (by filename).
- [[graphify_graphify_manifest_ingest_rationale_45]] — code: Canonical package node id, keyed by package NAME so every reference to the
- [[graphify_graphify_manifest_ingest_rationale_52]] — code: Parse a package manifest into a canonical package node + ``depends_on`` edges.
- [[graphify_graphify_manifest_ingest_rationale_115]] — code: A dependency block may be a list of names or a name->spec map.
- [[graphify_graphify_manifest_ingest_rationale_145]] — code: Minimal line parser for apm.yml when PyYAML is unavailable: a top-level     ``n
- [[graphify_graphify_manifest_ingest_rationale_170]] — code: `requests>=2.0` -> `requests`; `pkg[extra]==1; python_version<'3.9'` -> `pkg`.

## Dependências

- [[graphify_graphify_manifest_ingest]] → `imports_from` → [[graphify_graphify_ids]]
- [[graphify_graphify_manifest_ingest_pkg_id]] → `calls` → [[graphify_graphify_ids_make_id]]
- [[graphify_graphify_manifest_ingest]] → `contains` → [[graphify_graphify_manifest_ingest_coerce_deps]]
- [[graphify_graphify_manifest_ingest]] → `contains` → [[graphify_graphify_manifest_ingest_extract_package_manifest]]
- [[graphify_graphify_manifest_ingest]] → `contains` → [[graphify_graphify_manifest_ingest_is_package_manifest_path]]
- [[graphify_graphify_manifest_ingest]] → `indirect_call` → [[graphify_graphify_manifest_ingest_parse_apm]]
- [[graphify_graphify_manifest_ingest]] → `contains` → [[graphify_graphify_manifest_ingest_parse_apm_fallback]]
- [[graphify_graphify_manifest_ingest]] → `indirect_call` → [[graphify_graphify_manifest_ingest_parse_gomod]]
- [[graphify_graphify_manifest_ingest]] → `indirect_call` → [[graphify_graphify_manifest_ingest_parse_pom]]
- [[graphify_graphify_manifest_ingest]] → `indirect_call` → [[graphify_graphify_manifest_ingest_parse_pyproject]]
- [[graphify_graphify_manifest_ingest]] → `contains` → [[graphify_graphify_manifest_ingest_pep508_name]]
- [[graphify_graphify_manifest_ingest]] → `contains` → [[graphify_graphify_manifest_ingest_pkg_id]]
- [[graphify_graphify_manifest_ingest_rationale_1]] → `rationale_for` → [[graphify_graphify_manifest_ingest]]
- [[graphify_graphify_manifest_ingest_is_package_manifest_path]] → `references` → [[graphify_graphify_manifest_ingest_py_path]]
- [[graphify_graphify_manifest_ingest_rationale_40]] → `rationale_for` → [[graphify_graphify_manifest_ingest_is_package_manifest_path]]
- [[graphify_graphify_manifest_ingest_extract_package_manifest]] → `references` → [[graphify_graphify_manifest_ingest_py_path]]
- [[graphify_graphify_manifest_ingest_extract_package_manifest]] → `calls` → [[graphify_graphify_manifest_ingest_pkg_id]]
- [[graphify_graphify_manifest_ingest_rationale_45]] → `rationale_for` → [[graphify_graphify_manifest_ingest_pkg_id]]
- [[graphify_graphify_manifest_ingest_extract_package_manifest]] → `references` → [[graphify_graphify_manifest_ingest_py_any]]
- [[graphify_graphify_manifest_ingest_rationale_52]] → `rationale_for` → [[graphify_graphify_manifest_ingest_extract_package_manifest]]
- [[graphify_graphify_manifest_ingest_coerce_deps]] → `references` → [[graphify_graphify_manifest_ingest_py_any]]
- [[graphify_graphify_manifest_ingest_parse_apm]] → `calls` → [[graphify_graphify_manifest_ingest_coerce_deps]]
- [[graphify_graphify_manifest_ingest_rationale_115]] → `rationale_for` → [[graphify_graphify_manifest_ingest_coerce_deps]]
- [[graphify_graphify_manifest_ingest_parse_apm]] → `calls` → [[graphify_graphify_manifest_ingest_parse_apm_fallback]]
- [[graphify_graphify_manifest_ingest_rationale_145]] → `rationale_for` → [[graphify_graphify_manifest_ingest_parse_apm_fallback]]
- [[graphify_graphify_manifest_ingest_parse_pyproject]] → `calls` → [[graphify_graphify_manifest_ingest_pep508_name]]
- [[graphify_graphify_manifest_ingest_rationale_170]] → `rationale_for` → [[graphify_graphify_manifest_ingest_pep508_name]]