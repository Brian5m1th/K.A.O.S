# assistant\app\obsidian\tools\wiki\create_entity_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_wiki_create_entity_tool]] — code: create_entity_tool.py
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_get_service]] — code: _get_service()
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_create_entity]] — code: create_entity()
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_update_entity]] — code: update_entity()
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_rationale_21]] — code: Cria uma página de entidade na wiki (ex: pessoa, projeto, tecnologia). Cria como
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_rationale_40]] — code: Atualiza uma entidade existente. Cria um draft da nova versão.

## Dependências

- [[assistant_app_obsidian_tools_wiki_create_entity_tool_get_service]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_app_obsidian_tools_wiki_create_entity_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_create_entity_tool_create_entity]]
- [[assistant_app_obsidian_tools_wiki_create_entity_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_create_entity_tool_get_service]]
- [[assistant_app_obsidian_tools_wiki_create_entity_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_create_entity_tool_update_entity]]
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_create_entity]] → `calls` → [[assistant_app_obsidian_tools_wiki_create_entity_tool_get_service]]
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_update_entity]] → `calls` → [[assistant_app_obsidian_tools_wiki_create_entity_tool_get_service]]
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_create_entity]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_draft_path]]
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_create_entity]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_frontmatter]]
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_create_entity]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_wiki_path]]
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_rationale_21]] → `rationale_for` → [[assistant_app_obsidian_tools_wiki_create_entity_tool_create_entity]]
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_rationale_40]] → `rationale_for` → [[assistant_app_obsidian_tools_wiki_create_entity_tool_update_entity]]
- [[assistant_app_obsidian_tools_wiki_create_entity_tool_update_entity]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_draft_path]]