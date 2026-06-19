from pathlib import Path
from loguru import logger
from app.config.settings import settings

VAULT_FOLDERS = [
    "Projetos",
    "Arquitetura",
    "SDD",
    "Estudos",
    "IA",
    "Python",
    "Java",
    "AWS",
    "CI-CD",
    "Diario",
    "Inbox",
]

WIKI_FOLDERS = [
    "raw",
    "raw/assets",
    "wiki",
    "wiki/entities",
    "wiki/concepts",
    "wiki/sources",
    "wiki/synthesis",
]


def create_vault_structure() -> list[str]:
    vault = Path(settings.OBSIDIAN_VAULT_PATH)
    if not vault.exists():
        logger.error(f"[error] vault_init - vault nao encontrado: {vault}")
        raise FileNotFoundError(f"Vault nao encontrado: {vault}")

    created: list[str] = []
    all_folders = VAULT_FOLDERS + WIKI_FOLDERS
    for folder in all_folders:
        folder_path = vault / folder
        if not folder_path.exists():
            folder_path.mkdir(parents=True)
            created.append(folder)
            logger.info(f"[info] vault_init - pasta criada: {folder}")

    if created:
        logger.info(
            f"[info] vault_init - {len(created)} pastas criadas: {', '.join(created)}"
        )
    else:
        logger.info("[info] vault_init - estrutura ja existe")

    if created:
        _create_bootstrap_files(vault)

    return created


def _create_bootstrap_files(vault: Path) -> None:
    wiki_index = vault / "wiki" / "index.md"
    if not wiki_index.exists():
        wiki_index.write_text(
            "# Wiki — Indice\n\n"
            "## Entities\n\n"
            "## Concepts\n\n"
            "## Sources\n\n"
            "## Synthesis\n"
        )
        logger.info("[info] vault_init - wiki/index.md criado")

    wiki_log = vault / "wiki" / "log.md"
    if not wiki_log.exists():
        wiki_log.write_text(
            "# Wiki — Log de Alteracoes\n\n## 2026-06-18\n\n- Wiki inicializada\n"
        )
        logger.info("[info] vault_init - wiki/log.md criado")
