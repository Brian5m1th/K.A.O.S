import os
import sys
import re
from pathlib import Path
import yaml

def normalize_id(filename):
    # Convert spaces/underscores/dashes to dashes, lower case, strip extension
    s = Path(filename).stem.strip().lower()
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s

def parse_frontmatters(content):
    lines = content.splitlines()
    if not lines:
        return None, None, ""

    def clean(l):
        return l.replace('\ufeff', '').strip()

    # Find where the first frontmatter starts and ends
    first_line_clean = clean(lines[0]) if len(lines) > 0 else ""
    second_line_clean = clean(lines[1]) if len(lines) > 1 else ""
    
    fm1_start = -1
    if first_line_clean == "---":
        fm1_start = 0
    elif first_line_clean == "" and second_line_clean == "---":
        fm1_start = 1

    if fm1_start == -1:
        # No frontmatter at the start
        return None, None, content

    fm1_end = -1
    for idx in range(fm1_start + 1, len(lines)):
        if clean(lines[idx]) == "---":
            fm1_end = idx
            break

    if fm1_end == -1:
        # Invalid first frontmatter (no closing marker)
        return None, None, content

    # Try parsing first frontmatter
    fm1_text = "\n".join(lines[fm1_start+1:fm1_end])
    fm1_meta = {}
    try:
        parsed = yaml.safe_load(fm1_text)
        if isinstance(parsed, dict):
            fm1_meta = parsed
    except Exception:
        pass

    # Check if there is a second frontmatter following immediately
    fm2_start = -1
    fm2_end = -1
    for idx in range(fm1_end + 1, len(lines)):
        line_clean = clean(lines[idx])
        if line_clean == "---":
            # Check if all lines between fm1_end and this line are empty/BOM
            between_text = "\n".join(lines[fm1_end+1:idx]).replace('\ufeff', '').strip()
            if between_text == "":
                fm2_start = idx
                break
            else:
                # Found a "---" but there is content in between, so it's not a duplicate frontmatter block
                break

    if fm2_start != -1:
        for idx in range(fm2_start + 1, len(lines)):
            if clean(lines[idx]) == "---":
                fm2_end = idx
                break

    if fm2_end != -1:
        # Try parsing second frontmatter
        fm2_text = "\n".join(lines[fm2_start+1:fm2_end])
        fm2_meta = {}
        try:
            parsed = yaml.safe_load(fm2_text)
            if isinstance(parsed, dict):
                fm2_meta = parsed
        except Exception:
            pass
        
        # Body starts after second frontmatter end
        body = "\n".join(lines[fm2_end+1:])
        return fm1_meta, fm2_meta, body
    else:
        # Only single frontmatter
        body = "\n".join(lines[fm1_end+1:])
        return fm1_meta, None, body

