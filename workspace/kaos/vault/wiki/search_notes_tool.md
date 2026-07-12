# assistant\app\obsidian\tools\search_notes_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_search_notes_tool]] — code: search_notes_tool.py
- [[assistant_app_obsidian_tools_search_notes_tool_get_service]] — code: _get_service()
- [[assistant_app_obsidian_tools_search_notes_tool_search_notes]] — code: search_notes()
- [[assistant_app_obsidian_tools_search_notes_tool_rationale_13]] — code: Busca textual por palavra-chave em todas as notas do Vault.

## Dependências

- [[assistant_app_obsidian_tools_search_notes_tool_get_service]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_app_obsidian_tools_search_notes_tool]] → `contains` → [[assistant_app_obsidian_tools_search_notes_tool_get_service]]
- [[assistant_app_obsidian_tools_search_notes_tool]] → `contains` → [[assistant_app_obsidian_tools_search_notes_tool_search_notes]]
- [[assistant_app_obsidian_tools_search_notes_tool_search_notes]] → `calls` → [[assistant_app_obsidian_tools_search_notes_tool_get_service]]
- [[assistant_app_obsidian_tools_search_notes_tool_rationale_13]] → `rationale_for` → [[assistant_app_obsidian_tools_search_notes_tool_search_notes]]