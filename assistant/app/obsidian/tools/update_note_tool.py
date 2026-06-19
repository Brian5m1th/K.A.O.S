from loguru import logger
from langchain_core.tools import tool
from app.domain.document import NoteResponse


def _get_service():
    from app.obsidian.services.obsidian_service import ObsidianService

    return ObsidianService()


@tool
def update_note(path: str, content: str, mode: str = "overwrite") -> dict:
    """Atualiza uma nota existente (overwrite ou append)."""
    logger.info("[info] update_note - atualizando nota")
    svc = _get_service()
    svc.update_note(relative_path=path, content=content, mode=mode)
    return NoteResponse(status="UPDATED", path=path).model_dump()
