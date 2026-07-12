# assistant\app\obsidian\tools\read_note_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_read_note_tool]] — code: read_note_tool.py
- [[assistant_app_obsidian_tools_read_note_tool_get_service]] — code: _get_service()
- [[assistant_app_obsidian_tools_read_note_tool_read_note]] — code: read_note()
- [[assistant_app_obsidian_tools_read_note_tool_rationale_13]] — code: Lê o conteúdo de uma nota existente no Vault pelo seu caminho relativo.

## Dependências

- [[assistant_app_obsidian_tools_read_note_tool_get_service]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_app_obsidian_tools_read_note_tool]] → `contains` → [[assistant_app_obsidian_tools_read_note_tool_get_service]]
- [[assistant_app_obsidian_tools_read_note_tool]] → `contains` → [[assistant_app_obsidian_tools_read_note_tool_read_note]]
- [[assistant_app_obsidian_tools_read_note_tool_read_note]] → `calls` → [[assistant_app_obsidian_tools_read_note_tool_get_service]]
- [[assistant_app_obsidian_tools_read_note_tool_rationale_13]] → `rationale_for` → [[assistant_app_obsidian_tools_read_note_tool_read_note]]