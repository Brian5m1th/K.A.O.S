from loguru import logger
from langchain_core.tools import tool
from app.agent.nodes.executor import TOOL_REGISTRY
from app.router.intent_classifier import IntentType


def parse_tool_call(user_message: str) -> tuple[str, dict] | None:
    lower = user_message.lower().strip()
    for tool_name in TOOL_REGISTRY:
        if tool_name.replace("_", " ") in lower or tool_name in lower:
            logger.info(f"[info] fast_router - tool match: {tool_name}")
            return tool_name, {}
    return None


async def fast_route(user_message: str) -> str | None:
    logger.info("[start] fast_route")
    parsed = parse_tool_call(user_message)
    if parsed is None:
        logger.info("[skip] fast_route - nenhuma tool reconhecida")
        logger.debug("[finish] fast_route")
        return None

    tool_name, tool_args = parsed
    logger.info(f"[info] fast_route - executando: {tool_name}")
    tool_fn = TOOL_REGISTRY.get(tool_name)
    if not tool_fn:
        logger.error(f"[error] fast_route - tool nao registrada: {tool_name}")
        logger.debug("[finish] fast_route")
        return None

    result = tool_fn.invoke(tool_args)
    logger.debug("[finish] fast_route")
    return str(result) if result else None