# graphify\graphify\multigraph_compat.py

## Símbolos

- [[graphify_graphify_multigraph_compat]] — code: multigraph_compat.py
- [[graphify_graphify_multigraph_compat_capabilitycheck]] — code: CapabilityCheck
- [[graphify_graphify_multigraph_compat_multigraphcapabilityresult]] — code: MultigraphCapabilityResult
- [[graphify_graphify_multigraph_compat_multigraphcapabilityresult_ok]] — code: .ok()
- [[graphify_graphify_multigraph_compat_multigraphcapabilityresult_failed]] — code: .failed()
- [[graphify_graphify_multigraph_compat_multigraphcapabilityresult_error_message]] — code: .error_message()
- [[graphify_graphify_multigraph_compat_check]] — code: _check()
- [[graphify_graphify_multigraph_compat_build_probe_graph]] — code: _build_probe_graph()
- [[graphify_graphify_multigraph_compat_probe_keyed_parallel_edges]] — code: _probe_keyed_parallel_edges()
- [[graphify_graphify_multigraph_compat_probe_node_link_round_trip]] — code: _probe_node_link_round_trip()
- [[graphify_graphify_multigraph_compat_probe_duplicate_key_overwrite_semantics]] — code: _probe_duplicate_key_overwrite_semantics()
- [[graphify_graphify_multigraph_compat_probe_reserved_key_attr_rejected]] — code: _probe_reserved_key_attr_rejected()
- [[graphify_graphify_multigraph_compat_probe_remove_edges_from_two_tuple_semantics]] — code: _probe_remove_edges_from_two_tuple_semantics()
- [[graphify_graphify_multigraph_compat_probe_to_undirected_preserves_multigraph_type]] — code: _probe_to_undirected_preserves_multigraph_type()
- [[graphify_graphify_multigraph_compat_probe_multigraph_capabilities]] — code: probe_multigraph_capabilities()
- [[graphify_graphify_multigraph_compat_require_multigraph_capabilities]] — code: require_multigraph_capabilities()
- [[graphify_graphify_multigraph_compat_rationale_1]] — code: Runtime compatibility probe for Graphify MultiDiGraph mode.  Verifies that the
- [[graphify_graphify_multigraph_compat_rationale_139]] — code: Verify the Python language guarantee that NetworkX add_edge inherits.      Pyt

## Dependências

