from loguru import logger
from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama

from app.agent.state import AgentState
from app.config.settings import settings

SYSTEM_PROMPT = """Você é um assistente pessoal inteligente com acesso ao Vault Obsidian do usuário.

Ferramentas disponíveis:
- create_note(title, folder, content): Cria uma nova nota no Vault
- read_note(path): Lê o conteúdo de uma nota
- update_note(path, content, mode): Atualiza uma nota (overwrite ou append)
- delete_note(path): Remove uma nota
- search_notes(query): Busca notas por palavra-chave

Use as ferramentas quando o usuário solicitar explicitamente ações de memória.
Prefira responder diretamente quando tiver contexto suficiente."""

_llm = ChatOllama(
    model=settings.OLLAMA_MODEL, base_url=settings.OLLAMA_BASE_URL
)


def planner(state: AgentState) -> dict:
    logger.info("[start] planner")
    context_text = "\n\n".join(
        f"[{c['path']}]\n{c['content']}"
        for c in state.get("retrieved_context", [])
    )
    system_with_context = SYSTEM_PROMPT
    if context_text:
        system_with_context += f"\n\nContexto recuperado do Vault:\n{context_text}"

    messages = [SystemMessage(content=system_with_context)] + state["messages"]
    response = _llm.invoke(messages)

    if hasattr(response, "tool_calls") and response.tool_calls:
        tool_call = response.tool_calls[0]
        logger.info(f"[info] planner - ferramenta: {tool_call['name']}")
        logger.debug("[finish] planner")
        return {
            "tool_to_call": tool_call["name"],
            "tool_args": tool_call["args"],
            "messages": [response],
        }

    logger.debug("[finish] planner")
    return {"tool_to_call": None, "messages": [response]}
