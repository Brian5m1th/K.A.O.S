from loguru import logger
from langchain_core.tools import tool


def _get_memory():
    from app.memory.memory_service import MemoryService
    return MemoryService()


@tool
def save_conversation(summary: str, user_message: str, assistant_response: str) -> str:
    """Salva um resumo de conversa no vault como memoria de longo prazo."""
    logger.info("[info] save_conversation - salvando memoria")
    svc = _get_memory()
    path = svc.save_conversation(
        session_id="agent",
        summary=summary,
        user_message=user_message,
        assistant_response=assistant_response,
    )
    return f"Conversa salva em: {path}"
