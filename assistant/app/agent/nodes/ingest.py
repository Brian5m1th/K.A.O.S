import time
from pathlib import Path
from loguru import logger
from langchain_core.messages import SystemMessage, HumanMessage

from app.agent.state import AgentState
from app.config.settings import settings
from app.obsidian.tools.wiki.create_entity_tool import create_entity
from app.obsidian.tools.wiki.create_concept_tool import create_concept
from app.obsidian.tools.wiki.create_source_tool import create_source
from app.obsidian.tools.wiki.update_index_tool import update_index
from app.obsidian.tools.wiki.append_log_tool import append_log
from app.rag.embeddings.embedder import get_embedder
from app.rag.indexer.vault_indexer import VaultIndexer
from app.rag.chunking.text_splitter import MarkdownSplitter


def _get_llm():
    from langchain_ollama import ChatOllama
    return ChatOllama(model=settings.OLLAMA_MODEL, base_url=settings.OLLAMA_BASE_URL)


INGEST_PROMPT = """You are analyzing a source document for the K.A.O.S knowledge wiki.

Extract the following from the document and return as JSON:
{
  "title": "Document title",
  "summary": "2-3 paragraph summary of key points",
  "entities": [
    {"name": "Entity Name", "summary": "What this entity is", "tags": ["tag1"]}
  ],
  "concepts": [
    {"name": "Concept Name", "summary": "What this concept is", "tags": ["tag1"]}
  ],
  "tags": ["tag1", "tag2"]
}

Entities are concrete objects: people, projects, technologies, organizations.
Concepts are abstractions: RAG, embeddings, LangGraph, design patterns.

Respond with ONLY the JSON, no other text."""


def ingest_source(state: AgentState) -> dict:
    start = time.perf_counter()
    logger.info("[start] ingest_source")

    source_path = state.get("ingest_source_path", "")
    if not source_path:
        return {
            "messages": [HumanMessage(content="Erro: caminho da fonte nao fornecido. Especifique o arquivo em raw/.")]
        }

    vault = Path(settings.OBSIDIAN_VAULT_PATH)
    raw_file = vault / "raw" / source_path
    if not raw_file.exists():
        return {
            "messages": [HumanMessage(content=f"Erro: arquivo nao encontrado em raw/{source_path}")]
        }

    content = raw_file.read_text(encoding="utf-8")
    logger.info(f"[info] ingest_source - lido: raw/{source_path} ({len(content)} chars)")

    llm = _get_llm()
    response = llm.invoke([
        SystemMessage(content=INGEST_PROMPT),
        HumanMessage(content=f"Documento: {source_path}\n\n{content[:8000]}"),
    ])

    import json
    import re
    text = response.content.strip()
    json_match = re.search(r"\{.*\}", text, re.DOTALL)
    if not json_match:
        logger.error("[error] ingest_source - falha ao extrair JSON da resposta LLM")
        return {
            "messages": [HumanMessage(content="Erro ao processar o documento: resposta do LLM invalida.")]
        }

    try:
        data = json.loads(json_match.group())
    except json.JSONDecodeError as e:
        logger.error(f"[error] ingest_source - JSON invalido: {e}")
        return {
            "messages": [HumanMessage(content=f"Erro ao processar o documento: JSON invalido.")]
        }

    title = data.get("title", Path(source_path).stem)
    summary = data.get("summary", "")
    entities = data.get("entities", [])
    concepts = data.get("concepts", [])
    tags = data.get("tags", [])
    source_tags = tags + ["fonte"]

    source_draft = create_source.invoke({
        "name": title,
        "content": summary,
        "tags": source_tags,
    })
    logger.info(f"[info] ingest_source - source draft: {source_draft}")

    created = {"source": source_draft, "entities": [], "concepts": []}

    for entity in entities:
        try:
            draft = create_entity.invoke({
                "name": entity["name"],
                "summary": entity.get("summary", ""),
                "tags": entity.get("tags", []),
                "sources": [source_draft],
            })
            created["entities"].append(draft)
            logger.info(f"[info] ingest_source - entity draft: {draft}")
        except Exception as e:
            logger.error(f"[error] ingest_source - entidade {entity.get('name')}: {e}")

    for concept in concepts:
        try:
            draft = create_concept.invoke({
                "name": concept["name"],
                "summary": concept.get("summary", ""),
                "tags": concept.get("tags", []),
                "sources": [source_draft],
            })
            created["concepts"].append(draft)
            logger.info(f"[info] ingest_source - concept draft: {draft}")
        except Exception as e:
            logger.error(f"[error] ingest_source - conceito {concept.get('name')}: {e}")

    try:
        vault = Path(settings.OBSIDIAN_VAULT_PATH)
        splitter = MarkdownSplitter()
        embedder = get_embedder()
        indexer = VaultIndexer()
        indexer.index_file(str(raw_file))
        logger.info("[info] ingest_source - reindexado no Qdrant")
    except Exception as e:
        logger.warning(f"[skip] ingest_source - reindex falhou: {e}")

    elapsed = (time.perf_counter() - start) * 1000
    entity_names = [e["name"] for e in entities]
    concept_names = [c["name"] for c in concepts]

    result_msg = (
        f"## Documento processado: {title}\n\n"
        f"**Resumo**: {summary[:300]}...\n\n"
        f"**Entidades extraidas** ({len(entities)}): {', '.join(entity_names) if entity_names else 'nenhuma'}\n"
        f"**Conceitos extraidos** ({len(concepts)}): {', '.join(concept_names) if concept_names else 'nenhum'}\n\n"
        f"**Drafts criados**:\n"
        f"- Source: `{source_draft}`\n"
        f"- Entities: {', '.join(created['entities'])}\n"
        f"- Concepts: {', '.join(created['concepts'])}\n\n"
        f"Use `approve_draft` para aprovar cada draft ou `reject_draft` para rejeitar.\n"
        f"Use `list_drafts()` para ver todos os pendentes.\n\n"
        f"_Processado em {elapsed:.0f}ms_"
    )

    logger.info(f"[audit] ingest_source | title={title} | entities={len(entities)} | concepts={len(concepts)} | latency_ms={elapsed:.0f}")
    logger.debug("[finish] ingest_source")
    return {
        "messages": [HumanMessage(content=result_msg)],
        "ingest_source_path": None,
    }
