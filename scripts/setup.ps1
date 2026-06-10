param(
    [string]$Model = "qwen3:14b"
)

$ErrorActionPreference = "Stop"

Write-Host "=== Setup do Ambiente - AI Assistant ===" -ForegroundColor Cyan

# --- Ollama ---
$ollamaPath = "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe"
if (-not (Test-Path $ollamaPath)) {
    Write-Host "[1/3] Instalando Ollama..." -ForegroundColor Yellow
    $url = "https://ollama.com/install.ps1"
    Invoke-RestMethod -Uri $url | Invoke-Expression
} else {
    Write-Host "[1/3] Ollama ja instalado." -ForegroundColor Green
}

# Add Ollama to PATH for this session
$env:PATH += ";$env:LOCALAPPDATA\Programs\Ollama"

# --- Model ---
Write-Host "[2/3] Baixando modelo $Model..." -ForegroundColor Yellow
ollama pull $Model

Write-Host "[3/3] Verificando modelo..." -ForegroundColor Yellow
ollama list

Write-Host "=== Setup concluido! ===" -ForegroundColor Cyan
Write-Host "Execute 'ollama run $Model' para testar." -ForegroundColor Green
