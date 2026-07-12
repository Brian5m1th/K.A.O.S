#!/usr/bin/env python
"""
Graphify → Obsidian Export

Exporta o grafo do Graphify para formato compatível com Obsidian (wiki-links).
Gera arquivos .md por nó/arquivo com links wiki [[...]].

Uso:
    python scripts/export-graphify-obsidian.py --output vault/
    python scripts/export-graphify-obsidian.py --output ~/Documents/ObsidianVault --format obsidian
"""

import json
import argparse
from pathlib import Path
from typing import Optional

from loguru import logger


def export_to_obsidian(graph_path: Path, output_dir: Path, format: str = "obsidian"):
    """Exporta graphify-out/graph.json para formato Obsidian."""
    
    if not graph_path.exists():
        logger.error(f"Graph file not found: {graph_path}")
        return False
    
    with open(graph_path, "r", encoding="utf-8") as f:
        graph = json.load(f)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Agrupar nós por arquivo
    files = {}
    for node in graph.get("nodes", []):
        source_file = node.get("source_file", "")
        if not source_file:
            continue
        
        if source_file not in files:
            files[source_file] = {
                "nodes": [],
                "edges": [],
            }
        
        files[source_file]["nodes"].append(node)
    
    # Agrupar edges
    for link in graph.get("links", []):
        source = link.get("source", "")
        target = link.get("target", "")
        relation = link.get("relation", "uses")
        
        # Encontrar arquivo do source
        for node in graph.get("nodes", []):
            if node.get("id") == source:
                source_file = node.get("source_file", "")
                if source_file and source_file in files:
                    files[source_file]["edges"].append({
                        "source": source,
                        "target": target,
                        "relation": relation,
                    })
                break
    
    # Gerar arquivos .md
    generated = 0
    for file_path, data in files.items():
        if not data["nodes"]:
            continue
        
        # Criar nome do arquivo
        rel_path = Path(file_path)
        md_name = rel_path.stem + ".md"
        md_path = output_dir / md_name
        
        # Garantir diretório
        md_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Gerar conteúdo
        lines = [
            f"# {rel_path}",
            "",
            "## Símbolos",
            "",
        ]
        
        for node in data["nodes"]:
            node_id = node.get("id", "")
            label = node.get("label", "")
            node_type = node.get("type", "code")
            lines.append(f"- [[{node_id}]] — {node_type}: {label}")
        
        if data["edges"]:
            lines.extend(["", "## Dependências", ""])
            for edge in data["edges"]:
                lines.append(f"- [[{edge['source']}]] → `{edge['relation']}` → [[{edge['target']}]]")
        
        content = "\n".join(lines)
        md_path.write_text(content, encoding="utf-8")
        generated += 1
    
    # Index file
    index_path = output_dir / "index.md"
    index_lines = [
        "# Knowledge Graph Index",
        "",
        f"Generated from Graphify ({len(files)} files, {sum(len(d['nodes']) for d in files.values())} symbols)",
        "",
        "## Files",
        "",
    ]
    
    for file_path in sorted(files.keys()):
        rel = Path(file_path)
        index_lines.append(f"- [[{rel.stem}]] — {file_path}")
    
    (output_dir / "index.md").write_text("\n".join(index_lines), encoding="utf-8")
    
    logger.info(f"Exported {generated} files to {output_dir}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Export Graphify graph to Obsidian format")
    parser.add_argument(
        "--graph",
        default="graphify-out/graph.json",
        help="Path to graphify-out/graph.json",
    )
    parser.add_argument(
        "--output",
        default="vault/",
        help="Output directory for Obsidian vault",
    )
    parser.add_argument(
        "--format",
        choices=["obsidian", "wiki", "markdown"],
        default="obsidian",
        help="Output format",
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
    
    graph_path = Path(args.graph)
    output_dir = Path(args.output)
    
    if export_to_obsidian(graph_path, output_dir, args.format):
        print(f"✅ Exportado para {args.output}")
    else:
        print("❌ Falha na exportação")
        sys.exit(1)


if __name__ == "__main__":
    import sys
    main()