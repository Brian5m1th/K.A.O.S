# assistant\app\obsidian\tools\wiki\lint_wiki_tool.py

## Símbolos

- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool]] — code: lint_wiki_tool.py
- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_find_orphans]] — code: _find_orphans()
- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_find_broken_links]] — code: _find_broken_links()
- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_lint_wiki]] — code: lint_wiki()
- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_rationale_59]] — code: Verifica a saúde da wiki: orphans, broken links.

## Dependências

- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_find_broken_links]]
- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_find_orphans]]
- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool]] → `contains` → [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_lint_wiki]]
- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_find_orphans]] → `references` → [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_py_path]]
- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_lint_wiki]] → `calls` → [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_find_orphans]]
- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_find_broken_links]] → `references` → [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_py_path]]
- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_lint_wiki]] → `calls` → [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_find_broken_links]]
- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_lint_wiki]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_resolve_wiki_path]]
- [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_rationale_59]] → `rationale_for` → [[assistant_app_obsidian_tools_wiki_lint_wiki_tool_lint_wiki]]