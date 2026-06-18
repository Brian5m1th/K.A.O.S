# K.A.O.S — Setup Guide

> Guia de execução do assistente K.A.O.S em diferentes ambientes.

## Pré-requisitos

- Git
- Docker Desktop (recomendado) ou Python 3.13+
- Ollama (com modelo baixado: `qwen3:14b` ou similar)
- Obsidian vault (opcional, mas recomendado)

---

## Modo 1: Docker (recomendado)

### 1. Configurar ambiente

```bash
cd infra/docker
cp .env.docker .env
# Edite .env conforme necessário (Ollama, Vault path, etc)
```

### 2. Iniciar stack

```bash
docker compose up -d
```

### 3. Acessar

| Serviço | URL |
|---------|-----|
| K.A.O.S API | http://localhost:8000 |
| Open WebUI | http://localhost:3000 |
| Qdrant Dashboard | http://localhost:6333/dashboard |
| PostgreSQL | localhost:5433 |

### 4. Primeira execução

```bash
# Criar estrutura de pastas do vault
curl -X POST http://localhost:8000/indexing/init-folders

# Indexar documentos no Qdrant
curl -X POST http://localhost:8000/indexing/full
```

### Volumes persistentes

| Volume | Path no container | Descrição |
|--------|------------------|-----------|
| `postgres_data` | `/var/lib/postgresql/data` | Banco de dados |
| `qdrant_data` | `/qdrant/storage` | Vetores Qdrant |
| `vault_data` | `/vault` | Obsidian vault |
| `open_webui_data` | `/app/backend/data` | Config Open WebUI |

O vault é montado em `/vault` dentro do container. Para usar um vault existente, ajuste o bind mount no `docker-compose.yml`.

---

## Modo 2: Windows Nativo

### 1. Instalar Python 3.13

Baixe do [python.org](https://www.python.org/downloads/) e instale com "Add to PATH".

### 2. Instalar uv

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. Configurar ambiente

```powershell
cd assistant
uv sync
```

### 4. Configurar .env

```powershell
cp .env.example .env
# Edite OBSIDIAN_VAULT_PATH para o caminho do seu vault
# Edite OLLAMA_BASE_URL=http://localhost:11434
```

### 5. Iniciar dependências (Docker)

```powershell
cd infra/docker
docker compose up -d postgres qdrant
```

### 6. Iniciar K.A.O.S

```powershell
cd assistant
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Modo 3: WSL (Ubuntu/Debian)

### 1. Instalar dependências

```bash
sudo apt update && sudo apt install -y python3.13 python3.13-venv pipx
pipx install uv
```

### 2. Configurar ambiente

```bash
cd assistant
uv sync
cp .env.example .env
# Editar .env
```

### 3. Iniciar

```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Variáveis de Ambiente

| Variável | Obrigatório | Padrão | Descrição |
|----------|-------------|--------|-----------|
| `OBSIDIAN_VAULT_PATH` | Sim | — | Caminho absoluto do vault |
| `OLLAMA_BASE_URL` | Sim | `http://localhost:11434` | URL do Ollama |
| `OLLAMA_MODEL` | Sim | `qwen3:14b` | Modelo principal |
| `OLLAMA_FAST_MODEL` | Sim | `qwen3:4b` | Modelo rápido |
| `QDRANT_HOST` | Sim | `localhost` | Host do Qdrant |
| `QDRANT_PORT` | Sim | `6333` | Porta do Qdrant |
| `DATABASE_URL` | Não | — | PostgreSQL (opcional) |
| `OPENAI_API_KEY` | Não | — | Fallback OpenAI |
| `ANTHROPIC_API_KEY` | Não | — | Fallback Claude |
| `GEMINI_API_KEY` | Não | — | Fallback Gemini |

---

## Fallback Chain

O K.A.O.S suporta fallback automático entre provedores LLM. Configure no `.env`:

```env
# Ordem de fallback caso o provider principal falhe
FALLBACK_CHAIN=ollama:qwen3:14b,openai:gpt-4o,claude:claude-sonnet-4-20250514

# Mapeamento de modelos para IDs de API
MODEL_MAP={"gpt-4o":{"provider":"openai","model":"gpt-4o"},"claude-sonnet":{"provider":"claude","model":"claude-sonnet-4-20250514"}}
```

---

## Verificação

```bash
# Health check
curl http://localhost:8000/health

# Listar modelos
curl http://localhost:8000/v1/models

# Chat (teste rápido)
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"kaos","messages":[{"role":"user","content":"Ola"}]}'
```

---

## Estrutura do Vault

O vault Obsidian deve conter:

```
/vault/
├── raw/               # Documentos fonte brutos
│   └── assets/
├── wiki/              # Conhecimento estruturado
│   ├── entities/      # Entidades (pessoas, projetos, techs)
│   ├── concepts/      # Conceitos abstratos
│   ├── sources/       # Fontes documentadas
│   ├── synthesis/     # Sínteses e análises
│   ├── index.md       # Índice geral
│   └── log.md         # Log de operações
├── users/             # Dados por usuário
│   └── {user_id}/
│       ├── preferencias.md
│       └── conversa_*.md
├── Projetos/
├── Arquitetura/
├── SDD/
├── Estudos/
├── IA/
├── Python/
├── Java/
├── AWS/
├── CI-CD/
├── Diario/
└── Inbox/
```
