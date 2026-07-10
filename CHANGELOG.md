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
