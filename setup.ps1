# K.A.O.S Desktop & Environment Setup Script
# Este script automatiza a instalação de dependências como Rustup, MSVC toolchain, Node.js, Python, Docker Desktop e UV.

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "  Iniciando a instalação do K.A.O.S Desktop  " -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan

# 1. Verificar privilégios e winget
if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    Write-Error "O utilitário 'winget' não foi encontrado no sistema. Por favor, instale o App Installer na Microsoft Store."
    Exit 1
}

# Função auxiliar para instalar pacotes via winget
function Install-Package {
    param (
        [string]$PackageId,
        [string]$Name
    )
    Write-Host "Verificando se $Name já está instalado..." -ForegroundColor Yellow
    $check = winget list --id $PackageId -e 2>$null
    if ($check) {
        Write-Host "$Name já está instalado." -ForegroundColor Green
    } else {
        Write-Host "Instalando $Name..." -ForegroundColor Cyan
        winget install --id $PackageId -e --silent --accept-source-agreements --accept-package-agreements
        if ($LASTEXITCODE -eq 0) {
            Write-Host "$Name instalado com sucesso." -ForegroundColor Green
        } else {
            Write-Warning "Falha ou reinicialização necessária para $Name."
        }
    }
}

# Instalar dependências básicas do sistema
Install-Package "Git.Git" "Git"
Install-Package "Python.Python.3.13" "Python 3.13"
Install-Package "OpenJS.NodeJS.LTS" "Node.js (LTS)"
Install-Package "Rustlang.Rustup" "Rustup"
Install-Package "Docker.DockerDesktop" "Docker Desktop"

# 2. Configurar o Rustup e a toolchain MSVC
Write-Host "Configurando Rustup para usar a toolchain x86_64-pc-windows-msvc..." -ForegroundColor Yellow

# Garantir que o cargo está no PATH da sessão atual do PowerShell
$env:PATH += ";$env:USERPROFILE\.cargo\bin"

# Executar comandos do rustup
if (Get-Command rustup -ErrorAction SilentlyContinue) {
    Write-Host "Instalando a toolchain stable-x86_64-pc-windows-msvc..." -ForegroundColor Cyan
    rustup toolchain install stable-x86_64-pc-windows-msvc
    
    Write-Host "Definindo a toolchain estável MSVC como padrão..." -ForegroundColor Cyan
    rustup default stable-x86_64-pc-windows-msvc
    
    Write-Host "Adicionando o target x86_64-pc-windows-msvc..." -ForegroundColor Cyan
    rustup target add x86_64-pc-windows-msvc
    
    Write-Host "Rustup configurado com sucesso para MSVC." -ForegroundColor Green
} else {
    Write-Warning "Rustup instalado, mas o executável 'rustup' não pôde ser localizado na sessão atual. Por favor, reinicie o PowerShell após o término do script."
}

# 3. Instalar o UV (Gerenciador de pacotes Python)
Write-Host "Verificando o gerenciador de pacotes UV..." -ForegroundColor Yellow
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "Instalando UV..." -ForegroundColor Cyan
    powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
    $env:PATH += ";$env:USERPROFILE\.local\bin"
} else {
    Write-Host "UV já está instalado." -ForegroundColor Green
}

# 4. Instalar dependências do Frontend (Desktop)
Write-Host "Instalando dependências do frontend (desktop)..." -ForegroundColor Yellow
if (Test-Path "desktop") {
    Push-Location desktop
    npm install
    Pop-Location
    Write-Host "Dependências do frontend instaladas com sucesso." -ForegroundColor Green
} else {
    Write-Warning "Pasta 'desktop' não encontrada no diretório atual."
}

# 5. Configurar o ambiente virtual do Backend
Write-Host "Instalando dependências do backend (assistant)..." -ForegroundColor Yellow
if (Test-Path "assistant") {
    Push-Location assistant
    if (Get-Command uv -ErrorAction SilentlyContinue) {
        uv sync
        Write-Host "Ambiente do backend sincronizado com sucesso." -ForegroundColor Green
    } else {
        Write-Warning "Não foi possível executar 'uv sync' pois o UV não está disponível nesta sessão."
    }
    Pop-Location
} else {
    Write-Warning "Pasta 'assistant' não encontrada no diretório atual."
}

# 6. Iniciar serviços do Docker Compose
Write-Host "Verificando estado do Docker Compose..." -ForegroundColor Yellow
if (Get-Command docker -ErrorAction SilentlyContinue) {
    if (Test-Path "infra/docker") {
        Write-Host "Iniciando contêineres do Docker Compose (Ollama, Postgres, Qdrant, etc.)..." -ForegroundColor Cyan
        Push-Location infra/docker
        docker compose up -d
        Pop-Location
        Write-Host "Serviços do Docker iniciados com sucesso!" -ForegroundColor Green
    }
} else {
    Write-Warning "Docker não encontrado ou não está rodando. Por favor, inicie o Docker Desktop para rodar a infraestrutura."
}

Write-Host "=============================================" -ForegroundColor Green
Write-Host " Configuração concluída! Abra um novo terminal" -ForegroundColor Green
Write-Host " para aplicar as alterações do PATH." -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Green
