import re
from enum import Enum
from loguru import logger
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from app.config.settings import settings


class IntentType(str, Enum):
    FAST = "FAST"
    MEMORY = "MEMORY"
    SMART = "SMART"


FAST_KEYWORDS = [
    "liste minhas notas",
    "liste notas",
    "mostre minhas notas",
    "list notes",
    "list my notes",
    "crie uma nota",
    "criar nota",
    "create note",
    "create_note",
    "read_note",
    "update_note",
    "delete_note",
    "search_notes",
    "save_conversation",
    "salve esta conversa",
    "guarde isto",
    "atualize esta nota",
    "oi",
    "olá",
    "ola",
    "hello",
    "hi",
    "tudo bem",
    "como vai",
]

MEMORY_KEYWORDS = [
    "o que voce sabe sobre",
    "o que existe na nota",
    "what do you know about",
    "what is in the note",
    "busque no vault",
    "search in vault",
    "contexto",
    "context",
    "recupere",
    "retrieve",
    "lembra",
    "remember",
    "ja falamos sobre",
    "we talked about",
    "explique",
    "explique sobre",
    "resumo",
    "resumir",
    "o que e",
    "o que eh",
]

SYSTEM_PROMPT_CLASSIFIER = """Classifique a intencao do usuario em uma das categorias:

FAST: acao direta em ferramentas (criar, ler, atualizar, deletar, listar notas, salvar conversa). Nao precisa de conhecimento externo.

MEMORY: pergunta que requer conhecimento do Vault Obsidian (busca semantica, contexto, lembrancas). Precisa de RAG.

SMART: pergunta complexa que requer raciocinio, planejamento ou multiplas ferramentas. Usa LangGraph.

Responda apenas com o nome da categoria: FAST, MEMORY ou SMART."""


class IntentClassifier:
    def __init__(self):
        logger.info("[start] IntentClassifier - __init__")
        self._llm: ChatOllama | None = None
        logger.debug("[finish] IntentClassifier - __init__")

    def _get_llm(self) -> ChatOllama:
        if self._llm is None:
            logger.info("[info] IntentClassifier - lazy loading LLM")
            self._llm = ChatOllama(
                model=settings.OLLAMA_FAST_MODEL,
                base_url=settings.OLLAMA_BASE_URL,
                temperature=0,
            )
        return self._llm

    def _match_keyword(self, message: str) -> IntentType | None:
        lower = message.lower().strip()
        for kw in FAST_KEYWORDS:
            if kw in lower:
                logger.info(
                    f"[info] IntentClassifier - keyword FAST: \"{kw}\""
                )
                return IntentType.FAST
        for kw in MEMORY_KEYWORDS:
            if kw in lower:
                logger.info(
                    f"[info] IntentClassifier - keyword MEMORY: \"{kw}\""
                )
                return IntentType.MEMORY
        return None

    async def classify(self, message: str) -> IntentType:
        logger.info(f"[start] IntentClassifier - classify")
        keyword_match = self._match_keyword(message)
        if keyword_match:
            logger.debug("[finish] IntentClassifier - classify (keyword)")
            return keyword_match

        logger.info("[info] IntentClassifier - fallback LLM")
        llm = self._get_llm()
        response = await llm.ainvoke([
            SystemMessage(content=SYSTEM_PROMPT_CLASSIFIER),
            HumanMessage(content=message),
        ])
        content = response.content.strip().upper()
        if "FAST" in content:
            logger.debug("[finish] IntentClassifier - classify (LLM: FAST)")
            return IntentType.FAST
        if "MEMORY" in content:
            logger.debug("[finish] IntentClassifier - classify (LLM: MEMORY)")
            return IntentType.MEMORY
        logger.debug("[finish] IntentClassifier - classify (LLM: SMART default)")
        return IntentType.SMART