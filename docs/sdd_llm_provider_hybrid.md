Source: K.A.O.S Architecture
Tags: #sdd #llm #provider #openai #claude #gemini #ollama #hybrid
Related: [[index]] [[00_visao_geral]] [[02_fluxo_dados]] [[sdd_knowledge_wiki_layer]] [[sdd_arquitetura_orquestracao]]

# SDD — Provedor Híbrido de LLM (Local + Cloud)

## Objetivo

Desacoplar o K.A.O.S de qualquer provedor de LLM específico, permitindo alternar entre:

- **Local**: Ollama (Qwen3, Llama, Mistral)
- **Cloud**: OpenAI (GPT-5), Anthropic (Claude), Google (Gemini), xAI (Grok)
- **OpenAI-compatible**: Qualquer provedor com API compatível

Sem alterar a lógica do RAG, LangGraph, Triple Router, Wiki Layer ou agentes.

---

## Problema Atual

Hoje o sistema depende diretamente do Ollama via `ChatOllama`:

```
planner.py: _get_llm() → ChatOllama(model, base_url)
intent_classifier.py: _get_llm() → ChatOllama(model, base_url)
```

### Problemas

| Problema | Impacto |
|----------|---------|
| Lock-in tecnológico | Trocar de LLM requer refatorar o core |
| Sem fallback | Se Ollama cai, o sistema inteiro para |
| Sem escolha de custo | Todo request usa o mesmo modelo |
| Sem escolha de latência | Perguntas simples pagam o custo do modelo grande |
| Sem escolha de qualidade | Perguntas complexas limitadas ao melhor modelo local |

---

## Arquitetura

```
                    ┌──────────────┐
                    │   OpenWebUI  │
                    └──────┬───────┘
                           │
                           ▼

                  ┌─────────────────┐
                  │    Triple Router │
                  │  FAST/MEMORY/   │
                  │  SMART/INGEST   │
                  └────────┬────────┘
                           │
                           ▼

                  ┌─────────────────┐
                  │   LLM Factory   │
                  │  (provider +    │
                  │   model selec-  │
                  │   tion)         │
                  └────────┬────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼

         Ollama         OpenAI       Anthropic
         Local          Cloud         Cloud
         (default)      (GPT-5)      (Claude)

                           ▼
                        Gemini
                         Cloud
```

---

## Camada de Abstração

```
app/
└── llm/
    ├── __init__.py
    ├── provider.py          # Interface BaseProvider
    ├── factory.py           # LLMFactory (provider + model selection)
    │
    └── providers/
        ├── __init__.py
        ├── ollama_provider.py
        ├── openai_provider.py
        ├── claude_provider.py
        └── gemini_provider.py
```

---

## Interface BaseProvider

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import AsyncIterator


@dataclass
class LLMResponse:
    content: str
    tool_calls: list | None = None


@dataclass
class ProviderMetrics:
    provider: str
    model: str
    latency_ms: float
    tokens: int
    cost: float
    fallback_used: bool = False


class BaseProvider(ABC):
    @abstractmethod
    async def chat(
        self,
        messages: list[dict],
        stream: bool = False,
        temperature: float = 0.7,
    ) -> LLMResponse | AsyncIterator[str]:
        ...

    @abstractmethod
    async def chat_with_tools(
        self,
        messages: list[dict],
        tools: list[dict],
        temperature: float = 0.7,
    ) -> LLMResponse:
        ...
```

---

## Factory Pattern

```python
class LLMFactory:
    _providers: dict[str, type[BaseProvider]] = {
        "ollama": OllamaProvider,
        "openai": OpenAIProvider,
        "anthropic": ClaudeProvider,
        "gemini": GeminiProvider,
    }

    @classmethod
    def build(cls, provider_name: str, model: str) -> BaseProvider:
        provider_cls = cls._providers.get(provider_name)
        if not provider_cls:
            raise ValueError(f"Unknown provider: {provider_name}")
        return provider_cls(model=model)

    @classmethod
    def resolve(cls, model_id: str) -> tuple[str, str]:
        """Resolve um model_id (ex: 'kaos-rag') para (provider, model_name)."""
        return MODEL_MAP.get(model_id, ("ollama", "qwen3:14b"))
