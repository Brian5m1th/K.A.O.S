# assistant\app\obsidian\tools\create_note_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_create_note_tool]] — code: create_note_tool.py
- [[assistant_app_obsidian_tools_create_note_tool_get_service]] — code: _get_service()
- [[assistant_app_obsidian_tools_create_note_tool_create_note]] — code: create_note()
- [[assistant_app_obsidian_tools_create_note_tool_rationale_14]] — code: Cria uma nova nota Markdown no Vault Obsidian.

## Dependências

- [[assistant_app_obsidian_tools_create_note_tool_create_note]] → `calls` → [[assistant_app_domain_document_noteresponse]]
- [[assistant_app_obsidian_tools_create_note_tool_get_service]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_app_obsidian_tools_create_note_tool]] → `contains` → [[assistant_app_obsidian_tools_create_note_tool_create_note]]
- [[assistant_app_obsidian_tools_create_note_tool]] → `contains` → [[assistant_app_obsidian_tools_create_note_tool_get_service]]
- [[assistant_app_obsidian_tools_create_note_tool_create_note]] → `calls` → [[assistant_app_obsidian_tools_create_note_tool_get_service]]
- [[assistant_app_obsidian_tools_create_note_tool_rationale_14]] → `rationale_for` → [[assistant_app_obsidian_tools_create_note_tool_create_note]]