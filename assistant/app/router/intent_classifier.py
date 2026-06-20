from enum import Enum
from loguru import logger
from langchain_core.messages import SystemMessage, HumanMessage
from app.config.settings import settings
from app.llm.factory import LLMFactory


class IntentType(str, Enum):
    FAST = "FAST"
    MEMORY = "MEMORY"
    SMART = "SMART"
    INGEST = "INGEST"


INGEST_KEYWORDS = [
    "ingira esta fonte",
    "ingira este source",
    "ingest this source",
    "processe esta fonte",
    "processe este documento",
    "process this source",
    "ingira",
    "ingest",
]

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
        self._factory: LLMFactory | None = None
        logger.debug("[finish] IntentClassifier - __init__")

    def _get_provider(self):
        if self._factory is None:
            self._factory = LLMFactory()
        return self._factory.build(settings.FAST_MODEL_ID, temperature=0)

    def _match_keyword(self, message: str) -> IntentType | None:
        lower = message.lower().strip()
        for kw in INGEST_KEYWORDS:
            if kw in lower:
                logger.info(f'[info] IntentClassifier - keyword INGEST: "{kw}"')
                return IntentType.INGEST
        for kw in FAST_KEYWORDS:
            if kw in lower:
                logger.info(f'[info] IntentClassifier - keyword FAST: "{kw}"')
                return IntentType.FAST
        for kw in MEMORY_KEYWORDS:
            if kw in lower:
                logger.info(f'[info] IntentClassifier - keyword MEMORY: "{kw}"')
                return IntentType.MEMORY
        return None

    async def classify(self, message: str) -> IntentType:
        logger.info("[start] IntentClassifier - classify")
        keyword_match = self._match_keyword(message)
        if keyword_match:
            logger.debug("[finish] IntentClassifier - classify (keyword)")
            return keyword_match

        logger.info("[info] IntentClassifier - fallback LLM")
        try:
            provider = self._get_provider()
            response = await provider.ainvoke(
                [
                    SystemMessage(content=SYSTEM_PROMPT_CLASSIFIER),
                    HumanMessage(content=message),
                ]
            )
            content = response.content.strip().upper()
        except Exception as e:
            logger.warning(f"[warn] IntentClassifier - LLM fallback falhou: {e}")
            logger.debug("[finish] IntentClassifier - classify (LLM fallback: SMART)")
            return IntentType.SMART
        if "INGEST" in content:
            logger.debug("[finish] IntentClassifier - classify (LLM: INGEST)")
            return IntentType.INGEST
        if "FAST" in content:
            logger.debug("[finish] IntentClassifier - classify (LLM: FAST)")
            return IntentType.FAST
        if "MEMORY" in content:
            logger.debug("[finish] IntentClassifier - classify (LLM: MEMORY)")
            return IntentType.MEMORY
        logger.debug("[finish] IntentClassifier - classify (LLM: SMART default)")
        return IntentType.SMART
