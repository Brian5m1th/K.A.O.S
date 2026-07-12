# [2.7.0](https://github.com/Brian5m1th/K.A.O.S/compare/v2.6.0...v2.7.0) (2026-07-12)


### Bug Fixes

* **frontend:** remove barrel files creating import cycles, fix direct infra imports ([566cab2](https://github.com/Brian5m1th/K.A.O.S/commit/566cab26f251350b7a52c1c71cb14d6e559cb74e))


### Features

* **autonomous:** architecture reviewer, self-healing drl, predictive engine, wireguard vpn config ([8875e60](https://github.com/Brian5m1th/K.A.O.S/commit/8875e60ae22d7846144f145704a122e3768d71c0))
* **ci:** add knowledge graph enrichment + dashboard generation to CI/CD ([d95be91](https://github.com/Brian5m1th/K.A.O.S/commit/d95be91e08b14ff871bf6546c8862b096b511f3e))
* disable unavailable MCP servers + add-server command ([ae1b726](https://github.com/Brian5m1th/K.A.O.S/commit/ae1b726a61996f4dc9c3a3c44d3a21e3788b896f))
* **graph:** add Knowledge Graph dashboard (Chart.js, self-contained HTML) ([dd81bf7](https://github.com/Brian5m1th/K.A.O.S/commit/dd81bf7ecc5c7a9157b704a019ed3b05be56b031))
* **sprint7:** mem0, neo4j, falkordb adapters, graphrag experiment, auto-tag engine ([f8d7620](https://github.com/Brian5m1th/K.A.O.S/commit/f8d76207330bff589b6f78da9a4fe532c10a3a05))

# [2.6.0](https://github.com/Brian5m1th/K.A.O.S/compare/v2.5.5...v2.6.0) (2026-07-12)


### Bug Fixes

* **deploy:** use --ignore-buildable flag on docker compose pull ([df0d98f](https://github.com/Brian5m1th/K.A.O.S/commit/df0d98f3c3db4f0f25907e556963963ca6540ed6))
* eliminate all mock/fabricated data patterns ([a206737](https://github.com/Brian5m1th/K.A.O.S/commit/a20673759ca8f9e7d5703697655cbbdc3dd77333))
* gitignore — exclude airllm/, graphify/, graphify-out/cache/, local config dirs ([b5d6916](https://github.com/Brian5m1th/K.A.O.S/commit/b5d6916a636d73415adaac748d1bbd6dd27c5942))
* lint errors — ruff cleanup (30 issues fixed) ([cdd503f](https://github.com/Brian5m1th/K.A.O.S/commit/cdd503f3406f1d4e257c20107033c15564de06b6))
* remove graphify/ submodule from index — no .gitmodules entry ([f657a3b](https://github.com/Brian5m1th/K.A.O.S/commit/f657a3bc3020af68f9f800839354803b986a36d5))
* ruff auto-fix — 13 unused import issues ([477fe66](https://github.com/Brian5m1th/K.A.O.S/commit/477fe66ba753b73de7cbcb6831b2a9269c14c3c4))


### Features

* 11 framework adapters — Graphify, Qdrant, Ollama, AirLLM, OpenAI, Gemini, Claude, LangGraph, PostgreSQL, NetworkX, EvidenceEngine ([2c3683f](https://github.com/Brian5m1th/K.A.O.S/commit/2c3683f14cdac0ae509040739209e9dceb4b2f6b))
* 5 Desktop stores + Graphify Inspector — zero framework imports ([5c5234b](https://github.com/Brian5m1th/K.A.O.S/commit/5c5234b24b6a7480b8260c6d3ad00a1f9020a450))
* 6 REST APIs, 24 endpoints, FastAPI dependency injection ([d1fe5b8](https://github.com/Brian5m1th/K.A.O.S/commit/d1fe5b8ec140ba48801d51c9cd42ac0a22e806de))
* 7 capability services — Graph, Memory, Retrieval, Inference, Planner, Evidence, Knowledge ([5806684](https://github.com/Brian5m1th/K.A.O.S/commit/5806684206236db8d83041b8a6ac0434b5bbeadf))
* define 6 domain ports for capability-first architecture ([dd6003d](https://github.com/Brian5m1th/K.A.O.S/commit/dd6003d2931cd5dad4375e2b8e956f196ec5fb29))
* generic ProviderRegistry for runtime provider swapping ([bc1c6a4](https://github.com/Brian5m1th/K.A.O.S/commit/bc1c6a4bfe8e8f8e8133978222bc0d6eb9e5417f))
* GitHub Actions graphify-update, secrets API/desktop store, graphify obsidian export scripts ([11ac716](https://github.com/Brian5m1th/K.A.O.S/commit/11ac7163f1e3a987bb9a63c05c591523c2bfab43))
* integrate Graphify graph.json as code intelligence source ([39216a8](https://github.com/Brian5m1th/K.A.O.S/commit/39216a8fb79b6a4c772b2f81f0e49927c4d36d0a))
* kaos-research laboratory — evidence-driven framework evaluation ([16b14d0](https://github.com/Brian5m1th/K.A.O.S/commit/16b14d0c53cdb87004b9eb49cb04f18d976b085f))
* **production:** K.A.O.S production readiness — mock elimination, store consolidation, unified dashboard, offline gate, Windows fix ([77593e4](https://github.com/Brian5m1th/K.A.O.S/commit/77593e49a6fcee0f47b9ffaa7c1ef891934620c7))

## [2.5.5](https://github.com/Brian5m1th/K.A.O.S/compare/v2.5.4...v2.5.5) (2026-07-11)


### Bug Fixes

* **cargo:** remove unused net.timeout key and update docs submodule ([a17619c](https://github.com/Brian5m1th/K.A.O.S/commit/a17619cb7269160920e445e28d53ec77cd948f45))
* **desktop:** resolve duplicate kaos-client module state causing localhost fallback ([57646c0](https://github.com/Brian5m1th/K.A.O.S/commit/57646c0dd8b8820f1aa59a328a6fdd38b64451f2))
* **ops:** restore production api gateway, update deploy cleanup, and update docs submodule ([dd409df](https://github.com/Brian5m1th/K.A.O.S/commit/dd409dfc9267b4ab97b96d53c0c8c9e9e9b010c3))

## [2.5.4](https://github.com/Brian5m1th/K.A.O.S/compare/v2.5.3...v2.5.4) (2026-07-11)


### Bug Fixes

* **backend:** initialize VaultWatcher in the background to prevent lifespan startup block ([dd66826](https://github.com/Brian5m1th/K.A.O.S/commit/dd668264ecac67f4d149f390c11af8cc5c844c56))

## [2.5.3](https://github.com/Brian5m1th/K.A.O.S/compare/v2.5.2...v2.5.3) (2026-07-11)


### Bug Fixes

* **ci:** run workspace permissions cleanup unconditionally and stop containers first ([b6e5729](https://github.com/Brian5m1th/K.A.O.S/commit/b6e57292a6fc007d54a5c7bf15393f175b7c609a))

## [2.5.2](https://github.com/Brian5m1th/K.A.O.S/compare/v2.5.1...v2.5.2) (2026-07-11)


### Bug Fixes

* **ci:** add workspace permissions cleanup step before checkout on self-hosted runner ([e60ed4f](https://github.com/Brian5m1th/K.A.O.S/commit/e60ed4f4a9494f4e148691d13ec544dd8c3bdd98))

## [2.5.1](https://github.com/Brian5m1th/K.A.O.S/compare/v2.5.0...v2.5.1) (2026-07-11)


### Bug Fixes

* **infra:** adjust postgres and kaos-api healthchecks to prevent deploy and rollback timeouts ([8c07c27](https://github.com/Brian5m1th/K.A.O.S/commit/8c07c27f3ed85030b1af8c19e4050f155775186a))

# [2.5.0](https://github.com/Brian5m1th/K.A.O.S/compare/v2.4.0...v2.5.0) (2026-07-10)


### Features

* **infra:** update prod docker stack with logging limits, alertmanager, and blackbox monitoring ([2988362](https://github.com/Brian5m1th/K.A.O.S/commit/2988362fdb8af286ba6d88b06f1c027c5b0509c9))

# [2.4.0](https://github.com/Brian5m1th/K.A.O.S/compare/v2.3.9...v2.4.0) (2026-07-10)


### Features

* **deploy:** implement runtime version endpoint and add --build with tag interpolation to CD ([5d2498c](https://github.com/Brian5m1th/K.A.O.S/commit/5d2498cf41554c715eee251cca73a59b2d4abea1))

## [2.3.9](https://github.com/Brian5m1th/K.A.O.S/compare/v2.3.8...v2.3.9) (2026-07-10)


### Bug Fixes

* **cd:** gerar .env.prod a partir do secret ENV_PROD ([5bd21c5](https://github.com/Brian5m1th/K.A.O.S/commit/5bd21c5698b366230d65fea88042e6e8a0aaf984))
* **deploy:** update healthcheck verification port to 1010 to match docker compose external mapping ([cb4e1f1](https://github.com/Brian5m1th/K.A.O.S/commit/cb4e1f1f96f93c1a48d3ca162c9d1dca9405606f))

## [2.3.8](https://github.com/Brian5m1th/K.A.O.S/compare/v2.3.7...v2.3.8) (2026-07-10)


### Bug Fixes

* **kaos-api:** move BootstrapManager.boot() to background task to pass container healthcheck on startup ([f2bad1b](https://github.com/Brian5m1th/K.A.O.S/commit/f2bad1b906d2c1be8c49bdc06d4662c750cc0234))

## [2.3.7](https://github.com/Brian5m1th/K.A.O.S/compare/v2.3.6...v2.3.7) (2026-07-10)


### Bug Fixes

* **cd:** remover --build do deploy e ampliar janela de health do kaos-api ([d4d355d](https://github.com/Brian5m1th/K.A.O.S/commit/d4d355db8b471e6ace2f5dd31879518b49cf8a84))

## [2.3.6](https://github.com/Brian5m1th/K.A.O.S/compare/v2.3.5...v2.3.6) (2026-07-10)


### Bug Fixes

* **kaos-api:** warmup do embedder nao-bloqueante + rebuild no deploy ([4887ce0](https://github.com/Brian5m1th/K.A.O.S/commit/4887ce0cd91d14b1e8aa866d86ab4880fb450a86))

## [2.3.5](https://github.com/Brian5m1th/K.A.O.S/compare/v2.3.4...v2.3.5) (2026-07-10)


### Bug Fixes

* **infra:** relaxar dependencia do ollama para service_started (imagem sem curl) ([b7ecc16](https://github.com/Brian5m1th/K.A.O.S/commit/b7ecc168f1ee9976809a0bd3cda84072a77b52c3))

## [2.3.4](https://github.com/Brian5m1th/K.A.O.S/compare/v2.3.3...v2.3.4) (2026-07-10)


### Bug Fixes

* **cd:** tornar prepare do .env.prod anterior ao login e tolerar falhas de ghcr ([2ded963](https://github.com/Brian5m1th/K.A.O.S/commit/2ded9637ff74c9238471ef7f4e8c7ee8a49f474e))

## [2.3.3](https://github.com/Brian5m1th/K.A.O.S/compare/v2.3.2...v2.3.3) (2026-07-10)


### Bug Fixes

* **cd:** resolve .env.prod via secret and fix qdrant/ollama healthchecks ([0edb183](https://github.com/Brian5m1th/K.A.O.S/commit/0edb1831b0b4f7c3784592cc7245e8fa920b9192))

## [2.3.2](https://github.com/Brian5m1th/K.A.O.S/compare/v2.3.1...v2.3.2) (2026-07-10)


### Bug Fixes

* **cd:** gerar .env.prod a partir do secret ENV_PROD ([#94](https://github.com/Brian5m1th/K.A.O.S/issues/94)) ([cda358d](https://github.com/Brian5m1th/K.A.O.S/commit/cda358d87b7c70da7ed6820ff36c657caafd7e3f))

## [2.3.1](https://github.com/Brian5m1th/K.A.O.S/compare/v2.3.0...v2.3.1) (2026-07-10)


### Bug Fixes

* **cors:** include tauri v2 origins (http/https://tauri.localhost) in default CORS_ORIGINS ([e0d1d3d](https://github.com/Brian5m1th/K.A.O.S/commit/e0d1d3d897593f6004836dce4b63c257819f90df))

# [2.3.0](https://github.com/Brian5m1th/K.A.O.S/compare/v2.2.2...v2.3.0) (2026-07-10)


### Bug Fixes

* corrige lint Python (E402/F401), coverage thresholds e templates de teste ([415725b](https://github.com/Brian5m1th/K.A.O.S/commit/415725b4ff513e66ffe1d79c0eeb21de0c285b51))
* **deploy:** prepare environment file by copying persistent .env.prod from host to runner workspace ([857142e](https://github.com/Brian5m1th/K.A.O.S/commit/857142e9abf1ae59b1e9a5c9d791400424c88577))
* **docker:** add code source volumes and healthcheck for dev reliability ([c9c44b5](https://github.com/Brian5m1th/K.A.O.S/commit/c9c44b5659539e679ff453fd1a17058154e172ba))
* **formatting:** apply ruff formatting across assistant backend and test files ([6347772](https://github.com/Brian5m1th/K.A.O.S/commit/6347772f8ffff3a0c591070ce3ca3bdc81123cfb))
* **linter:** resolve all unused imports, variables and re-exports in backend assistant ([ef8fad0](https://github.com/Brian5m1th/K.A.O.S/commit/ef8fad02ed9af3761306bcf0865e7fef9dbf1545))
* ruff format 19 arquivos e ajusta drift threshold para 50% ([af93355](https://github.com/Brian5m1th/K.A.O.S/commit/af93355ac1e3805bcbccf21dfbae447adcaa955a))
* suprime F841 restantes (result1, client_box) ([0f81df7](https://github.com/Brian5m1th/K.A.O.S/commit/0f81df76af61d7097b562cb8c1f2799e5f0ae453))


### Features

* **bootstrap:** implement BootstrapManager with 8-stage async startup pipeline ([0943c9e](https://github.com/Brian5m1th/K.A.O.S/commit/0943c9ec903e5d817eb1d847c2f8cae41e55b709))
* **desktop:** add bootstrap state machine with Tauri commands for health check ([96f3dcd](https://github.com/Brian5m1th/K.A.O.S/commit/96f3dcd71c021d6ab9e196094422d3fb0012f9ec))
* **devops:** consolidate CI/CD pipelines, integrate cloudflared, enforce healthchecks & update desktop API default url ([5f52e78](https://github.com/Brian5m1th/K.A.O.S/commit/5f52e787eff5d422801c0e423ab76d935e40180b))
* **env:** implement EnvironmentService with multi-strategy path resolution and KIRL integration ([5c8eb85](https://github.com/Brian5m1th/K.A.O.S/commit/5c8eb85ed3de9ea8086853262c375d2b572174ce))
* Fase 5 (Refatoracao Arquitetural) + Fase 6 (Estrategia de Testes) ([00a80d9](https://github.com/Brian5m1th/K.A.O.S/commit/00a80d93972bb8a6198a233bb5c8684757592491))
* finaliza implementacoes pendentes de RAG, sandbox Wasm, Wiki-First, integracoes (email/whatsapp/aws) e correcoes de heatmap ([a2763cc](https://github.com/Brian5m1th/K.A.O.S/commit/a2763cce2cba7b441a455afc4947b22c2b87c1df))
* implementa adaptador github_tool.py sob o protocolo mcp ([2a08d93](https://github.com/Brian5m1th/K.A.O.S/commit/2a08d9318238ed1e722eadbe9cbbe68473103e94))
* implementa deteccao de contradicoes logicas e cronologicas no analisador do vault ([2dbbe4a](https://github.com/Brian5m1th/K.A.O.S/commit/2dbbe4ac949fe2ac6cc9c775026d5694ab42cb65))
* implementa executor OpenCodeExecutor com whitelist/blacklist e sandbox Docker ([6a0fe4c](https://github.com/Brian5m1th/K.A.O.S/commit/6a0fe4c2bb7939e86d804a6463eac28f0df5a3b8))
* implementa handshake de criptografia efemera PyNaCl e setup seguro ([0fa7c89](https://github.com/Brian5m1th/K.A.O.S/commit/0fa7c8902a5105bdda5c6d2b31a39715433658ff))
* implementa interface agnostica AIRuntime e RuntimeSelector ([87d6433](https://github.com/Brian5m1th/K.A.O.S/commit/87d643357c99a22b2373937aafa0264c08539852))
* implementa nova arquitetura desacoplada do K.A.O.S (runtimes, capability registry, workspace intelligence e credentials) ([f0d37f9](https://github.com/Brian5m1th/K.A.O.S/commit/f0d37f9f326dba38f358930f7e4243b7bca3c6d1))
* implementa segregacao de usuario por contextvars e cache sqlite de embeddings ([fc01f9c](https://github.com/Brian5m1th/K.A.O.S/commit/fc01f9cdc2089538b25e2e47fd7838422adefd14))
* **marketplace:** add workflow templates API and dynamic frontend integration ([fece02e](https://github.com/Brian5m1th/K.A.O.S/commit/fece02e93eb418114ff3c82bcc4552510e054ebc))

## [2.2.2](https://github.com/Brian5m1th/K.A.O.S/compare/v2.2.1...v2.2.2) (2026-07-10)


### Bug Fixes

* **ci:** grant issues write permission and guard PR comment against forks ([383e65d](https://github.com/Brian5m1th/K.A.O.S/commit/383e65ddb03cc217557df09bdd1d7831d250efe8))

## [2.2.1](https://github.com/Brian5m1th/K.A.O.S/compare/v2.2.0...v2.2.1) (2026-07-08)


### Bug Fixes

* **ci:** allow release.yml to trigger on semantic-release published events ([258c8a0](https://github.com/Brian5m1th/K.A.O.S/commit/258c8a0f51b9e6ab796c8fe78262adc474fd4235))

# [2.2.0](https://github.com/Brian5m1th/K.A.O.S/compare/v2.1.0...v2.2.0) (2026-07-08)


### Features

* K.A.O.S stabilization and real backend integrations ([#90](https://github.com/Brian5m1th/K.A.O.S/issues/90)) ([32ba21a](https://github.com/Brian5m1th/K.A.O.S/commit/32ba21a5a2c3a741a046660d489030c739df60cd)), closes [#89](https://github.com/Brian5m1th/K.A.O.S/issues/89)
* **release:** implement SDD-RELEASE-001 automatic versioning & release pipeline ([be0fef3](https://github.com/Brian5m1th/K.A.O.S/commit/be0fef3446746006b0e92ce95dc09eaec1846c36))
