from loguru import logger
from langchain_core.messages import HumanMessage

from app.agent.state import AgentState
from app.rag.retriever.semantic_retriever import SemanticRetriever

_retriever: SemanticRetriever | None = None


def _get_retriever() -> SemanticRetriever:
    global _retriever
    if _retriever is None:
        _retriever = SemanticRetriever()
    return _retriever


def retrieve_context(state: AgentState) -> dict:
    logger.info("[start] retrieve_context")
    last_message = next(
        (m for m in reversed(state["messages"]) if isinstance(m, HumanMessage)),
        None,
    )
    if not last_message:
        logger.info("[skip] retrieve_context - sem mensagem do usuario")
        logger.debug("[finish] retrieve_context")
        return {"retrieved_context": []}

    query = last_message.content
    logger.info(f"[info] retrieve_context - query=\"{query}\"")
    results = _get_retriever().search(query=query, limit=5)
    logger.info(f"[info] retrieve_context - resultados={len(results)}")
    context = [
        {"path": r.path, "content": r.excerpt, "score": r.score}
        for r in results
    ]
    logger.debug("[finish] retrieve_context")
    return {"retrieved_context": context}
