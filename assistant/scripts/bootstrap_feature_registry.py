#!/usr/bin/env python3
"""
bootstrap_feature_registry.py — K.A.O.S Feature Registry Bootstrap via Git

Gera o features-index.json completo DIRETAMENTE do histórico git do repositório.

Fontes de dados (em ordem de prioridade):
  1. Git log completo — cada commit feat/fix extrai: Fase, SDD, escopo, arquivos tocados
  2. `git diff-tree` — arquivos modificados por commit vinculam code_refs reais
  3. `git log --diff-filter=A` — arquivos criados vinculam ao commit/feature de origem
  4. SDDs em docs/ — corroboram e enriquecem o que o git já disse

Por que git e não varredura local:
  - O git é a fonte de verdade: ele sabe QUANDO cada feature foi criada/alterada
  - Commits têm scope explícito (feat(orchestrator):, feat: Fase 8)
  - PRs mergeados têm título descritivo com feature name
  - Não precisa de heurísticas de conteúdo — o próprio dev declarou a feature no commit

Uso:
    cd K.A.O.S
    uv run python assistant/scripts/bootstrap_feature_registry.py
    uv run python assistant/scripts/bootstrap_feature_registry.py --dry-run
    uv run python assistant/scripts/bootstrap_feature_registry.py --verbose
    uv run python assistant/scripts/bootstrap_feature_registry.py --max-commits 500

CI (GitHub Actions):
    - Rodado no drift-check.yml ANTES do audit engine
    - Se o registry estiver desatualizado (< 10 features), roda automaticamente
"""

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

# ── Path setup ────────────────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).resolve().parent
_ASSISTANT_DIR = _SCRIPT_DIR.parent
_PROJECT_ROOT = _ASSISTANT_DIR.parent

sys.path.insert(0, str(_ASSISTANT_DIR))

from app.audit.runtime_resolver import RuntimePathResolver  # noqa: E402


# ── Modelos internos ──────────────────────────────────────────────────────────


@dataclass
class GitFeature:
    """Feature extraída do histórico git."""

    id: str
    name: str
    phase: str
    status: str
    docs: list[str] = field(default_factory=list)
    code_refs: list[str] = field(default_factory=list)
    last_commit: str = ""
    first_commit: str = ""
    created_at: str = ""
    updated_at: str = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "phase": self.phase,
            "status": self.status,
            "docs": sorted(set(self.docs)),
            "codeRefs": sorted(set(self.code_refs)),
            "lastCommit": self.last_commit,
            "createdAt": self.created_at or datetime.now(timezone.utc).isoformat(),
            "updatedAt": self.updated_at or datetime.now(timezone.utc).isoformat(),
        }


# ── Git helpers ───────────────────────────────────────────────────────────────


def _git(*args, cwd: Path = _PROJECT_ROOT) -> str:
    """Roda um comando git e retorna stdout. Nunca lança exceção."""
    try:
        result = subprocess.run(
            ["git", *args],
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=60,
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"[git] Erro: {e}")
        return ""


def get_all_commits(max_commits: int = 500) -> list[dict]:
    """
    Retorna todos os commits no formato:
    [{"hash": str, "subject": str, "author": str, "date": str}]
    """
    raw = _git(
        "log",
        f"--max-count={max_commits}",
        "--no-merges",
        "--format=%H\x1f%s\x1f%an\x1f%aI",
    )
    commits = []
    for line in raw.splitlines():
        parts = line.split("\x1f")
        if len(parts) == 4:
            commits.append(
                {
                    "hash": parts[0],
                    "subject": parts[1].strip(),
                    "author": parts[2],
                    "date": parts[3],
                }
            )
    return commits


def get_files_changed_in_commit(commit_hash: str) -> list[str]:
    """Retorna lista de arquivos modificados/criados num commit."""
    raw = _git("diff-tree", "--no-commit-id", "-r", "--name-only", commit_hash)
    return [f.strip() for f in raw.splitlines() if f.strip()]


# ── Parsers de commits ────────────────────────────────────────────────────────

