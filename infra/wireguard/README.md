# WireGuard VPN — K.A.O.S Production Access

> Configuração WireGuard para acesso remoto seguro ao ambiente produtivo.

## Topologia

```
[Admin Laptop] ──── WireGuard ──── [Cloudflare Tunnel] ──── [K.A.O.S API]
                                      │
                                      └─── [Grafana]
                                      └─── [N8N]
```

## Setup

```bash
# Instalar WireGuard
# Linux: apt install wireguard
# macOS: brew install wireguard-tools
# Windows: https://www.wireguard.com/install/

# Gerar chaves
wg genkey | tee privatekey | wg pubkey > publickey

# Copiar config para /etc/wireguard/kaos.conf
sudo cp kaos.conf /etc/wireguard/
sudo wg-quick up kaos
```

## Arquivos

- `kaos.conf` — Config do peer cliente (template)
- `server.conf` — Config do servidor (template)
- `setup.ps1` — Script de setup Windows

> **Nota:** Substituir `{{SERVER_PUBLIC_KEY}}`, `{{ENDPOINT}}` e `{{ALLOWED_IPS}}` pelos valores reais.
