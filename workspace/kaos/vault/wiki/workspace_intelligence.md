# assistant\app\api\workspace_intelligence.py

## Símbolos

- [[assistant_app_api_workspace_intelligence]] — code: workspace_intelligence.py
- [[assistant_app_api_workspace_intelligence_autotagrequest]] — code: AutoTagRequest
- [[assistant_app_api_workspace_intelligence_suggestlinksrequest]] — code: SuggestLinksRequest
- [[assistant_app_api_workspace_intelligence_auto_tag_endpoint]] — code: auto_tag_endpoint()
- [[assistant_app_api_workspace_intelligence_suggest_connections_endpoint]] — code: suggest_connections_endpoint()
- [[assistant_app_api_workspace_intelligence_health_endpoint]] — code: health_endpoint()
- [[assistant_app_api_workspace_intelligence_rationale_1]] — code: Workspace Intelligence API Router.  SDD-KAOS-EVOLUTION-001: Provides FastAPI r
- [[assistant_app_api_workspace_intelligence_rationale_28]] — code: Auto-tags a file inside the Obsidian Vault based on content or neighbors.
- [[assistant_app_api_workspace_intelligence_rationale_45]] — code: Recommends wiki links for a target markdown document.
- [[assistant_app_api_workspace_intelligence_rationale_56]] — code: Checks vault structure sanity metrics.

## Dependências

- [[assistant_app_api_workspace_intelligence]] → `contains` → [[assistant_app_api_workspace_intelligence_auto_tag_endpoint]]
- [[assistant_app_api_workspace_intelligence]] → `contains` → [[assistant_app_api_workspace_intelligence_autotagrequest]]
- [[assistant_app_api_workspace_intelligence]] → `contains` → [[assistant_app_api_workspace_intelligence_health_endpoint]]
- [[assistant_app_api_workspace_intelligence]] → `contains` → [[assistant_app_api_workspace_intelligence_suggest_connections_endpoint]]
- [[assistant_app_api_workspace_intelligence]] → `contains` → [[assistant_app_api_workspace_intelligence_suggestlinksrequest]]
- [[assistant_app_api_workspace_intelligence]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_workspace_intelligence_rationale_1]] → `rationale_for` → [[assistant_app_api_workspace_intelligence]]
- [[assistant_app_api_workspace_intelligence_auto_tag_endpoint]] → `references` → [[assistant_app_api_workspace_intelligence_autotagrequest]]
- [[assistant_app_api_workspace_intelligence_autotagrequest]] → `inherits` → [[assistant_app_api_workspace_intelligence_py_basemodel]]
- [[assistant_app_api_workspace_intelligence_autotagrequest]] → `uses` → [[assistant_app_capability_workspace_intelligence_service_workspaceintelligenceservice]]
- [[assistant_app_api_workspace_intelligence_suggestlinksrequest]] → `inherits` → [[assistant_app_api_workspace_intelligence_py_basemodel]]
- [[assistant_app_api_workspace_intelligence_suggest_connections_endpoint]] → `references` → [[assistant_app_api_workspace_intelligence_suggestlinksrequest]]
- [[assistant_app_api_workspace_intelligence_suggestlinksrequest]] → `uses` → [[assistant_app_capability_workspace_intelligence_service_workspaceintelligenceservice]]
- [[assistant_app_api_workspace_intelligence_auto_tag_endpoint]] → `calls` → [[assistant_app_capability_registry_capabilityregistry_update_status]]
- [[assistant_app_api_workspace_intelligence_auto_tag_endpoint]] → `calls` → [[assistant_app_capability_workspace_intelligence_service_workspaceintelligenceservice]]
- [[assistant_app_api_workspace_intelligence_auto_tag_endpoint]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_api_workspace_intelligence_rationale_28]] → `rationale_for` → [[assistant_app_api_workspace_intelligence_auto_tag_endpoint]]
- [[assistant_app_api_workspace_intelligence_rationale_45]] → `rationale_for` → [[assistant_app_api_workspace_intelligence_suggest_connections_endpoint]]
- [[assistant_app_api_workspace_intelligence_suggest_connections_endpoint]] → `calls` → [[assistant_app_capability_workspace_intelligence_service_workspaceintelligenceservice]]
- [[assistant_app_api_workspace_intelligence_suggest_connections_endpoint]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_api_workspace_intelligence_health_endpoint]] → `calls` → [[assistant_app_capability_workspace_intelligence_service_workspaceintelligenceservice]]
- [[assistant_app_api_workspace_intelligence_health_endpoint]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_api_workspace_intelligence_rationale_56]] → `rationale_for` → [[assistant_app_api_workspace_intelligence_health_endpoint]]