# Padrão Conventional Commits: type(scope): subject
_CONV_COMMIT = re.compile(
    r"^(?P<type>feat|fix|refactor|test|docs|ci|chore|style|perf)"
    r"(?:\((?P<scope>[^)]+)\))?"
    r":\s*(?P<subject>.+)$",
    re.IGNORECASE,
)

# Padrão Fase explícita: "Fase 8", "Fase 1.3", "F2", "fase9"
_FASE_PATTERN = re.compile(
    r"[Ff]ase\s*(\d+[\.\d]*)|[Ff](\d+)(?:\b|[-_])", re.IGNORECASE
)

# Padrão SDD explícita: "SDD-KAOS-MCP-001", "SDD040", "SDD-KIRL"
_SDD_PATTERN = re.compile(r"SDD[-_]?([A-Z0-9\-_]+)", re.IGNORECASE)

# PR number no subject: "(#86)", "#86"
_PR_PATTERN = re.compile(r"\(#(\d+)\)|#(\d+)")


def _normalize_id(raw: str) -> str:
    """Converte qualquer string em feature-id normalizado kebab-case."""
    raw = re.sub(r"[()#\[\]]", "", raw.lower().strip())
    raw = re.sub(r"[\s_/\\\.]+", "-", raw)
    raw = re.sub(r"[^a-z0-9\-]", "", raw)
    raw = re.sub(r"-{2,}", "-", raw)
    return raw.strip("-") or "unknown"


def _name_from_subject(subject: str) -> str:
    """Extrai um nome limpo de feature a partir do subject do commit."""
    # Remover prefixos tipo "feat:", "fix:", "(#86)", "SDD-XXX"
    name = re.sub(
        r"^(feat|fix|refactor|test|docs|ci|chore|style|perf)(\([^)]+\))?:\s*",
        "",
        subject,
        flags=re.IGNORECASE,
    )
    name = re.sub(r"SDD[-_][A-Z0-9\-_]+", "", name, flags=re.IGNORECASE)
    name = re.sub(r"\(#\d+\)", "", name)
    name = re.sub(r"#\d+", "", name)
    name = re.sub(r"\s{2,}", " ", name).strip()
    # Capitalizar primeira letra
    return name[:1].upper() + name[1:] if name else "Unknown Feature"


def _extract_phase(subject: str) -> str:
    """Extrai a Fase mencionada no commit."""
    m = _FASE_PATTERN.search(subject)
    if m:
        num = m.group(1) or m.group(2)
        return f"Fase {num}"

    subject_lower = subject.lower()
    # Heurísticas por keyword
    if (
        "kirl" in subject_lower
        or "drl" in subject_lower
        or "documentation runtime" in subject_lower
    ):
        return "Fase 0"
    if "desktop stabilization" in subject_lower or "stabiliz" in subject_lower:
        return "Fase 1"
    if (
        "graphify" in subject_lower
        or "knowledge graph" in subject_lower
        or "readiness" in subject_lower
    ):
        return "Fase 2"
    if "provider" in subject_lower and "catalog" in subject_lower:
        return "Fase 3"
    if (
        "observability" in subject_lower
        or "prometheus" in subject_lower
        or "loki" in subject_lower
    ):
        return "Fase 4"
    if "opencode" in subject_lower:
        return "Fase 5"
    if (
        "rbac" in subject_lower
        or "multi user" in subject_lower
        or "multiuser" in subject_lower
    ):
        return "Fase 6"
    if "mcp" in subject_lower:
        return "Fase 7"
    if (
        "orchestrat" in subject_lower
        or "agent runtime" in subject_lower
        or "circuit breaker" in subject_lower
    ):
        return "Fase 8"
    if "n8n" in subject_lower:
        return "Fase 8.5"
    if "launcher" in subject_lower or "auto.update" in subject_lower:
        return "Fase 9"
    if "roadmap expansion" in subject_lower or "roadmap" in subject_lower:
        return "Fase 9+"
    return "Fase 1"


