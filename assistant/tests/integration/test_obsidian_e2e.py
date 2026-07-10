"""Testes de integracao E2E para validacao de notas geradas pelo Python no Obsidian.

Valida o ciclo completo: criacao -> leitura -> verificacao de integridade ->
atualizacao -> delecao, simulando o uso real das ferramentas da IA.
"""

import pytest
from pathlib import Path
from datetime import datetime
from app.config.settings import settings
from app.obsidian.services.obsidian_service import ObsidianService


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def vault(tmp_path: Path) -> Path:
    """Cria um vault temporario e configura o settings."""
    original = settings.OBSIDIAN_VAULT_PATH
    settings.OBSIDIAN_VAULT_PATH = str(tmp_path)
    yield tmp_path
    settings.OBSIDIAN_VAULT_PATH = original


@pytest.fixture
def svc(vault: Path) -> ObsidianService:
    """Retorna uma instancia do ObsidianService apontando para o vault temp."""
    return ObsidianService()


# ---------------------------------------------------------------------------
# Testes E2E - Validacao de criacao de notas pelo Python
# ---------------------------------------------------------------------------


class TestNoteCreationE2E:
    """Validacao completa do ciclo de vida de notas criadas pelo Python."""

    def test_full_roundtrip_create_read(
        self, svc: ObsidianService, vault: Path
    ) -> None:
        """Cria uma nota via Python e verifica que pode ser lida de volta com
        conteudo identico."""
        original_content = (
            "# Nota de Teste\n\nConteudo criado pelo Python.\n\n- Item 1\n- Item 2"
        )
        relative_path = svc.create_note(
            title="Roundtrip Test",
            folder="Projetos",
            content=original_content,
        )

        # Verificar pelo servico
        result = svc.read_note(relative_path)
        assert result.content == original_content, (
            "Conteudo lido deve ser identico ao original"
        )
        assert relative_path in result.path, "Path deve conter o caminho relativo"

        # Verificar pelo filesystem diretamente
        disk_path = vault / relative_path
        assert disk_path.exists(), "Arquivo deve existir em disco"
        disk_content = disk_path.read_text(encoding="utf-8")
        assert disk_content == original_content, "Conteudo em disco deve ser identico"

    def test_create_note_with_frontmatter(
        self, svc: ObsidianService, vault: Path
    ) -> None:
        """Valida que notas com frontmatter YAML sao preservadas."""
        content = """---
id: test-note
type: knowledge
status: active
---

# Nota com Frontmatter

Conteudo da nota com metadados.
"""
        path = svc.create_note("Frontmatter Note", "SDD", content)
        result = svc.read_note(path)

        assert "id: test-note" in result.content
        assert "type: knowledge" in result.content
        assert "status: active" in result.content
        assert "# Nota com Frontmatter" in result.content

    def test_create_note_utf8_special_chars(
        self, svc: ObsidianService, vault: Path
    ) -> None:
        """Valida que caracteres UTF-8 especiais (acentos, emoji, simbolos)
        sao preservados corretamente."""
        content = "# Acentuação\n\nAção, contribuição, órgão, FAQ.\n\n🔍 Busca\n\nCódigo: 42 ✓"
        path = svc.create_note("UTF-8 Test", "Inbox", content)
        result = svc.read_note(path)

        assert "Ação" in result.content
        assert "contribuição" in result.content
        assert "órgão" in result.content
        assert "🔍" in result.content
        assert "✓" in result.content

        # Verificar encoding do arquivo em disco
        disk_path = vault / path
        raw_bytes = disk_path.read_bytes()
        raw_bytes.decode("utf-8")  # Nao deve levantar excecao

    def test_create_and_list_consistency(
        self, svc: ObsidianService, vault: Path
    ) -> None:
        """Apos criar notas, a listagem deve retorna-las."""
        svc.create_note("Listagem A", "Inbox", "Conteudo A")
        svc.create_note("Listagem B", "Estudos", "Conteudo B")

        inbox_notes = svc.list_notes("Inbox")
        estudos_notes = svc.list_notes("Estudos")

        assert any("Listagem A" in n for n in inbox_notes)
        assert any("Listagem B" in n for n in estudos_notes)

    def test_create_update_read_cycle(self, svc: ObsidianService, vault: Path) -> None:
        """Cria nota, atualiza, le de volta e verifica conteudo modificado."""
        path = svc.create_note("Ciclo Update", "Inbox", "Versao 1")

        svc.update_note(path, "Versao 2", mode="overwrite")
        result = svc.read_note(path)
        assert result.content == "Versao 2"

        svc.update_note(path, "\nVersao 3", mode="append")
        result = svc.read_note(path)
        assert "Versao 2" in result.content
        assert "Versao 3" in result.content

    def test_create_delete_confirm_removed(
        self, svc: ObsidianService, vault: Path
    ) -> None:
        """Cria nota, deleta, e confirma que foi removida do disco e do servico."""
        path = svc.create_note("Serah Deletada", "Inbox", "Conteudo temporario")
        disk_path = vault / path
        assert disk_path.exists()

        svc.delete_note(path)
        assert not disk_path.exists(), "Arquivo deve ser removido do disco"

        with pytest.raises(FileNotFoundError):
            svc.read_note(path)

    def test_create_multiple_folders_deep_path(
        self, svc: ObsidianService, vault: Path
    ) -> None:
        """Cria nota em subpasta aninhada e valida resolucao de caminho."""
        content = "# Nota Profunda"
        path = svc.create_note("Profunda", "Arquitetura/Decisoes/ADR-042", content)
        result = svc.read_note(path)

        assert result.content == content
        disk_path = vault / path
        assert disk_path.exists()
        assert "Arquitetura" in path
        assert "Decisoes" in path

    def test_note_content_roundtrip_markdown_structure(
        self, svc: ObsidianService, vault: Path
    ) -> None:
        """Valida que a estrutura Markdown complexa e preservada."""
        content = """# Documento Complexo

## Secao 1

Texto com **negrito** e *italico*.

### Subsecao

- Lista item 1
- Lista item 2

```python
def hello():
    print("Hello, K.A.O.S!")
```

| Coluna 1 | Coluna 2 |
|----------|----------|
| Valor 1  | Valor 2  |

> Citacao importante.
"""
        path = svc.create_note("Markdown Complexo", "Estudos", content)
        result = svc.read_note(path)

        assert "**negrito**" in result.content
        assert "*italico*" in result.content
        assert "def hello():" in result.content
        assert "| Coluna 1 |" in result.content
        assert "> Citacao importante" in result.content
        assert result.content == content

    def test_large_content_preservation(
        self, svc: ObsidianService, vault: Path
    ) -> None:
        """Valida que notas com conteudo grande (>10KB) sao preservadas."""
        paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 300
        content = f"# Nota Grande\n\n{paragraph}\n\n## Fim\n\n{paragraph[:500]}"
        assert len(content) > 10_000, (
            f"Conteudo deve ter mais de 10KB (tem {len(content)} bytes)"
        )

        path = svc.create_note("Nota Grande", "Inbox", content)
        result = svc.read_note(path)

        assert len(result.content) == len(content)
        assert result.content == content

    def test_timestamp_accuracy(self, svc: ObsidianService, vault: Path) -> None:
        """Verifica que o timestamp do arquivo e razoavel."""
        before = datetime.now()
        path = svc.create_note("Timestamp Test", "Inbox", "teste")
        after = datetime.now()
        result = svc.read_note(path)

        assert before <= result.last_modified <= after
