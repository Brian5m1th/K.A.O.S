from pathlib import Path
from loguru import logger
from langchain_core.tools import tool

from app.obsidian.tools.wiki.wiki_utils import frontmatter, draft_path, source_path


def _get_service():
    from app.obsidian.services.obsidian_service import ObsidianService

    return ObsidianService()


@tool
def create_source(name: str, content: str, tags: list[str] | None = None) -> str:
    """Cria uma página de source (fonte) na wiki com resumo do documento ingerido. Cria como draft."""
    logger.info(f"[info] create_source - {name}")
    svc = _get_service()
    path = source_path(name)
    fm = frontmatter(name, "source", tags)
    full = f"{fm}# {name}\n\n{content}\n"
    dst = draft_path(path)
    svc.create_note(Path(dst).stem, str(Path(dst).parent), full)
    logger.info(f"[info] create_source - draft criado: {dst}")
    return dst
