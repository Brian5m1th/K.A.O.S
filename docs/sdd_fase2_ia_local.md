Source: Antigravity AI
Tags: #sdd #python #ollama #fastapi #fase2
Related: [[index]] [[backlog]] [[sdd_fase1_fundacao]] [[sdd_fase3_obsidian_service]]

# SDD — Fase 2: IA Local com Ollama

## Objetivo

Conectar a aplicação FastAPI ao servidor Ollama rodando localmente. Ao final desta fase, o usuário consegue enviar mensagens pelo Open WebUI e receber respostas do modelo `qwen3:14b` via streaming, 100% offline.

---

## Critério de Sucesso

> O Open WebUI exibe respostas em tempo real do Qwen3 14B sem qualquer conexão com a internet.

---

## Tarefas

- [ ] Instalar Ollama no sistema
- [ ] Baixar o modelo `qwen3:14b`
- [ ] Criar `LLMService` — camada de abstração sobre o Ollama
- [ ] Criar endpoint `POST /api/chat/message` com suporte a streaming
- [ ] Integrar Open WebUI via Docker Compose
- [ ] Validar funcionamento 100% offline

---

## 1. Arquitetura do Módulo

```text
app/
├── api/
│   └── chat.py              # Endpoint POST /api/chat/message
├── service/
│   └── llm_service.py       # LLMService — comunicação com Ollama
└── domain/
    └── chat.py              # DTOs: ChatRequest, ChatResponse, Message
```

---

## 2. DTOs de Domínio (`domain/chat.py`)

```python
from pydantic import BaseModel, Field
from typing import Literal

class Message(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str

class ChatRequest(BaseModel):
    session_id: str = Field(..., description="ID único da sessão de conversa")
    message: str = Field(..., min_length=1, max_length=8000)
    history: list[Message] = Field(default_factory=list)

class ChatResponse(BaseModel):
    session_id: str
    content: str
    model: str
```

---

## 3. LLM Service (`service/llm_service.py`)

Abstração completa sobre o Ollama. Usa o cliente `httpx` de forma assíncrona para suportar streaming.

```python
from typing import AsyncIterator
import httpx
from loguru import logger
from app.config.settings import settings
from app.domain.chat import Message

class LLMService:
    def __init__(self) -> None:
        self._base_url = settings.OLLAMA_BASE_URL
        self._model = settings.OLLAMA_MODEL

    async def stream_chat(
        self,
        messages: list[Message],
    ) -> AsyncIterator[str]:
        """Envia mensagens ao Ollama e retorna a resposta em streaming."""
        payload = {
            "model": self._model,
            "messages": [m.model_dump() for m in messages],
            "stream": True,
        }
        logger.debug(f"Enviando {len(messages)} mensagens ao Ollama ({self._model})")

        async with httpx.AsyncClient(timeout=120.0) as client:
            async with client.stream("POST", f"{self._base_url}/api/chat", json=payload) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line:
                        import json
                        chunk = json.loads(line)
                        if not chunk.get("done"):
                            yield chunk["message"]["content"]

    async def check_availability(self) -> bool:
        """Verifica se o Ollama está acessível."""
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(f"{self._base_url}/api/tags")
                return response.status_code == 200
        except httpx.ConnectError:
            return False
```

---

## 4. Endpoint de Chat com Streaming (`api/chat.py`)

Utiliza `StreamingResponse` do FastAPI para enviar tokens à medida que o Ollama os gera.

```python
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.domain.chat import ChatRequest, Message
from app.service.llm_service import LLMService

router = APIRouter(prefix="/api/chat", tags=["Chat"])

def get_llm_service() -> LLMService:
    return LLMService()

@router.post("/message")
async def send_message(
    request: ChatRequest,
    llm: LLMService = Depends(get_llm_service),
) -> StreamingResponse:
    """Envia uma mensagem e recebe a resposta do LLM em streaming."""

    messages = list(request.history)
    messages.append(Message(role="user", content=request.message))

    async def token_generator():
        async for token in llm.stream_chat(messages=messages):
            yield token

    return StreamingResponse(token_generator(), media_type="text/plain")
```

---

## 5. Integração Open WebUI no Docker Compose

Adicionar ao `docker/docker-compose.yml` existente:

```yaml
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_BASE_URL=http://host.docker.internal:11434
    volumes:
      - open_webui_data:/app/backend/data
    extra_hosts:
      - "host.docker.internal:host-gateway"
    depends_on:
      - postgres

volumes:
  open_webui_data:
```

> **Nota**: O Ollama deve rodar diretamente no host (não em container) para ter acesso à GPU com melhor performance. O `host.docker.internal` resolve o endereço do host a partir de dentro do container.

---

## 6. Comandos de Setup do Ollama

```bash
# Instalar Ollama (Linux/macOS)
curl -fsSL https://ollama.com/install.sh | sh

# Baixar o modelo Qwen3 14B
ollama pull qwen3:14b

# Verificar modelos disponíveis
ollama list

# Testar via CLI antes de integrar
ollama run qwen3:14b "Olá, como posso te ajudar?"
```

---

## 7. Validação de Disponibilidade no Health Check

Extender o `api/health.py` existente para verificar a conectividade com o Ollama:

```python
@router.get("/readiness", response_model=ReadinessResponse)
async def readiness_check(llm: LLMService = Depends(get_llm_service)) -> ReadinessResponse:
    ollama_ok = await llm.check_availability()
    return ReadinessResponse(
        status="ready" if ollama_ok else "degraded",
        services={"ollama": ollama_ok}
    )
```

---

## Dependências Desta Fase

- [[sdd_fase1_fundacao]] — Fundação deve estar completa

## Desbloqueia

- [[sdd_fase3_obsidian_service]] — O chat passará a injetar contexto do Obsidian