def _extract_feature_id_from_commit(commit: dict) -> str | None:
    """
    Extrai o ID de feature de um commit. Retorna None se não for feat/fix relevante.

    Lógica:
    1. Conventional commit com scope → scope é o feature id
    2. SDD-XXX no subject → SDD id é o feature id
    3. Fase X no subject → "fase-X" como feature id base + nome descritivo
    4. Descrição livre → normalizar o subject
    """
    subject = commit["subject"]

    # Ignorar commits sem valor para features
    if re.match(r"^(style|chore|ci|docs):", subject, re.IGNORECASE):
        # Exceto se mencionar SDD ou Fase explicitamente
        if not _FASE_PATTERN.search(subject) and not _SDD_PATTERN.search(subject):
            return None

    # 1. Scope explícito no conventional commit
    m = _CONV_COMMIT.match(subject)
    if m and m.group("scope"):
        scope = m.group("scope").strip()
        # Ignorar scopes genéricos
        if scope.lower() not in ("desktop", "backend", "ci", "all", "misc"):
            return _normalize_id(scope)

    # 2. SDD-XXX explícito
    sdd_m = _SDD_PATTERN.search(subject)
    if sdd_m:
        sdd_id = sdd_m.group(1).strip("-_")
        return _normalize_id("sdd-" + sdd_id)

    # 3. Fase explícita — gerar ID composto com o nome descritivo
    fase_m = _FASE_PATTERN.search(subject)
    if fase_m:
        num = (fase_m.group(1) or fase_m.group(2)).replace(".", "-")
        # Extrair palavras-chave do subject para diferenciar features da mesma fase
        keywords = re.sub(r"[Ff]ase\s*\d+[\.\d]*|\s*-\s*", " ", subject)
        keywords = re.sub(
            r"(feat|fix|chore|docs|ci|style|perf)(\([^)]+\))?:\s*",
            "",
            keywords,
            flags=re.IGNORECASE,
        )
        keywords = re.sub(
            r"SDD[-_][A-Z0-9\-_]+|\(#\d+\)|#\d+", "", keywords, flags=re.IGNORECASE
        )
        keywords = keywords.strip()
        # Pegar primeiras 3 palavras significativas
        words = [w for w in keywords.split() if len(w) > 2][:3]
        slug = "-".join(words) if words else "feature"
        return _normalize_id(f"fase{num}-{slug}")

    # 4. Feat sem scope — normalizar o subject
    if re.match(r"^feat:", subject, re.IGNORECASE):
        clean = re.sub(r"^feat:\s*", "", subject, flags=re.IGNORECASE)
        clean = re.sub(r"\(#\d+\)|#\d+", "", clean).strip()
        # Pegar primeiras 4 palavras
        words = [w for w in clean.split() if len(w) > 2][:4]
        if words:
            return _normalize_id("-".join(words))

    return None


def _classify_files_to_categories(files: list[str]) -> dict:
    """Classifica arquivos em docs e code_refs."""
    docs = []
    code_refs = []
    for f in files:
        if f.endswith(".md") or "docs/" in f:
            docs.append(f)
        elif f.endswith(
            (".py", ".ts", ".tsx", ".rs", ".toml", ".json", ".yml", ".yaml")
        ):
            # Ignorar arquivos de lock, generated, etc.
            if not any(
                x in f
                for x in [
                    "lock",
                    "node_modules",
                    "__pycache__",
                    ".venv",
                    "dist/",
                    "build/",
                ]
            ):
                code_refs.append(f)
    return {"docs": docs, "code_refs": code_refs}


# ── Feature merger ────────────────────────────────────────────────────────────


def _merge_into(
    features: dict[str, GitFeature], feat_id: str, commit: dict, files: dict
):
    """Adiciona ou atualiza uma feature no dicionário."""
    if feat_id not in features:
        features[feat_id] = GitFeature(
            id=feat_id,
            name=_name_from_subject(commit["subject"]),
            phase=_extract_phase(commit["subject"]),
            status="done",  # se tem commit, está feito
            docs=files["docs"][:],
            code_refs=files["code_refs"][:],
            last_commit=commit["hash"][:12],
            first_commit=commit["hash"][:12],
            created_at=commit["date"],
            updated_at=commit["date"],
        )
    else:
        feat = features[feat_id]
        # Atualizar: o commit mais recente win (commits vêm do mais novo para o mais antigo)
        if not feat.last_commit:
            feat.last_commit = commit["hash"][:12]
        feat.first_commit = commit["hash"][
            :12
        ]  # sempre sobrescrever (vai para o mais antigo)
        feat.created_at = commit["date"]  # mais antigo = data de criação

        # Merge de arquivos
        for d in files["docs"]:
            if d not in feat.docs:
                feat.docs.append(d)
        for r in files["code_refs"]:
            if r not in feat.code_refs:
                feat.code_refs.append(r)