- [[graphify_graphify_multigraph_compat]] → `contains` → [[graphify_graphify_multigraph_compat_build_probe_graph]]
- [[graphify_graphify_multigraph_compat]] → `contains` → [[graphify_graphify_multigraph_compat_capabilitycheck]]
- [[graphify_graphify_multigraph_compat]] → `contains` → [[graphify_graphify_multigraph_compat_check]]
- [[graphify_graphify_multigraph_compat]] → `contains` → [[graphify_graphify_multigraph_compat_multigraphcapabilityresult]]
- [[graphify_graphify_multigraph_compat]] → `contains` → [[graphify_graphify_multigraph_compat_probe_duplicate_key_overwrite_semantics]]
- [[graphify_graphify_multigraph_compat]] → `contains` → [[graphify_graphify_multigraph_compat_probe_keyed_parallel_edges]]
- [[graphify_graphify_multigraph_compat]] → `contains` → [[graphify_graphify_multigraph_compat_probe_multigraph_capabilities]]
- [[graphify_graphify_multigraph_compat]] → `contains` → [[graphify_graphify_multigraph_compat_probe_node_link_round_trip]]
- [[graphify_graphify_multigraph_compat]] → `contains` → [[graphify_graphify_multigraph_compat_probe_remove_edges_from_two_tuple_semantics]]
- [[graphify_graphify_multigraph_compat]] → `contains` → [[graphify_graphify_multigraph_compat_probe_reserved_key_attr_rejected]]
- [[graphify_graphify_multigraph_compat]] → `contains` → [[graphify_graphify_multigraph_compat_probe_to_undirected_preserves_multigraph_type]]
- [[graphify_graphify_multigraph_compat]] → `contains` → [[graphify_graphify_multigraph_compat_require_multigraph_capabilities]]
- [[graphify_graphify_multigraph_compat_rationale_1]] → `rationale_for` → [[graphify_graphify_multigraph_compat]]
- [[graphify_graphify_multigraph_compat_check]] → `references` → [[graphify_graphify_multigraph_compat_capabilitycheck]]
- [[graphify_graphify_multigraph_compat_multigraphcapabilityresult_failed]] → `references` → [[graphify_graphify_multigraph_compat_capabilitycheck]]
- [[graphify_graphify_multigraph_compat_multigraphcapabilityresult]] → `method` → [[graphify_graphify_multigraph_compat_multigraphcapabilityresult_error_message]]
- [[graphify_graphify_multigraph_compat_multigraphcapabilityresult]] → `method` → [[graphify_graphify_multigraph_compat_multigraphcapabilityresult_failed]]
- [[graphify_graphify_multigraph_compat_multigraphcapabilityresult]] → `method` → [[graphify_graphify_multigraph_compat_multigraphcapabilityresult_ok]]
- [[graphify_graphify_multigraph_compat_probe_multigraph_capabilities]] → `references` → [[graphify_graphify_multigraph_compat_multigraphcapabilityresult]]
- [[graphify_graphify_multigraph_compat_require_multigraph_capabilities]] → `references` → [[graphify_graphify_multigraph_compat_multigraphcapabilityresult]]
- [[graphify_graphify_multigraph_compat_require_multigraph_capabilities]] → `calls` → [[graphify_graphify_multigraph_compat_multigraphcapabilityresult_error_message]]
- [[graphify_graphify_multigraph_compat_probe_multigraph_capabilities]] → `calls` → [[graphify_graphify_multigraph_compat_check]]
- [[graphify_graphify_multigraph_compat_build_probe_graph]] → `references` → [[multidigraph]]
- [[graphify_graphify_multigraph_compat_probe_keyed_parallel_edges]] → `calls` → [[graphify_graphify_multigraph_compat_build_probe_graph]]
- [[graphify_graphify_multigraph_compat_probe_node_link_round_trip]] → `calls` → [[graphify_graphify_multigraph_compat_build_probe_graph]]
- [[graphify_graphify_multigraph_compat_probe_to_undirected_preserves_multigraph_type]] → `calls` → [[graphify_graphify_multigraph_compat_build_probe_graph]]
- [[graphify_graphify_multigraph_compat_probe_duplicate_key_overwrite_semantics]] → `calls` → [[multidigraph]]
- [[graphify_graphify_multigraph_compat_probe_remove_edges_from_two_tuple_semantics]] → `calls` → [[multidigraph]]
- [[graphify_graphify_multigraph_compat_probe_reserved_key_attr_rejected]] → `calls` → [[multidigraph]]
- [[graphify_graphify_multigraph_compat_probe_multigraph_capabilities]] → `indirect_call` → [[graphify_graphify_multigraph_compat_probe_keyed_parallel_edges]]
- [[graphify_graphify_multigraph_compat_probe_multigraph_capabilities]] → `indirect_call` → [[graphify_graphify_multigraph_compat_probe_node_link_round_trip]]
- [[graphify_graphify_multigraph_compat_probe_multigraph_capabilities]] → `indirect_call` → [[graphify_graphify_multigraph_compat_probe_duplicate_key_overwrite_semantics]]
- [[graphify_graphify_multigraph_compat_probe_multigraph_capabilities]] → `indirect_call` → [[graphify_graphify_multigraph_compat_probe_reserved_key_attr_rejected]]
- [[graphify_graphify_multigraph_compat_rationale_139]] → `rationale_for` → [[graphify_graphify_multigraph_compat_probe_reserved_key_attr_rejected]]
- [[graphify_graphify_multigraph_compat_probe_multigraph_capabilities]] → `indirect_call` → [[graphify_graphify_multigraph_compat_probe_remove_edges_from_two_tuple_semantics]]
- [[graphify_graphify_multigraph_compat_probe_multigraph_capabilities]] → `indirect_call` → [[graphify_graphify_multigraph_compat_probe_to_undirected_preserves_multigraph_type]]
- [[graphify_graphify_multigraph_compat_require_multigraph_capabilities]] → `calls` → [[graphify_graphify_multigraph_compat_probe_multigraph_capabilities]]