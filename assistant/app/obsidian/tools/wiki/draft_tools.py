from pathlib import Path
from loguru import logger
from langchain_core.tools import tool

from app.obsidian.tools.wiki.wiki_utils import resolve_wiki_path, draft_path
from app.obsidian.tools.wiki.append_log_tool import append_log
from app.obsidian.tools.wiki.update_index_tool import update_index


def _is_draft(path: str) -> bool:
    return Path(path).stem.endswith(".draft")


def _draft_to_final(draft_rel: str) -> str:
    return draft_rel.replace(".draft.md", ".md")


def _final_to_draft(final_rel: str) -> str:
    return draft_path(final_rel)


@tool
def approve_draft(path: str) -> str:
    """Aprova um draft: renomeia .draft.md para .md e atualiza index + log."""
    logger.info(f"[info] approve_draft - {path}")
    vault = resolve_wiki_path("wiki").parent
    if not _is_draft(path):
        src = resolve_wiki_path(_final_to_draft(path))
        final_rel = path
    else:
        src = resolve_wiki_path(path)
        final_rel = _draft_to_final(path)
    dst = vault / final_rel
    if not src.exists():
        return f"Erro: draft nao encontrado: {src}"
    src.rename(dst)
    update_index.invoke({})
    entry = f"APPROVED | {final_rel}"
    append_log.invoke({"entry": entry})
    logger.info(f"[info] approve_draft - aprovado: {final_rel}")
    return f"Draft aprovado: {final_rel}"


@tool
def reject_draft(path: str) -> str:
    """Rejeita um draft: deleta o arquivo .draft.md."""
    logger.info(f"[info] reject_draft - {path}")
    if not _is_draft(path):
        path = _final_to_draft(path)
    src = resolve_wiki_path(path)
    if not src.exists():
        return f"Erro: draft nao encontrado: {path}"
    src.unlink()
    entry = f"REJECTED | {path}"
    append_log.invoke({"entry": entry})
    logger.info(f"[info] reject_draft - rejeitado: {path}")
    return f"Draft rejeitado e removido: {path}"


@tool
def list_drafts() -> str:
    """Lista todos os drafts pendentes na wiki."""
    logger.info("[info] list_drafts")
    vault = resolve_wiki_path("wiki").parent
    drafts = []
    for f in vault.rglob("*.draft.md"):
        rel = str(f.relative_to(vault))
        drafts.append(rel)
    if not drafts:
        return "Nenhum draft pendente."
    result = "Drafts pendentes:\n"
    for d in sorted(drafts):
        result += f"- {d}\n"
    return result
