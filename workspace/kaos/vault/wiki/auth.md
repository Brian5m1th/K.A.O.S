# graphify\worked\httpx\raw\auth.py

## Símbolos

- [[graphify_worked_httpx_raw_auth]] — code: auth.py
- [[graphify_worked_httpx_raw_auth_auth]] — code: Auth
- [[graphify_worked_httpx_raw_auth_auth_auth_flow]] — code: .auth_flow()
- [[graphify_worked_httpx_raw_auth_basicauth]] — code: BasicAuth
- [[graphify_worked_httpx_raw_auth_basicauth_init]] — code: .__init__()
- [[graphify_worked_httpx_raw_auth_basicauth_auth_flow]] — code: .auth_flow()
- [[graphify_worked_httpx_raw_auth_bearerauth]] — code: BearerAuth
- [[graphify_worked_httpx_raw_auth_bearerauth_init]] — code: .__init__()
- [[graphify_worked_httpx_raw_auth_bearerauth_auth_flow]] — code: .auth_flow()
- [[graphify_worked_httpx_raw_auth_digestauth]] — code: DigestAuth
- [[graphify_worked_httpx_raw_auth_digestauth_init]] — code: .__init__()
- [[graphify_worked_httpx_raw_auth_digestauth_auth_flow]] — code: .auth_flow()
- [[graphify_worked_httpx_raw_auth_digestauth_parse_challenge]] — code: ._parse_challenge()
- [[graphify_worked_httpx_raw_auth_digestauth_build_credentials]] — code: ._build_credentials()
- [[graphify_worked_httpx_raw_auth_netrcauth]] — code: NetRCAuth
- [[graphify_worked_httpx_raw_auth_netrcauth_auth_flow]] — code: .auth_flow()
- [[graphify_worked_httpx_raw_auth_rationale_1]] — code: Authentication handlers. Auth objects are callables that modify a request befor
- [[graphify_worked_httpx_raw_auth_rationale_13]] — code: Base class for all authentication handlers.
- [[graphify_worked_httpx_raw_auth_rationale_16]] — code: Modify the request. May yield to inspect the response.
- [[graphify_worked_httpx_raw_auth_rationale_21]] — code: HTTP Basic Authentication.
- [[graphify_worked_httpx_raw_auth_rationale_36]] — code: Bearer token authentication.
- [[graphify_worked_httpx_raw_auth_rationale_47]] — code: HTTP Digest Authentication.     Requires a full request/response cycle: sends t
- [[graphify_worked_httpx_raw_auth_rationale_72]] — code: Extract digest parameters from the WWW-Authenticate header.
- [[graphify_worked_httpx_raw_auth_rationale_82]] — code: Compute the Authorization header value for a digest challenge.
- [[graphify_worked_httpx_raw_auth_rationale_101]] — code: Load credentials from ~/.netrc based on the request host.

## Dependências

