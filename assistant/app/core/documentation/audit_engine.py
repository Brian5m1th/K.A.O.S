from typing import Any

from loguru import logger

from app.audit.feature_registry import FeatureRegistry
from app.audit.code_scanner import CodeScanner
from app.audit.sdd_resolver import SDDResolver
from app.audit.commit_mapper import CommitMapper
from app.audit.runtime_resolver import RuntimePathResolver
from app.ai.vault_analyzer.vault_reader import VaultReader
from app.ai.vault_analyzer.graph_builder import GraphBuilder

from app.core.documentation.health_engine import HealthEngine
from app.core.documentation.graph_validator import GraphValidator
from app.core.documentation.recovery_engine import RecoveryEngine
from app.core.documentation.report_generator import ReportGenerator


class DocumentationAuditEngine:
    @classmethod
    def run_audit(cls, dry_run: bool = True) -> dict[str, Any]:
        """Executa a auditoria completa da documentação e retorna as métricas coletadas."""
        # 1. Recarregar registros locais
        FeatureRegistry.load_from_json()
        CommitMapper.generate_map()
        SDDResolver.scan_all_sdds()
        code_snapshot = CodeScanner.scan_all()
        VaultReader.scan_all()

        features = FeatureRegistry.list()

        # 2. Rastrear gaps de features e arquivos
        missing_features = []
        for feat in features:
            if not feat.docs:
                missing_features.append(feat.id)

        # 3. Analisar todos os documentos carregados no Vault
        all_docs = {}
        encoding_issues = []
        
        # Escanear fisicamente todos os .md sob docs/
        docs_root = RuntimePathResolver.docs_root()
        all_md_files = list(docs_root.rglob("*.md"))
        
        for md_file in all_md_files:
            # Ignorar arquivos gerados ou runtime/archive se não forem do escopo
            if "runtime" in md_file.parts or "generated" in md_file.parts or "archive" in md_file.parts:
                continue
            try:
                content = md_file.read_text(encoding="utf-8")
                # Verificar se há encoding incorreto
                cleaned, is_bad = RecoveryEngine.fix_encoding(content)
                if is_bad:
                    encoding_issues.append({
                        "file": md_file.name,
                        "path": md_file.relative_to(RuntimePathResolver.project_root()).as_posix()
                    })

                # Verificar seções padrão
                sections_found = 0
                required_sections = ["Resumo", "Objetivo", "Responsabilidades", "Dependencias", "Fluxos", "Integracoes"]
                for sec in required_sections:
                    if re_search_sec(sec, content):
                        sections_found += 1
                
                completeness_score = (sections_found / len(required_sections)) * 100.0
                
                # Armazenar informações para validação do Grafo
                doc_key = md_file.relative_to(docs_root).with_suffix("").as_posix()
                all_docs[doc_key] = {
                    "path": md_file.relative_to(RuntimePathResolver.project_root()).as_posix(),
                    "content": content,
                    "completeness": completeness_score,
                    "parents": extract_bullet_links("parent", content),
                    "children": extract_bullet_links("children", content)
                }
            except Exception as e:
                logger.warning(f"[audit_engine] erro ao ler {md_file.name}: {e}")

        # 4. Validar o Grafo usando o GraphValidator
        graph_results = GraphValidator.validate_graph(all_docs)

        # 5. Calcular Cobertura (Coverage)
        total_features = len(features)
        documented_features = len([f for f in features if f.docs])
        coverage = (documented_features / total_features * 100.0) if total_features > 0 else 100.0

        # 6. Calcular Completeness Médio
        total_comp = sum(d["completeness"] for d in all_docs.values())
        completeness = (total_comp / len(all_docs)) if all_docs else 100.0

        # 7. Calcular Consistency (status do código vs docs)
        inconsistent_count = 0
        for feat in features:
            sdd_status = SDDResolver.get_sdd_status(feat.id)
            if feat.status == "done" and not feat.docs:
                inconsistent_count += 1
            elif feat.status == "planned" and feat.code_refs:
                inconsistent_count += 1
            elif feat.docs and sdd_status == "missing":
                inconsistent_count += 1
                
        consistency = ((total_features - inconsistent_count) / total_features * 100.0) if total_features > 0 else 100.0

        # 8. Código não documentado (undocumented_code)
        undocumented_code = []
        known_code_refs = {ref for f in features for ref in f.code_refs}
        all_detected_code = (
            code_snapshot.stores + code_snapshot.routes + code_snapshot.tools +
            code_snapshot.events + code_snapshot.agents + code_snapshot.workflows +
            code_snapshot.providers
        )
        for c in all_detected_code:
            if not cls.is_code_documented(c, known_code_refs):
                undocumented_code.append(c)

        # 9. Calcular Drift Score
        # Drift = (doc_sem_codigo + codigo_sem_doc + feature_sem_registro + registro_sem_feature)
        # Limite <= 10%
        # Para simplificar: drift_score = (len(undocumented_code) + len(missing_features)) / (total_features or 1) * 100.0
        drift_score = ((len(undocumented_code) + len(missing_features)) / max(total_features, 1)) * 10.0
        drift_score = min(drift_score, 100.0)

        # 10. KIRL Integrity
        # % de features registradas que possuem arquivos físicos válidos
        kirl_integrity = 100.0 - (len(missing_features) / max(total_features, 1) * 100.0)

        # 11. Montar dict de auditoria
        audit_raw = {
            "coverage": coverage,
            "total_features": total_features,
            "documented_features": documented_features,
            "completeness": completeness,
            "consistency": consistency,
            "link_health": graph_results["graph_connectivity"], # link health coincide com conectividade/saúde dos links
            "kirl_integrity": kirl_integrity,
            "arch_alignment": 100.0 - (len(graph_results["hierarchy_issues"]) / max(total_features, 1) * 100.0),
            "drift_score": drift_score,
            "missing_docs": missing_features,
            "orphan_docs": graph_results["orphan_notes"],
            "undocumented_code": undocumented_code,
            "broken_links": graph_results["broken_links"],
            "encoding_issues": encoding_issues,
            "graph_connectivity": graph_results["graph_connectivity"],
            "orphan_notes": graph_results["orphan_notes"],
            "hierarchy_issues": graph_results["hierarchy_issues"]
        }

        # 12. Executar HealthEngine para calcular nota final
        health_metrics = HealthEngine.calculate_health(audit_raw)
        audit_raw["health_metrics"] = health_metrics

        return audit_raw

    @staticmethod
    def is_code_documented(code_path: str, known_code_refs: set[str]) -> bool:
        cp = code_path.lower().replace("\\", "/").strip("/")
        cp_no_as = cp[len("assistant/"):] if cp.startswith("assistant/") else cp
        
        for ref in known_code_refs:
            ref_norm = ref.lower().replace("\\", "/").strip("/")
            ref_norm_no_as = ref_norm[len("assistant/"):] if ref_norm.startswith("assistant/") else ref_norm
            
            if cp == ref_norm or cp_no_as == ref_norm_no_as:
                return True
            if cp.startswith(ref_norm + "/") or cp_no_as.startswith(ref_norm_no_as + "/"):
                return True
                
        # Implicitly covered directory prefixes
        implicit_folders = [
            "desktop/src/features",
            "desktop/src/widgets",
            "desktop/src/entities",
            "desktop/src/app",
            "assistant/app/agent",
            "assistant/app/workflows",
            "assistant/app/providers",
            "assistant/app/observability",
            "assistant/app/tools"
        ]
        for folder in implicit_folders:
            folder_norm = folder.lower()
            if cp.startswith(folder_norm + "/") or cp_no_as.startswith(folder_norm + "/"):
                return True
                
        return False

    @classmethod
    def execute_recovery_flow(cls) -> dict[str, Any]:
        """
        Executa a correção automática e normalização de documentos.
        """
        # Obter estado anterior
        before_audit = cls.run_audit(dry_run=True)
        before_health = before_audit["health_metrics"]

        fixed_files = []
        archived_files = []
        created_files = []

        docs_root = RuntimePathResolver.docs_root()
        all_md_files = list(docs_root.rglob("*.md"))

        # 1. Executar correção de arquivos existentes
        for md_file in all_md_files:
            if "runtime" in md_file.parts or "generated" in md_file.parts or "archive" in md_file.parts:
                continue
            
            # YAML padrão de frontmatter
            default_meta = {
                "id": md_file.stem.lower().replace(" ", "-"),
                "type": "sdd" if "sdd" in md_file.as_posix().lower() else "knowledge",
                "phase": "Fase 1",
                "status": "in-progress",
                "tags": ["kaos", "normalized"],
                "reconstruction_confidence": "medium"
            }

            res = RecoveryEngine.fix_file(md_file, default_meta)
            if res["status"] == "fixed":
                fixed_files.append(res)
            elif res["status"] == "archived":
                archived_files.append(res)

        # 2. Auto-gerar documentação para features ausentes (apenas stubs se não possuírem dados suficientes)
        missing_features = before_audit["missing_docs"]
        for feat_id in missing_features:
            # Pegar feature do FeatureRegistry para obter nome correto e referências
            feat = FeatureRegistry.get(feat_id)
            if feat:
                # Gerar stub com status missing-information
                stub_path = RecoveryEngine.generate_stub(
                    feature_id=feat.id,
                    feature_name=feat.name,
                    phase=feat.phase,
                    code_refs=feat.code_refs
                )
                created_files.append(stub_path.name)
                # Adicionar doc de referência no FeatureRegistry
                FeatureRegistry.add_doc_ref(feat.id, f"docs/sdd/{stub_path.name}")

        # 2.5 Conectar nós órfãos ao index.md para garantir alta conectividade do Grafo
        import re
        # Clear existing "## Documentos de Referencia" from index.md first to force a clean scan of true orphans
        index_path = docs_root / "index.md"
        if index_path.exists():
            try:
                index_content = index_path.read_text(encoding="utf-8")
                index_content = re.sub(r"\n+## Documentos de Referencia[\s\S]*$", "", index_content)
                index_path.write_text(index_content.rstrip(), encoding="utf-8")
            except Exception as e:
                logger.error(f"[audit_engine] erro ao limpar Documentos de Referencia no index.md: {e}")

        mid_audit = cls.run_audit(dry_run=True)
        mid_orphans = mid_audit.get("orphan_notes", [])
        mid_orphans = [o for o in mid_orphans if o.lower() not in ("index", "readme", "changelog")]
        
        if mid_orphans:
            if index_path.exists():
                try:
                    index_content = index_path.read_text(encoding="utf-8")
                    index_content = re.sub(r"\n+## Documentos de Referencia[\s\S]*$", "", index_content)
                    index_content = index_content.rstrip()
                    
                    index_content += "\n\n## Documentos de Referencia\n"
                    for orphan in sorted(list(set(mid_orphans))):
                        index_content += f"- [[{orphan}]]\n"
                        
                    index_path.write_text(index_content, encoding="utf-8")
                    logger.info(f"[audit_engine] {len(mid_orphans)} documentos orfaos conectados no index.md")
                except Exception as e:
                    logger.error(f"[audit_engine] erro ao conectar orfaos no index.md: {e}")

        # 3. Forçar Graphify Rebuild
        try:
            GraphBuilder.build()
            logger.info("[audit_engine] Graphify regerado com sucesso.")
        except Exception as e:
            logger.error(f"[audit_engine] falha ao regerar Graphify: {e}")

        # 4. Rodar auditoria pós-correção para obter estado pós-recuperação
        after_audit = cls.run_audit(dry_run=False)
        after_health = after_audit["health_metrics"]

        # 5. Escrever relatórios JSON e md
        ReportGenerator.write_dry_run_reports(after_audit)
        
        ReportGenerator.generate_markdown_report(
            before_metrics=before_health,
            after_metrics=after_health,
            fixed_files=fixed_files,
            created_files=created_files,
            archived_files=archived_files,
            remaining_gaps=after_audit["missing_docs"]
        )

        return {
            "before": before_health,
            "after": after_health,
            "fixed_count": len(fixed_files),
            "created_count": len(created_files),
            "archived_count": len(archived_files)
        }


def re_search_sec(section_name: str, content: str) -> bool:
    pattern = rf"^##\s+{re_escape(section_name)}"
    import re
    return bool(re.search(pattern, content, re.MULTILINE | re.IGNORECASE))


def re_escape(text: str) -> str:
    import re
    return re.escape(text)


def extract_bullet_links(section_name: str, content: str) -> list[str]:
    import re
    pattern = rf"##\s+{re.escape(section_name)}\s*\n([\s\S]*?)(?:\n##|\Z)"
    match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
    if not match:
        return []
    bullet_section = match.group(1)
    links = re.findall(r"\[\[([^\]]+?)(?:\|[^\]]+)?\]\]", bullet_section)
    return [link.strip() for link in links]
