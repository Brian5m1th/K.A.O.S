from fastapi import APIRouter

from app.rag.indexer.vault_indexer import VaultIndexer

router = APIRouter(prefix="/indexing", tags=["Indexing"])


def _get_indexer() -> VaultIndexer:
    return VaultIndexer()


@router.post("/full")
async def full_reindex() -> dict:
    indexer = _get_indexer()
    return indexer.index_vault()
