#!/usr/bin/env python3
"""
Script de migração: Obsidian memoria.md -> PostgreSQL memory_sessions/messages
Execute: python scripts/migrate_memory_to_postgres.py [--dry-run]
"""
import sys
import argparse
from pathlib import Path
from loguru import logger

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config.settings import settings
from app.memory.postgres_repository import PostgresMemoryRepository


def parse_memoria_file(filepath: Path) -> list[dict]:
    """Parse memoria.md e extrai conversas."""
    content = filepath.read_text(encoding="utf-8")
    conversations = []
    
    # Split por "## Conversa" ou similar
    sections = content.split("## Conversa")
    
    for section in sections[1:]:  # Pula o cabeçalho
        lines = section.strip().split("\n")
        if not lines:
            continue
            
        # Extrai metadados
        session_id = None
        user_id = None
        summary = ""
        user_msg = ""
        assistant_msg = ""
        
        current_field = None
        for line in lines:
            line = line.strip()
            if line.startswith("**Sessao:**"):
                session_id = line.replace("**Sessao:**", "").strip()
            elif line.startswith("**Usuario:**"):
                user_id = line.replace("**Usuario:**", "").strip()
            elif line.startswith("## Resumo"):
                current_field = "summary"
            elif line.startswith("## Usuario"):
                current_field = "user"
            elif line.startswith("## Assistente"):
                current_field = "assistant"
            elif line and current_field == "summary":
                summary += line + "\n"
            elif line and current_field == "user":
                user_msg += line + "\n"
            elif line and current_field == "assistant":
                assistant_msg += line + "\n"
        
        if session_id and user_id:
            conversations.append({
                "session_id": session_id,
                "user_id": user_id,
                "summary": summary.strip(),
                "user_message": user_msg.strip(),
                "assistant_response": assistant_msg.strip(),
            })
    
    return conversations


async def migrate(dry_run: bool = False):
    vault_path = Path(settings.OBSIDIAN_VAULT_PATH)
    users_dir = vault_path / "users"
    
    if not users_dir.exists():
        logger.warning(f"Diretório de usuários não encontrado: {users_dir}")
        return
    
    repo = PostgresMemoryRepository()
    await repo.init_db()
    
    total_migrated = 0
    errors = 0
    
    for user_dir in users_dir.iterdir():
        if not user_dir.is_dir():
            continue
            
        user_id = user_dir.name
        memoria_file = user_dir / "memoria.md"
        
        if not memoria_file.exists():
            continue
            
        logger.info(f"Processando {user_id}...")
        conversations = parse_memoria_file(memoria_file)
        
        for conv in conversations:
            if dry_run:
                logger.info(f"[DRY-RUN] Migraria: user={user_id} session={conv['session_id']}")
                total_migrated += 1
                continue
                
            try:
                await repo.save_conversation(
                    user_id=user_id,
                    session_id=conv["session_id"],
                    summary=conv["summary"],
                    user_message=conv["user_message"],
                    assistant_response=conv["assistant_response"],
                )
                total_migrated += 1
                logger.info(f"Migrado: user={user_id} session={conv['session_id']}")
            except Exception as e:
                logger.error(f"Erro ao migrar {user_id}/{conv['session_id']}: {e}")
                errors += 1
    
    await repo.close()
    
    logger.info(f"=== Migração {'simulada' if dry_run else 'concluída'} ===")
    logger.info(f"Total: {total_migrated} conversas")
    logger.info(f"Erros: {errors}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Migra memoria.md do Obsidian para PostgreSQL")
    parser.add_argument("--dry-run", action="store_true", help="Apenas simula, não grava no banco")
    args = parser.parse_args()
    
    import asyncio
    asyncio.run(migrate(dry_run=args.dry_run))