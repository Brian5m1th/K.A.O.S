from loguru import logger
from fastapi import APIRouter
from pydantic import BaseModel, Field
from qdrant_client import QdrantClient

from app.config.settings import settings
from app.rag.retriever.semantic_retriever import SemanticRetriever

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
async def get_rag_context(request: RAGContextRequest) -> RAGContextResponse:
    logger.info("[start] rag - get_rag_context")
    retriever = SemanticRetriever()
    results = retriever.search(query=request.query, limit=request.limit)
    logger.debug("[finish] rag - get_rag_context")
    return RAGContextResponse(
        query=request.query,
        context=[
            RAGContextResult(path=r.path, score=r.score, excerpt=r.excerpt)
            for r in results
        ],
    )


@router.get("/diagnostics", response_model=RAGDiagnosticsResponse)
async def get_rag_diagnostics() -> RAGDiagnosticsResponse:
    logger.info("[start] rag - diagnostics")
    client = QdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)
    resp = RAGDiagnosticsResponse(
        qdrant_host=settings.QDRANT_HOST,
        qdrant_port=settings.QDRANT_PORT,
        collection=settings.QDRANT_COLLECTION,
        points_count=None,
        dimension=None,
        status="checking",
    )
    try:
        collections = [c.name for c in client.get_collections().collections]
        if settings.QDRANT_COLLECTION not in collections:
            resp.status = "no_collection"
            resp.error = f"Colecao '{settings.QDRANT_COLLECTION}' nao encontrada"
            logger.warning(f"[warn] rag - diagnostics: {resp.error}")
            logger.debug("[finish] rag - diagnostics")
            return resp
        info = client.get_collection(settings.QDRANT_COLLECTION)
        resp.points_count = info.points_count
        resp.dimension = info.config.params.vectors.size
        resp.status = "ok"
        logger.info(f"[info] rag - diagnostics: {resp.points_count} pontos, dim={resp.dimension}")
    except Exception as e:
        resp.status = "error"
        resp.error = str(e)
        logger.error(f"[error] rag - diagnostics: {e}")
    logger.debug("[finish] rag - diagnostics")
    return resp
