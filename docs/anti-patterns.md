# Anti-patterns — K.A.O.S

> Práticas que NÃO devem ser usadas no projeto.

---

## A01 — Comentários explicando passos

```python
# ❌ NÃO FAÇA
# Soma o total
total = sum(values)
# Retorna o resultado
return total
```

```python
# ✅ FAÇA
total = sum(values)
return total
```

---

## A02 — `print()` para debug

```python
# ❌ NÃO FAÇA
print(f"mensagem: {msg}")
```

```python
# ✅ FAÇA
from loguru import logger
logger.debug(f"mensagem: {msg}")
```

---

## A03 — Log sem marcador

```python
# ❌ NÃO FAÇA
logger.info("Arquivo indexado")
```

```python
# ✅ FAÇA
logger.info("[info] VaultIndexer - arquivo indexado")
```

---

## A04 — `except:` genérico

```python
# ❌ NÃO FAÇA
try:
    process()
except:
    pass
```

```python
# ✅ FAÇA
try:
    process()
except ValueError as e:
    logger.error(f"[error] modulo - erro de valor: {e}")
```

---

## A05 — Mutação de parâmetros recebidos

```python
# ❌ NÃO FAÇA
def process(items: list[str]) -> None:
    items.append("novo")  # modifica a lista original
```

```python
# ✅ FAÇA
def process(items: list[str]) -> list[str]:
    result = items.copy()
    result.append("novo")
    return result
```

---

## A06 — Nomes de uma letra (exceto `i` em loops)

```python
# ❌ NÃO FAÇA
def f(x, y):
    return x + y
```

```python
# ✅ FAÇA
def add(first: float, second: float) -> float:
    return first + second
```

---

## A07 — Strings mágicas sem constante

```python
# ❌ NÃO FAÇA
if role == "admin":
    grant_access()
```

```python
# ✅ FAÇA
ROLE_ADMIN = "admin"
if role == ROLE_ADMIN:
    grant_access()
```

---

## A08 — Arquivos > 500 linhas

Arquivos muito longos indicam responsabilidade demais. Quebre em módulos menores.

---

## A09 — Import relativo

```python
# ❌ NÃO FAÇA
from ..foo import bar
```

```python
# ✅ FAÇA
from app.foo import bar
```

---

## A10 — Emoji em código server-side

Emojis são permitidos APENAS em frontend voltado ao usuário. Nunca em logs, mensagens de API ou nomes de variáveis/arquivos no backend.

---

## A11 — Comentário inline explicando passo

```python
# ❌ NÃO FAÇA
response = await client.post(url)  # faz a requisicao POST
```

O código já deixa claro o que faz. Confie nas funções e nomes descritivos.
