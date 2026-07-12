# assistant\app\core\mcp_health.py

## Símbolos

- [[assistant_app_core_mcp_health]] — code: mcp_health.py
- [[assistant_app_core_mcp_health_mcphealthmonitor]] — code: MCPHealthMonitor
- [[assistant_app_core_mcp_health_mcphealthmonitor_get_health_summary]] — code: .get_health_summary()
- [[assistant_app_core_mcp_health_mcphealthmonitor_invalidate_cache]] — code: .invalidate_cache()
- [[assistant_app_core_mcp_health_rationale_1]] — code: MCP Health Monitor — aggregates health information for all registered MCP serve
- [[assistant_app_core_mcp_health_rationale_15]] — code: Periodically collects health data from MCP servers.      Uses a simple TTL cac
- [[assistant_app_core_mcp_health_rationale_27]] — code: Return a list of health statuses for all running MCP servers.          Results
- [[assistant_app_core_mcp_health_rationale_61]] — code: Force cache refresh on next call.

## Dependências

- [[assistant_app_core_mcp_health]] → `contains` → [[assistant_app_core_mcp_health_mcphealthmonitor]]
- [[assistant_app_core_mcp_health_rationale_1]] → `rationale_for` → [[assistant_app_core_mcp_health]]
- [[assistant_app_core_mcp_health_mcphealthmonitor]] → `method` → [[assistant_app_core_mcp_health_mcphealthmonitor_get_health_summary]]
- [[assistant_app_core_mcp_health_mcphealthmonitor]] → `method` → [[assistant_app_core_mcp_health_mcphealthmonitor_invalidate_cache]]
- [[assistant_app_core_mcp_health_mcphealthmonitor]] → `uses` → [[assistant_app_core_mcp_manager_mcpmanager]]
- [[assistant_app_core_mcp_health_rationale_15]] → `rationale_for` → [[assistant_app_core_mcp_health_mcphealthmonitor]]
- [[assistant_app_core_mcp_health_mcphealthmonitor_get_health_summary]] → `calls` → [[assistant_app_core_mcp_manager_mcpmanager]]
- [[assistant_app_core_mcp_health_rationale_27]] → `rationale_for` → [[assistant_app_core_mcp_health_mcphealthmonitor_get_health_summary]]
- [[assistant_app_core_mcp_health_rationale_61]] → `rationale_for` → [[assistant_app_core_mcp_health_mcphealthmonitor_invalidate_cache]]