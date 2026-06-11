from loguru import logger
from langchain_core.tools import tool
from app.domain.document import NoteResponse


def _get_service():
    from app.obsidian.services.obsidian_service import ObsidianService
    return ObsidianService()


@tool
def create_note(title: str, folder: str, content: str) -> dict:
    """Cria uma nova nota Markdown no Vault Obsidian."""
    logger.info("[info] create_note - criando nota")
    svc = _get_service()
    path = svc.create_note(title=title, folder=folder, content=content)
    return NoteResponse(status="CREATED", path=path).model_dump()
