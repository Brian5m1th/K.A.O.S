# assistant\tests\unit\test_opencode_executor.py

## Símbolos

- [[assistant_tests_unit_test_opencode_executor]] — code: test_opencode_executor.py
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor]] — code: TestOpenCodeExecutor
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_validate_command_whitelisted]] — code: .test_validate_command_whitelisted()
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_validate_command_blacklisted]] — code: .test_validate_command_blacklisted()
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_validate_command_unknown]] — code: .test_validate_command_unknown()
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_execute_without_approval_fails]] — code: .test_execute_without_approval_fails()
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_execute_invalid_command_fails]] — code: .test_execute_invalid_command_fails()
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_execute_in_docker_sandbox]] — code: .test_execute_in_docker_sandbox()
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_execute_in_local_fallback]] — code: .test_execute_in_local_fallback()

## Dependências

- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor]] → `uses` → [[assistant_app_core_opencode_executor_opencodeexecutor]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_validate_command_blacklisted]] → `calls` → [[assistant_app_core_opencode_executor_opencodeexecutor_validate_command]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_validate_command_unknown]] → `calls` → [[assistant_app_core_opencode_executor_opencodeexecutor_validate_command]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_validate_command_whitelisted]] → `calls` → [[assistant_app_core_opencode_executor_opencodeexecutor_validate_command]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_execute_in_docker_sandbox]] → `calls` → [[assistant_app_core_opencode_executor_opencodeexecutor_execute]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_execute_in_local_fallback]] → `calls` → [[assistant_app_core_opencode_executor_opencodeexecutor_execute]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_execute_invalid_command_fails]] → `calls` → [[assistant_app_core_opencode_executor_opencodeexecutor_execute]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_execute_without_approval_fails]] → `calls` → [[assistant_app_core_opencode_executor_opencodeexecutor_execute]]
- [[assistant_tests_unit_test_opencode_executor]] → `contains` → [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor]] → `method` → [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_execute_in_docker_sandbox]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor]] → `method` → [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_execute_in_local_fallback]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor]] → `method` → [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_execute_invalid_command_fails]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor]] → `method` → [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_execute_without_approval_fails]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor]] → `method` → [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_validate_command_blacklisted]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor]] → `method` → [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_validate_command_unknown]]
- [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor]] → `method` → [[assistant_tests_unit_test_opencode_executor_testopencodeexecutor_test_validate_command_whitelisted]]