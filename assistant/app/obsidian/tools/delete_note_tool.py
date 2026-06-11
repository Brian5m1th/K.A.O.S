from loguru import logger
from langchain_core.tools import tool
from app.domain.document import NoteResponse


def _get_service():
    from app.obsidian.services.obsidian_service import ObsidianService
    return ObsidianService()


@tool
def delete_note(path: str) -> dict:
    """Remove uma nota do Vault Obsidian."""
    logger.info("[info] delete_note - removendo nota")
    svc = _get_service()
    svc.delete_note(relative_path=path)
    return NoteResponse(status="DELETED", path=path).model_dump()
