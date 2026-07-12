# graphify\graphify\mcp_ingest.py

## Símbolos

- [[graphify_graphify_mcp_ingest]] — code: mcp_ingest.py
- [[graphify_graphify_mcp_ingest_is_mcp_config_path]] — code: is_mcp_config_path()
- [[graphify_graphify_mcp_ingest_extract_mcp_config]] — code: extract_mcp_config()
- [[graphify_graphify_mcp_ingest_emit_server]] — code: _emit_server()
- [[graphify_graphify_mcp_ingest_detect_package_from_args]] — code: _detect_package_from_args()
- [[graphify_graphify_mcp_ingest_strip_version]] — code: _strip_version()
- [[graphify_graphify_mcp_ingest_add_node]] — code: _add_node()
- [[graphify_graphify_mcp_ingest_add_edge]] — code: _add_edge()
- [[graphify_graphify_mcp_ingest_make_id]] — code: _make_id()
- [[graphify_graphify_mcp_ingest_rationale_1]] — code: mcp_ingest.py — Extract MCP (Model Context Protocol) server configuration files.
- [[graphify_graphify_mcp_ingest_rationale_82]] — code: Return True when ``path`` is a recognised MCP config filename.
- [[graphify_graphify_mcp_ingest_rationale_87]] — code: Parse an MCP config file into Graphify nodes and edges.      Behaviour matches
- [[graphify_graphify_mcp_ingest_rationale_181]] — code: Emit nodes/edges for one entry under ``mcpServers``.
- [[graphify_graphify_mcp_ingest_rationale_285]] — code: Return the first arg that looks like an npm or pypi package id, else None.
- [[graphify_graphify_mcp_ingest_rationale_303]] — code: Drop the ``@version`` suffix from an npm package id, preserving the scope.
- [[graphify_graphify_mcp_ingest_rationale_329]] — code: Append a node if not already present. ``kind`` is metadata, not file_type.
- [[graphify_graphify_mcp_ingest_rationale_354]] — code: Append an edge if (source, target, relation) is not already present.
- [[graphify_graphify_mcp_ingest_rationale_380]] — code: Build a stable node ID via the single shared recipe (#1378).

## Dependências

- [[graphify_graphify_mcp_ingest_extract_mcp_config]] → `calls` → [[graphify_graphify_extractors_base_file_stem]]
- [[graphify_graphify_mcp_ingest]] → `imports_from` → [[graphify_graphify_ids]]
- [[graphify_graphify_mcp_ingest]] → `contains` → [[graphify_graphify_mcp_ingest_add_edge]]
- [[graphify_graphify_mcp_ingest]] → `contains` → [[graphify_graphify_mcp_ingest_add_node]]
- [[graphify_graphify_mcp_ingest]] → `contains` → [[graphify_graphify_mcp_ingest_detect_package_from_args]]
- [[graphify_graphify_mcp_ingest]] → `contains` → [[graphify_graphify_mcp_ingest_emit_server]]
- [[graphify_graphify_mcp_ingest]] → `contains` → [[graphify_graphify_mcp_ingest_extract_mcp_config]]
- [[graphify_graphify_mcp_ingest]] → `contains` → [[graphify_graphify_mcp_ingest_is_mcp_config_path]]
- [[graphify_graphify_mcp_ingest]] → `contains` → [[graphify_graphify_mcp_ingest_make_id]]
- [[graphify_graphify_mcp_ingest]] → `contains` → [[graphify_graphify_mcp_ingest_strip_version]]
- [[graphify_graphify_mcp_ingest]] → `imports_from` → [[graphify_security]]
- [[graphify_graphify_mcp_ingest_rationale_1]] → `rationale_for` → [[graphify_graphify_mcp_ingest]]
- [[graphify_graphify_mcp_ingest_is_mcp_config_path]] → `references` → [[graphify_graphify_mcp_ingest_py_path]]
- [[graphify_graphify_mcp_ingest_rationale_82]] → `rationale_for` → [[graphify_graphify_mcp_ingest_is_mcp_config_path]]
- [[graphify_graphify_mcp_ingest_extract_mcp_config]] → `references` → [[graphify_graphify_mcp_ingest_py_path]]
- [[graphify_graphify_mcp_ingest_extract_mcp_config]] → `calls` → [[graphify_graphify_mcp_ingest_add_node]]
- [[graphify_graphify_mcp_ingest_extract_mcp_config]] → `calls` → [[graphify_graphify_mcp_ingest_emit_server]]
- [[graphify_graphify_mcp_ingest_extract_mcp_config]] → `calls` → [[graphify_graphify_mcp_ingest_make_id]]
- [[graphify_graphify_mcp_ingest_extract_mcp_config]] → `references` → [[graphify_graphify_mcp_ingest_py_any]]
- [[graphify_graphify_mcp_ingest_rationale_87]] → `rationale_for` → [[graphify_graphify_mcp_ingest_extract_mcp_config]]
- [[graphify_graphify_mcp_ingest_add_edge]] → `references` → [[graphify_graphify_mcp_ingest_py_any]]
- [[graphify_graphify_mcp_ingest_add_node]] → `references` → [[graphify_graphify_mcp_ingest_py_any]]
- [[graphify_graphify_mcp_ingest_detect_package_from_args]] → `references` → [[graphify_graphify_mcp_ingest_py_any]]
- [[graphify_graphify_mcp_ingest_emit_server]] → `references` → [[graphify_graphify_mcp_ingest_py_any]]
- [[graphify_graphify_mcp_ingest_emit_server]] → `calls` → [[graphify_graphify_mcp_ingest_add_edge]]
- [[graphify_graphify_mcp_ingest_emit_server]] → `calls` → [[graphify_graphify_mcp_ingest_add_node]]
- [[graphify_graphify_mcp_ingest_emit_server]] → `calls` → [[graphify_graphify_mcp_ingest_detect_package_from_args]]
- [[graphify_graphify_mcp_ingest_emit_server]] → `calls` → [[graphify_graphify_mcp_ingest_make_id]]
- [[graphify_graphify_mcp_ingest_rationale_181]] → `rationale_for` → [[graphify_graphify_mcp_ingest_emit_server]]
- [[graphify_graphify_mcp_ingest_detect_package_from_args]] → `calls` → [[graphify_graphify_mcp_ingest_strip_version]]
- [[graphify_graphify_mcp_ingest_rationale_285]] → `rationale_for` → [[graphify_graphify_mcp_ingest_detect_package_from_args]]
- [[graphify_graphify_mcp_ingest_rationale_303]] → `rationale_for` → [[graphify_graphify_mcp_ingest_strip_version]]
- [[graphify_graphify_mcp_ingest_add_node]] → `calls` → [[graphify_graphify_security_sanitize_label]]
- [[graphify_graphify_mcp_ingest_rationale_329]] → `rationale_for` → [[graphify_graphify_mcp_ingest_add_node]]
- [[graphify_graphify_mcp_ingest_rationale_354]] → `rationale_for` → [[graphify_graphify_mcp_ingest_add_edge]]
- [[graphify_graphify_mcp_ingest_rationale_380]] → `rationale_for` → [[graphify_graphify_mcp_ingest_make_id]]