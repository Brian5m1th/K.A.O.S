# assistant\app\api\prompts.py

## Símbolos

- [[assistant_app_api_prompts]] — code: prompts.py
- [[assistant_app_api_prompts_promptschema]] — code: PromptSchema
- [[assistant_app_api_prompts_promptresponse]] — code: PromptResponse
- [[assistant_app_api_prompts_list_prompts]] — code: list_prompts()
- [[assistant_app_api_prompts_create_prompt]] — code: create_prompt()
- [[assistant_app_api_prompts_update_prompt]] — code: update_prompt()
- [[assistant_app_api_prompts_delete_prompt]] — code: delete_prompt()

## Dependências

- [[assistant_app_api_prompts]] → `imports_from` → [[assistant_app_database]]
- [[assistant_app_api_prompts]] → `contains` → [[assistant_app_api_prompts_create_prompt]]
- [[assistant_app_api_prompts]] → `contains` → [[assistant_app_api_prompts_delete_prompt]]
- [[assistant_app_api_prompts]] → `contains` → [[assistant_app_api_prompts_list_prompts]]
- [[assistant_app_api_prompts]] → `contains` → [[assistant_app_api_prompts_promptresponse]]
- [[assistant_app_api_prompts]] → `contains` → [[assistant_app_api_prompts_promptschema]]
- [[assistant_app_api_prompts]] → `contains` → [[assistant_app_api_prompts_update_prompt]]
- [[assistant_app_api_prompts]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_prompts_create_prompt]] → `references` → [[assistant_app_api_prompts_promptschema]]
- [[assistant_app_api_prompts_promptresponse]] → `inherits` → [[assistant_app_api_prompts_promptschema]]
- [[assistant_app_api_prompts_promptschema]] → `inherits` → [[assistant_app_api_prompts_py_basemodel]]
- [[assistant_app_api_prompts_promptschema]] → `uses` → [[assistant_app_models_prompt_prompt]]
- [[assistant_app_api_prompts_update_prompt]] → `references` → [[assistant_app_api_prompts_promptschema]]
- [[assistant_app_api_prompts_create_prompt]] → `calls` → [[assistant_app_api_prompts_promptresponse]]
- [[assistant_app_api_prompts_list_prompts]] → `calls` → [[assistant_app_api_prompts_promptresponse]]
- [[assistant_app_api_prompts_promptresponse]] → `uses` → [[assistant_app_models_prompt_prompt]]
- [[assistant_app_api_prompts_update_prompt]] → `calls` → [[assistant_app_api_prompts_promptresponse]]
- [[assistant_app_api_prompts_list_prompts]] → `references` → [[assistant_app_api_prompts_py_asyncsession]]
- [[assistant_app_api_prompts_list_prompts]] → `indirect_call` → [[assistant_app_models_prompt_prompt]]
- [[assistant_app_api_prompts_create_prompt]] → `references` → [[assistant_app_api_prompts_py_asyncsession]]
- [[assistant_app_api_prompts_delete_prompt]] → `references` → [[assistant_app_api_prompts_py_asyncsession]]
- [[assistant_app_api_prompts_update_prompt]] → `references` → [[assistant_app_api_prompts_py_asyncsession]]
- [[assistant_app_api_prompts_create_prompt]] → `calls` → [[assistant_app_models_prompt_prompt]]
- [[assistant_app_api_prompts_update_prompt]] → `indirect_call` → [[assistant_app_models_prompt_prompt]]
- [[assistant_app_api_prompts_delete_prompt]] → `indirect_call` → [[assistant_app_models_prompt_prompt]]