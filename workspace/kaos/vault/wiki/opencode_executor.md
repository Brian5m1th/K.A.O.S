# assistant\app\core\opencode_executor.py

## Símbolos

- [[assistant_app_core_opencode_executor]] — code: opencode_executor.py
- [[assistant_app_core_opencode_executor_opencodeexecutor]] — code: OpenCodeExecutor
- [[assistant_app_core_opencode_executor_opencodeexecutor_validate_command]] — code: .validate_command()
- [[assistant_app_core_opencode_executor_opencodeexecutor_execute]] — code: .execute()

## Dependências

- [[assistant_app_core_opencode_executor_opencodeexecutor]] → `uses` → [[assistant_app_core_environment_service_environmentservice]]
- [[assistant_app_core_opencode_executor_opencodeexecutor_execute]] → `calls` → [[assistant_app_core_environment_service_environmentservice_detect]]
- [[assistant_app_core_opencode_executor]] → `contains` → [[assistant_app_core_opencode_executor_opencodeexecutor]]
- [[assistant_app_core_opencode_executor_opencodeexecutor]] → `method` → [[assistant_app_core_opencode_executor_opencodeexecutor_execute]]
- [[assistant_app_core_opencode_executor_opencodeexecutor]] → `method` → [[assistant_app_core_opencode_executor_opencodeexecutor_validate_command]]
- [[assistant_app_core_opencode_executor_opencodeexecutor_execute]] → `calls` → [[assistant_app_core_opencode_executor_opencodeexecutor_validate_command]]