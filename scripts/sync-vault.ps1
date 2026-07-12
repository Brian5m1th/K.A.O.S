#!/usr/bin/env pwsh
# sync-vault.ps1 — Sincroniza docs/wiki/ → workspace/kaos/vault/wiki/
# Uso: ./scripts/sync-vault.ps1
# One-way sync: docs/ é a fonte de verdade

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot

$source = Join-Path $root "docs/wiki"
$target = Join-Path $root "workspace/kaos/vault/wiki"

if (-not (Test-Path $source)) {
    Write-Error "Fonte não encontrada: $source"
    exit 1
}

if (-not (Test-Path $target)) {
    Write-Warning "Criando diretório alvo: $target"
    New-Item -ItemType Directory -Path $target -Force | Out-Null
}

Write-Host "Syncing: $source → $target"
robocopy $source $target /MIR /NP /NDL /NJH /NJS

Write-Host "Sync concluído com sucesso."