# ── SDDs do filesystem ────────────────────────────────────────────────────────


def enrich_with_sdds(features: dict[str, GitFeature]) -> None:
    """
    Lê todos os SDDs do filesystem e os vincula às features existentes.
    Cria features para SDDs que o git não capturou (SDDs sem commit rastreável).
    """
    sdd_dirs = [
        _PROJECT_ROOT / "docs" / "sdd",
        _PROJECT_ROOT / "docs" / "architecture",
        _PROJECT_ROOT / "docs" / "governance",
        _PROJECT_ROOT / "docs" / "ci-cd",
        _PROJECT_ROOT / "docs" / "security",
        _PROJECT_ROOT / "docs" / "monitoring",
        _PROJECT_ROOT / "docs" / "guides",
        _PROJECT_ROOT / ".opencode" / "plans",
    ]

    for sdd_dir in sdd_dirs:
        if not sdd_dir.exists():
            continue
        for md_file in sdd_dir.rglob("*.md"):
            try:
                rel_path = md_file.relative_to(_PROJECT_ROOT).as_posix()
                content = md_file.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            # Extrair ID do frontmatter
            sdd_id = md_file.stem
            if content.strip().startswith("---"):
                try:
                    import yaml

                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        meta = yaml.safe_load(parts[1])
                        if meta and "id" in meta:
                            sdd_id = str(meta["id"])
                except Exception:
                    pass

            feat_id = _normalize_id(sdd_id)
            if len(feat_id) < 2:
                continue

            # Tentar vincular a feature existente por similaridade
            matched = False
            feat_id_clean = feat_id.replace("-", "")
            for fid, feat in features.items():
                fid_clean = fid.replace("-", "")
                if (feat_id_clean in fid_clean or fid_clean in feat_id_clean) and len(
                    feat_id_clean
                ) >= 3:
                    if rel_path not in feat.docs:
                        feat.docs.append(rel_path)
                    matched = True
                    break

            # SDD sem feature correspondente → criar feature nova
            if not matched:
                title_m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                name = (
                    title_m.group(1).strip()
                    if title_m
                    else _normalize_id(sdd_id).replace("-", " ").title()
                )
                name = re.sub(r"\*+|`+", "", name).strip()[:80]

                phase = "Fase 1"
                status_m = re.search(
                    r"status:\s*(done|approved|in.progress|planned|wip)",
                    content,
                    re.IGNORECASE,
                )
                if status_m:
                    s = status_m.group(1).lower()
                    status = (
                        "done"
                        if s in ("done", "approved")
                        else (
                            "in-progress"
                            if "progress" in s or "wip" in s
                            else "planned"
                        )
                    )
                else:
                    status = "done" if "docs/sdd" in rel_path else "in-progress"

                features[feat_id] = GitFeature(
                    id=feat_id,
                    name=name,
                    phase=phase,
                    status=status,
                    docs=[rel_path],
                    code_refs=[],
                    created_at=datetime.now(timezone.utc).isoformat(),
                    updated_at=datetime.now(timezone.utc).isoformat(),
                )


