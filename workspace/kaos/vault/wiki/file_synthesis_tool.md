# assistant\app\obsidian\tools\wiki\file_synthesis_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_wiki_file_synthesis_tool]] — code: file_synthesis_tool.py
- [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_get_service]] — code: _get_service()
- [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_file_synthesis_page]] — code: file_synthesis_page()
- [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_rationale_20]] — code: Arquiva uma resposta complexa como pagina de sintese na wiki. Cria como draft.

## Dependências

- [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_get_service]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_app_obsidian_tools_wiki_file_synthesis_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_file_synthesis_page]]
- [[assistant_app_obsidian_tools_wiki_file_synthesis_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_get_service]]
- [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_file_synthesis_page]] → `calls` → [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_get_service]]
- [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_file_synthesis_page]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_draft_path]]
- [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_file_synthesis_page]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_frontmatter]]
- [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_file_synthesis_page]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_wiki_path]]
- [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_rationale_20]] → `rationale_for` → [[assistant_app_obsidian_tools_wiki_file_synthesis_tool_file_synthesis_page]]