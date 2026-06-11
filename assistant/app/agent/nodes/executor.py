from loguru import logger

from app.agent.state import AgentState
from app.obsidian.tools.create_note_tool import create_note
from app.obsidian.tools.read_note_tool import read_note
from app.obsidian.tools.update_note_tool import update_note
from app.obsidian.tools.delete_note_tool import delete_note
from app.obsidian.tools.search_notes_tool import search_notes

TOOL_REGISTRY: dict = {
    "create_note": create_note,
    "read_note": read_note,
    "update_note": update_note,
    "delete_note": delete_note,
    "search_notes": search_notes,
}


def executor(state: AgentState) -> dict:
    logger.info("[start] executor")
    tool_name = state.get("tool_to_call")
    tool_args = state.get("tool_args", {})

    if not tool_name or tool_name not in TOOL_REGISTRY:
        logger.error(f"[error] executor - ferramenta desconhecida: {tool_name}")
        logger.debug("[finish] executor")
        return {
            "tool_result": {
                "error": f"Ferramenta '{tool_name}' não encontrada."
            }
        }

    logger.info(f"[info] executor - executando: {tool_name}")
    tool_fn = TOOL_REGISTRY[tool_name]
    result = tool_fn.invoke(tool_args)
    logger.debug("[finish] executor")
    return {"tool_result": result, "tool_to_call": None}
