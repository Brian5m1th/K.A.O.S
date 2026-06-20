# K.A.O.S — Guia de Instalação Rápida

> Para detalhes completos, veja [SETUP.md](SETUP.md).

---

## Opção 1: Docker (recomendado)

```powershell
# 1. Clone
git clone --recurse-submodules https://github.com/Brian5m1th/K.A.O.S.git
cd K.A.O.S

# 2. Configure
cd infra/docker
cp .env.docker .env

# 3. Suba
docker compose up -d

# 4. Inicialize
curl -X POST http://localhost:8000/indexing/init-folders
curl -X POST http://localhost:8000/indexing/full
```

**Serviços disponíveis:**
| Serviço | URL |
|---------|-----|
| API | http://localhost:8000 |
| Open WebUI | http://localhost:3000 |
| Qdrant | http://localhost:6333 |
| N8N | http://localhost:5678 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3001 (admin/admin) |
| Loki | http://localhost:3100 |

---

## Opção 2: Windows Nativo (dev)

```powershell
# 1. Instale uv
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
$env:Path += ";$env:USERPROFILE\.local\bin"

# 2. Clone
git clone --recurse-submodules https://github.com/Brian5m1th/K.A.O.S.git
cd K.A.O.S\assistant

# 3. Configure
cp .env.example .env
# Edite .env: OBSIDIAN_VAULT_PATH, OLLAMA_BASE_URL

# 4. Sync deps
uv sync

# 5. Infra (postgres + qdrant)
docker compose -f ../../infra/docker/docker-compose.yml up -d postgres qdrant

# 6. API
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Opção 3: Desktop Launcher

```powershell
cd desktop
npm install

# Dev (hot-reload)
npm run dev

# Build produção
npm run tauri build
# Instalador em: src-tauri/target/release/bundle/
```

---

## Provider Selection (Desktop)

| Provider | URL | Teste |
|----------|-----|-------|
| Ollama (Local) | http://localhost:11434 | GET /api/tags |
| OpenAI | https://api.openai.com/v1 | GET /models |
| Anthropic | https://api.anthropic.com/v1 | HEAD |
| Google | https://generativelanguage.googleapis.com/v1 | GET /models |

---

## Primeiros Passos

1. **API Key** — Primeira execução gera chave em `assistant/data/api_key.txt` (logada no startup)
2. **Healthcheck** — `GET /health` → `{"status":"ok"}`
3. **Auth** — Header `X-API-Key` em todas as chamadas (exceto /health, /docs, /auth/*, /api/setup/*)

---

## Backup do Vault

```powershell
# Manual
C:\Scripts\kaos-backup\backup.exe

# Agendado (diário 23:00)
powershell -ExecutionPolicy Bypass -File C:\Scripts\kaos-backup\install.ps1
```

---

## Recursos

- [SETUP.md](SETUP.md) — Guia completo
- [README_tecnico.md](README_tecnico.md) — Documentação técnica
- [backlog.md](backlog.md) — Status do projeto