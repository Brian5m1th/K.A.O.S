# assistant\app\obsidian\tools\wiki\create_concept_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_wiki_create_concept_tool]] — code: create_concept_tool.py
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_get_service]] — code: _get_service()
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_create_concept]] — code: create_concept()
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_update_concept]] — code: update_concept()
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_rationale_21]] — code: Cria uma página de conceito na wiki (ex: RAG, embeddings, LangGraph). Cria como
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_rationale_40]] — code: Atualiza um conceito existente. Cria um draft da nova versão.

## Dependências

- [[assistant_app_obsidian_tools_wiki_create_concept_tool_get_service]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_app_obsidian_tools_wiki_create_concept_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_create_concept_tool_create_concept]]
- [[assistant_app_obsidian_tools_wiki_create_concept_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_create_concept_tool_get_service]]
- [[assistant_app_obsidian_tools_wiki_create_concept_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_create_concept_tool_update_concept]]
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_create_concept]] → `calls` → [[assistant_app_obsidian_tools_wiki_create_concept_tool_get_service]]
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_update_concept]] → `calls` → [[assistant_app_obsidian_tools_wiki_create_concept_tool_get_service]]
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_create_concept]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_draft_path]]
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_create_concept]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_frontmatter]]
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_create_concept]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_wiki_path]]
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_rationale_21]] → `rationale_for` → [[assistant_app_obsidian_tools_wiki_create_concept_tool_create_concept]]
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_rationale_40]] → `rationale_for` → [[assistant_app_obsidian_tools_wiki_create_concept_tool_update_concept]]
- [[assistant_app_obsidian_tools_wiki_create_concept_tool_update_concept]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_draft_path]]