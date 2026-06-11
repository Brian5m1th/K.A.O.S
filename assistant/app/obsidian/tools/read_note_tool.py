from langchain_core.tools import tool


def _get_service():
    from app.obsidian.services.obsidian_service import ObsidianService
    return ObsidianService()


@tool
def read_note(path: str) -> dict:
    """Lê o conteúdo de uma nota existente no Vault pelo seu caminho relativo."""
    svc = _get_service()
    result = svc.read_note(relative_path=path)
    return result.model_dump(mode="json")
