# airllm\funding.json

## Símbolos

- [[airllm_funding]] — code: funding.json
- [[airllm_funding_schema]] — code: $schema
- [[airllm_funding_version]] — code: version
- [[airllm_funding_entity]] — code: entity
- [[airllm_funding_entity_type]] — code: type
- [[airllm_funding_entity_role]] — code: role
- [[airllm_funding_entity_name]] — code: name
- [[airllm_funding_entity_email]] — code: email
- [[airllm_funding_entity_description]] — code: description
- [[airllm_funding_entity_webpageurl]] — code: webpageUrl
- [[airllm_funding_webpageurl_url]] — code: url
- [[airllm_funding_projects]] — code: projects
- [[airllm_funding_funding]] — code: funding
- [[airllm_funding_funding_channels]] — code: channels
- [[airllm_funding_funding_plans]] — code: plans

## Dependências

- [[airllm_funding]] → `contains` → [[airllm_funding_entity]]
- [[airllm_funding]] → `contains` → [[airllm_funding_funding]]
- [[airllm_funding]] → `contains` → [[airllm_funding_projects]]
- [[airllm_funding]] → `contains` → [[airllm_funding_schema]]
- [[airllm_funding]] → `contains` → [[airllm_funding_version]]
- [[airllm_funding_entity]] → `contains` → [[airllm_funding_entity_description]]
- [[airllm_funding_entity]] → `contains` → [[airllm_funding_entity_email]]
- [[airllm_funding_entity]] → `contains` → [[airllm_funding_entity_name]]
- [[airllm_funding_entity]] → `contains` → [[airllm_funding_entity_role]]
- [[airllm_funding_entity]] → `contains` → [[airllm_funding_entity_type]]
- [[airllm_funding_entity]] → `contains` → [[airllm_funding_entity_webpageurl]]
- [[airllm_funding_entity_webpageurl]] → `contains` → [[airllm_funding_webpageurl_url]]
- [[airllm_funding_funding]] → `contains` → [[airllm_funding_funding_channels]]
- [[airllm_funding_funding]] → `contains` → [[airllm_funding_funding_plans]]