# assistant\app\obsidian\tools\wiki\create_source_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_wiki_create_source_tool]] — code: create_source_tool.py
- [[assistant_app_obsidian_tools_wiki_create_source_tool_get_service]] — code: _get_service()
- [[assistant_app_obsidian_tools_wiki_create_source_tool_create_source]] — code: create_source()
- [[assistant_app_obsidian_tools_wiki_create_source_tool_rationale_16]] — code: Cria uma página de source (fonte) na wiki com resumo do documento ingerido. Cria

## Dependências

- [[assistant_app_obsidian_tools_wiki_create_source_tool_get_service]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_app_obsidian_tools_wiki_create_source_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_create_source_tool_create_source]]
- [[assistant_app_obsidian_tools_wiki_create_source_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_create_source_tool_get_service]]
- [[assistant_app_obsidian_tools_wiki_create_source_tool_create_source]] → `calls` → [[assistant_app_obsidian_tools_wiki_create_source_tool_get_service]]
- [[assistant_app_obsidian_tools_wiki_create_source_tool_create_source]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_draft_path]]
- [[assistant_app_obsidian_tools_wiki_create_source_tool_create_source]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_frontmatter]]
- [[assistant_app_obsidian_tools_wiki_create_source_tool_create_source]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_source_path]]
- [[assistant_app_obsidian_tools_wiki_create_source_tool_rationale_16]] → `rationale_for` → [[assistant_app_obsidian_tools_wiki_create_source_tool_create_source]]