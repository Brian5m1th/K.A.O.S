# graphify\graphify\cargo_introspect.py

## Símbolos

- [[graphify_graphify_cargo_introspect]] — code: cargo_introspect.py
- [[graphify_graphify_cargo_introspect_load_toml]] — code: _load_toml()
- [[graphify_graphify_cargo_introspect_member_manifest_paths]] — code: _member_manifest_paths()
- [[graphify_graphify_cargo_introspect_introspect_cargo]] — code: introspect_cargo()
- [[graphify_graphify_cargo_introspect_rationale_1]] — code: Cargo manifest introspection for workspace-internal crate dependencies.
- [[graphify_graphify_cargo_introspect_rationale_48]] — code: Return crate nodes and internal dependency edges from Cargo manifests.

## Dependências

- [[graphify_graphify_cargo_introspect]] → `contains` → [[graphify_graphify_cargo_introspect_introspect_cargo]]
- [[graphify_graphify_cargo_introspect]] → `contains` → [[graphify_graphify_cargo_introspect_load_toml]]
- [[graphify_graphify_cargo_introspect]] → `contains` → [[graphify_graphify_cargo_introspect_member_manifest_paths]]
- [[graphify_graphify_cargo_introspect_rationale_1]] → `rationale_for` → [[graphify_graphify_cargo_introspect]]
- [[graphify_graphify_cargo_introspect_introspect_cargo]] → `calls` → [[graphify_graphify_cargo_introspect_load_toml]]
- [[graphify_graphify_cargo_introspect_load_toml]] → `references` → [[graphify_graphify_cargo_introspect_py_any]]
- [[graphify_graphify_cargo_introspect_load_toml]] → `references` → [[graphify_graphify_cargo_introspect_py_path]]
- [[graphify_graphify_cargo_introspect_introspect_cargo]] → `references` → [[graphify_graphify_cargo_introspect_py_path]]
- [[graphify_graphify_cargo_introspect_member_manifest_paths]] → `references` → [[graphify_graphify_cargo_introspect_py_path]]
- [[graphify_graphify_cargo_introspect_introspect_cargo]] → `references` → [[graphify_graphify_cargo_introspect_py_any]]
- [[graphify_graphify_cargo_introspect_member_manifest_paths]] → `references` → [[graphify_graphify_cargo_introspect_py_any]]
- [[graphify_graphify_cargo_introspect_introspect_cargo]] → `calls` → [[graphify_graphify_cargo_introspect_member_manifest_paths]]
- [[graphify_graphify_cargo_introspect_rationale_48]] → `rationale_for` → [[graphify_graphify_cargo_introspect_introspect_cargo]]