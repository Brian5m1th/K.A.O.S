import time
from loguru import logger
from fastapi import APIRouter
from qdrant_client import QdrantClient

from app.config.settings import settings
from app.obsidian.vault_init import create_vault_structure
from app.rag.indexer.vault_indexer import VaultIndexer

router = APIRouter(prefix="/indexing", tags=["Indexing"])


def _get_indexer() -> VaultIndexer:
    return VaultIndexer()


@router.post("/full")
async def full_reindex() -> dict:
    logger.info("[start] indexing - full_reindex")
    start = time.perf_counter()
    indexer = _get_indexer()
    result = indexer.index_vault()
    elapsed = (time.perf_counter() - start) * 1000
    try:
        client = QdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)
        info = client.get_collection(settings.QDRANT_COLLECTION)
        result["qdrant_points"] = info.points_count
    except Exception:
        result["qdrant_points"] = 0
    result["latency_ms"] = round(elapsed, 0)
    logger.info(f"[audit] indexing | {result.get('files', 0)} files | {result.get('chunks', 0)} chunks | qdrant={result.get('qdrant_points', 0)} | {elapsed:.0f}ms")
    logger.debug("[finish] indexing - full_reindex")
    return result


@router.post("/init-folders")
async def init_vault_folders() -> dict:
    logger.info("[start] indexing - init_vault_folders")
    created = create_vault_structure()
    logger.debug("[finish] indexing - init_vault_folders")
    return {"created": created, "total": len(created)}
