from enum import Enum
from loguru import logger
from langchain_core.messages import SystemMessage, HumanMessage
from app.config.settings import settings
from app.llm.factory import LLMFactory
from app.domain.intent import IntentResult
from app.domain.workflow import WorkflowType
from app.domain.command import CommandType


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
    "atualize esta nota",
    "oi",
    "olá",
    "ola",
    "hello",
    "hi",
    "tudo bem",
    "como vai",
]

MEMORY_COMMAND_KEYWORDS = [
    "salve esta conversa",
    "guarde isto",
    "memorize esta conversa",
    "grave esta conversa",
    "adicione ao vault",
    "salve no obsidian",
    "save this conversation",
    "memorize this",
    "memorize isso",
    "guarde essa informacao",
    "registre essa discussao",
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

FAST: acao direta em ferramentas (criar, ler, atualizar, deletar, listar notas). Nao precisa de conhecimento externo.

MEMORY: pergunta que requer conhecimento do Vault Obsidian (busca semantica, contexto, lembrancas). Precisa de RAG.

SMART: pergunta complexa que requer raciocinio, planejamento ou multiplas ferramentas. Usa LangGraph.

Responda apenas com o nome da categoria: FAST, MEMORY ou SMART."""


class IntentClassifier:
    def __init__(self):
        self._factory: LLMFactory | None = None

    def _get_provider(self):
        if self._factory is None:
            self._factory = LLMFactory()
        return self._factory.build(settings.FAST_MODEL_ID, temperature=0)

    def _match_keyword(self, message: str) -> IntentResult | None:
        lower = message.lower().strip()
        for kw in INGEST_KEYWORDS:
            if kw in lower:
                logger.info(f'[info] IntentClassifier - keyword INGEST: "{kw}"')
                return IntentResult(workflow=WorkflowType.INGEST, confidence=0.95)
        for kw in MEMORY_COMMAND_KEYWORDS:
            if kw in lower:
                logger.info(f'[info] IntentClassifier - keyword MEMORY_COMMAND: "{kw}"')
                return IntentResult(
                    workflow=WorkflowType.MEMORY,
                    command=CommandType.SAVE_CONVERSATION,
                    confidence=0.96,
                )
        for kw in FAST_KEYWORDS:
            if kw in lower:
                logger.info(f'[info] IntentClassifier - keyword CHAT: "{kw}"')
                return IntentResult(workflow=WorkflowType.CHAT, confidence=0.95)
        for kw in MEMORY_KEYWORDS:
            if kw in lower:
                logger.info(f'[info] IntentClassifier - keyword RAG: "{kw}"')
                return IntentResult(workflow=WorkflowType.RAG, confidence=0.95)
        return None

    async def classify(self, message: str) -> IntentResult:
        keyword_match = self._match_keyword(message)
        if keyword_match:
            logger.debug(f"[finish] IntentClassifier - classify (keyword: {keyword_match.workflow.value})")
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
            return IntentResult(workflow=WorkflowType.AGENT, confidence=0.0)

        if "INGEST" in content:
            return IntentResult(workflow=WorkflowType.INGEST, confidence=0.7)
        if "FAST" in content:
            return IntentResult(workflow=WorkflowType.CHAT, confidence=0.7)
        if "MEMORY" in content:
            return IntentResult(workflow=WorkflowType.RAG, confidence=0.7)
        return IntentResult(workflow=WorkflowType.AGENT, confidence=0.5)
