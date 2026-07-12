# assistant\app\obsidian\tools\list_notes_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_list_notes_tool]] — code: list_notes_tool.py
- [[assistant_app_obsidian_tools_list_notes_tool_get_service]] — code: _get_service()
- [[assistant_app_obsidian_tools_list_notes_tool_list_notes]] — code: list_notes()
- [[assistant_app_obsidian_tools_list_notes_tool_rationale_13]] — code: Lista notas Markdown no Vault Obsidian, opcionalmente filtradas por pasta.

## Dependências

- [[assistant_app_obsidian_tools_list_notes_tool_get_service]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_app_obsidian_tools_list_notes_tool]] → `contains` → [[assistant_app_obsidian_tools_list_notes_tool_get_service]]
- [[assistant_app_obsidian_tools_list_notes_tool]] → `contains` → [[assistant_app_obsidian_tools_list_notes_tool_list_notes]]
- [[assistant_app_obsidian_tools_list_notes_tool_list_notes]] → `calls` → [[assistant_app_obsidian_tools_list_notes_tool_get_service]]
- [[assistant_app_obsidian_tools_list_notes_tool_rationale_13]] → `rationale_for` → [[assistant_app_obsidian_tools_list_notes_tool_list_notes]]