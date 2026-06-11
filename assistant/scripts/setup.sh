#!/usr/bin/env bash
set -euo pipefail

MODEL="${1:-qwen3:14b}"

echo "=== Setup do Ambiente - K.A.O.S ==="

# --- Ollama ---
if ! command -v ollama &>/dev/null; then
    echo "[1/3] Instalando Ollama..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        curl -fsSL https://ollama.com/install.sh | sh
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        curl -fsSL https://ollama.com/install.sh | sh
    else
        echo "Sistema operacional nao suportado. Instale manualmente: https://ollama.com"
        exit 1
    fi
else
    echo "[1/3] Ollama ja instalado."
fi

# --- Model ---
echo "[2/3] Baixando modelo ${MODEL}..."
ollama pull "${MODEL}"

echo "[3/3] Verificando modelo..."
ollama list

echo "=== Setup concluido! ==="
echo "Execute 'ollama run ${MODEL}' para testar."
