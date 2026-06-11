Source: Antigravity AI
Tags: #sdd #python #obsidian #fastapi #fase3 #tools
Related: [[index]] [[backlog]] [[sdd_fase2_ia_local]] [[sdd_obsidian_tools]] [[sdd_obsidian_memoria]] [[sdd_fase4_rag_pipeline]]

# SDD — Fase 3: ObsidianService e Ferramentas de Nota

## Objetivo

Implementar a camada completa de integração Python ↔ Vault Obsidian. A IA passará a ter acesso de leitura e escrita no Vault através de ferramentas bem definidas, formando a base da memória de longo prazo.

---

## Critério de Sucesso

> A IA consegue criar uma nota em `Inbox/`, ler seu conteúdo de volta e realizar uma busca textual por palavras-chave no Vault — tudo via chamadas Python ao `ObsidianService`.

---

## Tarefas

### ⚙️ Configuração
- [ ] Identificar caminho absoluto do Vault no sistema
- [ ] Configurar `OBSIDIAN_VAULT_PATH` no `.env`
- [ ] Criar módulo `app/obsidian/` com `__init__.py`

### 📖 Leitura
- [ ] Implementar `ObsidianService`
- [ ] Implementar `ReadNoteTool`
- [ ] Implementar `ListNotesTool`
- [ ] Testar leitura de arquivos Markdown existentes

### ✏️ Escrita
- [ ] Implementar `CreateNoteTool`
- [ ] Implementar `UpdateNoteTool`
- [ ] Implementar `DeleteNoteTool`
- [ ] Validar criação de notas pelo Python

### 🔍 Busca
- [ ] Implementar `SearchNotesTool` (busca textual)
- [ ] Criar testes automatizados

---

## 1. Estrutura de Módulos

```text
app/
├── obsidian/
│   ├── __init__.py
│   ├── services/
│   │   └── obsidian_service.py   # Acesso ao filesystem do Vault
│   └── tools/
│       ├── __init__.py
│       ├── create_note_tool.py
│       ├── read_note_tool.py
│       ├── update_note_tool.py
│       ├── delete_note_tool.py
│       └── search_notes_tool.py
└── domain/
    └── document.py               # DTOs: NoteRequest, NoteResponse, SearchResult
```

---

## 2. DTOs de Domínio (`domain/document.py`)

```python
from pydantic import BaseModel, Field
from datetime import datetime

class NoteCreateRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    folder: str = Field(default="Inbox")
    content: str = Field(..., min_length=1)

class NoteUpdateRequest(BaseModel):
    path: str = Field(..., description="Caminho relativo à raiz do Vault")
    content: str
    mode: str = Field(default="overwrite", pattern="^(overwrite|append)$")

class NoteResponse(BaseModel):
    status: str
    path: str

class NoteReadResult(BaseModel):
    path: str
    content: str
    last_modified: datetime

class SearchResult(BaseModel):
    path: str
    score: float = 1.0
    excerpt: str

class SearchResponse(BaseModel):
    query: str
    total: int
    documents: list[SearchResult]
```

---

## 3. ObsidianService (`obsidian/services/obsidian_service.py`)

Responsável exclusivamente pelo acesso ao filesystem. Não contém regras de negócio.

```python
import os
import re
from pathlib import Path
from datetime import datetime
from loguru import logger
from app.config.settings import settings
from app.domain.document import NoteReadResult, SearchResult

class ObsidianService:
    """Serviço de acesso ao Vault Obsidian via sistema de arquivos."""

    def __init__(self) -> None:
        self._vault_path = Path(settings.OBSIDIAN_VAULT_PATH)
        if not self._vault_path.exists():
            raise ValueError(f"Vault não encontrado em: {self._vault_path}")
        logger.info(f"ObsidianService iniciado. Vault: {self._vault_path}")

    def _resolve_path(self, relative_path: str) -> Path:
        """Resolve um caminho relativo à raiz do Vault com segurança."""
        resolved = (self._vault_path / relative_path).resolve()
        # Garante que o caminho está dentro do Vault (path traversal protection)
        if not str(resolved).startswith(str(self._vault_path.resolve())):
            raise PermissionError(f"Acesso negado fora do Vault: {relative_path}")
        return resolved

    def create_note(self, title: str, folder: str, content: str) -> str:
        """Cria uma nota Markdown no Vault. Retorna o caminho relativo criado."""
        folder_path = self._vault_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)

        safe_title = re.sub(r'[<>:"/\\|?*]', "_", title)
        file_path = folder_path / f"{safe_title}.md"

        if file_path.exists():
            raise FileExistsError(f"Nota já existe: {folder}/{safe_title}.md")

        file_path.write_text(content, encoding="utf-8")
        relative = str(file_path.relative_to(self._vault_path))
        logger.info(f"Nota criada: {relative}")
        return relative

    def read_note(self, relative_path: str) -> NoteReadResult:
        """Lê o conteúdo de uma nota pelo caminho relativo."""
        file_path = self._resolve_path(relative_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Nota não encontrada: {relative_path}")

        content = file_path.read_text(encoding="utf-8")
        last_modified = datetime.fromtimestamp(file_path.stat().st_mtime)
        return NoteReadResult(path=relative_path, content=content, last_modified=last_modified)

    def update_note(self, relative_path: str, content: str, mode: str = "overwrite") -> None:
        """Atualiza uma nota existente. Modos: 'overwrite' ou 'append'."""
        file_path = self._resolve_path(relative_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Nota não encontrada: {relative_path}")

        if mode == "append":
            existing = file_path.read_text(encoding="utf-8")
            file_path.write_text(existing + "\n\n" + content, encoding="utf-8")
        else:
            file_path.write_text(content, encoding="utf-8")
        logger.info(f"Nota atualizada ({mode}): {relative_path}")

    def delete_note(self, relative_path: str) -> None:
        """Remove uma nota do Vault."""
        file_path = self._resolve_path(relative_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Nota não encontrada: {relative_path}")
        file_path.unlink()
        logger.info(f"Nota removida: {relative_path}")

    def list_notes(self, folder: str = "") -> list[str]:
        """Lista caminhos relativos de todos os .md em uma pasta."""
        search_path = self._vault_path / folder if folder else self._vault_path
        return [
            str(p.relative_to(self._vault_path))
            for p in search_path.rglob("*.md")
            if not p.name.startswith(".")
        ]

    def search_text(self, query: str, max_results: int = 10) -> list[SearchResult]:
        """Busca textual por palavra-chave em todos os arquivos Markdown do Vault."""
        results: list[SearchResult] = []
        query_lower = query.lower()

        for path in self._vault_path.rglob("*.md"):
            if path.name.startswith("."):
                continue
            try:
                content = path.read_text(encoding="utf-8")
                if query_lower in content.lower():
                    # Extrai um trecho ao redor da primeira ocorrência
                    idx = content.lower().index(query_lower)
                    start = max(0, idx - 100)
                    end = min(len(content), idx + 200)
                    excerpt = content[start:end].strip()
                    relative = str(path.relative_to(self._vault_path))
                    results.append(SearchResult(path=relative, excerpt=excerpt))
                    if len(results) >= max_results:
                        break
            except (UnicodeDecodeError, OSError):
                continue

        return results
```