```

---

## MODEL_MAP e Configuração

```python
# settings.py

DEFAULT_PROVIDER: str = "ollama"

MODEL_MAP: dict[str, tuple[str, str]] = {
    # Local (Ollama)
    "kaos-fast":     ("ollama",    "qwen3:4b"),
    "kaos-rag":      ("ollama",    "qwen3:8b"),
    "kaos":          ("ollama",    "qwen3:14b"),

    # Cloud (OpenAI)
    "kaos-cloud":    ("openai",    "gpt-5"),
    "kaos-nano":     ("openai",    "gpt-5-nano"),

    # Cloud (Anthropic)
    "kaos-sonnet":   ("anthropic", "claude-sonnet-4"),
    "kaos-opus":     ("anthropic", "claude-opus-4"),

    # Cloud (Google)
    "kaos-gemini":   ("gemini",    "gemini-2.5-pro"),
    "kaos-flash":    ("gemini",    "gemini-2.5-flash"),
}

FALLBACK_CHAIN: list[str] = [
    "openai",
    "anthropic",
    "gemini",
    "ollama",
]
```

---

## Provedores

### OllamaProvider

```python
class OllamaProvider(BaseProvider):
    def __init__(self, model: str):
        self.model = model
        self.client = ChatOllama(
            model=model,
            base_url=settings.OLLAMA_BASE_URL,
        )

    async def chat(self, messages, stream=False, temperature=0.7):
        # Wraps ChatOllama.invoke() / .stream()
        ...
```

### OpenAIProvider

```python
class OpenAIProvider(BaseProvider):
    def __init__(self, model: str):
        self.model = model
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    async def chat(self, messages, stream=False, temperature=0.7):
        if stream:
            return self._stream(messages, temperature)
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
        )
        return LLMResponse(content=response.choices[0].message.content)
```

### ClaudeProvider

```python
class ClaudeProvider(BaseProvider):
    def __init__(self, model: str):
        self.model = model
        self.client = AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)

    async def chat(self, messages, stream=False, temperature=0.7):
        # Converte formato de mensagens para Anthropic
        ...
```

### GeminiProvider

```python
class GeminiProvider(BaseProvider):
    def __init__(self, model: str):
        self.model = model
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    async def chat(self, messages, stream=False, temperature=0.7):
        # Converte formato de mensagens para Gemini
        ...
```

---

## Fallback Automático

```python
async def chat_with_fallback(
    model_id: str,
    messages: list[dict],
    stream: bool = False,
) -> LLMResponse | AsyncIterator[str]:
    provider_name, model = LLMFactory.resolve(model_id)

    for fallback_provider in [provider_name] + FALLBACK_CHAIN:
        try:
            provider = LLMFactory.build(fallback_provider, model)
            return await provider.chat(messages, stream=stream)
        except Exception as e:
            logger.warning(f"[fallback] {fallback_provider} falhou: {e}")
            continue

    raise RuntimeError("Todos os provedores de LLM falharam")
```

---

## Embeddings Independentes

Embeddings **não** dependem do provider de LLM. Continuam usando:

- **Dev**: `nomic-embed-text` (768d, rápido)
- **Prod**: `BAAI/bge-m3` (1024d, multilíngue)

```
RAG → Qdrant → Embedder (BGE-M3 / nomic)
                      ↑
               independente do provider LLM
