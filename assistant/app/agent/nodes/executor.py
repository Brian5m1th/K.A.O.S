from loguru import logger

from app.agent.state import AgentState
from app.obsidian.tools.create_note_tool import create_note
from app.obsidian.tools.read_note_tool import read_note
from app.obsidian.tools.update_note_tool import update_note
from app.obsidian.tools.delete_note_tool import delete_note
from app.obsidian.tools.search_notes_tool import search_notes
from app.obsidian.tools.list_notes_tool import list_notes
from app.obsidian.tools.save_conversation_tool import save_conversation
from app.obsidian.tools.list_projects_tool import list_projects
from app.obsidian.tools.wiki import (
    create_entity,
    update_entity,
    create_concept,
    update_concept,
    create_source,
    create_synthesis,
    file_synthesis_page,
    append_log,
    update_index,
    approve_draft,
    reject_draft,
    list_drafts,
    read_wiki_page,
    lint_wiki,
)
from app.providers.email.email_tool import read_emails, send_email
from app.providers.whatsapp.whatsapp_tool import send_whatsapp
from app.providers.aws.aws_tool import aws_list_instances, aws_describe_service, aws_run_command

TOOL_REGISTRY: dict = {
    "create_note": create_note,
    "read_note": read_note,
    "update_note": update_note,
    "delete_note": delete_note,
    "search_notes": search_notes,
    "list_notes": list_notes,
    "list_projects": list_projects,
    "save_conversation": save_conversation,
    "create_entity": create_entity,
    "update_entity": update_entity,
    "create_concept": create_concept,
    "update_concept": update_concept,
    "create_source": create_source,
    "create_synthesis": create_synthesis,
    "file_synthesis_page": file_synthesis_page,
    "append_log": append_log,
    "update_index": update_index,
    "approve_draft": approve_draft,
    "reject_draft": reject_draft,
    "list_drafts": list_drafts,
    "read_wiki_page": read_wiki_page,
    "lint_wiki": lint_wiki,
    "read_emails": read_emails,
    "send_email": send_email,
    "send_whatsapp": send_whatsapp,
    "aws_list_instances": aws_list_instances,
    "aws_describe_service": aws_describe_service,
    "aws_run_command": aws_run_command,
}


def executor(state: AgentState) -> dict:
    user_id = state.get("user_id", "")
    logger.info(f"[start] executor [user={user_id}]")
    tool_name = state.get("tool_to_call")
    tool_args = state.get("tool_args", {})

    if not tool_name or tool_name not in TOOL_REGISTRY:
        logger.error(f"[error] executor - ferramenta desconhecida: {tool_name}")
        logger.debug("[finish] executor")
        return {"tool_result": {"error": f"Ferramenta '{tool_name}' não encontrada."}}

    if "user_id" not in tool_args and user_id:
        tool_args["user_id"] = user_id

    logger.info(f"[info] executor - executando: {tool_name} [user={user_id}]")
    tool_fn = TOOL_REGISTRY[tool_name]
    result = tool_fn.invoke(tool_args)
    logger.debug("[finish] executor")
    return {"tool_result": result, "tool_to_call": None}
