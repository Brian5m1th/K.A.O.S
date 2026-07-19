from pathlib import Path
from datetime import date
from loguru import logger
from langchain_core.tools import tool

from app.obsidian.tools.wiki.wiki_utils import frontmatter, draft_path, wiki_path
from app.obsidian.tools.wiki.append_log_tool import append_log


def _get_service():
    from app.obsidian.services.obsidian_service import ObsidianService

    return ObsidianService()


@tool
def file_synthesis_page(
    question: str, answer: str, tags: list[str] | None = None
) -> str:
    """Arquiva uma resposta complexa como pagina de sintese na wiki. Cria como draft."""
    logger.info(f'[info] file_synthesis_page - question="{question[:60]}..."')
    svc = _get_service()
    title = question.strip().rstrip("?")[:80] or f"Sintese-{date.today().isoformat()}"
    path = wiki_path("synthesis", title)
    fm = frontmatter(title, "synthesis", tags or [], sources=[])
    body = f"# {title}\n\n## Pergunta\n\n{question}\n\n## Resposta\n\n{answer}\n"
    full = f"{fm}{body}\n"
    dst = draft_path(path)
    svc.create_note(Path(dst).stem, str(Path(dst).parent), full)
    try:
        append_log.invoke({"entry": f"Síntese criada: [[{dst}]] — {title}"})
    except Exception as e:
        logger.debug("[wiki] append_log failed (non-critical): {}", e)
    logger.info(f"[info] file_synthesis_page - draft criado: {dst}")
    return dst
