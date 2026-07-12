# docs\architecture\DESKTOP_ARCHITECTURE.md

## Símbolos

- [[docs_architecture_desktop_architecture]] — code: DESKTOP_ARCHITECTURE.md
- [[docs_architecture_desktop_architecture_arquitetura_desktop_k_a_o_s]] — code: Arquitetura Desktop — K.A.O.S
- [[docs_architecture_desktop_architecture_stack]] — code: Stack
- [[docs_architecture_desktop_architecture_comunicação]] — code: Comunicação
- [[docs_architecture_desktop_architecture_providerstore_tauri_plugin]] — code: ProviderStore (Tauri Plugin)
- [[docs_architecture_desktop_architecture_estrutura_de_diretórios]] — code: Estrutura de Diretórios
- [[docs_architecture_desktop_architecture_fluxo_de_inicialização]] — code: Fluxo de Inicialização
- [[docs_architecture_desktop_architecture_auto_update]] — code: Auto-Update
- [[docs_architecture_desktop_architecture_segurança]] — code: Segurança

## Dependências

- [[docs_architecture_desktop_architecture]] → `contains` → [[docs_architecture_desktop_architecture_arquitetura_desktop_k_a_o_s]]
- [[docs_architecture_desktop_architecture_arquitetura_desktop_k_a_o_s]] → `contains` → [[docs_architecture_desktop_architecture_auto_update]]
- [[docs_architecture_desktop_architecture_arquitetura_desktop_k_a_o_s]] → `contains` → [[docs_architecture_desktop_architecture_comunicação]]
- [[docs_architecture_desktop_architecture_arquitetura_desktop_k_a_o_s]] → `contains` → [[docs_architecture_desktop_architecture_estrutura_de_diretórios]]
- [[docs_architecture_desktop_architecture_arquitetura_desktop_k_a_o_s]] → `contains` → [[docs_architecture_desktop_architecture_fluxo_de_inicialização]]
- [[docs_architecture_desktop_architecture_arquitetura_desktop_k_a_o_s]] → `contains` → [[docs_architecture_desktop_architecture_segurança]]
- [[docs_architecture_desktop_architecture_arquitetura_desktop_k_a_o_s]] → `contains` → [[docs_architecture_desktop_architecture_stack]]
- [[docs_architecture_desktop_architecture_comunicação]] → `contains` → [[docs_architecture_desktop_architecture_providerstore_tauri_plugin]]