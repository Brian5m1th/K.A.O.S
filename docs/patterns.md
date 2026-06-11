# Padrões de Código — K.A.O.S

> Padrões obrigatórios para todo código produzido no projeto.

---

## P12 — Padrão de Logs (Estruturado)

Todos os métodos públicos DEVEM seguir este padrão de marcadores:

| Marcador | Nível | Onde usar |
|:---------|:------|:----------|
| `[start]` | `info` | Primeira linha de método público |
| `[finish]` | `debug` | Última linha antes do retorno |
| `[skip]` | `info` | Branch ignorada condicionalmente |
| `[error]` | `error` | Exception capturada e tratada |
| `[info]` | `info` | Evento de negócio relevante |
| `[sending]` | `info` | Envio de dado para serviço externo |
| `[received]` | `info` | Recebimento de dado de serviço externo |
| `[fallback]` | `warning` | Ativação de fallback |

**Formato:**

```python
logger.info("[start] Classe - metodo")
logger.debug("[finish] Classe - metodo")
logger.info("[skip] Classe - motivo")
logger.error("[error] Classe - descricao")
logger.info("[info] Classe - evento")
logger.info("[sending] Classe - destino")
logger.info("[received] Classe - origem")
logger.warning("[fallback] Classe - motivo")
```

---

## Obrigatórios

### 1. Sem comentários inline

NÃO adicione comentários explicando O QUE o código faz. O código deve ser autoexplicativo.

### 2. Type hints

Toda função/método DEVE ter type hints nos parâmetros e retorno.

### 3. Sem emoji em server-side

Emojis são permitidos APENAS em interfaces voltadas ao usuário final (frontend). Proibidos em logs, código backend, nomes de arquivo.

### 4. Nomes em inglês

Código (variáveis, funções, classes, arquivos) em inglês. Mensagens para o usuário podem ser em português.

### 5. Loguru como logger único

Use `from loguru import logger`. Não use `logging` diretamente.

---

## Anti-patterns (NÃO FAÇA)

| ID | Prática | Problema |
|:---|:--------|:---------|
| A01 | Comentários explicando passos | Código deve ser autoexplicativo |
| A02 | `print()` para debug | Use `logger.debug()` |
| A03 | Log sem marcador | Dificulta filtragem |
| A04 | `except:` genérico | Esconde erros reais |
| A05 | Mutação de parâmetros recebidos | Efeito colateral inesperado |
| A06 | Nomes de uma letra (exceto `i` em loops) | Código ilegível |
| A07 | Strings mágicas sem constante | Dificulta manutenção |
| A08 | Arquivos > 500 linhas | Dificulta compreensão |
| A09 | Import relativo (`from ..foo import bar`) | Prefira imports absolutos |
| A10 | Emoji em código server-side | Semântica ambígua |
| A11 | Comentário inline explicando passo | Código verboso sem necessidade |

---

## Ferramentas

- **Linter:** `ruff`
- **Formatter:** `ruff format`
- **Type checker:** `mypy` (futuro)

Execute antes de todo commit:

```bash
ruff check .
ruff format --check .
```
