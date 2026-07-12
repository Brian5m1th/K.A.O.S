#!/usr/bin/env pwsh
# check-duplicates.ps1 — Verifica se docs/wiki/ e workspace/kaos/vault/wiki/ estão sincronizados
# Uso: ./scripts/check-duplicates.ps1
# Exit code: 0 se sincronizado, 1 se divergente

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot

$source = Join-Path $root "docs/wiki"
$target = Join-Path $root "workspace/kaos/vault/wiki"

if (-not (Test-Path $source) -or -not (Test-Path $target)) {
    Write-Warning "Um dos diretórios não existe"
    exit 1
}

$diff = Compare-Object (Get-ChildItem $source -Recurse -Name) (Get-ChildItem $target -Recurse -Name)

if ($diff) {
    Write-Warning "Wiki e vault divergentes! Execute ./scripts/sync-vault.ps1"
    $diff | Select-Object -First 20 | ForEach-Object { Write-Host "  $($_.InputObject) ($($_.SideIndicator))" }
    exit 1
}

Write-Host "OK — Wiki e vault estão sincronizados."
exit 0
