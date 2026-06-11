Source: Antigravity AI
Tags: #sdd #python #fastapi #fundação #fase1
Related: [[index]] [[backlog]] [[01_estrutura_pastas]] [[sdd_fase2_ia_local]]

# SDD — Fase 1: Fundação do Projeto Python

## Objetivo

Configurar a estrutura base do projeto Python seguindo os padrões corporativos definidos em [[01_estrutura_pastas]]. Ao final desta fase, o projeto deve ter ambiente, dependências, configuração e um endpoint de health check funcionando.

---

## Critério de Sucesso

> A aplicação FastAPI sobe localmente via `uv run` e responde `200 OK` no endpoint `GET /health`.

---

## Tarefas

- [ ] Configurar Python 3.13
- [ ] Configurar ambiente virtual com `uv`
- [ ] Estruturar projeto base
- [ ] Configurar Docker Compose
- [ ] Configurar FastAPI
- [ ] Configurar sistema de logs
- [ ] Configurar arquivos de ambiente (`.env`)

---

## 1. Estrutura de Pastas Inicial

```text
assistant/
├── app/
│   ├── api/
│   │   └── health.py          # GET /health → 200 OK
│   ├── config/
│   │   └── settings.py        # Pydantic Settings (lê o .env)
│   └── main.py                # Inicialização da aplicação FastAPI
├── tests/
│   └── test_health.py
├── infra/
│   └── docker/
│       └── docker-compose.yml
├── .env
├── .gitignore
└── pyproject.toml
```

---

## 2. Gerenciamento de Dependências (`pyproject.toml`)

Utilizar `uv` como gerenciador. O arquivo `pyproject.toml` define as dependências e a versão do Python.

```toml
[project]
name = "kaos-platform"
version = "0.1.0"
requires-python = ">=3.12,<3.14"

dependencies = [
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.30.0",
    "pydantic-settings>=2.0.0",
    "loguru>=0.7.0",
]

[dependency-groups]
dev = [
    "pytest>=8.0.0",
    "httpx>=0.27.0",
    "pytest-asyncio>=0.23.0",
]
```

---

## 3. Configuração de Ambiente (`config/settings.py`)

Padrão `pydantic-settings` para leitura automática do arquivo `.env`.

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # App
    APP_NAME: str = "K.A.O.S"
    APP_ENV: str = "development"
    APP_PORT: int = 8000
    LOG_LEVEL: str = "INFO"

    # Vault
    OBSIDIAN_VAULT_PATH: str = ""

    # LLM
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen3:14b"

    # Qdrant
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "obsidian_memory"

    # PostgreSQL
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/kaos"

settings = Settings()
```

---

## 4. Ponto de Entrada (`main.py`)

```python
from fastapi import FastAPI
from loguru import logger
from app.api.health import router as health_router
from app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
)

app.include_router(health_router)

@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    logger.info(f"[start] {settings.APP_NAME} - modo {settings.APP_ENV}")
    yield
    logger.debug(f"[finish] {settings.APP_NAME} - encerrado")
```

---

## 5. Health Check (`api/health.py`)

```python
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/health", tags=["Health"])

class HealthResponse(BaseModel):
    status: str
    version: str

@router.get("", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(status="ok", version="0.1.0")
```

---

## 6. Docker Compose (Serviços Base)

```yaml
# infra/docker/docker-compose.yml
services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: ai-p
      POSTGRES_PASSWORD: ai-admin
      POSTGRES_DB: kaos
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ai-p -d kaos"]
      interval: 10s
      timeout: 5s
      retries: 5

  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "6333:6333"
    volumes:
      - qdrant_data:/qdrant/storage

volumes:
  postgres_data:
  qdrant_data:
```

---

## 7. Sistema de Logs (`loguru`)

A configuração do `loguru` é feita no `main.py` via interceptação do logger padrão do Python para que frameworks como o `uvicorn` também usem o mesmo formato.

```python
import logging
import sys
from loguru import logger

def configure_logging(log_level: str) -> None:
    logger.remove()
    logger.add(
        sys.stdout,
        level=log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        colorize=True,
    )
    # Intercepta loggers externos (uvicorn, fastapi)
    class InterceptHandler(logging.Handler):
        def emit(self, record: logging.LogRecord) -> None:
            logger.opt(depth=6, exception=record.exc_info).log(
                record.levelname, record.getMessage()
            )

    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
```

---

## 8. Comandos de Setup

```bash
# Instalar uv (se necessário)
pip install uv

# Criar projeto e instalar dependências
uv sync

# Subir infraestrutura
docker compose -f infra/docker/docker-compose.yml up -d

# Rodar a aplicação localmente
cd assistant && uv run uvicorn app.main:app --reload --port 8000

# Rodar os testes
cd assistant && uv run pytest
```

---

## Dependências Desta Fase

Nenhuma — é a fase inicial.

## Desbloqueia

- [[sdd_fase2_ia_local]] — Integração com Ollama
- [[sdd_fase3_obsidian_service]] — ObsidianService