```

---

## Smart Routing por Contexto e Custo

O Triple Router pode escolher o provider com base no tipo de requisição:

| Rota | Provider Padrão | Motivo |
|------|----------------|--------|
| FAST | Ollama qwen3:4b | Latência mínima |
| MEMORY | Ollama qwen3:8b | Custo zero, privacidade |
| SMART | Conforme model_id | Definido pelo Open WebUI |
| INGEST | Claude Sonnet (se configurado) | Qualidade de extração |

Futuro: roteamento dinâmico baseado em:
- **Custo**: pergunta simples → Ollama; pergunta complexa → Claude
- **Contexto**: análise de código → GPT-5; busca factual → Gemini
- **Latência**: tempo real → modelo pequeno local

---

## Métricas por Provider

Registradas em log estruturado e (futuro) PostgreSQL:

```python
@dataclass
class ProviderMetrics:
    provider: str        # "ollama", "openai", etc.
    model: str           # "qwen3:14b", "gpt-5", etc.
    latency_ms: float
    tokens: int
    prompt_tokens: int
    completion_tokens: int
    cost: float
    fallback_used: bool
    fallback_chain: list[str] | None = None
```

Exemplo de log:

```
[provider] provider=openai model=gpt-5 latency=1234ms tokens=1534 cost=$0.013 fallback=False
[provider] provider=anthropic model=claude-sonnet latency=890ms tokens=892 cost=$0.008 fallback=False
[provider] provider=ollama model=qwen3:4b latency=456ms tokens=234 cost=$0.000 fallback=False
```

---

## Compatibilidade com Wiki Layer

A Wiki Layer é independente do provider LLM:

```
Wiki → Retriever → Contexto → Provider → Resposta
                                    ↑
                            Qualquer LLM funciona
```

O `AGENTS.md`, `index.md`, `log.md` e as ferramentas wiki não dependem do provedor escolhido. A camada de conhecimento é agnóstica em relação ao modelo.

---

## Refatorações Necessárias

### Arquivos a modificar

| Arquivo | Mudança |
|---------|---------|
| `app/config/settings.py` | Adicionar `DEFAULT_PROVIDER`, `MODEL_MAP`, `FALLBACK_CHAIN`, API keys |
| `app/agent/nodes/planner.py` | Substituir `ChatOllama` por `LLMFactory.build()` |
| `app/router/intent_classifier.py` | Substituir `ChatOllama` por `LLMFactory.build()` |
| `app/router/memory_router.py` | Substituir `ChatOllama` por `LLMFactory.build()` |
| `app/router/fast_router.py` | Sem mudança (não usa LLM) |
| `app/service/llm_service.py` | Manter para compatibilidade ou deprecate |
| `app/api/openai.py` | Usar provider em vez de chamar Ollama direto |
| `app/service/agent_service.py` | Passar model_id resolvido para o grafo |

### Arquivos novos

| Arquivo | Conteúdo |
|---------|----------|
| `app/llm/__init__.py` | Exports públicos |
| `app/llm/provider.py` | `BaseProvider`, `LLMResponse`, `ProviderMetrics` |
| `app/llm/factory.py` | `LLMFactory`, `chat_with_fallback` |
| `app/llm/providers/__init__.py` | Exports |
| `app/llm/providers/ollama_provider.py` | `OllamaProvider` |
| `app/llm/providers/openai_provider.py` | `OpenAIProvider` |
| `app/llm/providers/claude_provider.py` | `ClaudeProvider` |
| `app/llm/providers/gemini_provider.py` | `GeminiProvider` |

---

## Critérios de Aceite

### Fase 1 — Abstração + Factory
- [ ] `BaseProvider` interface definida
- [ ] `LLMFactory` com `build()` e `resolve()`
- [ ] OllamaProvider funcionando (migração do código existente)

### Fase 2 — Provedores Cloud
- [ ] OpenAIProvider funcionando (com `OPENAI_API_KEY`)
- [ ] ClaudeProvider funcionando (com `ANTHROPIC_API_KEY`)
- [ ] GeminiProvider funcionando (com `GEMINI_API_KEY`)

### Fase 3 — Fallback + Métricas
- [ ] `chat_with_fallback` roteando para próximo provider em caso de falha
- [ ] `ProviderMetrics` registrado em log estruturado
- [ ] Cálculo de custo por provider

### Fase 4 — Smart Routing (futuro)
- [ ] Roteamento dinâmico por custo
- [ ] Roteamento dinâmico por latência
- [ ] Roteamento dinâmico por tipo de request
