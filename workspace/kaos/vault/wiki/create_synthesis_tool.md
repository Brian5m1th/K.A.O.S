# assistant\app\obsidian\tools\wiki\create_synthesis_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_wiki_create_synthesis_tool]] — code: create_synthesis_tool.py
- [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_get_service]] — code: _get_service()
- [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_create_synthesis]] — code: create_synthesis()
- [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_rationale_21]] — code: Cria uma página de síntese na wiki (análise, comparação, tese). Cria como draft.

## Dependências

- [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_get_service]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_app_obsidian_tools_wiki_create_synthesis_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_create_synthesis]]
- [[assistant_app_obsidian_tools_wiki_create_synthesis_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_get_service]]
- [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_create_synthesis]] → `calls` → [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_get_service]]
- [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_create_synthesis]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_draft_path]]
- [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_create_synthesis]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_frontmatter]]
- [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_create_synthesis]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_wiki_path]]
- [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_rationale_21]] → `rationale_for` → [[assistant_app_obsidian_tools_wiki_create_synthesis_tool_create_synthesis]]