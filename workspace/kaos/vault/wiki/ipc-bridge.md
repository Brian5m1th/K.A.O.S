# desktop\src\shared\api\ipc-bridge.ts

## Símbolos

- [[desktop_src_shared_api_ipc_bridge]] — code: ipc-bridge.ts
- [[desktop_src_shared_api_ipc_bridge_istauri]] — code: isTauri()
- [[desktop_src_shared_api_ipc_bridge_invokeipc]] — code: invokeIpc()
- [[desktop_src_shared_api_ipc_bridge_fetchhealth]] — code: fetchHealth()
- [[desktop_src_shared_api_ipc_bridge_fetchbootstrapstate]] — code: fetchBootstrapState()
- [[desktop_src_shared_api_ipc_bridge_listenipc]] — code: listenIpc()

## Dependências

- [[desktop_src_shared_api_ipc_bridge]] → `contains` → [[desktop_src_shared_api_ipc_bridge_fetchbootstrapstate]]
- [[desktop_src_shared_api_ipc_bridge]] → `contains` → [[desktop_src_shared_api_ipc_bridge_fetchhealth]]
- [[desktop_src_shared_api_ipc_bridge]] → `contains` → [[desktop_src_shared_api_ipc_bridge_invokeipc]]
- [[desktop_src_shared_api_ipc_bridge]] → `contains` → [[desktop_src_shared_api_ipc_bridge_istauri]]
- [[desktop_src_shared_api_ipc_bridge]] → `contains` → [[desktop_src_shared_api_ipc_bridge_listenipc]]
- [[desktop_src_shared_api_ipc_bridge_invokeipc]] → `calls` → [[desktop_src_shared_api_ipc_bridge_istauri]]
- [[desktop_src_shared_api_ipc_bridge_listenipc]] → `calls` → [[desktop_src_shared_api_ipc_bridge_istauri]]
- [[desktop_src_shared_api_ipc_bridge_invokeipc]] → `calls` → [[desktop_src_shared_api_ipc_bridge_fetchbootstrapstate]]
- [[desktop_src_shared_api_ipc_bridge_invokeipc]] → `calls` → [[desktop_src_shared_api_ipc_bridge_fetchhealth]]