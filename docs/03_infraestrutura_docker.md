Source: K.A.O.S Project
Tags: #infraestrutura #docker #compose #servicos
Related: [[index]] [[00_visao_geral]] [[backlog]]

# Infraestrutura Docker

## Docker Compose

O arquivo `infra/docker/docker-compose.yml` orquestra os servicos de infraestrutura do K.A.O.S.

### Servicos

#### PostgreSQL (`postgres:16-alpine`)
- **Porta**: 5433 (host) → 5432 (container)
- **Usuario**: `ai-p` | **Senha**: `ai-admin` | **Database**: `kaos`
- **Volume**: `postgres_data`

#### Qdrant (`qdrant/qdrant:latest`)
- **Porta REST**: 6333 | **Porta gRPC**: 6334
- **Volume**: `qdrant_data`
- **Funcao**: Armazenamento de embeddings vetoriais

#### Open WebUI (`ghcr.io/open-webui/open-webui:latest`)
- **Porta**: 3000 (host) → 8080 (container)
- **Modo**: OpenAI (conecta ao proxy `/v1/chat/completions` do K.A.O.S)
- **Depende**: postgres, kaos-api

#### N8N (`n8nio/n8n:latest`)
- **Porta**: 5678
- **Funcao**: Automacao de fluxos e integracoes
- **Volume**: `n8n_data`

#### K.A.O.S API (`assistant/Dockerfile`)
- **Porta**: 8000
- **Build**: Multi-stage com Python 3.13-slim + torch CPU-only
- **Volume**: `vault_data:/vault` (ou bind mount para vault existente)
- **Nota**: O `.venv` e instalado durante o build — **nao** use bind mount sobre `/app`

### Arquivo .env

Copie `infra/docker/.env.docker` para `infra/docker/.env` e ajuste:

```env
APP_NAME=K.A.O.S
APP_ENV=production
APP_PORT=8000
LOG_LEVEL=INFO
OBSIDIAN_VAULT_PATH=/vault
OLLAMA_BASE_URL=http://host.docker.internal:11434
OLLAMA_MODEL=qwen3:14b
OLLAMA_FAST_MODEL=qwen3:4b
QDRANT_HOST=qdrant
QDRANT_PORT=6333
```

### Comandos

```bash
# Subir todos os servicos
docker compose -f infra/docker/docker-compose.yml up -d

# Ver logs
docker compose -f infra/docker/docker-compose.yml logs -f

# Logs de um servico especifico
docker compose -f infra/docker/docker-compose.yml logs -f kaos-api

# Parar servicos
docker compose -f infra/docker/docker-compose.yml down

# Resetar volumes (perde dados)
docker compose -f infra/docker/docker-compose.yml down -v

# Rebuildar a imagem da API (apos alteracoes no codigo)
docker compose -f infra/docker/docker-compose.yml build kaos-api
```
```
