from pathlib import Path
from loguru import logger
from langchain_core.tools import tool

from app.obsidian.tools.wiki.wiki_utils import frontmatter, draft_path, wiki_path


def _get_service():
    from app.obsidian.services.obsidian_service import ObsidianService

    return ObsidianService()


@tool
def create_concept(
    name: str,
    summary: str,
    tags: list[str] | None = None,
    sources: list[str] | None = None,
) -> str:
    """Cria uma página de conceito na wiki (ex: RAG, embeddings, LangGraph). Cria como draft."""
    logger.info(f"[info] create_concept - {name}")
    svc = _get_service()
    path = wiki_path("concepts", name)
    fm = frontmatter(name, "concept", tags, sources)
    content = f"{fm}# {name}\n\n{summary}\n"
    dst = draft_path(path)
    svc.create_note(Path(dst).stem, str(Path(dst).parent), content)
    logger.info(f"[info] create_concept - draft criado: {dst}")
    return dst


@tool
def update_concept(
    path: str,
    content: str,
    tags: list[str] | None = None,
    sources: list[str] | None = None,
) -> str:
    """Atualiza um conceito existente. Cria um draft da nova versão."""
    logger.info(f"[info] update_concept - {path}")
    svc = _get_service()
    dst = draft_path(path)
    svc.update_note(dst, content, mode="overwrite")
    logger.info(f"[info] update_concept - draft atualizado: {dst}")
    return dst
