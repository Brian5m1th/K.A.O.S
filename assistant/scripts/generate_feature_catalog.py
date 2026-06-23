#!/usr/bin/env python3
"""
Gera o Feature Catalog a partir do Feature Registry.

Le features-index.json e produz docs/features/FEATURE_CATALOG.md.

Uso:
    python assistant/scripts/generate_feature_catalog.py
"""

import json
from datetime import datetime
from pathlib import Path

from app.audit.runtime_resolver import RuntimePathResolver


REGISTRY_PATH = RuntimePathResolver.features_index_path()
OUTPUT_PATH = Path("docs/features/FEATURE_CATALOG.md")


def load_registry(path: Path) -> dict:
    if not path.exists():
        print(f"[catalog] ERRO: registry nao encontrado em {path}")
        print("[catalog] Execute uma auditoria primeiro.")
        return {"features": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_catalog(data: dict) -> str:
    features = data.get("features", [])
    total = len(features)
    documented = sum(1 for f in features if f.get("docs"))
    coverage = (documented / total * 100) if total > 0 else 0

    lines = []
    lines.append("# Catalogo de Features — K.A.O.S")
    lines.append("")
    lines.append(
        f"*Gerado automaticamente em {datetime.now().strftime('%Y-%m-%d %H:%M')}*"
    )
    lines.append("")
    lines.append("## Resumo")
    lines.append("")
    lines.append("| Metrica | Valor |")
    lines.append("|---------|-------|")
    lines.append(f"| Total de features | {total} |")
    lines.append(f"| Documentadas | {documented} |")
    lines.append(f"| Cobertura | {coverage:.1f}% |")
    lines.append("")

    phases = {}
    for f in features:
        phase = f.get("phase", "sem-fase")
        if phase not in phases:
            phases[phase] = []
        phases[phase].append(f)

    for phase in sorted(phases.keys()):
        phase_features = phases[phase]
        lines.append(f"## {phase}")
        lines.append("")
        lines.append("| ID | Nome | Status | Documentacao | Ultimo Commit |")
        lines.append("|----|------|--------|-------------|---------------|")

        for f in sorted(phase_features, key=lambda x: x.get("name", "")):
            fid = f.get("id", "")
            name = f.get("name", "")
            status = f.get("status", "unknown")
            docs = ", ".join(f.get("docs", [])) if f.get("docs") else "⚠ Nenhum"
            commit = f.get("lastCommit", "")[:8] if f.get("lastCommit") else "-"
            lines.append(f"| `{fid}` | {name} | {status} | {docs} | `{commit}` |")

        lines.append("")

    lines.append("---")
    lines.append("*Gerado automaticamente pelo KIRL FeatureRegistry.*")

    return "\n".join(lines)


def main():
    data = load_registry(REGISTRY_PATH)
    catalog = generate_catalog(data)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(catalog, encoding="utf-8")
    print(f"[catalog] Catalogo gerado: {OUTPUT_PATH}")
    print(
        f"[catalog] {len(data.get('features', []))} features, "
        f"{sum(1 for f in data.get('features', []) if f.get('docs'))} documentadas"
    )


if __name__ == "__main__":
    main()
