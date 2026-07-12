# assistant\app\obsidian\tools\save_conversation_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_save_conversation_tool]] — code: save_conversation_tool.py
- [[assistant_app_obsidian_tools_save_conversation_tool_get_memory]] — code: _get_memory()
- [[assistant_app_obsidian_tools_save_conversation_tool_save_conversation]] — code: save_conversation()
- [[assistant_app_obsidian_tools_save_conversation_tool_rationale_15]] — code: Salva um resumo de conversa no vault como memoria de longo prazo.

## Dependências

- [[assistant_app_obsidian_tools_save_conversation_tool]] → `contains` → [[assistant_app_obsidian_tools_save_conversation_tool_get_memory]]
- [[assistant_app_obsidian_tools_save_conversation_tool]] → `contains` → [[assistant_app_obsidian_tools_save_conversation_tool_save_conversation]]
- [[assistant_app_obsidian_tools_save_conversation_tool_save_conversation]] → `calls` → [[assistant_app_obsidian_tools_save_conversation_tool_get_memory]]
- [[assistant_app_obsidian_tools_save_conversation_tool_rationale_15]] → `rationale_for` → [[assistant_app_obsidian_tools_save_conversation_tool_save_conversation]]