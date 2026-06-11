from loguru import logger
from langchain_core.tools import tool


def _get_memory():
    from app.memory.memory_service import MemoryService
    return MemoryService()


@tool
def save_conversation(summary: str, user_message: str, assistant_response: str, user_id: str = "default") -> str:
    """Salva um resumo de conversa no vault como memoria de longo prazo."""
    logger.info(f"[info] save_conversation - salvando memoria [user={user_id}]")
    svc = _get_memory()
    path = svc.save_conversation(
        user_id=user_id,
        session_id="agent",
        summary=summary,
        user_message=user_message,
        assistant_response=assistant_response,
    )
    return f"Conversa salva em: {path}"