def fix_metadata(dry_run=False):
    docs_dir = Path("docs")
    if not docs_dir.exists():
        print(f"Error: docs directory not found at {docs_dir.absolute()}")
        return

    all_md_files = list(docs_dir.rglob("*.md"))
    print(f"Found {len(all_md_files)} markdown files to check.")

    modified_count = 0
    gaps_created = 0

    for path in all_md_files:
        # Skip files inside .git directory or runtime registry
        if ".git" in path.parts or "runtime" in path.parts:
            continue

        rel_path = path.relative_to(docs_dir).as_posix()
        try:
            content = path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Error reading {rel_path}: {e}")
            continue

        # Parse frontmatters
        fm1_meta, fm2_meta, body = parse_frontmatters(content)

        is_modified = False
        reason = ""
        meta = {}

        if fm1_meta is not None and fm2_meta is not None:
            # Case A: Double Frontmatter - Merge them
            # Start with fm2_meta (old meta), update with fm1_meta (new normalized meta)
            meta = fm2_meta.copy()
            meta.update(fm1_meta)
            is_modified = True
            reason = "Merged duplicate frontmatters"
        elif fm1_meta is not None:
            # Case B: Standard Single Frontmatter
            meta = fm1_meta.copy()
        else:
            # Case C: No Frontmatter
            meta = {}
            is_modified = True
            reason = "Created missing frontmatter"

        # Define default types and tags based on path
        default_type = "knowledge"
        default_tags = ["kaos"]
        if "rules" in path.parts:
            default_type = "rule"
            default_tags = ["kaos", "rule"]
        elif "skills" in path.parts:
            default_type = "skill"
            default_tags = ["kaos", "skill"]
        elif "agents" in path.parts:
            default_type = "agent"
            default_tags = ["kaos", "agent"]
        elif "tools" in path.parts:
            default_type = "tool"
            default_tags = ["kaos", "tool"]
        elif "sdd" in path.parts:
            default_type = "sdd"
            default_tags = ["kaos", "normalized"]

        # Normalize ID
        if "id" not in meta:
            meta["id"] = normalize_id(path.name)
            is_modified = True
            if not reason: reason = "Added missing fields"
        elif not isinstance(meta["id"], str):
            meta["id"] = str(meta["id"])
            is_modified = True
            if not reason: reason = "Normalized id to string"

        # Normalize Type
        if "type" not in meta:
            meta["type"] = default_type
            is_modified = True
            if not reason: reason = "Added missing fields"

        # Normalize Status
        if "status" not in meta:
            meta["status"] = "active" if default_type != "sdd" else "in-progress"
            is_modified = True
            if not reason: reason = "Added missing fields"

        # Normalize Phase
        if "phase" not in meta:
            meta["phase"] = "Fase 1"
            is_modified = True
            if not reason: reason = "Added missing fields"

        # Normalize Tags
        tags = meta.get("tags")
        if tags is None:
            meta["tags"] = default_tags
            is_modified = True
            if not reason: reason = "Added missing fields"
        elif not isinstance(tags, list):
            meta["tags"] = [str(tags)]
            is_modified = True
            if not reason: reason = "Normalized tags to list"
        elif len(tags) == 0:
            meta["tags"] = default_tags
            is_modified = True
            if not reason: reason = "Populated empty tags list"

        if is_modified:
            # Reconstruct content
            yaml_content = yaml.dump(meta, allow_unicode=True, sort_keys=False).strip()
            new_frontmatter = f"---\n{yaml_content}\n---\n"
            new_file_content = new_frontmatter + "\n" + body.lstrip()

            modified_count += 1
            mode_prefix = "[DRY RUN] Would update" if dry_run else "Updating"
            print(f"{mode_prefix} {rel_path} - Reason: {reason}")
            
            if not dry_run:
                try:
                    path.write_text(new_file_content, encoding="utf-8")
                except Exception as e:
                    print(f"Failed writing to {rel_path}: {e}")

    # Case D: Create Gaps (links refer to nonexistent files)
    gaps_to_create = [
        ("docs/sdd/Feature Registry.md", "feature-registry", "Feature Registry"),
        ("docs/sdd/SDD-AI-Vault-Analyzer.md", "sdd-ai-vault-analyzer", "SDD AI Vault Analyzer"),
        ("docs/sdd/SDD-Graphify.md", "sdd-graphify", "SDD Graphify")
    ]

    for filepath, sdd_id, title in gaps_to_create:
        gap_path = Path(filepath)
        if not gap_path.exists():
            gaps_created += 1
            gap_meta = {
                "id": sdd_id,
                "type": "sdd",
                "phase": "Fase 1",
                "status": "planned",
                "tags": ["kaos", "normalized"]
            }
            yaml_content = yaml.dump(gap_meta, allow_unicode=True, sort_keys=False).strip()
            gap_content = f"---\n{yaml_content}\n---\n\n# {title}\n\nDocumento de especificação para {title}.\n"
            
            mode_prefix = "[DRY RUN] Would create" if dry_run else "Creating"
            print(f"{mode_prefix} {filepath} (Gap filled)")
            
            if not dry_run:
                try:
                    gap_path.parent.mkdir(parents=True, exist_ok=True)
                    gap_path.write_text(gap_content, encoding="utf-8")
                except Exception as e:
                    print(f"Failed to create gap file {filepath}: {e}")

    print("\n----------------------------------------------")
    print(f"Execution complete. Total modified/to-modify: {modified_count}")
    print(f"Gaps created/to-create: {gaps_created}")
    print("----------------------------------------------")

if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("RUNNING IN DRY RUN MODE (NO FILES WILL BE WRITTEN)")
    fix_metadata(dry_run=dry_run)
