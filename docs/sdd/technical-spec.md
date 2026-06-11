# Technical Specification — [Nome da Feature]

> Template para detalhar a implementação da feature.

---

## 1. Arquivos Envolvidos

| Arquivo | Tipo | Ação |
|:--------|:-----|:-----|
| `app/exemplo.py` | Novo | Criar |
| `app/existente.py` | Existente | Modificar |

---

## 2. Estrutura de Dados

```python
@dataclass
class Exemplo:
    campo: str
    valor: int
```

---

## 3. API / Interfaces

### `POST /api/exemplo`

**Request:**
```json
{
  "campo": "texto",
  "valor": 42
}
```

**Response:**
```json
{
  "status": "ok",
  "dados": {}
}
```

---

## 4. Fluxo de Implementação

1. Criar módulo `app/exemplo/`
2. Implementar classe `ExemploService`
3. Criar endpoint em `app/api/exemplo.py`
4. Registrar rota em `app/main.py`
5. Escrever testes em `tests/unit/exemplo/`

---

## 5. Dependências

- Bibliotecas novas
- Configurações de ambiente
- Serviços externos necessários

---

## 6. Testes

| Teste | Tipo | O que valida |
|:------|:-----|:-------------|
| `test_exemplo_basico` | Unit | Comportamento padrão |
| `test_exemplo_erro` | Unit | Tratamento de erro |
| `test_exemplo_integracao` | Integration | Interação com Qdrant |
