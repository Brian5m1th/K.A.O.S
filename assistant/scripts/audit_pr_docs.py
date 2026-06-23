#!/usr/bin/env python3
"""
Auditoria de documentacao para PRs.

Verifica se os commits de um Pull Request possuem documentacao associada.
Se faltar, gera AUTO-SDD automaticamente e registra no FeatureRegistry.

Uso:
    python assistant/scripts/audit_pr_docs.py --base main --head feat/minha-feature
    python assistant/scripts/audit_pr_docs.py --commits "abc123,def456"
"""

import argparse
import subprocess
import sys
from pathlib import Path

from app.audit.runtime_resolver import RuntimePathResolver


def get_commits_from_range(base: str, head: str) -> list[dict]:
    """Obtém commits entre base e head."""
    cmd = [
        "git",
        "log",
        f"{base}..{head}",
        "--no-merges",
        "--pretty=format:%H|%s",
    ]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=RuntimePathResolver.project_root(),
            timeout=30,
        )
        if result.returncode != 0:
            print(f"[audit_pr] ERRO: git log falhou: {result.stderr}")
            return []

        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split("|", 1)
            if len(parts) == 2:
                commits.append({"hash": parts[0][:8], "message": parts[1]})
        return commits
    except Exception as e:
        print(f"[audit_pr] ERRO: {e}")
        return []


def get_commits_from_list(commits_str: str) -> list[dict]:
    """Parse lista de commits."""
    return [
        {
            "hash": c.split(":")[0].strip()[:8] if ":" in c else c.strip()[:8],
            "message": c.split(":", 1)[1].strip() if ":" in c else "",
        }
        for c in commits_str.split(",")
        if c.strip()
    ]


def classify_impact(message: str) -> str:
    """Classifica impacto do commit."""
    msg = message.lower()
    high_patterns = [
        "event bus",
        "workflow",
        "provider",
        "model router",
        "observability",
        "memory",
        "circuit breaker",
        "dead letter",
        "orchestrator",
        "n8n",
        "sse",
        "tool layer",
        "agent",
        "launcher",
    ]
    medium_patterns = [
        "api",
        "endpoint",
        "store",
        "hook",
        "component",
        "schema",
        "config",
        "migration",
        "database",
        "registry",
    ]

    for pattern in high_patterns:
        if pattern in msg:
            return "high"
    for pattern in medium_patterns:
        if pattern in msg:
            return "medium"
    return "low"


def check_documentation_exists(feature_id: str) -> bool:
    """Verifica se existe SDD para a feature."""
    patterns = [
        Path(f"docs/sdd/{feature_id}.md"),
        Path(f"docs/sdd/SDD-{feature_id.upper()}.md"),
        Path(f"docs/sdd/sdd_{feature_id}.md"),
        RuntimePathResolver.auto_dir() / f"AUTO-SDD-{feature_id}.md",
    ]
    for path in patterns:
        if path.exists():
            return True

    sdd_dir = Path("docs/sdd")
    if sdd_dir.exists():
        for md_file in sdd_dir.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
                if feature_id.lower() in content.lower():
                    return True
            except Exception:
                pass
    return False


def generate_auto_sdd(
    feature_id: str,
    feature_name: str,
    commit_hash: str,
    commit_message: str,
    impact: str,
    code_refs: list[str],
) -> Path:
    """Gera AUTO-SDD para a feature."""
    from app.audit.sdd_generator import SDDGenerator, SDDTemplate

    template = SDDTemplate(
        feature_id=feature_id,
        feature_name=feature_name,
        commit_hash=commit_hash,
        commit_message=commit_message,
        phase="auto-detected",
        detected_code_refs=code_refs,
        impact_type=impact,
    )
    return SDDGenerator.generate_sdd(template)


