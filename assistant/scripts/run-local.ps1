<#
.SYNOPSIS
    Inicia o K.A.O.S FastAPI localmente com Python/UV corretos

.DESCRIPTION
    Detecta automaticamente o Python correto (venv > system), 
    executa uv sync e inicia o servidor uvicorn com hot-reload
#>

param(
    [int]$Port = 8000,
    [string]$Host = "0.0.0.0",
    [switch]$NoReload,
    [string]$PythonPath = ""
)

$ErrorActionPreference = "Stop"
$ProjectRoot = "C:\workspace\Extras\K.A.O.S\assistant"

Write-Host "=== K.A.O.S Local Launcher ===" -ForegroundColor Cyan
Write-Host "Projeto: $ProjectRoot" -ForegroundColor Gray

# Detecta Python correto
if (-not [string]::IsNullOrEmpty($PythonPath)) {
    $Python = $PythonPath
} elseif (Test-Path "$ProjectRoot\.venv\Scripts\python.exe") {
    $Python = "$ProjectRoot\.venv\Scripts\python.exe"
    Write-Host "Usando Python do venv: $Python" -ForegroundColor Green
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $Python = (Get-Command python).Source
    Write-Host "Usando Python do PATH: $Python" -ForegroundColor Yellow
} elseif (Get-Command "C:\Users\brian\AppData\Local\Programs\Python\Python312\python.exe" -ErrorAction SilentlyContinue) {
    $Python = "C:\Users\brian\AppData\Local\Programs\Python\Python312\python.exe"
    Write-Host "Usando Python 3.12: $Python" -ForegroundColor Yellow
} else {
    Write-Error "Python não encontrado! Instale Python 3.12+ ou crie venv."
    exit 1
}

# Verifica se UV está disponível
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "Instalando UV..." -ForegroundColor Cyan
    & $Python -m pip install -q uv
}

# Sync dependências
Write-Host "Sincronizando dependências com UV..." -ForegroundColor Cyan
Set-Location $ProjectRoot
& $Python -m uv sync

# Monta comando uvicorn
$UvicornArgs = @("uvicorn", "app.main:app", "--host", $Host, "--port", $Port)
if (-not $NoReload) { $UvicornArgs += "--reload" }

Write-Host "Iniciando K.A.O.S em http://${Host}:${Port}" -ForegroundColor Green
Write-Host "Modelos disponíveis: kaos (SMART/qwen3:14b), kaos-rag (MEMORY/qwen3:14b), kaos-fast (FAST/qwen3:4b)" -ForegroundColor Gray
Write-Host "Pressione Ctrl+C para parar" -ForegroundColor Gray
Write-Host "---" -ForegroundColor Gray

# Executa
try {
    & $Python -m $UvicornArgs
}
catch {
    Write-Error "Erro ao iniciar servidor: $_"
    exit 1
}