- [[graphify_worked_httpx_raw_auth]] → `contains` → [[graphify_worked_httpx_raw_auth_auth]]
- [[graphify_worked_httpx_raw_auth]] → `contains` → [[graphify_worked_httpx_raw_auth_basicauth]]
- [[graphify_worked_httpx_raw_auth]] → `contains` → [[graphify_worked_httpx_raw_auth_bearerauth]]
- [[graphify_worked_httpx_raw_auth]] → `contains` → [[graphify_worked_httpx_raw_auth_digestauth]]
- [[graphify_worked_httpx_raw_auth]] → `contains` → [[graphify_worked_httpx_raw_auth_netrcauth]]
- [[graphify_worked_httpx_raw_auth_rationale_1]] → `rationale_for` → [[graphify_worked_httpx_raw_auth]]
- [[graphify_worked_httpx_raw_auth_auth]] → `method` → [[graphify_worked_httpx_raw_auth_auth_auth_flow]]
- [[graphify_worked_httpx_raw_auth_basicauth]] → `inherits` → [[graphify_worked_httpx_raw_auth_auth]]
- [[graphify_worked_httpx_raw_auth_bearerauth]] → `inherits` → [[graphify_worked_httpx_raw_auth_auth]]
- [[graphify_worked_httpx_raw_auth_digestauth]] → `inherits` → [[graphify_worked_httpx_raw_auth_auth]]
- [[graphify_worked_httpx_raw_auth_netrcauth]] → `inherits` → [[graphify_worked_httpx_raw_auth_auth]]
- [[graphify_worked_httpx_raw_auth_rationale_13]] → `rationale_for` → [[graphify_worked_httpx_raw_auth_auth]]
- [[graphify_worked_httpx_raw_auth_auth_auth_flow]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[graphify_worked_httpx_raw_auth_rationale_16]] → `rationale_for` → [[graphify_worked_httpx_raw_auth_auth_auth_flow]]
- [[graphify_worked_httpx_raw_auth_basicauth]] → `method` → [[graphify_worked_httpx_raw_auth_basicauth_auth_flow]]
- [[graphify_worked_httpx_raw_auth_basicauth]] → `method` → [[graphify_worked_httpx_raw_auth_basicauth_init]]
- [[graphify_worked_httpx_raw_auth_netrcauth_auth_flow]] → `calls` → [[graphify_worked_httpx_raw_auth_basicauth]]
- [[graphify_worked_httpx_raw_auth_rationale_21]] → `rationale_for` → [[graphify_worked_httpx_raw_auth_basicauth]]
- [[graphify_worked_httpx_raw_auth_basicauth_auth_flow]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[graphify_worked_httpx_raw_auth_bearerauth]] → `method` → [[graphify_worked_httpx_raw_auth_bearerauth_auth_flow]]
- [[graphify_worked_httpx_raw_auth_bearerauth]] → `method` → [[graphify_worked_httpx_raw_auth_bearerauth_init]]
- [[graphify_worked_httpx_raw_auth_rationale_36]] → `rationale_for` → [[graphify_worked_httpx_raw_auth_bearerauth]]
- [[graphify_worked_httpx_raw_auth_bearerauth_auth_flow]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[graphify_worked_httpx_raw_auth_digestauth]] → `method` → [[graphify_worked_httpx_raw_auth_digestauth_auth_flow]]
- [[graphify_worked_httpx_raw_auth_digestauth]] → `method` → [[graphify_worked_httpx_raw_auth_digestauth_build_credentials]]
- [[graphify_worked_httpx_raw_auth_digestauth]] → `method` → [[graphify_worked_httpx_raw_auth_digestauth_init]]
- [[graphify_worked_httpx_raw_auth_digestauth]] → `method` → [[graphify_worked_httpx_raw_auth_digestauth_parse_challenge]]
- [[graphify_worked_httpx_raw_auth_rationale_47]] → `rationale_for` → [[graphify_worked_httpx_raw_auth_digestauth]]
- [[graphify_worked_httpx_raw_auth_digestauth_auth_flow]] → `calls` → [[graphify_worked_httpx_raw_auth_digestauth_build_credentials]]
- [[graphify_worked_httpx_raw_auth_digestauth_auth_flow]] → `calls` → [[graphify_worked_httpx_raw_auth_digestauth_parse_challenge]]
- [[graphify_worked_httpx_raw_auth_digestauth_auth_flow]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[graphify_worked_httpx_raw_auth_digestauth_parse_challenge]] → `references` → [[graphify_worked_httpx_raw_models_response]]
- [[graphify_worked_httpx_raw_auth_rationale_72]] → `rationale_for` → [[graphify_worked_httpx_raw_auth_digestauth_parse_challenge]]
- [[graphify_worked_httpx_raw_auth_digestauth_build_credentials]] → `references` → [[graphify_worked_httpx_raw_models_request]]
- [[graphify_worked_httpx_raw_auth_rationale_82]] → `rationale_for` → [[graphify_worked_httpx_raw_auth_digestauth_build_credentials]]
- [[graphify_worked_httpx_raw_auth_netrcauth]] → `method` → [[graphify_worked_httpx_raw_auth_netrcauth_auth_flow]]
- [[graphify_worked_httpx_raw_auth_rationale_101]] → `rationale_for` → [[graphify_worked_httpx_raw_auth_netrcauth]]
- [[graphify_worked_httpx_raw_auth_netrcauth_auth_flow]] → `references` → [[graphify_worked_httpx_raw_models_request]]