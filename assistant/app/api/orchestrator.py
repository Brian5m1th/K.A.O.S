from uuid import UUID

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from loguru import logger

from app.domain.chat import ChatRequest
from app.orchestrator.dead_letter_queue import DeadLetterQueue
from app.orchestrator.universal_orchestrator import UniversalOrchestrator
from app.providers.register_all import register_all_providers
from app.workflows.impl.registry import register_workflows

_orchestrator: UniversalOrchestrator | None = None

router = APIRouter(prefix="/api/orchestrator", tags=["Orchestrator"])


def _get_orchestrator() -> UniversalOrchestrator:
    global _orchestrator
    if _orchestrator is None:
        register_all_providers()
        register_workflows()
        _orchestrator = UniversalOrchestrator()
    return _orchestrator


@router.post("/execute")
async def execute_workflow(
    request: ChatRequest,
    workflow: str = "chat",
    capabilities: str = "",
) -> StreamingResponse:
    logger.info(
        f"[start] orchestrator - execute workflow={workflow} user={request.user_id or 'anonymous'}"
    )

    cap_list = [c.strip() for c in capabilities.split(",") if c.strip()]
    user_uuid = UUID(request.user_id) if request.user_id else UUID(int=0)

    orchestrator = _get_orchestrator()

    async def stream():
        async for chunk in orchestrator.execute(
            request=request,
            workflow=workflow,
            capabilities=cap_list,
            user_id=user_uuid,
        ):
            yield chunk

    return StreamingResponse(stream(), media_type="text/plain")


@router.get("/dlq")
async def list_dlq():
    return {
        "failed": [str(f.execution_id) for f in DeadLetterQueue.list_all()],
        "count": DeadLetterQueue.count(),
    }


@router.delete("/dlq")
async def clear_dlq():
    DeadLetterQueue.clear()
    return {"status": "cleared"}
