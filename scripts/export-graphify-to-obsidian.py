#!/usr/bin/env python3
"""
Graphify Export to Obsidian Vault

Exporta o graphify-out/graph.json para formato Obsidian (wiki-links + markdown).
"""

import json
import subprocess
import sys
from pathlib import Path
from loguru import logger


def export_graphify_to_obsidian(
    graph_path: Path = Path("graphify-out/graph.json"),
    output_dir: Path = Path("vault"),
    format: str = "wiki",  # "wiki" ou "markdown"
) -> bool:
    """Exporta graphify graph para formato Obsidian."""
    
    try:
        # Método 1: Usar graphify export (se disponível)
        result = subprocess.run(
            ["graphify", "export", "wiki", "--output", str(output_dir)],
            capture_output=True,
            text=True,
            timeout=60,
        )
        
        if result.returncode == 0:
            logger.info(f"Exportado via graphify CLI para {output_dir}")
            return True
        
        logger.warning(f"graphify export falhou: {result.stderr}")
        
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception) as e:
        logger.warning(f"graphify CLI export falhou: {e}")
    
    # Método 2: Parsing manual do graph.json
    try:
        return _manual_export_to_obsidian(graph_path, output_dir)
    except Exception as e:
        logger.error(f"Export manual falhou: {e}")
        return False


def _manual_export_to_obsidian(graph_path: Path, output_dir: Path) -> bool:
    """Export manual do graph.json para formato Obsidian."""
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(graph_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    nodes = data.get("nodes", [])
    links = data.get("links", [])
    
    # Mapear ID -> label
    node_map = {n["id"]: n for n in nodes}
    
    # Criar arquivo por nó
    created = 0
    for node in nodes:
        node_id = node.get("id", "")
        label = node.get("label", node_id)
        source_file = node.get("source_file", "")
        
        if not node_id:
            continue
        
        # Sanitizar nome do arquivo
        safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in label)
        safe_name = safe_name[:100]  # limite
        
        md_path = Path("vault") / f"{safe_name}.md"
        md_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Coletar conexões
        outgoing = [l for l in links if l.get("source") == node_id]
        incoming = [l for l in links if l.get("target") == node_id]
        
        lines = [
            f"# {label}",
            "",
            f"**File:** `{source_file}`",
            f"**Type:** {node.get('file_type', 'unknown')}",
            f"**Degree:** {len(outgoing) + len(incoming)}",
            "",
        ]
        
        if outgoing:
            lines.append("## Outgoing")
            for link in outgoing[:20]:
                target = node_map.get(link.get("target", ""), {})
                target_label = target.get("label", link.get("target", ""))
                rel = link.get("relation", "uses")
                lines.append(f"- [[{target_label}]] — {rel}")
            lines.append("")
        
        if incoming:
            lines.append("## Incoming")
            for link in incoming[:20]:
                source = node_map.get(link.get("source", ""), {})
                source_label = source.get("label", link.get("source", ""))
                rel = link.get("relation", "used by")
                lines.append(f"- [[{source_label}]] — {rel}")
            lines.append("")
        
        content = "\n".join(lines)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(content, encoding="utf-8")
        created += 1
    
    # Index file
    index_path = Path("vault") / "INDEX.md"
    index_content = f"# K.A.O.S Knowledge Graph\n\nTotal nodes: {len(nodes)}\nTotal edges: {len(links)}\n\n"
    index_content += "\n".join(f"- [[{n.get('label', n['id'])}]]" for n in nodes[:50])
    index_path.write_text(index_content, encoding="utf-8")
    
    logger.info(f"✅ Exportado {created} notas para Obsidian em vault/")
    return True


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Export Graphify to Obsidian")
    parser.add_argument(
        "--graph",
        default="graphify-out/graph.json",
        help="Path to graph.json",
    )
    parser.add_argument(
        "-o", "--output",
        default="vault",
        help="Output directory",
    )
    parser.add_argument(
        "--format",
        choices=["wiki", "markdown"],
        default="wiki",
        help="Output format",
    )
    
    args = parser.parse_args()
    
    success = export_graphify_to_obsidian(
        graph_path=Path(args.graph),
        output_dir=Path(args.output),
        format=args.format,
    )
    
    if success:
        logger.info("✅ Export completed")
        sys.exit(0)
    else:
        logger.error("❌ Export failed")
        sys.exit(1)


if __name__ == "__main__":
    main()