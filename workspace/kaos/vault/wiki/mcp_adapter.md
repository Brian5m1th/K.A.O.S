# assistant\app\tools\mcp_adapter.py

## Símbolos

- [[assistant_app_tools_mcp_adapter]] — code: mcp_adapter.py
- [[assistant_app_tools_mcp_adapter_make_tool_fn]] — code: _make_tool_fn()
- [[assistant_app_tools_mcp_adapter_build_mcp_tool]] — code: build_mcp_tool()
- [[assistant_app_tools_mcp_adapter_register_all_mcp_tools]] — code: register_all_mcp_tools()
- [[assistant_app_tools_mcp_adapter_rationale_1]] — code: MCP Adapter — converts MCP tool definitions into LangChain BaseTool instances a
- [[assistant_app_tools_mcp_adapter_rationale_15]] — code: Return an async function that invokes the MCP tool.
- [[assistant_app_tools_mcp_adapter_rationale_31]] — code: Convert a single MCP tool definition into a LangChain StructuredTool.      Ret
- [[assistant_app_tools_mcp_adapter_rationale_61]] — code: Iterate all active MCP servers and register their tools in TOOL_REGISTRY.

## Dependências

- [[assistant_app_tools_mcp_adapter_register_all_mcp_tools]] → `calls` → [[assistant_app_core_mcp_manager_mcpmanager]]
- [[assistant_app_tools_mcp_adapter]] → `contains` → [[assistant_app_tools_mcp_adapter_build_mcp_tool]]
- [[assistant_app_tools_mcp_adapter]] → `contains` → [[assistant_app_tools_mcp_adapter_make_tool_fn]]
- [[assistant_app_tools_mcp_adapter]] → `contains` → [[assistant_app_tools_mcp_adapter_register_all_mcp_tools]]
- [[assistant_app_tools_mcp_adapter_rationale_1]] → `rationale_for` → [[assistant_app_tools_mcp_adapter]]
- [[assistant_app_tools_mcp_adapter_build_mcp_tool]] → `calls` → [[assistant_app_tools_mcp_adapter_make_tool_fn]]
- [[assistant_app_tools_mcp_adapter_make_tool_fn]] → `indirect_call` → [[graphify_tests_test_hook_guard_invoke]]
- [[assistant_app_tools_mcp_adapter_rationale_15]] → `rationale_for` → [[assistant_app_tools_mcp_adapter_make_tool_fn]]
- [[assistant_app_tools_mcp_adapter_build_mcp_tool]] → `references` → [[structuredtool]]
- [[assistant_app_tools_mcp_adapter_rationale_31]] → `rationale_for` → [[assistant_app_tools_mcp_adapter_build_mcp_tool]]
- [[assistant_app_tools_mcp_adapter_register_all_mcp_tools]] → `calls` → [[assistant_app_tools_mcp_adapter_build_mcp_tool]]
- [[assistant_app_tools_mcp_adapter_rationale_61]] → `rationale_for` → [[assistant_app_tools_mcp_adapter_register_all_mcp_tools]]