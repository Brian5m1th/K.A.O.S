# assistant\app\providers\aws\aws_tool.py

## Símbolos

- [[assistant_app_providers_aws_aws_tool]] — code: aws_tool.py
- [[assistant_app_providers_aws_aws_tool_run_aws_cli]] — code: _run_aws_cli()
- [[assistant_app_providers_aws_aws_tool_aws_list_instances]] — code: aws_list_instances()
- [[assistant_app_providers_aws_aws_tool_aws_describe_service]] — code: aws_describe_service()
- [[assistant_app_providers_aws_aws_tool_aws_run_command]] — code: aws_run_command()
- [[assistant_app_providers_aws_aws_tool_register_aws_tools]] — code: register_aws_tools()
- [[assistant_app_providers_aws_aws_tool_rationale_1]] — code: AWS Tools — Ferramentas LangChain para comandos AWS.  Utiliza subprocess para
- [[assistant_app_providers_aws_aws_tool_rationale_18]] — code: Executa um comando AWS CLI e retorna o resultado.      Args:         command:
- [[assistant_app_providers_aws_aws_tool_rationale_68]] — code: Lista instancias EC2 da conta AWS.      Args:         profile: Nome do perfil
- [[assistant_app_providers_aws_aws_tool_rationale_104]] — code: Descreve o status de um servico AWS.      Args:         service: Nome do serv
- [[assistant_app_providers_aws_aws_tool_rationale_123]] — code: Executa um comando AWS CLI customizado.      ATENCAO: Apenas comandos de leitu
- [[assistant_app_providers_aws_aws_tool_rationale_165]] — code: Registra as ferramentas AWS no TOOL_REGISTRY global.

## Dependências

- [[assistant_app_providers_aws_aws_tool]] → `contains` → [[assistant_app_providers_aws_aws_tool_aws_describe_service]]
- [[assistant_app_providers_aws_aws_tool]] → `contains` → [[assistant_app_providers_aws_aws_tool_aws_list_instances]]
- [[assistant_app_providers_aws_aws_tool]] → `contains` → [[assistant_app_providers_aws_aws_tool_aws_run_command]]
- [[assistant_app_providers_aws_aws_tool]] → `contains` → [[assistant_app_providers_aws_aws_tool_register_aws_tools]]
- [[assistant_app_providers_aws_aws_tool]] → `contains` → [[assistant_app_providers_aws_aws_tool_run_aws_cli]]
- [[assistant_app_providers_aws_aws_tool_rationale_1]] → `rationale_for` → [[assistant_app_providers_aws_aws_tool]]
- [[assistant_app_providers_aws_aws_tool_aws_describe_service]] → `calls` → [[assistant_app_providers_aws_aws_tool_run_aws_cli]]
- [[assistant_app_providers_aws_aws_tool_aws_list_instances]] → `calls` → [[assistant_app_providers_aws_aws_tool_run_aws_cli]]
- [[assistant_app_providers_aws_aws_tool_aws_run_command]] → `calls` → [[assistant_app_providers_aws_aws_tool_run_aws_cli]]
- [[assistant_app_providers_aws_aws_tool_rationale_18]] → `rationale_for` → [[assistant_app_providers_aws_aws_tool_run_aws_cli]]
- [[assistant_app_providers_aws_aws_tool_run_aws_cli]] → `references` → [[assistant_app_providers_aws_aws_tool_py_any]]
- [[assistant_app_providers_aws_aws_tool_run_aws_cli]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_providers_aws_aws_tool_rationale_68]] → `rationale_for` → [[assistant_app_providers_aws_aws_tool_aws_list_instances]]
- [[assistant_app_providers_aws_aws_tool_register_aws_tools]] → `indirect_call` → [[assistant_app_providers_aws_aws_tool_aws_list_instances]]
- [[assistant_app_providers_aws_aws_tool_rationale_104]] → `rationale_for` → [[assistant_app_providers_aws_aws_tool_aws_describe_service]]
- [[assistant_app_providers_aws_aws_tool_register_aws_tools]] → `indirect_call` → [[assistant_app_providers_aws_aws_tool_aws_describe_service]]
- [[assistant_app_providers_aws_aws_tool_rationale_123]] → `rationale_for` → [[assistant_app_providers_aws_aws_tool_aws_run_command]]
- [[assistant_app_providers_aws_aws_tool_register_aws_tools]] → `indirect_call` → [[assistant_app_providers_aws_aws_tool_aws_run_command]]
- [[assistant_app_providers_aws_aws_tool_rationale_165]] → `rationale_for` → [[assistant_app_providers_aws_aws_tool_register_aws_tools]]