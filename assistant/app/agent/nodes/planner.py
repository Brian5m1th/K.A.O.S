import time
from loguru import logger
from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama

from app.agent.state import AgentState
from app.config.settings import settings
from app.memory.memory_service import MemoryService

SYSTEM_PROMPT = """Você é um assistente pessoal inteligente com acesso ao Vault Obsidian do usuário.

Ferramentas disponíveis:
- create_note(title, folder, content): Cria uma nova nota no Vault
- read_note(path): Lê o conteúdo de uma nota
- update_note(path, content, mode): Atualiza uma nota (overwrite ou append)
- delete_note(path): Remove uma nota
- list_notes(folder): Lista notas por pasta (vazio para todas)
- search_notes(query): Busca notas por palavra-chave
- list_projects(): Lista projetos no Vault (pastas com notas)
- save_conversation(summary, user_message, assistant_response): Salva um resumo de conversa como memoria de longo prazo

Use as ferramentas quando o usuário solicitar explicitamente ações de memória.
Prefira responder diretamente quando tiver contexto suficiente.

Comandos especiais:
- "salve esta conversa" ou "guarde isto" -> use save_conversation
- "atualize esta nota" -> use search_notes + read_note + update_note"""

_llm = ChatOllama(
    model=settings.OLLAMA_MODEL, base_url=settings.OLLAMA_BASE_URL
)


def planner(state: AgentState) -> dict:
    start = time.perf_counter()
    user_id = state.get("user_id", "")
    logger.info(f"[start] planner [user={user_id}]")
    
    context = state.get("retrieved_context", [])
    context_chars = sum(len(c.get("content", "")) for c in context)
    
    context_text = "\n\n".join(
        f"[{c['path']}]\n{c['content']}"
        for c in context
    )
    system_with_context = SYSTEM_PROMPT
    if context_text:
        system_with_context += f"\n\nContexto recuperado do Vault:\n{context_text}"

    memory = MemoryService()
    preferences = memory.get_preferences(user_id)
    if preferences:
        system_with_context += f"\n\nPreferencias do usuario:\n{preferences}"

    messages = [SystemMessage(content=system_with_context)] + state["messages"]
    prompt_chars = len(system_with_context) + sum(len(m.content) for m in state["messages"])
    
    response = _llm.invoke(messages)

    elapsed = (time.perf_counter() - start) * 1000
    logger.info(
        f"[audit] planner | user={user_id} | context_chunks={len(context)} | "
        f"context_chars={context_chars} | prompt_chars={prompt_chars} | latency_ms={elapsed:.0f}"
    )

    if hasattr(response, "tool_calls") and response.tool_calls:
        tool_call = response.tool_calls[0]
        logger.info(f"[info] planner - ferramenta: {tool_call['name']} [user={user_id}]")
        logger.debug("[finish] planner")
        return {
            "tool_to_call": tool_call["name"],
            "tool_args": tool_call["args"],
            "messages": [response],
        }

    logger.debug("[finish] planner")
    return {"tool_to_call": None, "messages": [response]}
