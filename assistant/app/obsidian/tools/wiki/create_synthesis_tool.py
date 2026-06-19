from pathlib import Path
from loguru import logger
from langchain_core.tools import tool

from app.obsidian.tools.wiki.wiki_utils import frontmatter, draft_path, wiki_path


def _get_service():
    from app.obsidian.services.obsidian_service import ObsidianService

    return ObsidianService()


@tool
def create_synthesis(
    title: str,
    content: str,
    citations: list[str] | None = None,
    tags: list[str] | None = None,
) -> str:
    """Cria uma página de síntese na wiki (análise, comparação, tese). Cria como draft."""
    logger.info(f"[info] create_synthesis - {title}")
    svc = _get_service()
    path = wiki_path("synthesis", title)
    fm = frontmatter(title, "synthesis", tags, citations)
    full = f"{fm}# {title}\n\n{content}\n"
    dst = draft_path(path)
    svc.create_note(Path(dst).stem, str(Path(dst).parent), full)
    logger.info(f"[info] create_synthesis - draft criado: {dst}")
    return dst
