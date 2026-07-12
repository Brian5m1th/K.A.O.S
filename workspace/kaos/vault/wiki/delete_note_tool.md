# assistant\app\obsidian\tools\delete_note_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_delete_note_tool]] — code: delete_note_tool.py
- [[assistant_app_obsidian_tools_delete_note_tool_get_service]] — code: _get_service()
- [[assistant_app_obsidian_tools_delete_note_tool_delete_note]] — code: delete_note()
- [[assistant_app_obsidian_tools_delete_note_tool_rationale_14]] — code: Remove uma nota do Vault Obsidian.

## Dependências

- [[assistant_app_obsidian_tools_delete_note_tool_delete_note]] → `calls` → [[assistant_app_domain_document_noteresponse]]
- [[assistant_app_obsidian_tools_delete_note_tool_get_service]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_app_obsidian_tools_delete_note_tool]] → `contains` → [[assistant_app_obsidian_tools_delete_note_tool_delete_note]]
- [[assistant_app_obsidian_tools_delete_note_tool]] → `contains` → [[assistant_app_obsidian_tools_delete_note_tool_get_service]]
- [[assistant_app_obsidian_tools_delete_note_tool_delete_note]] → `calls` → [[assistant_app_obsidian_tools_delete_note_tool_get_service]]
- [[assistant_app_obsidian_tools_delete_note_tool_rationale_14]] → `rationale_for` → [[assistant_app_obsidian_tools_delete_note_tool_delete_note]]