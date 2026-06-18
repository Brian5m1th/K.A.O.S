import time
from pathlib import Path
from loguru import logger
from langchain_core.messages import HumanMessage

from app.agent.state import AgentState
from app.config.settings import settings
from app.rag.retriever.semantic_retriever import SemanticRetriever

_retriever: SemanticRetriever | None = None


def _get_retriever() -> SemanticRetriever:
    global _retriever
    if _retriever is None:
        _retriever = SemanticRetriever()
    return _retriever


def _read_wiki_index() -> str:
    idx = Path(settings.OBSIDIAN_VAULT_PATH) / "wiki" / "index.md"
    if idx.exists():
        return idx.read_text(encoding="utf-8")
    return ""


def _read_wiki_page(relative_path: str) -> str | None:
    full = Path(settings.OBSIDIAN_VAULT_PATH) / relative_path
    if full.exists():
        return full.read_text(encoding="utf-8")
    return None


def retrieve_context(state: AgentState) -> dict:
    start = time.perf_counter()
    logger.info("[start] retrieve_context")
    last_message = next(
        (m for m in reversed(state["messages"]) if isinstance(m, HumanMessage)),
        None,
    )
    if not last_message:
        logger.info("[skip] retrieve_context - sem mensagem do usuario")
        logger.debug("[finish] retrieve_context")
        return {"retrieved_context": []}

    query = last_message.content.lower()
    logger.info(f'[info] retrieve_context - query="{query}"')
    wiki_context = []

    index_content = _read_wiki_index()
    if index_content:
        wiki_context.append({"path": "wiki/index.md", "content": index_content, "score": 1.0})
        matches = [line for line in index_content.splitlines() if query in line.lower()]
        for match in matches[:3]:
            for prefix in ["wiki/entities/", "wiki/concepts/", "wiki/sources/", "wiki/synthesis/"]:
                if prefix in match:
                    path_candidate = match.split("[[")[-1].split("]]")[0] if "[[" in match else match.strip()
                    content = _read_wiki_page(path_candidate)
                    if content:
                        wiki_context.append({"path": path_candidate, "content": content[:2000], "score": 0.9})
                        logger.info(f"[info] retrieve_context - wiki hit: {path_candidate}")

    results = _get_retriever().search(query=query, limit=3)
    elapsed = (time.perf_counter() - start) * 1000
    top_score = results[0].score if results else 0.0
    logger.info(
        f'[audit] retrieve | query="{query[:50]}..." | '
        f"wiki_pages={len(wiki_context) - 1} | qdrant_results={len(results)} | top_score={top_score:.4f} | latency_ms={elapsed:.0f}"
    )
    qdrant_context = [
        {"path": r.path, "content": r.excerpt, "score": r.score}
        for r in results
    ]
    combined = wiki_context + qdrant_context
    logger.debug("[finish] retrieve_context")
    return {"retrieved_context": combined}