def register_feature(feature_id: str, feature_name: str, commit_hash: str, impact: str):
    """Registra feature no registry se existir."""
    try:
        from app.audit.feature_registry import FeatureEntry, FeatureRegistry

        FeatureRegistry.load_from_json()
        existing = FeatureRegistry.get(feature_id)
        if existing:
            FeatureRegistry.update_last_commit(feature_id, commit_hash)
            print(f"[audit_pr] Feature atualizada: {feature_id}")
            return
        entry = FeatureEntry(
            id=feature_id,
            name=feature_name,
            phase="auto-detected",
            status="in-progress" if impact == "high" else "planned",
        )
        FeatureRegistry.register(entry)
        print(f"[audit_pr] Feature registrada: {feature_id}")
    except Exception as e:
        print(f"[audit_pr] AVISO: nao foi possivel registrar feature: {e}")


def audit_commits(commits: list[dict]) -> dict:
    """Audita lista de commits."""
    results = {
        "total": len(commits),
        "has_documentation": 0,
        "missing_documentation": 0,
        "auto_generated": 0,
        "details": [],
    }

    for commit in commits:
        msg = commit["message"]
        impact = classify_impact(msg)

        feature_id = (
            msg.split(":")[0].strip().lower() if ":" in msg else msg.split()[0].lower()
        )
        feature_name = msg.split(":", 1)[1].strip() if ":" in msg else msg

        has_docs = check_documentation_exists(feature_id)
        detail = {
            "hash": commit["hash"],
            "message": msg,
            "impact": impact,
            "has_documentation": has_docs,
            "feature_id": feature_id,
        }

        if has_docs:
            results["has_documentation"] += 1
            print(f"[audit_pr] ✔ {commit['hash']}: {msg[:50]}... -> documentado")
        else:
            results["missing_documentation"] += 1
            print(f"[audit_pr] ✘ {commit['hash']}: {msg[:50]}... -> SEM DOCUMENTACAO")

            try:
                path = generate_auto_sdd(
                    feature_id=feature_id,
                    feature_name=feature_name,
                    commit_hash=commit["hash"],
                    commit_message=msg,
                    impact=impact,
                    code_refs=[],
                )
                results["auto_generated"] += 1
                detail["auto_sdd_path"] = str(path)
                print(f"[audit_pr]   → SDD gerado: {path}")

                register_feature(feature_id, feature_name, commit["hash"], impact)
            except Exception as e:
                print(f"[audit_pr]   → ERRO ao gerar SDD: {e}")

        results["details"].append(detail)

    return results


def print_report(results: dict):
    """Exibe relatório formatado."""
    print(f"\n{'=' * 60}")
    print("RELATORIO DE AUDITORIA DE DOCUMENTACAO")
    print(f"{'=' * 60}")
    print(f"Total de commits:          {results['total']}")
    print(f"Com documentacao:          {results['has_documentation']}")
    print(f"SEM documentacao:          {results['missing_documentation']}")
    print(f"SDDs gerados:              {results['auto_generated']}")
    print(f"{'=' * 60}")

    if results["missing_documentation"] > 0:
        print("\nCommits SEM documentacao:")
        for d in results["details"]:
            if not d["has_documentation"]:
                print(f"  - {d['hash']} {d['message'][:60]}")
                if d.get("auto_sdd_path"):
                    print(f"    SDD gerado: {d['auto_sdd_path']}")

    passed = results["missing_documentation"] == 0
    print(f"\nStatus: {'✔ APROVADO' if passed else '✘ REPROVADO'}")
    return passed


def main():
    parser = argparse.ArgumentParser(description="Audita documentacao de PRs")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--base", help="Branch base (ex: main)")
    group.add_argument("--commits", help="Lista de commits (ex: abc123,def456)")
    parser.add_argument("--head", default="HEAD", help="Branch head (padrao: HEAD)")

    args = parser.parse_args()

    if args.base:
        commits = get_commits_from_range(args.base, args.head)
    else:
        commits = get_commits_from_list(args.commits)

    if not commits:
        print("[audit_pr] Nenhum commit encontrado.")
        sys.exit(0)

    results = audit_commits(commits)
    passed = print_report(results)
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
