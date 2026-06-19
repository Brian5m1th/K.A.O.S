# K.A.O.S — Guia de Setup

## Pré-requisitos

| Ferramenta | Versão | Onde obter |
|-----------|--------|-----------|
| Git | — | `winget install Git.Git` |
| Docker Desktop | latest | `winget install Docker.DockerDesktop` |
| Ollama | latest | `winget install Ollama.Ollama` |
| Python | 3.13 | [python.org](https://python.org) |
| uv | latest | `powershell -c "irm https://astral.sh/uv/install.ps1 \| iex"` |
| Node.js | 22 | `winget install OpenJS.NodeJS.LTS` |

---

## Modo 1: Docker (recomendado)

Stack completa isolada em containers. Nao precisa instalar Python nem Node.

### 1. Configurar ambiente

```powershell
cd infra/docker
cp .env.docker .env
# Edite .env se necessario (Ollama, vault, etc)
```

### 2. Iniciar

```powershell
docker compose -f infra/docker/docker-compose.yml up -d
```

### 3. Acessar servicos

| Servico | URL |
|---------|-----|
| K.A.O.S API | http://localhost:8000 |
| Open WebUI | http://localhost:3000 |
| Qdrant Dashboard | http://localhost:6333/dashboard |
| N8N | http://localhost:5678 |
| PostgreSQL | localhost:5433 |

### 4. Primeira execucao

```powershell
# Criar estrutura de pastas do vault
curl -X POST http://localhost:8000/indexing/init-folders

# Indexar documentos no Qdrant
curl -X POST http://localhost:8000/indexing/full
```

### Troubleshooting Docker

**"uvicorn: executable file not found"** — Nao use bind mount sobre `/app`. O `.venv` e criado no build e o volume `../../assistant:/app` esconde ele. O `docker-compose.yml` ja esta corrigido.

**"OBSIDIAN_VAULT_PATH vazio"** — O VaultWatcher agora ignora path vazio sem crashar.

**Reconstruir apos mudancas no codigo:**
```powershell
docker compose -f infra/docker/docker-compose.yml build kaos-api
docker compose -f infra/docker/docker-compose.yml up -d kaos-api
```

---

## Modo 2: Windows Nativo (desenvolvimento)

### 1. Instalar uv

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
# Feche e abra o terminal, ou recarregue o PATH manualmente
$env:Path += ";$env:USERPROFILE\.local\bin"
```

### 2. Configurar ambiente Python

```powershell
cd assistant
cp .env.example .env
# Edite .env: ajuste OBSIDIAN_VAULT_PATH e OLLAMA_BASE_URL
```

### 3. Sincronizar dependencias

```powershell
uv sync
```

### 4. Iniciar dependencias (Docker)

So sobe os servicos de infra (ignora o build do kaos-api):

```powershell
docker compose -f infra/docker/docker-compose.yml up -d postgres qdrant
```

### 5. Iniciar K.A.O.S API

```powershell
cd assistant
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Modo 3: Desktop Launcher (Tauri)

O desktop e um launcher em React + Tauri que se conecta ao backend.

### 1. Configurar ambiente

```powershell
cd desktop
npm install
```

### 2. Modo desenvolvimento (com hot-reload)

```powershell
cd desktop
npm run dev
```

### 3. Build de producao

```powershell
cd desktop
npm run tauri build
```

O instalador estara em `desktop/src-tauri/target/release/bundle/`.

### Provider Selection

Ao iniciar o desktop, escolha seu provedor LLM:

| Provider | URL Padrao | Testado via |
|----------|-----------|------------|
| Ollama (Local) | `http://localhost:11434` | `GET /api/tags` |
| OpenAI | `https://api.openai.com/v1` | `GET /models` |
| Anthropic Claude | `https://api.anthropic.com/v1` | HEAD |
| Google Gemini | `https://generativelanguage.googleapis.com/v1` | `GET /models` |

O teste de conexao considera `401`/`403` como "Connected" (servidor alcancavel, mas falta API key).

---

## CI/CD & Release

### Pipelines

| Workflow | Trigger | O que faz |
|----------|---------|-----------|
| `ci.yml` | Push/PR em `assistant/**`, `infra/**` | Lint (ruff), testes, build Docker |
| `desktop-ci.yml` | Push/PR em `desktop/**` | Build Tauri (3 OS), cache Rust/Node |
| `release.yml` | Tag `v*` | Build Docker multi-arch + Tauri 3 OS + GitHub Release |

### Criar uma release

```powershell
git tag v0.1.0-alpha.X
git push origin v0.1.0-alpha.X
```

O workflow `release.yml` vai:
1. Build Docker (amd64 + arm64) e push para GHCR
2. Build Tauri (Linux .deb/.rpm/.AppImage, Windows .exe/.msi, macOS .dmg)
3. Criar GitHub Release com artefatos assinados

### Chave de Assinatura Tauri

Ja gerada e configurada como secret do GitHub. Para regenerar:

```powershell
cargo tauri signer generate -w "$env:USERPROFILE\.tauri\kaos.key"
```

Secrets necessarias no GitHub:
- `TAURI_SIGNING_PRIVATE_KEY` — conteudo do `kaos.key`
- `TAURI_SIGNING_PASSWORD` — senha da chave

---

## Healthcheck

Endpoint: `GET http://localhost:8000/health`

Resposta esperada:
```json
{"status":"ok"}
```

O container leva ~30-60s para iniciar (download de modelo de embedding na primeira execucao).

---

## Backup da Chave de Assinatura

Sua chave privada do Tauri esta em `~/.tauri/kaos.key` (ou onde foi gerada). **Mantenha backup seguro** — sem ela, nao e possivel assinar atualizacoes do desktop.

```powershell
# Copiar para local seguro
copy "$env:USERPROFILE\.tauri\kaos.key" "D:\backups\kaos.key"
```

---

## Estrutura do Vault

```
/vault/
├── raw/               # Documentos fonte brutos
│   └── assets/
├── wiki/              # Conhecimento estruturado
│   ├── entities/
│   ├── concepts/
│   ├── sources/
│   ├── synthesis/
│   ├── index.md
│   └── log.md
├── users/
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
