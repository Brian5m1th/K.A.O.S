import re
from pathlib import Path
from typing import Any
from app.audit.runtime_resolver import RuntimePathResolver

class GraphValidator:
    @classmethod
    def validate_graph(cls, all_docs: dict[str, dict[str, Any]]) -> dict[str, Any]:
        """
        Valida o grafo de documentação:
        - Links quebrados (referências a notas inexistentes)
        - Backlinks
        - Relações parent/child
        - Conectividade geral (nós órfãos)
        """
        doc_names = set(all_docs.keys())
        broken_links = []
        orphans = []
        connections = {name: {"incoming": set(), "outgoing": set()} for name in doc_names}

        # Parse links e preencher grafo
        for name, info in all_docs.items():
            content = info.get("content", "")
            
            # Extrair wikilinks [[link]]
            wikilinks = re.findall(r"\[\[([^\]]+?)(?:\|[^\]]+)?\]\]", content)
            
            for link in wikilinks:
                link_clean = link.strip()
                # Procurar se a nota existe (case insensitive e com substituição de espaços por hífens/underscores se necessário)
                matched_target = cls._find_match(link_clean, doc_names)
                if matched_target:
                    connections[name]["outgoing"].add(matched_target)
                    connections[matched_target]["incoming"].add(name)
                else:
                    broken_links.append({
                        "source": name,
                        "target": link_clean,
                        "file_path": info.get("path", "")
                    })

        # Detectar nós órfãos (sem entrada e sem saída) e calcular conectividade
        disconnected_count = 0
        for name, conn in connections.items():
            if len(conn["incoming"]) == 0 and len(conn["outgoing"]) == 0:
                orphans.append(Path(name).name)
                disconnected_count += 1
            elif len(conn["incoming"]) == 0:
                # Pode ter links saindo mas nada apontando para ela (órfã parcial de entrada)
                pass

        total_nodes = len(doc_names)
        if total_nodes > 0:
            graph_connectivity = ((total_nodes - disconnected_count) / total_nodes) * 100.0
        else:
            graph_connectivity = 100.0

        # Validar integridade do parent/child
        # Ex: se nota A lista B como parent, B deve ter A listada como child ou pelo menos apontar de volta
        hierarchy_issues = []
        for name, info in all_docs.items():
            parents = info.get("parents", [])
            for p in parents:
                p_match = cls._find_match(p, doc_names)
                if not p_match:
                    hierarchy_issues.append(f"Nota '{name}' refere pai inexistente '{p}'")
                elif p_match not in connections[name]["outgoing"]:
                    # Não há link explícito para o pai no grafo
                    pass

        return {
            "broken_links": broken_links,
            "broken_links_count": len(broken_links),
            "orphan_notes": orphans,
            "orphan_count": len(orphans),
            "hierarchy_issues": hierarchy_issues,
            "graph_connectivity": graph_connectivity,
            "connections": {k: {"incoming": list(v["incoming"]), "outgoing": list(v["outgoing"])} for k, v in connections.items()}
        }

    @classmethod
    def _find_match(cls, target_name: str, doc_names: set[str]) -> str | None:
        """Encontra correspondência insensível a maiúsculas/minúsculas para o nome do documento."""
        target_lower = target_name.lower().strip()
        target_norm = target_lower.replace("-", " ").replace("_", " ").strip()
        
        # 1. Prioritize stem matching
        for name in doc_names:
            name_stem = Path(name).name
            if name_stem.lower().strip() == target_lower:
                return name
            name_stem_norm = name_stem.lower().replace("-", " ").replace("_", " ").strip()
            if name_stem_norm == target_norm:
                return name
                
        # 2. Fallback to full path name matching
        for name in doc_names:
            if name.lower().strip() == target_lower:
                return name
            name_norm = name.lower().replace("-", " ").replace("_", " ").strip()
            if name_norm == target_norm:
                return name
                
        return None
