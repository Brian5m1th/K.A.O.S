Source: Antigravity AI
Tags: #sdd #python #ollama #fastapi #fase2 #proxy #openai
Related: [[index]] [[backlog]] [[sdd_fase1_fundacao]] [[sdd_arquitetura_orquestracao]]

# SDD — Fase 2: IA Local com Ollama

## Objetivo

Conectar o Open WebUI ao Ollama via FastAPI como proxy OpenAI-compatível. O usuário envia mensagens pelo Open WebUI e recebe respostas do modelo `qwen3:4b` via streaming, 100% offline, com o system prompt do K.A.O.S. injetado em toda requisição.

---

## Critério de Sucesso

> O Open WebUI exibe respostas em tempo real do Qwen3 4B sem qualquer conexão com a internet, roteadas através do FastAPI.

---

## Tarefas

- [x] Instalar Ollama no sistema
- [x] Baixar o modelo `qwen3:4b`
- [x] Criar `LLMService` — camada de abstração sobre o Ollama
- [x] Criar endpoint `POST /api/chat/message` com suporte a streaming
- [x] Criar endpoint `POST /v1/chat/completions` (proxy OpenAI)
- [x] Criar system prompt do K.A.O.S. em `config/prompts.py`
- [x] Configurar CORS no FastAPI
- [x] Aumentar timeout do LLMService para 600s
- [x] Integrar Open WebUI via Docker Compose (modo OpenAI)
- [x] Validar funcionamento 100% offline

---

## 1. Arquitetura do Módulo

```
assistant/
├── app/
│   ├── api/
│   │   ├── chat.py              # Endpoint POST /api/chat/message
│   │   └── openai.py            # Proxy OpenAI /v1/chat/completions
│   ├── config/
│   │   ├── settings.py          # Configs (modelo, timeout, etc.)
│   │   └── prompts.py           # System prompt do K.A.O.S.
│   ├── service/
│   │   └── llm_service.py       # LLMService — comunicação com Ollama
│   └── domain/
│       └── chat.py              # DTOs: ChatRequest, ChatResponse, Message
└── .env                         # OLLAMA_MODEL=qwen3:4b
```

---

## 2. Modelo: Qwen3 14B → Qwen3 4B

O modelo original `qwen3:14b` (14.8B parâmetros, ~10 GB) mostrou-se inviável em CPU-only:

| Modelo | Parâmetros | Tamanho | Resposta (CPU) | Viável |
| :----- | :--------- | :------ | :------------- | :----- |
| qwen3:14b | 14.8B | 10 GB | >2 min (timeout) | ❌ |
| **qwen3:4b** | 3.8B | 2.5 GB | ~36s (pré-carregado) | ✅ |

> **Nota**: Para evitar latência de carga inicial (~172s), execute `ollama run qwen3:4b` e saia com `/bye` para manter o modelo cacheado.

---

## 3. Proxy OpenAI (/v1/chat/completions)

Endpoint que permite ao Open WebUI conectar-se como se fosse a API da OpenAI:

```python
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.service.llm_service import LLMService
from app.config.settings import settings
from app.config.prompts import KAOS_SYSTEM_PROMPT

router = APIRouter()

@router.post("/v1/chat/completions")
async def chat_completions(body: dict):
    """Proxy OpenAI-compatível. Injeta system prompt do K.A.O.S."""
    model = body.get("model", settings.OLLAMA_MODEL)
    messages = body.get("messages", [])

    # Injeta system prompt se não houver
    has_system = any(m.get("role") == "system" for m in messages)
    if not has_system:
        messages.insert(0, {"role": "system", "content": KAOS_SYSTEM_PROMPT})

    llm = LLMService()

    async def generate():
        async for token in llm.stream_chat(messages=messages):
            yield f"data: {json.dumps({'choices': [{'delta': {'content': token}}]})}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")
```

---

## 4. LLM Service com Timeout Aumentado

```python
# timeout foi aumentado de 120s para 600s
async with httpx.AsyncClient(timeout=600.0) as client:
    async with client.stream("POST", f"{self._base_url}/api/chat", json=payload) as response:
        ...
```

---

## 5. System Prompt do K.A.O.S. (`config/prompts.py`)

Prompt injetado em toda requisição para definir o comportamento do agente:

```python
KAOS_SYSTEM_PROMPT = """Você é K.A.O.S. (Knowledge Assistant & Offline System)..."""
```

---

## 6. Integração Open WebUI no Docker Compose

O Open WebUI é configurado no **modo OpenAI**, não Ollama direto:

```yaml
open-webui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "3000:8080"
    environment:
      - OPENAI_API_BASE_URL=http://host.docker.internal:8000
      - OPENAI_API_KEY=kaos-local
      - DEFAULT_MODEL=qwen3:4b
    volumes:
      - open_webui_data:/app/backend/data
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

> **Mudança crítica**: Anteriormente usava `OLLAMA_BASE_URL` (conexão direta ao Ollama). Agora usa `OPENAI_API_BASE_URL` apontando para o FastAPI na porta 8000.

---

## 7. Comandos de Setup

```bash
# Instalar e baixar modelo
ollama pull qwen3:4b

# Pré-carregar para evitar latência inicial
ollama run qwen3:4b
/bye

# Iniciar FastAPI (do diretório assistant/)
cd assistant
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Iniciar infraestrutura
docker compose -f infra/docker/docker-compose.yml up -d
```

---

## Dependências

- [[sdd_fase1_fundacao]] — Fundação deve estar completa
- [[sdd_arquitetura_orquestracao]] — SDD do proxy OpenAI

## Desbloqueia

- [[sdd_fase3_obsidian_service]] — Chat passa a injetar contexto do Obsidian
