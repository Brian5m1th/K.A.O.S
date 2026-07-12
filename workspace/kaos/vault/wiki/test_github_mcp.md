# assistant\tests\unit\test_github_mcp.py

## Símbolos

- [[assistant_tests_unit_test_github_mcp]] — code: test_github_mcp.py
- [[assistant_tests_unit_test_github_mcp_testgithubmcp]] — code: TestGithubMCP
- [[assistant_tests_unit_test_github_mcp_testgithubmcp_test_call_tool_read_code_fallback]] — code: .test_call_tool_read_code_fallback()
- [[assistant_tests_unit_test_github_mcp_testgithubmcp_test_call_tool_create_pr_fallback]] — code: .test_call_tool_create_pr_fallback()
- [[assistant_tests_unit_test_github_mcp_testgithubmcp_test_call_tool_unsupported]] — code: .test_call_tool_unsupported()
- [[assistant_tests_unit_test_github_mcp_testgithubmcp_test_mcp_manager_handshake]] — code: .test_mcp_manager_handshake()

## Dependências

- [[assistant_tests_unit_test_github_mcp_testgithubmcp]] → `uses` → [[assistant_app_core_mcp_manager_mcpmanager]]
- [[assistant_tests_unit_test_github_mcp_testgithubmcp_test_mcp_manager_handshake]] → `calls` → [[assistant_app_core_mcp_manager_mcpmanager]]
- [[assistant_tests_unit_test_github_mcp_testgithubmcp]] → `uses` → [[assistant_app_core_mcp_registry_mcpregistry]]
- [[assistant_tests_unit_test_github_mcp_testgithubmcp_test_mcp_manager_handshake]] → `indirect_call` → [[assistant_app_core_mcp_registry_mcpregistry]]
- [[assistant_tests_unit_test_github_mcp]] → `contains` → [[assistant_tests_unit_test_github_mcp_testgithubmcp]]
- [[assistant_tests_unit_test_github_mcp_testgithubmcp]] → `method` → [[assistant_tests_unit_test_github_mcp_testgithubmcp_test_call_tool_create_pr_fallback]]
- [[assistant_tests_unit_test_github_mcp_testgithubmcp]] → `method` → [[assistant_tests_unit_test_github_mcp_testgithubmcp_test_call_tool_read_code_fallback]]
- [[assistant_tests_unit_test_github_mcp_testgithubmcp]] → `method` → [[assistant_tests_unit_test_github_mcp_testgithubmcp_test_call_tool_unsupported]]
- [[assistant_tests_unit_test_github_mcp_testgithubmcp]] → `method` → [[assistant_tests_unit_test_github_mcp_testgithubmcp_test_mcp_manager_handshake]]