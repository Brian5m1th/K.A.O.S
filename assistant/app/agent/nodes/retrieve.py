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
    last_message = next(
        (m for m in reversed(state["messages"]) if isinstance(m, HumanMessage)),
        None,
    )
    if not last_message:
        return {"retrieved_context": []}

    results = _get_retriever().search(query=last_message.content, limit=5)
    context = [
        {"path": r.path, "content": r.excerpt, "score": r.score}
        for r in results
    ]
    return {"retrieved_context": context}
