from loguru import logger
from langchain_core.tools import tool


def _get_service():
    from app.obsidian.services.obsidian_service import ObsidianService
    return ObsidianService()


@tool
def list_notes(folder: str = "") -> dict:
    """Lista notas Markdown no Vault Obsidian, opcionalmente filtradas por pasta."""
    logger.info("[info] list_notes - listando notas")
    svc = _get_service()
    notes = svc.list_notes(folder=folder)
    return {"folder": folder or "/", "total": len(notes), "notes": notes}
