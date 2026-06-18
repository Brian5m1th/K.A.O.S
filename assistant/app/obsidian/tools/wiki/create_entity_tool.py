from loguru import logger
from langchain_core.tools import tool

from pathlib import Path
from loguru import logger
from langchain_core.tools import tool

from app.obsidian.tools.wiki.wiki_utils import frontmatter, draft_path, wiki_path


def _get_service():
    from app.obsidian.services.obsidian_service import ObsidianService
    return ObsidianService()


@tool
def create_entity(name: str, summary: str, tags: list[str] | None = None, sources: list[str] | None = None) -> str:
    """Cria uma página de entidade na wiki (ex: pessoa, projeto, tecnologia). Cria como draft."""
    logger.info(f"[info] create_entity - {name}")
    svc = _get_service()
    path = wiki_path("entities", name)
    fm = frontmatter(name, "entity", tags, sources)
    content = f"{fm}# {name}\n\n{summary}\n"
    dst = draft_path(path)
    svc.create_note(Path(dst).stem, str(Path(dst).parent), content)
    logger.info(f"[info] create_entity - draft criado: {dst}")
    return dst


@tool
def update_entity(path: str, content: str, tags: list[str] | None = None, sources: list[str] | None = None) -> str:
    """Atualiza uma entidade existente. Cria um draft da nova versão."""
    logger.info(f"[info] update_entity - {path}")
    svc = _get_service()
    dst = draft_path(path)
    svc.update_note(dst, content, mode="overwrite")
    logger.info(f"[info] update_entity - draft atualizado: {dst}")
    return dst
