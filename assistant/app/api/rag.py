from loguru import logger
from fastapi import APIRouter
from pydantic import BaseModel, Field
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
