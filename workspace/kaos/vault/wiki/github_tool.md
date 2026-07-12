# assistant\app\tools\github_tool.py

## Símbolos

- [[assistant_app_tools_github_tool]] — code: github_tool.py
- [[assistant_app_tools_github_tool_log_err]] — code: log_err()
- [[assistant_app_tools_github_tool_call_tool]] — code: call_tool()
- [[assistant_app_tools_github_tool_main]] — code: main()

## Dependências

- [[assistant_app_tools_github_tool]] → `contains` → [[assistant_app_tools_github_tool_call_tool]]
- [[assistant_app_tools_github_tool]] → `contains` → [[assistant_app_tools_github_tool_log_err]]
- [[assistant_app_tools_github_tool]] → `contains` → [[assistant_app_tools_github_tool_main]]
- [[assistant_app_tools_github_tool_main]] → `calls` → [[assistant_app_tools_github_tool_log_err]]
- [[assistant_app_tools_github_tool_main]] → `calls` → [[assistant_app_tools_github_tool_call_tool]]