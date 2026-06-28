from pathlib import Path
from loguru import logger
from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field
from qdrant_client import QdrantClient

from app.config.settings import settings
from app.rag.retriever.semantic_retriever import SemanticRetriever

from app.core.runtime_path_resolver import RuntimePathResolver

router = APIRouter(prefix="/rag", tags=["RAG"])


class RAGContextRequest(BaseModel):
    query: str = Field(..., min_length=1, description="Pergunta do usuário")
    limit: int = Field(default=5, ge=1, le=20)


class RAGContextResult(BaseModel):
    path: str
    score: float
    excerpt: str


class RAGContextResponse(BaseModel):
    query: str
    context: list[RAGContextResult]


class RAGDiagnosticsResponse(BaseModel):
    qdrant_host: str
    qdrant_port: int
    collection: str
    points_count: int | None
    dimension: int | None
    status: str
    error: str | None = None


@router.post("/context", response_model=RAGContextResponse)
async def get_context(body: RAGContextRequest):
    logger.info("[start] rag - get_context: {}", body.query)
    client = QdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)
    retriever = SemanticRetriever(client)

    try:
        results = await retriever.retrieve(body.query, limit=body.limit)
        response_items = []
        for r in results:
            response_items.append(
                RAGContextResult(
                    path=r.get("metadata", {}).get("path", "unknown"),
                    score=r.get("score", 0.0),
                    excerpt=r.get("content", ""),
                )
            )
        logger.debug("[finish] rag - get_context")
        return RAGContextResponse(query=body.query, context=response_items)
    except Exception as e:
        logger.error(f"[error] rag - get_context: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/diagnostics", response_model=RAGDiagnosticsResponse)
async def get_diagnostics():
    logger.info("[start] rag - diagnostics")
    resp = RAGDiagnosticsResponse(
        qdrant_host=settings.QDRANT_HOST,
        qdrant_port=settings.QDRANT_PORT,
        collection=settings.QDRANT_COLLECTION,
        points_count=None,
        dimension=None,
        status="healthy",
    )
    client = QdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)
    try:
        res = client.get_collection(settings.QDRANT_COLLECTION)
        resp.points_count = res.points_count
        resp.dimension = res.config.params.vectors.size
        logger.info(
            f"[info] rag - diagnostics: {resp.points_count} pontos, dim={resp.dimension}"
        )
    except Exception as e:
        resp.status = "error"
        resp.error = str(e)
        logger.error(f"[error] rag - diagnostics: {e}")
    logger.debug("[finish] rag - diagnostics")
    return resp


@router.get("/vault/files")
async def list_vault_files():
    logger.info("[start] rag - list_vault_files")
    vault_dir = RuntimePathResolver.get_vault_path().resolve()
    if not vault_dir.exists():
        logger.warning("[rag] vault directory does not exist: {}", vault_dir)
        return {"files": []}

    md_files = []
    # Buscar arquivos md recursivamente no vault
    for p in vault_dir.glob("**/*.md"):
        try:
            rel_path = p.relative_to(vault_dir)
            md_files.append(
                {
                    "name": p.name,
                    "path": str(rel_path).replace("\\", "/"),
                    "size": p.stat().st_size,
                }
            )
        except Exception:
            pass

    # Ordenar pelo caminho relativo
    md_files.sort(key=lambda x: x["path"].lower())

    logger.debug("[finish] rag - list_vault_files")
    return {"files": md_files}


@router.get("/vault/file")
async def get_vault_file(path: str):
    logger.info("[start] rag - get_vault_file: {}", path)
    
    # Prevenir Path Traversal e inputs absolutos maliciosos
    if Path(path).is_absolute() or ".." in path:
        raise HTTPException(status_code=403, detail="Access denied")

    vault_dir = RuntimePathResolver.get_vault_path().resolve()

    # Resolver o caminho absoluto e validar que não sai do vault
    target_path = (vault_dir / path).resolve()
    try:
        if not target_path.is_relative_to(vault_dir):
            raise HTTPException(status_code=403, detail="Access denied")
    except ValueError:
        raise HTTPException(status_code=403, detail="Access denied")

    if not target_path.exists() or not target_path.is_file():
        raise HTTPException(status_code=404, detail="File not found")

    try:
        content = target_path.read_text(encoding="utf-8")
        return PlainTextResponse(content)
    except Exception as e:
        logger.error("[rag] failed to read vault file: {}", e)
        raise HTTPException(status_code=500, detail=f"Failed to read file: {str(e)}")
