# assistant\app\obsidian\tools\list_projects_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_list_projects_tool]] — code: list_projects_tool.py
- [[assistant_app_obsidian_tools_list_projects_tool_get_vault_path]] — code: _get_vault_path()
- [[assistant_app_obsidian_tools_list_projects_tool_list_projects]] — code: list_projects()
- [[assistant_app_obsidian_tools_list_projects_tool_rationale_13]] — code: Lista projetos no Vault Obsidian (pastas de primeiro nivel com notas .md).

## Dependências

- [[assistant_app_obsidian_tools_list_projects_tool]] → `contains` → [[assistant_app_obsidian_tools_list_projects_tool_get_vault_path]]
- [[assistant_app_obsidian_tools_list_projects_tool]] → `contains` → [[assistant_app_obsidian_tools_list_projects_tool_list_projects]]
- [[assistant_app_obsidian_tools_list_projects_tool_get_vault_path]] → `references` → [[assistant_app_obsidian_tools_list_projects_tool_py_path]]
- [[assistant_app_obsidian_tools_list_projects_tool_list_projects]] → `calls` → [[assistant_app_obsidian_tools_list_projects_tool_get_vault_path]]
- [[assistant_app_obsidian_tools_list_projects_tool_rationale_13]] → `rationale_for` → [[assistant_app_obsidian_tools_list_projects_tool_list_projects]]