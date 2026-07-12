# graphify\graphify\google_workspace.py

## Símbolos

- [[graphify_graphify_google_workspace]] — code: google_workspace.py
- [[graphify_graphify_google_workspace_google_workspace_enabled]] — code: google_workspace_enabled()
- [[graphify_graphify_google_workspace_safe_yaml_str]] — code: _safe_yaml_str()
- [[graphify_graphify_google_workspace_extract_file_id_from_url]] — code: _extract_file_id_from_url()
- [[graphify_graphify_google_workspace_extract_resource_key]] — code: _extract_resource_key()
- [[graphify_graphify_google_workspace_read_google_shortcut]] — code: read_google_shortcut()
- [[graphify_graphify_google_workspace_run_gws_export]] — code: _run_gws_export()
- [[graphify_graphify_google_workspace_sidecar_path]] — code: _sidecar_path()
- [[graphify_graphify_google_workspace_with_frontmatter]] — code: _with_frontmatter()
- [[graphify_graphify_google_workspace_convert_google_workspace_file]] — code: convert_google_workspace_file()
- [[graphify_graphify_google_workspace_rationale_1]] — code: Optional Google Workspace shortcut export support.  Google Drive for desktop s
- [[graphify_graphify_google_workspace_rationale_26]] — code: Return True when Google Workspace shortcut export is enabled.
- [[graphify_graphify_google_workspace_rationale_36]] — code: Extract a Drive file ID from common Google Docs/Drive URL shapes.
- [[graphify_graphify_google_workspace_rationale_64]] — code: Read a .gdoc/.gsheet/.gslides shortcut and return export metadata.
- [[graphify_graphify_google_workspace_rationale_156]] — code: Export a Google Workspace shortcut to a Markdown sidecar.      Returns the con

## Dependências

- [[graphify_graphify_google_workspace_convert_google_workspace_file]] → `calls` → [[graphify_graphify_detect_xlsx_to_markdown]]
- [[graphify_graphify_google_workspace]] → `contains` → [[graphify_graphify_google_workspace_convert_google_workspace_file]]
- [[graphify_graphify_google_workspace]] → `contains` → [[graphify_graphify_google_workspace_extract_file_id_from_url]]
- [[graphify_graphify_google_workspace]] → `contains` → [[graphify_graphify_google_workspace_extract_resource_key]]
- [[graphify_graphify_google_workspace]] → `contains` → [[graphify_graphify_google_workspace_google_workspace_enabled]]
- [[graphify_graphify_google_workspace]] → `contains` → [[graphify_graphify_google_workspace_read_google_shortcut]]
- [[graphify_graphify_google_workspace]] → `contains` → [[graphify_graphify_google_workspace_run_gws_export]]
- [[graphify_graphify_google_workspace]] → `contains` → [[graphify_graphify_google_workspace_safe_yaml_str]]
- [[graphify_graphify_google_workspace]] → `contains` → [[graphify_graphify_google_workspace_sidecar_path]]
- [[graphify_graphify_google_workspace]] → `contains` → [[graphify_graphify_google_workspace_with_frontmatter]]
- [[graphify_graphify_google_workspace_rationale_1]] → `rationale_for` → [[graphify_graphify_google_workspace]]
- [[graphify_graphify_google_workspace_rationale_26]] → `rationale_for` → [[graphify_graphify_google_workspace_google_workspace_enabled]]
- [[graphify_graphify_google_workspace_with_frontmatter]] → `calls` → [[graphify_graphify_google_workspace_safe_yaml_str]]
- [[graphify_graphify_google_workspace_rationale_36]] → `rationale_for` → [[graphify_graphify_google_workspace_extract_file_id_from_url]]
- [[graphify_graphify_google_workspace_read_google_shortcut]] → `calls` → [[graphify_graphify_google_workspace_extract_file_id_from_url]]
- [[graphify_graphify_google_workspace_extract_resource_key]] → `references` → [[graphify_graphify_google_workspace_py_any]]
- [[graphify_graphify_google_workspace_read_google_shortcut]] → `calls` → [[graphify_graphify_google_workspace_extract_resource_key]]
- [[graphify_graphify_google_workspace_convert_google_workspace_file]] → `calls` → [[graphify_graphify_google_workspace_read_google_shortcut]]
- [[graphify_graphify_google_workspace_rationale_64]] → `rationale_for` → [[graphify_graphify_google_workspace_read_google_shortcut]]
- [[graphify_graphify_google_workspace_read_google_shortcut]] → `references` → [[graphify_graphify_google_workspace_py_path]]
- [[graphify_graphify_google_workspace_convert_google_workspace_file]] → `references` → [[graphify_graphify_google_workspace_py_path]]
- [[graphify_graphify_google_workspace_run_gws_export]] → `references` → [[graphify_graphify_google_workspace_py_path]]
- [[graphify_graphify_google_workspace_sidecar_path]] → `references` → [[graphify_graphify_google_workspace_py_path]]
- [[graphify_graphify_google_workspace_with_frontmatter]] → `references` → [[graphify_graphify_google_workspace_py_path]]
- [[graphify_graphify_google_workspace_convert_google_workspace_file]] → `calls` → [[graphify_graphify_google_workspace_run_gws_export]]
- [[graphify_graphify_google_workspace_convert_google_workspace_file]] → `calls` → [[graphify_graphify_google_workspace_sidecar_path]]
- [[graphify_graphify_google_workspace_convert_google_workspace_file]] → `calls` → [[graphify_graphify_google_workspace_with_frontmatter]]
- [[graphify_graphify_google_workspace_rationale_156]] → `rationale_for` → [[graphify_graphify_google_workspace_convert_google_workspace_file]]