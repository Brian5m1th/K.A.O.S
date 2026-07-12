# assistant\app\obsidian\tools\wiki\wiki_utils.py

## Símbolos

- [[assistant_app_obsidian_tools_wiki_wiki_utils]] — code: wiki_utils.py
- [[assistant_app_obsidian_tools_wiki_wiki_utils_slugify]] — code: slugify()
- [[assistant_app_obsidian_tools_wiki_wiki_utils_frontmatter]] — code: frontmatter()
- [[assistant_app_obsidian_tools_wiki_wiki_utils_draft_path]] — code: draft_path()
- [[assistant_app_obsidian_tools_wiki_wiki_utils_resolve_wiki_path]] — code: resolve_wiki_path()
- [[assistant_app_obsidian_tools_wiki_wiki_utils_wiki_path]] — code: wiki_path()
- [[assistant_app_obsidian_tools_wiki_wiki_utils_source_path]] — code: source_path()

## Dependências

- [[assistant_app_obsidian_tools_wiki_wiki_utils]] → `contains` → [[assistant_app_obsidian_tools_wiki_wiki_utils_draft_path]]
- [[assistant_app_obsidian_tools_wiki_wiki_utils]] → `contains` → [[assistant_app_obsidian_tools_wiki_wiki_utils_frontmatter]]
- [[assistant_app_obsidian_tools_wiki_wiki_utils]] → `contains` → [[assistant_app_obsidian_tools_wiki_wiki_utils_resolve_wiki_path]]
- [[assistant_app_obsidian_tools_wiki_wiki_utils]] → `contains` → [[assistant_app_obsidian_tools_wiki_wiki_utils_slugify]]
- [[assistant_app_obsidian_tools_wiki_wiki_utils]] → `contains` → [[assistant_app_obsidian_tools_wiki_wiki_utils_source_path]]
- [[assistant_app_obsidian_tools_wiki_wiki_utils]] → `contains` → [[assistant_app_obsidian_tools_wiki_wiki_utils_wiki_path]]
- [[assistant_app_obsidian_tools_wiki_wiki_utils_source_path]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_slugify]]
- [[assistant_app_obsidian_tools_wiki_wiki_utils_wiki_path]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_slugify]]
- [[assistant_app_obsidian_tools_wiki_wiki_utils_draft_path]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_py_path]]
- [[assistant_app_obsidian_tools_wiki_wiki_utils_resolve_wiki_path]] → `references` → [[assistant_app_obsidian_tools_wiki_wiki_utils_py_path]]