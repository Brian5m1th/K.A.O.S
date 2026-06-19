import time
from loguru import logger
from langchain_core.messages import SystemMessage

from app.agent.state import AgentState
from app.config.settings import settings
from app.llm.factory import LLMFactory
from app.memory.memory_service import MemoryService

SYSTEM_PROMPT = """Você é um assistente pessoal inteligente com acesso ao Vault Obsidian do usuário.

## Ferramentas de Notas
- create_note(title, folder, content): Cria uma nova nota no Vault
- read_note(path): Lê o conteúdo de uma nota
- update_note(path, content, mode): Atualiza uma nota (overwrite ou append)
- delete_note(path): Remove uma nota
- list_notes(folder): Lista notas por pasta (vazio para todas)
- search_notes(query): Busca notas por palavra-chave
- list_projects(): Lista projetos no Vault (pastas com notas)
- save_conversation(summary, user_message, assistant_response): Salva um resumo de conversa como memoria de longo prazo

## Ferramentas de Wiki (Conhecimento Estruturado)
- create_entity(name, summary, tags, sources): Cria página de entidade (pessoa, projeto, tecnologia)
- update_entity(path, content, tags, sources): Atualiza entidade existente
- create_concept(name, summary, tags, sources): Cria página de conceito (RAG, embeddings, LangGraph)
- update_concept(path, content, tags, sources): Atualiza conceito existente
- create_source(name, content, tags): Cria página de source com resumo do documento ingerido
- create_synthesis(title, content, citations, tags): Cria página de síntese (análise, comparação, tese)
- file_synthesis_page(question, answer, tags): Arquivamento automático de resposta complexa como síntese
- read_wiki_page(path): Lê uma página da wiki

## Ferramentas de Manutenção da Wiki
- approve_draft(path): Aprova um draft pendente (renomeia .draft.md para .md)
- reject_draft(path): Rejeita um draft (deleta .draft.md)
- list_drafts(): Lista todos os drafts pendentes
- append_log(entry): Adiciona entrada no log.md da wiki
- update_index(): Regenera o index.md com todas as páginas
- lint_wiki(): Verifica saúde da wiki (orphans, broken links, contradictions)

## Regras da Wiki
- Consulte AGENTS.md no wiki/ antes de criar/atualizar entidades e conceitos
- Toda criação/atualização usa Draft Mode: cria .draft.md, aguarda aprovação
- Entidades: wiki/entities/{slug}.md
- Conceitos: wiki/concepts/{slug}.md
- Sources: wiki/sources/YYYY-MM-DD_slug.md
- Síntese: wiki/synthesis/{slug}.md
- Todas as páginas wiki exigem frontmatter YAML (title, type, tags, sources, created, updated)
- Use append_log para registrar cada operação
- Use update_index após aprovação de drafts
- Respostas complexas ou análises profundas devem virar synthesis pages (use file_synthesis_page)

Use as ferramentas quando o usuário solicitar explicitamente ações de memória.
Prefira responder diretamente quando tiver contexto suficiente.

Comandos especiais:
- "salve esta conversa" ou "guarde isto" -> use save_conversation
- "atualize esta nota" -> use search_notes + read_note + update_note
- "ingira esta fonte" -> roteado automaticamente para o pipeline de ingestão (INGEST intent)"""

_factory: LLMFactory | None = None


def _get_factory() -> LLMFactory:
    global _factory
    if _factory is None:
        _factory = LLMFactory()
    return _factory


def planner(state: AgentState) -> dict:
    start = time.perf_counter()
    user_id = state.get("user_id", "")
    model = state.get("model")  # Get model from state (passed from request)
    logger.info(f"[start] planner [user={user_id} model={model}]")

    context = state.get("retrieved_context", [])
    context_chars = sum(len(c.get("content", "")) for c in context)

    context_text = "\n\n".join(f"[{c['path']}]\n{c['content']}" for c in context)
    system_with_context = SYSTEM_PROMPT
    if context_text:
        system_with_context += f"\n\nContexto recuperado do Vault:\n{context_text}"

    memory = MemoryService()
    preferences = memory.get_preferences(user_id)
    if preferences:
        system_with_context += f"\n\nPreferencias do usuario:\n{preferences}"

    messages = [SystemMessage(content=system_with_context)] + state["messages"]
    prompt_chars = len(system_with_context) + sum(
        len(m.content) for m in state["messages"]
    )

    factory = _get_factory()
    provider = factory.build(model or settings.OLLAMA_MODEL)
    response = provider.invoke(messages)

    elapsed = (time.perf_counter() - start) * 1000
    logger.info(
        f"[audit] planner | user={user_id} | context_chunks={len(context)} | "
        f"context_chars={context_chars} | prompt_chars={prompt_chars} | latency_ms={elapsed:.0f}"
    )

    if hasattr(response, "tool_calls") and response.tool_calls:
        tool_call = response.tool_calls[0]
        logger.info(
            f"[info] planner - ferramenta: {tool_call['name']} [user={user_id}]"
        )
        logger.debug("[finish] planner")
        return {
            "tool_to_call": tool_call["name"],
            "tool_args": tool_call["args"],
            "messages": [response],
        }

    logger.debug("[finish] planner")
    return {"tool_to_call": None, "messages": [response]}
