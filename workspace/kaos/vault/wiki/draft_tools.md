# assistant\app\obsidian\tools\wiki\draft_tools.py

## Símbolos

- [[assistant_app_obsidian_tools_wiki_draft_tools]] — code: draft_tools.py
- [[assistant_app_obsidian_tools_wiki_draft_tools_is_draft]] — code: _is_draft()
- [[assistant_app_obsidian_tools_wiki_draft_tools_draft_to_final]] — code: _draft_to_final()
- [[assistant_app_obsidian_tools_wiki_draft_tools_final_to_draft]] — code: _final_to_draft()
- [[assistant_app_obsidian_tools_wiki_draft_tools_approve_draft]] — code: approve_draft()
- [[assistant_app_obsidian_tools_wiki_draft_tools_reject_draft]] — code: reject_draft()
- [[assistant_app_obsidian_tools_wiki_draft_tools_list_drafts]] — code: list_drafts()
- [[assistant_app_obsidian_tools_wiki_draft_tools_rationale_24]] — code: Aprova um draft: renomeia .draft.md para .md e atualiza index + log.
- [[assistant_app_obsidian_tools_wiki_draft_tools_rationale_46]] — code: Rejeita um draft: deleta o arquivo .draft.md.
- [[assistant_app_obsidian_tools_wiki_draft_tools_rationale_62]] — code: Lista todos os drafts pendentes na wiki.

## Dependências

- [[assistant_app_obsidian_tools_wiki_draft_tools]] → `contains` → [[assistant_app_obsidian_tools_wiki_draft_tools_approve_draft]]
- [[assistant_app_obsidian_tools_wiki_draft_tools]] → `contains` → [[assistant_app_obsidian_tools_wiki_draft_tools_draft_to_final]]
- [[assistant_app_obsidian_tools_wiki_draft_tools]] → `contains` → [[assistant_app_obsidian_tools_wiki_draft_tools_final_to_draft]]
- [[assistant_app_obsidian_tools_wiki_draft_tools]] → `contains` → [[assistant_app_obsidian_tools_wiki_draft_tools_is_draft]]
- [[assistant_app_obsidian_tools_wiki_draft_tools]] → `contains` → [[assistant_app_obsidian_tools_wiki_draft_tools_list_drafts]]
- [[assistant_app_obsidian_tools_wiki_draft_tools]] → `contains` → [[assistant_app_obsidian_tools_wiki_draft_tools_reject_draft]]
- [[assistant_app_obsidian_tools_wiki_draft_tools_approve_draft]] → `calls` → [[assistant_app_obsidian_tools_wiki_draft_tools_is_draft]]
- [[assistant_app_obsidian_tools_wiki_draft_tools_reject_draft]] → `calls` → [[assistant_app_obsidian_tools_wiki_draft_tools_is_draft]]
- [[assistant_app_obsidian_tools_wiki_draft_tools_approve_draft]] → `calls` → [[assistant_app_obsidian_tools_wiki_draft_tools_draft_to_final]]
- [[assistant_app_obsidian_tools_wiki_draft_tools_approve_draft]] → `calls` → [[assistant_app_obsidian_tools_wiki_draft_tools_final_to_draft]]
- [[assistant_app_obsidian_tools_wiki_draft_tools_final_to_draft]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_draft_path]]
- [[assistant_app_obsidian_tools_wiki_draft_tools_reject_draft]] → `calls` → [[assistant_app_obsidian_tools_wiki_draft_tools_final_to_draft]]
- [[assistant_app_obsidian_tools_wiki_draft_tools_approve_draft]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_resolve_wiki_path]]
- [[assistant_app_obsidian_tools_wiki_draft_tools_rationale_24]] → `rationale_for` → [[assistant_app_obsidian_tools_wiki_draft_tools_approve_draft]]
- [[assistant_app_obsidian_tools_wiki_draft_tools_rationale_46]] → `rationale_for` → [[assistant_app_obsidian_tools_wiki_draft_tools_reject_draft]]
- [[assistant_app_obsidian_tools_wiki_draft_tools_reject_draft]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_resolve_wiki_path]]
- [[assistant_app_obsidian_tools_wiki_draft_tools_list_drafts]] → `calls` → [[assistant_app_obsidian_tools_wiki_wiki_utils_resolve_wiki_path]]
- [[assistant_app_obsidian_tools_wiki_draft_tools_rationale_62]] → `rationale_for` → [[assistant_app_obsidian_tools_wiki_draft_tools_list_drafts]]