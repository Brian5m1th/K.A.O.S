# assistant\app\auth\jwt.py

## Símbolos

- [[assistant_app_auth_jwt]] — code: jwt.py
- [[assistant_app_auth_jwt_get_secret]] — code: _get_secret()
- [[assistant_app_auth_jwt_create_access_token]] — code: create_access_token()
- [[assistant_app_auth_jwt_create_refresh_token]] — code: create_refresh_token()
- [[assistant_app_auth_jwt_decode_token]] — code: decode_token()

## Dependências

- [[assistant_app_auth_jwt]] → `contains` → [[assistant_app_auth_jwt_create_access_token]]
- [[assistant_app_auth_jwt]] → `contains` → [[assistant_app_auth_jwt_create_refresh_token]]
- [[assistant_app_auth_jwt]] → `contains` → [[assistant_app_auth_jwt_decode_token]]
- [[assistant_app_auth_jwt]] → `contains` → [[assistant_app_auth_jwt_get_secret]]
- [[assistant_app_auth_jwt_create_access_token]] → `calls` → [[assistant_app_auth_jwt_get_secret]]
- [[assistant_app_auth_jwt_create_refresh_token]] → `calls` → [[assistant_app_auth_jwt_get_secret]]
- [[assistant_app_auth_jwt_decode_token]] → `calls` → [[assistant_app_auth_jwt_get_secret]]
- [[assistant_app_auth_jwt_create_access_token]] → `references` → [[timedelta]]
- [[assistant_app_auth_jwt_create_refresh_token]] → `references` → [[timedelta]]
- [[assistant_app_auth_jwt_decode_token]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]