# ── Main ──────────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="Gera features-index.json a partir do histórico git + SDDs"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Não salva, apenas mostra o resultado"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Mostra todas as features e seus arquivos",
    )
    parser.add_argument(
        "--max-commits",
        type=int,
        default=500,
        help="Máximo de commits a analisar (default: 500)",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("K.A.O.S — Feature Registry Bootstrap via Git History")
    print("=" * 60)
    print(f"[git] Repositório: {_PROJECT_ROOT}")

    # Verificar se estamos num repo git
    if not (_PROJECT_ROOT / ".git").exists():
        print("[ERROR] Diretório não é um repositório git.")
        return 1

    # 1. Carregar todos os commits
    print(f"\n[1/4] Lendo commits (máx: {args.max_commits})...")
    commits = get_all_commits(args.max_commits)
    print(f"      -> {len(commits)} commits encontrados")

    # 2. Extrair features dos commits
    print("\n[2/4] Extraindo features do histórico git...")
    features: dict[str, GitFeature] = {}
    skipped = 0
    processed = 0

    for i, commit in enumerate(commits):
        feat_id = _extract_feature_id_from_commit(commit)
        if not feat_id:
            skipped += 1
            continue

        # Obter arquivos modificados neste commit
        files = {"docs": [], "code_refs": []}
        if not args.dry_run or args.verbose:
            changed = get_files_changed_in_commit(commit["hash"])
            files = _classify_files_to_categories(changed)

        _merge_into(features, feat_id, commit, files)
        processed += 1

        if args.verbose:
            print(f"  [{i + 1:3d}] {commit['hash'][:8]} -> {feat_id}")

    print(f"      -> {processed} commits processados, {skipped} ignorados")
    print(f"      -> {len(features)} features únicas extraídas do git")

    # 3. Enriquecer com SDDs do filesystem
    print("\n[3/4] Correlacionando SDDs do filesystem...")
    before_count = len(features)
    enrich_with_sdds(features)
    new_from_sdds = len(features) - before_count
    print(f"      -> {new_from_sdds} features adicionais de SDDs não rastreados no git")

    # 4. Estatísticas e output
    total = len(features)
    sorted_features = sorted(features.values(), key=lambda f: (f.phase, f.id))

    with_docs = sum(1 for f in sorted_features if f.docs)
    with_code = sum(1 for f in sorted_features if f.code_refs)
    by_status = {}
    by_phase = {}
    for f in sorted_features:
        by_status[f.status] = by_status.get(f.status, 0) + 1
        by_phase[f.phase] = by_phase.get(f.phase, 0) + 1

    print(f"\n{'=' * 60}")
    print("[4/4] Resultado Final")
    print(f"{'=' * 60}")
    print(f"  Total features:       {total}")
    print(f"  Com documentação:     {with_docs} ({with_docs / total * 100:.0f}%)")
    print(f"  Com código rastreado: {with_code} ({with_code / total * 100:.0f}%)")
    print("\n  Por status:")
    for status, count in sorted(by_status.items()):
        print(f"    {status:15}: {count:3d}")
    print("\n  Por fase:")
    for phase, count in sorted(by_phase.items(), key=lambda x: x[0]):
        print(f"    {phase:12}: {count:3d}")

    projected_coverage = (with_docs / total * 100) if total > 0 else 0
    print(f"\n  Coverage projetada:   {projected_coverage:.1f}%")
    if projected_coverage >= 50:
        print("  [OK] Drift check deverá passar (threshold 15% OK)")
    elif projected_coverage >= 15:
        print("  [WARN] Coverage limítrofe — adicionar mais docs refs")
    else:
        print("  [FAIL] Coverage baixa — pode haver problema no drift check")

    if args.verbose:
        print(f"\n{'=' * 60}")
        print("  Todas as features:")
        for feat in sorted_features:
            print(
                f"  {feat.id:55} | {feat.phase:10} | {feat.status:12} | "
                f"docs={len(feat.docs):2d} refs={len(feat.code_refs):2d} | {feat.last_commit}"
            )

    if args.dry_run:
        print("\n[dry-run] Nenhum arquivo salvo.")
        return 0

    # Salvar
    registry_path = RuntimePathResolver.features_index_path()
    registry_path.parent.mkdir(parents=True, exist_ok=True)

    output = {
        "version": "2.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generated_by": "bootstrap_feature_registry.py (git-history strategy)",
        "source": "git-log + filesystem-sdds",
        "total_features": total,
        "features": [f.to_dict() for f in sorted_features],
    }

    with open(registry_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n[OK] Salvo em: {registry_path}")
    print(f"   {total} features registradas a partir do git history")
    return 0


if __name__ == "__main__":
    sys.exit(main())
