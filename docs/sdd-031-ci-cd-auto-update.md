# SDD-031: CI/CD Pipeline + Auto Update + KAOS.exe Desktop

**Status:** Draft (2026-06-18)
**Related:** [[backlog]] [[sdd_user_context_propagation]]

---

## 1. Goal

Automate build, test, and release of the KAOS platform, plus deliver a native desktop launcher (`KAOS.exe`) with auto-update.

### Success Criteria

1. Every push/PR runs lint + tests automatically (CI)
2. Git tags (`v*`) produce a Docker image on GHCR + a GitHub Release
3. A Tauri-based Windows desktop app (`KAOS.exe`) that:
   - Lets the user select an LLM provider (Ollama, OpenAI, Claude, Gemini)
   - Points to the Obsidian vault path and calls `/indexing/init-folders`
   - Connects to the KAOS server and provides a chat interface
   - Handles disconnection gracefully (offline mode)
4. Auto-update: `KAOS.exe` checks for new releases via GitHub Releases

---

## 2. Repository Structure

```
.github/workflows/
  ci.yml              # lint + test on PR/push
  release.yml         # Docker image + GitHub Release on tag
  docker-publish.yml  # nightly Docker images
  auto-update.yml     # weekly check for new tags

desktop/
  src-tauri/           # Tauri Rust backend
    Cargo.toml
    tauri.conf.json    # updater plugin configured
    src/lib.rs         # check_server, check_ollama commands
    src/main.rs
    icons/
  src/                 # React frontend
    App.tsx            # screen router (provider → vault → chat)
    main.tsx
    components/
      ProviderScreen.tsx  # select provider, test connection
      VaultScreen.tsx     # input vault path, init-folders
      ChatScreen.tsx      # chat with offline mode
  package.json
  vite.config.ts
  tsconfig.json
  index.html
```

---

## 3. Workflows

### 3.1 CI (`ci.yml`)

- Trigger: PR or push to `dev`/`main`
- Steps: checkout → setup uv → install deps → ruff lint → ruff format check → pytest

### 3.2 Release (`release.yml`)

- Trigger: tag `v*`
- Jobs:
  - **docker**: build + push `ghcr.io/...` with semver + latest tags
  - **create-release**: draft GitHub Release
- Future: add Cosign signing

### 3.3 Docker Publish (`docker-publish.yml`)

- Trigger: push to `dev`/`main` touching `assistant/` or `infra/`
- Tags: branch name, `{branch}-{sha}`, `nightly` for dev

### 3.4 Auto Update Check (`auto-update.yml`)

- Trigger: weekly (Monday 06:00 UTC) or manual dispatch
- Checks latest tag and notifies if new version exists

---

## 4. Desktop Launcher

### 4.1 Architecture

```
KAOS.exe (Tauri)
├── Rust backend (src-tauri)
│   ├── command: check_server(url) → HealthResponse
│   └── command: check_ollama(url) → String (tags JSON)
└── React frontend (src/)
    ├── ProviderScreen    → select provider, test connection
    ├── VaultScreen       → set vault path, POST /indexing/init-folders
    └── ChatScreen        → POST /v1/chat/completions, offline fallback
```

### 4.2 Screens

1. **Provider Selection**: radio buttons for providers, URL input, "Test Connection" button
2. **Vault Config**: path input, "Initialize & Enter" button → calls init-folders API
3. **Chat**: message list, input box, "Send" button, "Disconnect" button

### 4.3 Offline Mode

- If `POST /v1/chat/completions` fails, a banner shows "Offline mode"
- Chat history remains visible
- User can disconnect and reconfigure

### 4.4 Auto-Update

- Tauri updater plugin configured to check GitHub Releases
- Update proxy JSON points to `https://github.com/Brian5m1th/K.A.O.S/releases/latest/download/KAOS_x64.msi`
- On each release, Tauri generates `.msi` + `.nsis` installers

---

## 5. Future Work

- [ ] Cosign Docker image signing
- [ ] Code signing certificate for Windows installer
- [ ] macOS + Linux launcher builds
- [ ] Integration tests for desktop ↔ server
- [ ] `KAOS.exe` tray icon + background service
