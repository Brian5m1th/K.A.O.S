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


def create_vault_structure() -> list[str]:
    vault = Path(settings.OBSIDIAN_VAULT_PATH)
    if not vault.exists():
        logger.error(f"[error] vault_init - vault nao encontrado: {vault}")
        raise FileNotFoundError(f"Vault nao encontrado: {vault}")

    created: list[str] = []
    for folder in VAULT_FOLDERS:
        folder_path = vault / folder
        if not folder_path.exists():
            folder_path.mkdir(parents=True)
            created.append(folder)
            logger.info(f"[info] vault_init - pasta criada: {folder}")

    if created:
        logger.info(f"[info] vault_init - {len(created)} pastas criadas: {', '.join(created)}")
    else:
        logger.info("[info] vault_init - estrutura ja existe")

    return created
