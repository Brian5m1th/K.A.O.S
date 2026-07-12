#!/usr/bin/env python
"""
Daily Graphify Update Script

Executa graphify update . e commita alterações no graphify-out/graph.json.
Pode ser rodado via cron, Task Scheduler (Windows) ou GitHub Actions.

Uso:
    python scripts/daily-graphify-update.py
    python scripts/daily-graphify-update.py --commit --push
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime
from loguru import logger


def run_graphify_update(repo_root: Path, commit: bool = False, push: bool = False) -> bool:
    """Executa graphify update . e opcionalmente commita/push."""
    
    logger.info("Iniciando graphify update...")
    
    # Verificar se graphify está instalado
    try:
        result = subprocess.run(
            ["graphify", "--version"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode != 0:
            logger.error("graphify não encontrado")
            return False
        logger.info(f"Graphify version: {result.stdout.strip()}")
    except FileNotFoundError:
        logger.error("graphify não encontrado no PATH")
        return False
    except subprocess.TimeoutExpired:
        logger.error("Timeout ao verificar graphify")
        return False
    
    # Executar graphify update
    try:
        logger.info("Executando graphify update . ...")
        result = subprocess.run(
            ["graphify", "update", "."],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            timeout=300,  # 5 min timeout
        )
        
        if result.returncode != 0:
            logger.error(f"graphify update falhou: {result.stderr}")
            return False
        
        logger.info("Graphify update concluído com sucesso")
        logger.debug(f"stdout: {result.stdout[:500]}")
        
    except subprocess.TimeoutExpired:
        logger.error("Timeout no graphify update (300s)")
        return False
    except Exception as e:
        logger.error(f"Erro ao executar graphify update: {e}")
        return False
    
    # Commit se solicitado
    if commit:
        if not _git_commit_and_push(push):
            return False
    
    return True


def _git_commit_and_push(push: bool = False) -> bool:
    """Commita graphify-out/graph.json se houve mudanças."""
    try:
        # Verificar se há mudanças
        result = subprocess.run(
            ["git", "diff", "--quiet", "graphify-out/graph.json"],
            capture_output=True,
        )
        
        if result.returncode == 0:
            logger.info("Nenhuma mudança em graphify-out/graph.json")
            return True
        
        # Commit
        msg = f"chore: auto-update graphify graph [{datetime.now().strftime('%Y-%m-%d')}]"
        
        subprocess.run(["git", "add", "graphify-out/graph.json"], check=True)
        subprocess.run(["git", "commit", "-m", f"chore: auto-update graphify graph [{datetime.now().strftime('%Y-%m-%d')}]"], check=True)
        logger.info("Graph commitado com sucesso")
        
        if push:
            subprocess.run(["git", "push"], check=True)
            logger.info("Push realizado")
        
        return True
        
    except subprocess.CalledProcessError as e:
        logger.error(f"Erro no git: {e}")
        return False


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Daily Graphify Update")
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Root do repositório",
    )
    parser.add_argument(
        "--commit",
        action="store_true",
        help="Commit changes to git",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push to remote after commit",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose logging",
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.remove()
        logger.add(sys.stderr, level="DEBUG")
    
    repo_root = Path(args.repo_root).resolve()
    
    success = run_graphify_update(repo_root, commit=args.commit, push=args.push)
    
    if success:
        logger.info("✅ Daily Graphify update concluído")
        sys.exit(0)
    else:
        logger.error("❌ Falha no daily graphify update")
        sys.exit(1)


if __name__ == "__main__":
    main()