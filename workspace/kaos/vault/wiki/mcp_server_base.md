# assistant\app\core\mcp_server_base.py

## Símbolos

- [[assistant_app_core_mcp_server_base]] — code: mcp_server_base.py
- [[assistant_app_core_mcp_server_base_mcpserver]] — code: MCPServer
- [[assistant_app_core_mcp_server_base_mcpserver_initialize]] — code: .initialize()
- [[assistant_app_core_mcp_server_base_mcpserver_shutdown]] — code: .shutdown()
- [[assistant_app_core_mcp_server_base_mcpserver_get_tools]] — code: .get_tools()
- [[assistant_app_core_mcp_server_base_mcpserver_call_tool]] — code: .call_tool()
- [[assistant_app_core_mcp_server_base_mcpserver_get_health]] — code: .get_health()
- [[assistant_app_core_mcp_server_base_rationale_1]] — code: Base interface for MCP (Model Context Protocol) servers.  Defines the abstract
- [[assistant_app_core_mcp_server_base_rationale_12]] — code: Abstract base class for MCP server implementations.      Each concrete subclas
- [[assistant_app_core_mcp_server_base_rationale_20]] — code: Start the MCP server subprocess and establish communication.          Returns
- [[assistant_app_core_mcp_server_base_rationale_28]] — code: Gracefully terminate the MCP server subprocess.          Returns True if shutd
- [[assistant_app_core_mcp_server_base_rationale_36]] — code: Return the list of available tools exposed by this MCP server.          Each t
- [[assistant_app_core_mcp_server_base_rationale_45]] — code: Invoke a tool on this MCP server with the given parameters.          Returns t
- [[assistant_app_core_mcp_server_base_rationale_53]] — code: Return health status information for this server.          Expected keys: {"st

## Dependências

- [[assistant_app_core_mcp_server_base]] → `contains` → [[assistant_app_core_mcp_server_base_mcpserver]]
- [[assistant_app_core_mcp_server_base]] → `imports_from` → [[assistant_app_core_mcp_server_base_py_abc]]
- [[assistant_app_core_mcp_server_base_rationale_1]] → `rationale_for` → [[assistant_app_core_mcp_server_base]]
- [[assistant_app_core_mcp_server_base_mcpserver]] → `method` → [[assistant_app_core_mcp_server_base_mcpserver_call_tool]]
- [[assistant_app_core_mcp_server_base_mcpserver]] → `method` → [[assistant_app_core_mcp_server_base_mcpserver_get_health]]
- [[assistant_app_core_mcp_server_base_mcpserver]] → `method` → [[assistant_app_core_mcp_server_base_mcpserver_get_tools]]
- [[assistant_app_core_mcp_server_base_mcpserver]] → `method` → [[assistant_app_core_mcp_server_base_mcpserver_initialize]]
- [[assistant_app_core_mcp_server_base_mcpserver]] → `method` → [[assistant_app_core_mcp_server_base_mcpserver_shutdown]]
- [[assistant_app_core_mcp_server_base_mcpserver]] → `inherits` → [[assistant_app_core_mcp_server_base_py_abc]]
- [[assistant_app_core_mcp_server_base_rationale_12]] → `rationale_for` → [[assistant_app_core_mcp_server_base_mcpserver]]
- [[assistant_app_core_mcp_server_base_rationale_20]] → `rationale_for` → [[assistant_app_core_mcp_server_base_mcpserver_initialize]]
- [[assistant_app_core_mcp_server_base_rationale_28]] → `rationale_for` → [[assistant_app_core_mcp_server_base_mcpserver_shutdown]]
- [[assistant_app_core_mcp_server_base_rationale_36]] → `rationale_for` → [[assistant_app_core_mcp_server_base_mcpserver_get_tools]]
- [[assistant_app_core_mcp_server_base_rationale_45]] → `rationale_for` → [[assistant_app_core_mcp_server_base_mcpserver_call_tool]]
- [[assistant_app_core_mcp_server_base_rationale_53]] → `rationale_for` → [[assistant_app_core_mcp_server_base_mcpserver_get_health]]