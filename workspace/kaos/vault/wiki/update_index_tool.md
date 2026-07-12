# assistant\app\obsidian\tools\wiki\update_index_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_wiki_update_index_tool]] — code: update_index_tool.py
- [[assistant_app_obsidian_tools_wiki_update_index_tool_scan_pages]] — code: _scan_pages()
- [[assistant_app_obsidian_tools_wiki_update_index_tool_page_title]] — code: _page_title()
- [[assistant_app_obsidian_tools_wiki_update_index_tool_update_index]] — code: update_index()
- [[assistant_app_obsidian_tools_wiki_update_index_tool_rationale_30]] — code: Regenera o index.md da wiki varrendo todas as páginas.

## Dependências

- [[assistant_app_obsidian_tools_wiki_update_index_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_update_index_tool_page_title]]
- [[assistant_app_obsidian_tools_wiki_update_index_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_update_index_tool_scan_pages]]
- [[assistant_app_obsidian_tools_wiki_update_index_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_update_index_tool_update_index]]
- [[assistant_app_obsidian_tools_wiki_update_index_tool_scan_pages]] → `references` → [[assistant_app_obsidian_tools_wiki_update_index_tool_py_path]]
- [[assistant_app_obsidian_tools_wiki_update_index_tool_update_index]] → `calls` → [[assistant_app_obsidian_tools_wiki_update_index_tool_scan_pages]]
- [[assistant_app_obsidian_tools_wiki_update_index_tool_page_title]] → `references` → [[assistant_app_obsidian_tools_wiki_update_index_tool_py_path]]
- [[assistant_app_obsidian_tools_wiki_update_index_tool_update_index]] → `calls` → [[assistant_app_obsidian_tools_wiki_update_index_tool_page_title]]
- [[assistant_app_obsidian_tools_wiki_update_index_tool_rationale_30]] → `rationale_for` → [[assistant_app_obsidian_tools_wiki_update_index_tool_update_index]]
- [[assistant_app_obsidian_tools_wiki_update_index_tool_update_index]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_resolve_wiki_path]]