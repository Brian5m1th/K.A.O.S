#!/usr/bin/env pwsh
# WireGuard VPN Setup for K.A.O.S — Windows
# Uso: ./setup.ps1 -Endpoint "vpn.kaos.example.com" -AllowedIPs "10.0.0.0/24, 172.16.0.0/12"

param(
    [Parameter(Mandatory = $true)]
    [string]$Endpoint,
    [string]$AllowedIPs = "10.0.0.0/24",
    [string]$ConfigPath = "$env:USERPROFILE\kaos-vpn.conf"
)

# Check if WireGuard is installed
$wg = Get-Command "wg" -ErrorAction SilentlyContinue
if (-not $wg) {
    Write-Error "WireGuard not found. Install from https://www.wireguard.com/install/"
    exit 1
}

# Generate keys
Write-Host "Generating WireGuard keys..."
$privateKey = (wg genkey) 
$publicKey = ($privateKey | wg pubkey)

Write-Host "Public key: $publicKey"

# Write config
@"
[Interface]
PrivateKey = $privateKey
Address = 10.0.0.2/24
DNS = 1.1.1.1

[Peer]
PublicKey = {{SERVER_PUBLIC_KEY}}
Endpoint = $Endpoint`:51820
AllowedIPs = $AllowedIPs
PersistentKeepalive = 25
"@ | Out-File -FilePath $ConfigPath -Encoding utf8

Write-Host "Config saved to: $ConfigPath"
Write-Host ""
Write-Host "Add this public key to the server: $publicKey"
Write-Host "Then connect with: wg-quick up `"$ConfigPath`""
