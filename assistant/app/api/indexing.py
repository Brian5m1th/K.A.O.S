from loguru import logger
from fastapi import APIRouter

from app.rag.indexer.vault_indexer import VaultIndexer

router = APIRouter(prefix="/indexing", tags=["Indexing"])


def _get_indexer() -> VaultIndexer:
    return VaultIndexer()


@router.post("/full")
async def full_reindex() -> dict:
    logger.info("[start] indexing - full_reindex")
    indexer = _get_indexer()
    result = indexer.index_vault()
    logger.debug("[finish] indexing - full_reindex")
    return result
