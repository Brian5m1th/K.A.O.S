import re
import shutil
import yaml
from pathlib import Path
from typing import Any
from app.audit.runtime_resolver import RuntimePathResolver

class RecoveryEngine:
    # Mapeamento de encoding UTF-8 com problemas
    ENCODING_REPLACEMENTS = {
        r"Conte\xC3\xBAdo": "Conteudo",
        r"Conte\xc3\xba do": "Conteudo",
        r"Conte\xc3\xbado": "Conteudo",
        r"Ingest\xC3\xA3o": "Ingestao",
        r"Ingest\xc3\xa3o": "Ingestao",
        r"Propaga\xC3\xA7\xC3\xA3o": "Propagacao",
        r"Propaga\xc3\xa7\xc3\xa3o": "Propagacao",
        r"Configura\xC3\xA7\xC3\xA3o": "Configuracao",
        r"Configura\xc3\xa7\xc3\xa3o": "Configuracao",
        r"Configura\xC3\xA7\xC3\xB5es": "Configuracoes",
        r"Configura\xc3\xa7\xc3\xb5es": "Configuracoes",
        r"Otimiza\xC3\xA7\xC3\xA3o": "Otimizacao",
        r"Otimiza\xc3\xa7\xc3\xa3o": "Otimizacao",
        r"Funda\xC3\xA7\xC3\xA3o": "Fundacao",
        r"Funda\xc3\xa7\xc3\xa3o": "Fundacao",
        r"Inten\xC3\xA7\xC3\xB5es": "Intencoes",
        r"Inten\xc3\xa7\xc3\xb5es": "Intencoes",
        r"Integra\xC3\xA7\xC3\xB5es": "Integracoes",
        r"Integra\xc3\xa7\xc3\xb5es": "Integracoes",
        r"Sem\xC3\xA2ntico": "Semantico",
        r"Sem\xc3\xa2ntico": "Semantico",
        r"Especifica\xC3\xA7\xC3\xA3o": "Especificacao",
        r"Especifica\xc3\xa7\xc3\xa3o": "Especificacao",
        r"Especifica\xC3\xA7\xC3\xB5es": "Especificacoes",
        r"Especifica\xc3\xa7\xc3\xb5es": "Especificacoes",
        r"T\xC3\xA9cnica": "Tecnica",
        r"T\xc3\xa9cnica": "Tecnica",
        r"Mem\xC3\xB3ria": "Memoria",
        r"Mem\xc3\xb3ria": "Memoria",
        r"Vis\xC3\xA3o": "Visao",
        r"Vis\xc3\xa3o": "Visao",
        r"\xC3\xA3": "ao",
        r"\xc3\xa3": "ao",
        r"\xC3\xBA": "u",
        r"\xc3\xba": "u",
        r"\xC3\xB3": "o",
        r"\xc3\xb3": "o",
        r"\xC3\xA9": "e",
        r"\xc3\xa9": "e",
        r"\xC3\xAD": "i",
        r"\xc3\xad": "i",
        r"\xC3\xA7": "c",
        r"\xc3\xa7": "c",
        r"\xC3\x89": "E",
        r"\xc3\x89": "E",
        r"\xC3\x93": "O",
        r"\xc3\x93": "O",
        r"\xC3\x8D": "I",
        r"\xc3\x8d": "I",
        r"\xC3\x81": "A",
        r"\xc3\x81": "A"
    }

    @classmethod
    def is_protected(cls, path: Path, content: str) -> bool:
        """Verifica se o arquivo é considerado READ-ONLY."""
        path_str = path.as_posix().lower()
        if "readme.md" in path_str:
            return True
        if "kirl_guide.md" in path_str or "sdd-kirl.md" in path_str:
            return True
        if "obsidian_guide.md" in path_str:
            return True
        if "roadmap" in path_str:
            return True
        if "architecture/" in path_str or "arquitetura/" in path_str:
            return True
        if "adr/" in path_str or "adr-" in path_str:
            return True
        
        # Check YAML metadata
        if "status: approved" in content.lower():
            return True
        return False

    @classmethod
    def fix_encoding(cls, content: str) -> tuple[str, bool]:
        """Corrige os caracteres mal codificados."""
        modified = False
        new_content = content
        for bad, good in cls.ENCODING_REPLACEMENTS.items():
            if bad in new_content or bad.lower() in new_content or bad.upper() in new_content:
                # Substituição case-insensitive
                new_content = re.sub(re.escape(bad), good, new_content, flags=re.IGNORECASE)
                modified = True
        return new_content, modified

    @classmethod
    def inject_frontmatter(cls, path: Path, content: str, default_meta: dict) -> tuple[str, bool]:
        """Injeta bloco de frontmatter se estiver ausente ou inválido."""
        if content.strip().startswith("---"):
            return content, False
            
        # Converter default_meta para string yaml
        meta_str = yaml.dump(default_meta, allow_unicode=True, sort_keys=False)
        new_content = f"---\n{meta_str}---\n\n{content}"
        return new_content, True

    @classmethod
    def fix_file(cls, path: Path, default_meta: dict) -> dict[str, Any]:
        """Aplica correções a um arquivo markdown e retorna o status."""
        try:
            content = path.read_text(encoding="utf-8")
        except Exception as e:
            return {"path": str(path), "status": "error", "error": str(e)}

        is_empty = len(content.strip()) < 50
        is_protected = cls.is_protected(path, content)

        # 1. Se estiver vazio/stub inútil e não protegido, categorizar e potencialmente arquivar
        if is_empty and not is_protected:
            # Não remove, move para docs/archive/
            archive_dir = RuntimePathResolver.docs_root() / "archive"
            archive_dir.mkdir(parents=True, exist_ok=True)
            target_path = archive_dir / path.name
            try:
                shutil.move(str(path), str(target_path))
                return {"path": path.name, "status": "archived", "target": str(target_path)}
            except Exception as e:
                return {"path": path.name, "status": "error_archiving", "error": str(e)}

        # 2. Corrigir encoding
        content, encoding_fixed = cls.fix_encoding(content)
        
        # 3. Injetar/Corrigir Frontmatter
        content, frontmatter_fixed = cls.inject_frontmatter(path, content, default_meta)

        # 3.5 Corrigir wikilinks
        content, links_fixed = cls.fix_wikilinks(content, path)

        # 4. Padronização estrutural (apenas para não protegidos)
        structure_fixed = False
        if not is_protected:
            content, structure_fixed = cls.standardize_sections(path.stem, content)

        # Salvar se modificado
        modified = encoding_fixed or frontmatter_fixed or structure_fixed or links_fixed
        if modified:
            try:
                path.write_text(content, encoding="utf-8")
                return {
                    "path": path.name,
                    "status": "fixed",
                    "encoding": encoding_fixed,
                    "frontmatter": frontmatter_fixed,
                    "structure": structure_fixed,
                    "links": links_fixed,
                    "protected": is_protected
                }
            except Exception as e:
                return {"path": path.name, "status": "error_writing", "error": str(e)}

        return {"path": path.name, "status": "unchanged", "protected": is_protected}

    _valid_stems_cache = None

    @classmethod
    def get_valid_stems(cls) -> set[str]:
        if cls._valid_stems_cache is None:
            # Escanear todos os arquivos .md na pasta docs_root
            docs_root = RuntimePathResolver.docs_root()
            stems = set()
            for f in docs_root.rglob("*.md"):
                if "runtime" not in f.parts and "generated" not in f.parts and "archive" not in f.parts:
                    stems.add(f.stem)
            cls._valid_stems_cache = stems
        return cls._valid_stems_cache

    @classmethod
    def fix_wikilinks(cls, content: str, file_path: Path) -> tuple[str, bool]:
        """Corrige e normaliza os wikilinks [[Target]] no conteúdo."""
        valid_stems = cls.get_valid_stems()
        
        # Mapeamento explícito de apelidos/redirecionamentos comuns para nomes reais
        redirections = {
            "00_visao_geral": "Visao Geral",
            "00 visao geral": "Visao Geral",
            "01_estrutura_pastas": "Estrutura de Pastas",
            "01 estrutura pastas": "Estrutura de Pastas",
            "02_fluxo_dados": "Fluxo de Dados",
            "02 fluxo dados": "Fluxo de Dados",
            "backlog": "Backlog do Projeto",
            "concepts/rag": "Busca Vetorial e RAG",
            "concepts/embeddings": "Gerador de Embeddings",
            "concepts/langgraph": "Orquestrador LangGraph",
            "wiki/entities/slug": "AGENTS",
            "entities/brian": "index",
            "entities/kaos": "index",
            "entities/qdrant": "index",
            "sources/2026-06-18_llm_wiki": "index",
            "synthesis/comparacao_mamba_rwkv": "index",
            "links": "index",
            "link": "index",
            "id": "index",
            "id-da-nota": "index",
            "chat-streaming": "SDD-Desktop-Stabilization-F1",
            "event-bus": "SDD-KIRL",
            "tool-schema": "Ferramentas do LangGraph",
            "pagina_inexistente": "index",
            "guia de configuracao": "SETUP",
            "configuracao de provedores": "Configuração de Provedores",
        }
        
        modified = False
        
        def replace_link(match) -> str:
            nonlocal modified
            full_match = match.group(0)
            target = match.group(1).strip()
            
            # Se tiver label [[Target|Label]], separar
            label = ""
            if "|" in target:
                target, label = target.split("|", 1)
                target = target.strip()
                label = label.strip()
                
            # Tratar target vazio
            if not target:
                return full_match
                
            replacement = None
            # 1. Verificar se o target já corresponde exatamente a um arquivo existente (case-insensitive)
            matched = cls._match_stem(target, valid_stems)
            if matched:
                if label:
                    replacement = f"[[{matched}|{label}]]"
                else:
                    replacement = f"[[{matched}]]"
                
            # 2. Verificar na tabela de redirecionamentos
            if not replacement:
                target_lower = target.lower()
                if target_lower in redirections:
                    matched = redirections[target_lower]
                    if label:
                        replacement = f"[[{matched}|{label}]]"
                    else:
                        replacement = f"[[{matched}]]"
                
            # 3. Tentar normalizar acentuação e typos comuns
            if not replacement:
                normalized_target = cls._normalize_target(target)
                matched = cls._match_stem(normalized_target, valid_stems)
                if matched:
                    if label:
                        replacement = f"[[{matched}|{label}]]"
                    else:
                        replacement = f"[[{matched}]]"
                
            # 4. Tratar links combinados/concatenados (e.g. "Padroes de Projeto EstratÉgia de Testes")
            if not replacement:
                split_links = cls._split_combined_link(target, valid_stems, redirections)
                if split_links:
                    replacement = " ".join([f"[[{lnk}]]" for lnk in split_links])
                
            if replacement and replacement != full_match:
                modified = True
                return replacement
                
            return full_match
            
        new_content = re.sub(r"\[\[([^\]]+?)\]\]", replace_link, content)
        return new_content, modified

    @classmethod
    def _normalize_target(cls, target: str) -> str:
        import unicodedata
        # Remove accents
        nfkd_form = unicodedata.normalize('NFKD', target)
        s = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
        
        # Common text adjustments
        s = s.lower()
        repls = {
            "viso geral": "visao geral",
            "visõ geral": "visao geral",
            "visõ": "visao",
            "informacaes": "informacoes",
            "integracaes": "integracoes",
            "orquestraçao": "orquestracao",
            "orquestracao": "orquestracao",
            "seviço": "servico",
            "sevico": "servico",
            "serviço": "servico",
            "copia": "copia",
        }
        for k, v in repls.items():
            s = s.replace(k, v)
        s = re.sub(r'[^a-z0-9 ]', ' ', s)
        s = re.sub(r'\s+', ' ', s).strip()
        return s

    @classmethod
    def _match_stem(cls, target: str, valid_stems: set[str]) -> str | None:
        target_norm = cls._normalize_target(target)
        for stem in valid_stems:
            if stem.lower() == target.lower():
                return stem
            stem_norm = cls._normalize_target(stem)
            if stem_norm == target_norm:
                return stem
        return None

    @classmethod
    def _split_combined_link(cls, target: str, valid_stems: set[str], redirections: dict) -> list[str]:
        target_norm = cls._normalize_target(target)
        
        # Sort valid stems by length descending to match longest first
        sorted_stems = sorted(list(valid_stems), key=len, reverse=True)
        
        matches = []
        remaining = target_norm
        
        extended_targets = []
        for stem in sorted_stems:
            extended_targets.append((cls._normalize_target(stem), stem))
        for redir_k, redir_v in redirections.items():
            extended_targets.append((cls._normalize_target(redir_k), redir_v))
            
        extended_targets.sort(key=lambda x: len(x[0]), reverse=True)
        
        for norm_t, canonical in extended_targets:
            if not norm_t or len(norm_t) < 4:
                continue
            if norm_t in remaining:
                if canonical not in matches:
                    matches.append(canonical)
                remaining = remaining.replace(norm_t, " ")
                
        return matches

    @classmethod
    def standardize_sections(cls, title: str, content: str) -> tuple[str, bool]:
        """Garante a estrutura padrão de seções requisitada."""
        sections = [
            "Resumo", "Objetivo", "Responsabilidades", "Dependencias",
            "Fluxos", "Integracoes", "Arquivos Relacionados",
            "Referencias KIRL", "Status", "Ultima Atualizacao"
        ]
        
        modified = False
        
        # Seções padrão que o projeto exige
        for section in sections:
            pattern = rf"^##\s+{re.escape(section)}"
            if not re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
                # Seção ausente, adicionar ao final
                content = content.rstrip()
                content += f"\n\n## {section}\n- Informações pendentes de validação ou auto-geração.\n"
                modified = True
                
        return content, modified

    @classmethod
    def generate_stub(cls, feature_id: str, feature_name: str, phase: str, code_refs: list[str]) -> Path:
        """Gera um stub para features que não possuem documentação nem relacionamentos suficientes."""
        sdd_dir = RuntimePathResolver.docs_root() / "sdd"
        sdd_dir.mkdir(parents=True, exist_ok=True)
        
        output_path = sdd_dir / f"{feature_id}.md"
        
        frontmatter = {
            "id": feature_id,
            "type": "stub",
            "phase": phase,
            "status": "missing-information",
            "tags": ["stub", "kirl-auto"],
            "reconstruction_confidence": "low",
            "created_at": RuntimePathResolver.resolve().name, # fallback or iso
            "updated_at": RuntimePathResolver.resolve().name
        }
        
        meta_str = yaml.dump(frontmatter, allow_unicode=True, sort_keys=False)
        
        body = f"""# {feature_name}
        
## Resumo
Este documento é um stub gerado automaticamente pelo KIRL Auto-Doc pois a feature `{feature_id}` não possuía documentação correspondente na base de conhecimento.

## Objetivo
Descrever o objetivo funcional e técnico da feature `{feature_id}`.

## Responsabilidades
- Pendente de detalhamento técnico.

## Dependencias
- Código-fonte referenciado: {", ".join([f"`{c}`" for c in code_refs]) or "Nenhum detectado"}.

## Fluxos
- Não mapeados.

## Integracoes
- Não mapeadas.

## Arquivos Relacionados
- Mapear caminhos de código e configurações.

## Referencias KIRL
- ID: `feature:{feature_id}`

## Status
status: missing-information

## Ultima Atualizacao
*Gerado em {RuntimePathResolver.resolve().name}*
"""
        output_path.write_text(f"---\n{meta_str}---\n\n{body}", encoding="utf-8")
        return output_path
