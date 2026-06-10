import pytest
from pathlib import Path
from app.config.settings import settings
from app.obsidian.services.obsidian_service import ObsidianService


@pytest.fixture
def vault(tmp_path: Path) -> Path:
    original = settings.OBSIDIAN_VAULT_PATH
    settings.OBSIDIAN_VAULT_PATH = str(tmp_path)
    yield tmp_path
    settings.OBSIDIAN_VAULT_PATH = original


def test_create_and_read_note(vault: Path) -> None:
    svc = ObsidianService()
    path = svc.create_note(title="Teste", folder="Inbox", content="# Teste\nConteúdo.")
    result = svc.read_note(path)
    assert "Conteúdo" in result.content


def test_create_note_duplicate_raises(vault: Path) -> None:
    svc = ObsidianService()
    svc.create_note(title="Unico", folder="Inbox", content="Conteúdo")
    with pytest.raises(FileExistsError):
        svc.create_note(title="Unico", folder="Inbox", content="Duplicado")


def test_read_nonexistent_raises(vault: Path) -> None:
    svc = ObsidianService()
    with pytest.raises(FileNotFoundError):
        svc.read_note("Inexistente.md")


def test_update_note_overwrite(vault: Path) -> None:
    svc = ObsidianService()
    path = svc.create_note(title="Atualizar", folder="Inbox", content="Original")
    svc.update_note(path, content="Modificado", mode="overwrite")
    result = svc.read_note(path)
    assert result.content == "Modificado"


def test_update_note_append(vault: Path) -> None:
    svc = ObsidianService()
    path = svc.create_note(title="Append", folder="Inbox", content="Linha 1")
    svc.update_note(path, content="Linha 2", mode="append")
    result = svc.read_note(path)
    assert "Linha 1" in result.content
    assert "Linha 2" in result.content


def test_delete_note(vault: Path) -> None:
    svc = ObsidianService()
    path = svc.create_note(title="Deletar", folder="Inbox", content="Será removido")
    svc.delete_note(path)
    with pytest.raises(FileNotFoundError):
        svc.read_note(path)


def test_delete_nonexistent_raises(vault: Path) -> None:
    svc = ObsidianService()
    with pytest.raises(FileNotFoundError):
        svc.delete_note("Inexistente.md")


def test_list_notes(vault: Path) -> None:
    svc = ObsidianService()
    svc.create_note("Nota1", "Inbox", "a")
    svc.create_note("Nota2", "Inbox", "b")
    notes = svc.list_notes("Inbox")
    assert len(notes) == 2


def test_list_notes_empty_folder(vault: Path) -> None:
    svc = ObsidianService()
    notes = svc.list_notes("Vazia")
    assert notes == []


def test_search_finds_keyword(vault: Path) -> None:
    svc = ObsidianService()
    svc.create_note("Python Async", "Inbox", "asyncio é usado para concorrência.")
    results = svc.search_text("asyncio")
    assert len(results) == 1
    assert "asyncio" in results[0].excerpt


def test_search_no_match(vault: Path) -> None:
    svc = ObsidianService()
    svc.create_note("Nota", "Inbox", "conteúdo qualquer")
    results = svc.search_text("inexistente")
    assert len(results) == 0


def test_search_max_results(vault: Path) -> None:
    svc = ObsidianService()
    for i in range(5):
        svc.create_note(f"Nota {i}", "Inbox", "palavra_chave")
    results = svc.search_text("palavra_chave", max_results=3)
    assert len(results) == 3


def test_path_traversal_protection(vault: Path) -> None:
    svc = ObsidianService()
    with pytest.raises(PermissionError):
        svc.read_note("../fora_do_vault/nota.md")


def test_special_chars_in_title(vault: Path) -> None:
    svc = ObsidianService()
    path = svc.create_note('Nota: Especial "Teste"', "Inbox", "conteúdo")
    assert "Nota_ Especial _Teste_" in path
