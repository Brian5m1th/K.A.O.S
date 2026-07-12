# assistant\app\core\mcp_registry.py

## Símbolos

- [[assistant_app_core_mcp_registry]] — code: mcp_registry.py
- [[assistant_app_core_mcp_registry_mcpregistry]] — code: MCPRegistry
- [[assistant_app_core_mcp_registry_mcpregistry_path]] — code: ._path()
- [[assistant_app_core_mcp_registry_mcpregistry_load]] — code: .load()
- [[assistant_app_core_mcp_registry_mcpregistry_save]] — code: .save()
- [[assistant_app_core_mcp_registry_mcpregistry_get_enabled_servers]] — code: .get_enabled_servers()
- [[assistant_app_core_mcp_registry_rationale_1]] — code: MCP Registry — manages the ``config/mcp.json`` file that lists configured MCP s
- [[assistant_app_core_mcp_registry_rationale_29]] — code: Reads and writes the MCP server registry file (``config/mcp.json``).
- [[assistant_app_core_mcp_registry_rationale_37]] — code: Load the MCP registry from disk.          Returns the registry dict, or a defa
- [[assistant_app_core_mcp_registry_rationale_58]] — code: Persist the MCP registry to disk.
- [[assistant_app_core_mcp_registry_rationale_67]] — code: Return only the enabled server entries from the registry.

## Dependências

- [[assistant_app_core_mcp_registry]] → `contains` → [[assistant_app_core_mcp_registry_mcpregistry]]
- [[assistant_app_core_mcp_registry_rationale_1]] → `rationale_for` → [[assistant_app_core_mcp_registry]]
- [[assistant_app_core_mcp_registry_mcpregistry]] → `method` → [[assistant_app_core_mcp_registry_mcpregistry_get_enabled_servers]]
- [[assistant_app_core_mcp_registry_mcpregistry]] → `method` → [[assistant_app_core_mcp_registry_mcpregistry_load]]
- [[assistant_app_core_mcp_registry_mcpregistry]] → `method` → [[assistant_app_core_mcp_registry_mcpregistry_path]]
- [[assistant_app_core_mcp_registry_mcpregistry]] → `method` → [[assistant_app_core_mcp_registry_mcpregistry_save]]
- [[assistant_app_core_mcp_registry_mcpregistry]] → `uses` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver]]
- [[assistant_app_core_mcp_registry_rationale_29]] → `rationale_for` → [[assistant_app_core_mcp_registry_mcpregistry]]
- [[assistant_app_core_mcp_registry_mcpregistry_load]] → `calls` → [[assistant_app_core_mcp_registry_mcpregistry_path]]
- [[assistant_app_core_mcp_registry_mcpregistry_path]] → `references` → [[assistant_app_core_mcp_registry_py_path]]
- [[assistant_app_core_mcp_registry_mcpregistry_path]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_get_config_path]]
- [[assistant_app_core_mcp_registry_mcpregistry_save]] → `calls` → [[assistant_app_core_mcp_registry_mcpregistry_path]]
- [[assistant_app_core_mcp_registry_mcpregistry_get_enabled_servers]] → `calls` → [[assistant_app_core_mcp_registry_mcpregistry_load]]
- [[assistant_app_core_mcp_registry_rationale_37]] → `rationale_for` → [[assistant_app_core_mcp_registry_mcpregistry_load]]
- [[assistant_app_core_mcp_registry_rationale_58]] → `rationale_for` → [[assistant_app_core_mcp_registry_mcpregistry_save]]
- [[assistant_app_core_mcp_registry_rationale_67]] → `rationale_for` → [[assistant_app_core_mcp_registry_mcpregistry_get_enabled_servers]]