---

## 4. Ferramentas LangGraph-Compatíveis

Cada tool é uma função pura com tipagem Pydantic. O LangGraph as registra via `@tool`.

### `create_note_tool.py`
```python
from langchain_core.tools import tool
from app.obsidian.services.obsidian_service import ObsidianService
from app.domain.document import NoteCreateRequest, NoteResponse

_svc = ObsidianService()

@tool
def create_note(title: str, folder: str, content: str) -> dict:
    """Cria uma nova nota Markdown no Vault Obsidian."""
    path = _svc.create_note(title=title, folder=folder, content=content)
    return NoteResponse(status="CREATED", path=path).model_dump()
```

### `read_note_tool.py`
```python
@tool
def read_note(path: str) -> dict:
    """Lê o conteúdo de uma nota existente no Vault pelo seu caminho relativo."""
    result = _svc.read_note(relative_path=path)
    return result.model_dump(mode="json")
```

### `update_note_tool.py`
```python
@tool
def update_note(path: str, content: str, mode: str = "overwrite") -> dict:
    """Atualiza uma nota existente (overwrite ou append)."""
    _svc.update_note(relative_path=path, content=content, mode=mode)
    return NoteResponse(status="UPDATED", path=path).model_dump()
```

### `delete_note_tool.py`
```python
@tool
def delete_note(path: str) -> dict:
    """Remove uma nota do Vault Obsidian."""
    _svc.delete_note(relative_path=path)
    return NoteResponse(status="DELETED", path=path).model_dump()
```

### `search_notes_tool.py`
```python
@tool
def search_notes(query: str, max_results: int = 5) -> dict:
    """Busca textual por palavra-chave em todas as notas do Vault."""
    results = _svc.search_text(query=query, max_results=max_results)
    return {
        "query": query,
        "total": len(results),
        "documents": [r.model_dump() for r in results],
    }
```

---

## 5. Testes Unitários

```text
tests/
└── unit/
    └── obsidian/
        ├── test_obsidian_service.py
        └── test_obsidian_tools.py
```

Estratégia: usar `tmp_path` do pytest para criar um Vault temporário em disco, sem depender do Vault real.

```python
# tests/unit/obsidian/test_obsidian_service.py
import pytest
from pathlib import Path
from app.obsidian.services.obsidian_service import ObsidianService

@pytest.fixture
def vault(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setenv("OBSIDIAN_VAULT_PATH", str(tmp_path))
    return tmp_path

def test_create_and_read_note(vault: Path) -> None:
    svc = ObsidianService()
    path = svc.create_note(title="Teste", folder="Inbox", content="# Teste\nConteúdo.")
    result = svc.read_note(path)
    assert "Conteúdo" in result.content

def test_search_finds_keyword(vault: Path) -> None:
    svc = ObsidianService()
    svc.create_note("Python Async", "Python", "asyncio é usado para concorrência.")
    results = svc.search_text("asyncio")
    assert len(results) == 1
    assert "Python" in results[0].path
```

---

## Dependências Desta Fase

- [[sdd_fase1_fundacao]] — Settings, logging e estrutura base
- [[sdd_fase2_ia_local]] — LLM Service para integrar resposta com contexto

## Desbloqueia

- [[sdd_fase4_rag_pipeline]] — Indexação vetorial das notas no Qdrant
- [[sdd_fase5_watcher_langgraph]] — Agente usa as tools registradas
