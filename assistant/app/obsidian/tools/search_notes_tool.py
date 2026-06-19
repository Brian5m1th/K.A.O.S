from loguru import logger
from langchain_core.tools import tool


def _get_service():
    from app.obsidian.services.obsidian_service import ObsidianService

    return ObsidianService()


@tool
def search_notes(query: str, max_results: int = 5) -> dict:
    """Busca textual por palavra-chave em todas as notas do Vault."""
    logger.info("[info] search_notes - buscando notas")
    svc = _get_service()
    results = svc.search_text(query=query, max_results=max_results)
    return {
        "query": query,
        "total": len(results),
        "documents": [r.model_dump() for r in results],
    }
