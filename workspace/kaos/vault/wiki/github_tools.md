# assistant\app\tools\github_tools.py

## Símbolos

- [[assistant_app_tools_github_tools]] — code: github_tools.py
- [[assistant_app_tools_github_tools_github_api]] — code: _github_api()
- [[assistant_app_tools_github_tools_github_list_repos]] — code: github_list_repos()
- [[assistant_app_tools_github_tools_github_get_repo]] — code: github_get_repo()
- [[assistant_app_tools_github_tools_github_list_issues]] — code: github_list_issues()
- [[assistant_app_tools_github_tools_register_github_tools]] — code: register_github_tools()
- [[assistant_app_tools_github_tools_rationale_40]] — code: Lista repositorios do GitHub do usuario ou de um owner especifico.
- [[assistant_app_tools_github_tools_rationale_54]] — code: Obtem detalhes de um repositorio do GitHub.
- [[assistant_app_tools_github_tools_rationale_62]] — code: Lista issues de um repositorio do GitHub.

## Dependências

- [[assistant_app_tools_github_tools]] → `contains` → [[assistant_app_tools_github_tools_github_api]]
- [[assistant_app_tools_github_tools]] → `contains` → [[assistant_app_tools_github_tools_github_get_repo]]
- [[assistant_app_tools_github_tools]] → `contains` → [[assistant_app_tools_github_tools_github_list_issues]]
- [[assistant_app_tools_github_tools]] → `contains` → [[assistant_app_tools_github_tools_github_list_repos]]
- [[assistant_app_tools_github_tools]] → `contains` → [[assistant_app_tools_github_tools_register_github_tools]]
- [[assistant_app_tools_github_tools_github_api]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_tools_github_tools_github_get_repo]] → `calls` → [[assistant_app_tools_github_tools_github_api]]
- [[assistant_app_tools_github_tools_github_list_issues]] → `calls` → [[assistant_app_tools_github_tools_github_api]]
- [[assistant_app_tools_github_tools_github_list_repos]] → `calls` → [[assistant_app_tools_github_tools_github_api]]
- [[assistant_app_tools_github_tools_rationale_40]] → `rationale_for` → [[assistant_app_tools_github_tools_github_list_repos]]
- [[assistant_app_tools_github_tools_register_github_tools]] → `indirect_call` → [[assistant_app_tools_github_tools_github_list_repos]]
- [[assistant_app_tools_github_tools_rationale_54]] → `rationale_for` → [[assistant_app_tools_github_tools_github_get_repo]]
- [[assistant_app_tools_github_tools_register_github_tools]] → `indirect_call` → [[assistant_app_tools_github_tools_github_get_repo]]
- [[assistant_app_tools_github_tools_rationale_62]] → `rationale_for` → [[assistant_app_tools_github_tools_github_list_issues]]
- [[assistant_app_tools_github_tools_register_github_tools]] → `indirect_call` → [[assistant_app_tools_github_tools_github_list_issues]]