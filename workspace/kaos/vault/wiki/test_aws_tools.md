# assistant\tests\unit\test_aws_tools.py

## Símbolos

- [[assistant_tests_unit_test_aws_tools]] — code: test_aws_tools.py
- [[assistant_tests_unit_test_aws_tools_testawstools]] — code: TestAWSTools
- [[assistant_tests_unit_test_aws_tools_testawstools_test_run_aws_cli_not_found]] — code: .test_run_aws_cli_not_found()
- [[assistant_tests_unit_test_aws_tools_testawstools_test_run_aws_cli_success]] — code: .test_run_aws_cli_success()
- [[assistant_tests_unit_test_aws_tools_testawstools_test_run_aws_cli_error]] — code: .test_run_aws_cli_error()
- [[assistant_tests_unit_test_aws_tools_testawstools_test_aws_list_instances_blocked_prefix]] — code: .test_aws_list_instances_blocked_prefix()
- [[assistant_tests_unit_test_aws_tools_testawstools_test_aws_run_command_blocked_write]] — code: .test_aws_run_command_blocked_write()
- [[assistant_tests_unit_test_aws_tools_testawstools_test_aws_run_command_allowed_read]] — code: .test_aws_run_command_allowed_read()
- [[assistant_tests_unit_test_aws_tools_rationale_1]] — code: Testes do provedor AWS.
- [[assistant_tests_unit_test_aws_tools_rationale_47]] — code: Comandos de escrita devem ser bloqueados.
- [[assistant_tests_unit_test_aws_tools_rationale_60]] — code: Comandos de leitura devem passar pela validacao (mas falhar sem CLI).

## Dependências

- [[assistant_tests_unit_test_aws_tools_testawstools_test_run_aws_cli_error]] → `calls` → [[assistant_app_providers_aws_aws_tool_run_aws_cli]]
- [[assistant_tests_unit_test_aws_tools_testawstools_test_run_aws_cli_not_found]] → `calls` → [[assistant_app_providers_aws_aws_tool_run_aws_cli]]
- [[assistant_tests_unit_test_aws_tools_testawstools_test_run_aws_cli_success]] → `calls` → [[assistant_app_providers_aws_aws_tool_run_aws_cli]]
- [[assistant_tests_unit_test_aws_tools]] → `contains` → [[assistant_tests_unit_test_aws_tools_testawstools]]
- [[assistant_tests_unit_test_aws_tools_rationale_1]] → `rationale_for` → [[assistant_tests_unit_test_aws_tools]]
- [[assistant_tests_unit_test_aws_tools_testawstools]] → `method` → [[assistant_tests_unit_test_aws_tools_testawstools_test_aws_list_instances_blocked_prefix]]
- [[assistant_tests_unit_test_aws_tools_testawstools]] → `method` → [[assistant_tests_unit_test_aws_tools_testawstools_test_aws_run_command_allowed_read]]
- [[assistant_tests_unit_test_aws_tools_testawstools]] → `method` → [[assistant_tests_unit_test_aws_tools_testawstools_test_aws_run_command_blocked_write]]
- [[assistant_tests_unit_test_aws_tools_testawstools]] → `method` → [[assistant_tests_unit_test_aws_tools_testawstools_test_run_aws_cli_error]]
- [[assistant_tests_unit_test_aws_tools_testawstools]] → `method` → [[assistant_tests_unit_test_aws_tools_testawstools_test_run_aws_cli_not_found]]
- [[assistant_tests_unit_test_aws_tools_testawstools]] → `method` → [[assistant_tests_unit_test_aws_tools_testawstools_test_run_aws_cli_success]]
- [[assistant_tests_unit_test_aws_tools_rationale_47]] → `rationale_for` → [[assistant_tests_unit_test_aws_tools_testawstools_test_aws_run_command_blocked_write]]
- [[assistant_tests_unit_test_aws_tools_rationale_60]] → `rationale_for` → [[assistant_tests_unit_test_aws_tools_testawstools_test_aws_run_command_allowed_read]]