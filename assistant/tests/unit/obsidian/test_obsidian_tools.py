import pytest
from pathlib import Path
from app.config.settings import settings


@pytest.fixture(autouse=True)
def vault(tmp_path: Path) -> None:
    original = settings.OBSIDIAN_VAULT_PATH
    settings.OBSIDIAN_VAULT_PATH = str(tmp_path)
    yield
    settings.OBSIDIAN_VAULT_PATH = original


def test_create_note_tool() -> None:
    from app.obsidian.tools.create_note_tool import create_note
    result = create_note.invoke({"title": "Tool Note", "folder": "Inbox", "content": "# Tool\nConteúdo."})
    assert result["status"] == "CREATED"


def test_read_note_tool() -> None:
    from app.obsidian.tools.create_note_tool import create_note
    from app.obsidian.tools.read_note_tool import read_note
    create_note.invoke({"title": "Leitura", "folder": "Inbox", "content": "Para ler"})
    result = read_note.invoke({"path": "Inbox/Leitura.md"})
    assert result["content"] == "Para ler"


def test_update_note_tool_overwrite() -> None:
    from app.obsidian.tools.create_note_tool import create_note
    from app.obsidian.tools.update_note_tool import update_note
    from app.obsidian.tools.read_note_tool import read_note
    create_note.invoke({"title": "Upd", "folder": "Inbox", "content": "Antigo"})
    update_note.invoke({"path": "Inbox/Upd.md", "content": "Novo"})
    result = read_note.invoke({"path": "Inbox/Upd.md"})
    assert result["content"] == "Novo"


def test_update_note_tool_append() -> None:
    from app.obsidian.tools.create_note_tool import create_note
    from app.obsidian.tools.update_note_tool import update_note
    from app.obsidian.tools.read_note_tool import read_note
    create_note.invoke({"title": "App", "folder": "Inbox", "content": "Primeira"})
    update_note.invoke({"path": "Inbox/App.md", "content": "Segunda", "mode": "append"})
    result = read_note.invoke({"path": "Inbox/App.md"})
    assert "Primeira" in result["content"]
    assert "Segunda" in result["content"]


def test_delete_note_tool() -> None:
    from app.obsidian.tools.create_note_tool import create_note
    from app.obsidian.tools.delete_note_tool import delete_note
    from app.obsidian.tools.read_note_tool import read_note
    create_note.invoke({"title": "Del", "folder": "Inbox", "content": "Será deletado"})
    delete_note.invoke({"path": "Inbox/Del.md"})
    with pytest.raises(FileNotFoundError):
        read_note.invoke({"path": "Inbox/Del.md"})


def test_search_notes_tool() -> None:
    from app.obsidian.tools.create_note_tool import create_note
    from app.obsidian.tools.search_notes_tool import search_notes
    create_note.invoke({"title": "Busca", "folder": "Inbox", "content": "termo específico aqui"})
    result = search_notes.invoke({"query": "específico"})
    assert result["total"] == 1
    assert "termo" in result["documents"][0]["excerpt"]
