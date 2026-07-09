import os
import re
from pathlib import Path
import yaml
import json

def scan_docs():
    docs_dir = Path("docs")
    if not docs_dir.exists():
        print(f"Error: docs directory not found at {docs_dir.absolute()}")
        return

    all_md_files = list(docs_dir.rglob("*.md"))
    print(f"Found {len(all_md_files)} markdown files in total.")

    # Create mapping for wiki links validation
    name_to_file = {}
    for path in all_md_files:
        stem = path.stem.strip().lower()
        name_to_file[stem] = path
        # also map with full filename lower
        name_to_file[path.name.lower()] = path

    broken_links = []
    double_frontmatter = []
    missing_frontmatter = []
    missing_fields = []
    placeholders = []
    tag_issues = []
    valid_files_count = 0

    for path in all_md_files:
        # Ignore files inside .git directory if any
        if ".git" in path.parts:
            continue
            
        rel_path = path.relative_to(docs_dir).as_posix()
        try:
            content = path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Error reading {rel_path}: {e}")
            continue

        # 1. Frontmatter Analysis
        # Count lines that consist exactly of "---" (after trimming whitespace and potential BOM)
        lines = content.splitlines()
        dash_lines_indices = []
        for idx, line in enumerate(lines):
            # Clean BOM and whitespace
            cleaned = line.replace('\ufeff', '').strip()
            if cleaned == "---":
                dash_lines_indices.append(idx)

        has_fm = False
        meta = {}
        
        # A valid frontmatter starts at line 0 (or line 1 if first line is empty)
        # and ends at some later index.
        first_line_clean = lines[0].replace('\ufeff', '').strip() if len(lines) > 0 else ""
        second_line_clean = lines[1].replace('\ufeff', '').strip() if len(lines) > 1 else ""
        
        starts_with_fm = (first_line_clean == "---") or (first_line_clean == "" and second_line_clean == "---")
        
        if starts_with_fm and len(dash_lines_indices) >= 2:
            has_fm = True
            fm_start = dash_lines_indices[0]
            fm_end = dash_lines_indices[1]
            fm_text = "\n".join(lines[fm_start+1:fm_end])
            try:
                meta = yaml.safe_load(fm_text) or {}
            except Exception as e:
                print(f"YAML parsing error in {rel_path}: {e}")
                meta = {}
        else:
            missing_frontmatter.append(rel_path)

        # 2. Check for duplicate/double frontmatter
        has_double_fm = False
        if has_fm:
            fm2_start = -1
            for idx in range(fm_end + 1, len(lines)):
                line_clean = lines[idx].replace('\ufeff', '').strip()
                if line_clean == "---":
                    between_text = "\n".join(lines[fm_end+1:idx]).replace('\ufeff', '').strip()
                    if between_text == "":
                        fm2_start = idx
                        break
                    else:
                        break
            if fm2_start != -1:
                for idx in range(fm2_start + 1, len(lines)):
                    line_clean = lines[idx].replace('\ufeff', '').strip()
                    if line_clean == "---":
                        has_double_fm = True
                        break
        
        if has_double_fm:
            double_frontmatter.append(rel_path)

        # 3. Check frontmatter fields
        if has_fm:
            required_fields = ["id", "type", "status", "tags"]
            missing = [f for f in required_fields if f not in meta]
            if missing:
                missing_fields.append((rel_path, missing))

            # Check tags specifically
            tags = meta.get("tags")
            if tags is None:
                tag_issues.append((rel_path, "Field 'tags' missing"))
            elif not isinstance(tags, list):
                tag_issues.append((rel_path, f"Field 'tags' is not a list (got {type(tags).__name__})"))
            elif len(tags) == 0:
                tag_issues.append((rel_path, "Field 'tags' is empty list"))
        
        # 4. Check placeholders / outdated text
        placeholders_in_file = []
        # Match word boundaries for TODO, FIXME, TBD, PLACEHOLDER
        for match in re.finditer(r"\b(TODO|FIXME|TBD|PLACEHOLDER)\b", content, re.IGNORECASE):
            # Extract line content
            line_no = content[:match.start()].count("\n") + 1
            placeholders_in_file.append(f"{match.group(0)} (L{line_no})")
            
        # Match empty checkboxes: "- [ ]"
        for match in re.finditer(r"- \[\s\]\s+(.*)", content):
            line_no = content[:match.start()].count("\n") + 1
            desc = match.group(1).strip()
            # truncate description if too long
            if len(desc) > 30:
                desc = desc[:30] + "..."
            placeholders_in_file.append(f"Checkbox: '{desc}' (L{line_no})")

        if placeholders_in_file:
            placeholders.append((rel_path, list(set(placeholders_in_file))))

        # 5. Check wiki links
        # Match [[Target]] or [[Target|Label]]
        wiki_links = re.findall(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]", content)
        for link in wiki_links:
            link_target = link.strip()
            if not link_target:
                continue
            
            link_lower = link_target.lower()
            
            # Skip media attachments
            if any(link_lower.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".gif", ".pdf", ".svg"]):
                continue
                
            # Check if this points to a file that exists
            found = False
            if link_lower in name_to_file:
                found = True
            elif f"{link_lower}.md" in name_to_file:
                found = True
            
            if not found:
                broken_links.append((rel_path, link_target))

    # Generate Markdown Report
    output_report_path = Path("docs/docs-audit-report-summary.md")
    
    report_content = []
    report_content.append("# Relatório de Auditoria de Documentação (K.A.O.S)")
    report_content.append(f"Gerado em: 2026-07-08\n")
    report_content.append(f"Total de arquivos `.md` analisados: **{len(all_md_files)}**\n")
    
    # Section: Summary of Findings
    report_content.append("## Resumo das Inconsistências Encontradas\n")
    report_content.append(f"- ⚠️ **Double Frontmatter (Cabeçalho Duplicado):** {len(double_frontmatter)} arquivos")
    report_content.append(f"- 🚫 **Missing Frontmatter (Sem Cabeçalho):** {len(missing_frontmatter)} arquivos")
    report_content.append(f"- 🔍 **Missing Required Fields (Campos Faltantes):** {len(missing_fields)} arquivos")
    report_content.append(f"- 🏷️ **Tag Issues (Problemas de Tags):** {len(tag_issues)} arquivos")
    report_content.append(f"- 📌 **Placeholders / TODOs:** {len(placeholders)} arquivos")
    report_content.append(f"- 🔗 **Broken Wiki Links (Links Quebrados / Gaps):** {len(broken_links)} links\n")
    
    # Section: Double Frontmatter
    report_content.append("## 1. Double Frontmatter (Cabeçalho Duplicado)")
    report_content.append("Arquivos que contêm mais de um bloco de metadados `---` (geralmente gerado por processos de normalização repetidos).\n")
    if double_frontmatter:
        for f in sorted(double_frontmatter):
            report_content.append(f"- [{f}](file:///c:/workspace/Freelancer/K.A.O.S/docs/{f})")
    else:
        report_content.append("*Nenhum arquivo com cabeçalho duplicado.*")
    report_content.append("")

    # Section: Missing Frontmatter
    report_content.append("## 2. Missing Frontmatter (Sem Cabeçalho)")
    report_content.append("Arquivos sem metadados YAML na primeira linha.\n")
    if missing_frontmatter:
        for f in sorted(missing_frontmatter):
            report_content.append(f"- [{f}](file:///c:/workspace/Freelancer/K.A.O.S/docs/{f})")
    else:
        report_content.append("*Nenhum arquivo sem cabeçalho.*")
    report_content.append("")

    # Section: Missing Fields
    report_content.append("## 3. Missing Required Fields (Campos Faltantes)")
    report_content.append("Campos obrigatórios esperados no frontmatter: `id`, `type`, `status`, `tags`.\n")
    if missing_fields:
        for f, fields in sorted(missing_fields, key=lambda x: x[0]):
            fields_str = ", ".join(f"`{x}`" for x in fields)
            report_content.append(f"- [{f}](file:///c:/workspace/Freelancer/K.A.O.S/docs/{f}) — Faltando: {fields_str}")
    else:
        report_content.append("*Todos os arquivos possuem os campos obrigatórios.*")
    report_content.append("")

    # Section: Tag Issues
    report_content.append("## 4. Tag Issues (Problemas de Tags)")
    report_content.append("Arquivos onde a propriedade `tags` não está preenchida corretamente ou está vazia.\n")
    if tag_issues:
        for f, desc in sorted(tag_issues, key=lambda x: x[0]):
            report_content.append(f"- [{f}](file:///c:/workspace/Freelancer/K.A.O.S/docs/{f}) — {desc}")
    else:
        report_content.append("*Todas as tags estão corretas.*")
    report_content.append("")

    # Section: Placeholders / TODOs
    report_content.append("## 5. Placeholders e Pendências")
    report_content.append("Arquivos contendo marcações de `TODO`, `TBD`, `FIXME`, ou caixas de seleção pendentes.\n")
    if placeholders:
        for f, items in sorted(placeholders, key=lambda x: x[0]):
            items_str = ", ".join(items)
            report_content.append(f"- [{f}](file:///c:/workspace/Freelancer/K.A.O.S/docs/{f}) — {items_str}")
    else:
        report_content.append("*Nenhum placeholder encontrado.*")
    report_content.append("")

    # Section: Broken Wiki Links
    report_content.append("## 6. Links Quebrados (Gaps de Documentação)")
    report_content.append("Referências de links wiki `[[Documento]]` para arquivos que não existem no diretório `docs`.\n")
    if broken_links:
        # Group by file containing the broken link
        by_file = {}
        for f, target in broken_links:
            if f not in by_file:
                by_file[f] = []
            by_file[f].append(target)
            
        for f, targets in sorted(by_file.items()):
            targets_str = ", ".join(f"`[[{x}]]`" for x in sorted(list(set(targets))))
            report_content.append(f"- [{f}](file:///c:/workspace/Freelancer/K.A.O.S/docs/{f}) — Aponta para: {targets_str}")
    else:
        report_content.append("*Nenhum link quebrado encontrado.*")
    report_content.append("")

    out_md = "\n".join(report_content)
    output_report_path.write_text(out_md, encoding="utf-8")
    print(f"Report successfully saved to {output_report_path.absolute()}")

if __name__ == "__main__":
    scan_docs()
