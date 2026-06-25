from loguru import logger
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.service.llm_service import LLMService

router = APIRouter(prefix="/health", tags=["Health"])


class HealthResponse(BaseModel):
    status: str
    version: str


class ReadinessResponse(BaseModel):
    status: str
    services: dict[str, bool]


def get_llm_service() -> LLMService:
    return LLMService()


@router.get("", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    logger.debug("[info] health - check OK")
    return HealthResponse(status="ok", version="0.1.0")


@router.get("/readiness", response_model=ReadinessResponse)
async def readiness_check(
    llm: LLMService = Depends(get_llm_service),
) -> ReadinessResponse:
    logger.debug("[start] health - readiness_check")
    ollama_ok = await llm.check_availability()
    if not ollama_ok:
        logger.debug("[fallback] health - Ollama indisponivel, modo degradado")
    logger.debug("[finish] health - readiness_check")
    return ReadinessResponse(
        status="ready" if ollama_ok else "degraded",
        services={"ollama": ollama_ok},
    )
