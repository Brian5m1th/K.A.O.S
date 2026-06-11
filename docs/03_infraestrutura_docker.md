Source: K.A.O.S Project
Tags: #infraestrutura #docker #compose #servicos
Related: [[index]] [[00_visao_geral]] [[backlog]]

# Infraestrutura Docker

## Docker Compose

O arquivo `infra/docker/docker-compose.yml` orquestra os servicos de infraestrutura do K.A.O.S.

### Servicos

#### PostgreSQL (`postgres:16-alpine`)
- **Porta**: 5432
- **Usuario**: `ai-p`
- **Senha**: `ai-admin`
- **Database**: `kaos`
- **Volume**: `postgres_data`

#### Qdrant (`qdrant/qdrant:latest`)
- **Porta REST**: 6333
- **Porta gRPC**: 6334
- **Volume**: `qdrant_data`
- **Funcao**: Armazenamento de embeddings vetoriais

#### Open WebUI (`ghcr.io/open-webui/open-webui:latest`)
- **Porta**: 3000 (mapeada para 8080 do container)
- **Modo**: OpenAI (conecta ao proxy `/v1/chat/completions` do K.A.O.S)
- **Depende**: postgres

### Variaveis de Ambiente

```env
# K.A.O.S
APP_NAME=K.A.O.S
APP_ENV=development
APP_PORT=8000
LOG_LEVEL=INFO
OBSIDIAN_VAULT_PATH=C:\Obsidian
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen3:4b
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION=obsidian_memory
```

### Comandos

```bash
# Subir todos os servicos
docker compose -f infra/docker/docker-compose.yml up -d

# Ver logs
docker compose -f infra/docker/docker-compose.yml logs -f

# Parar servicos
docker compose -f infra/docker/docker-compose.yml down

# Resetar volumes (perde dados)
docker compose -f infra/docker/docker-compose.yml down -v
```
