@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
title AI Assistant - Setup Ollama

echo === Setup do Ambiente - AI Assistant ===
echo.

where ollama >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [1/3] Instalando Ollama...
    PowerShell -Command "& { irm https://ollama.com/install.ps1 | iex }"
    if !ERRORLEVEL! NEQ 0 (
        echo.
        echo Falha na instalacao. Tente manualmente: https://ollama.com/download/windows
        pause
        exit /b
    )
) else (
    echo [1/3] Ollama ja instalado.
)

echo [2/3] Baixando modelo qwen3:14b...
ollama pull qwen3:14b

echo [3/3] Verificando modelo...
ollama list

echo.
echo === Setup concluido! ===
echo Execute 'ollama run qwen3:14b' para testar.
pause
