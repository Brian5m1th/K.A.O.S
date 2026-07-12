# assistant\app\core\documentation\graph_validator.py

## Símbolos

- [[assistant_app_core_documentation_graph_validator]] — code: graph_validator.py
- [[assistant_app_core_documentation_graph_validator_graphvalidator]] — code: GraphValidator
- [[assistant_app_core_documentation_graph_validator_graphvalidator_validate_graph]] — code: .validate_graph()
- [[assistant_app_core_documentation_graph_validator_graphvalidator_find_match]] — code: ._find_match()
- [[assistant_app_core_documentation_graph_validator_rationale_9]] — code: Valida o grafo de documentação:         - Links quebrados (referências a notas
- [[assistant_app_core_documentation_graph_validator_rationale_94]] — code: Encontra correspondência insensível a maiúsculas/minúsculas para o nome do docum

## Dependências

- [[assistant_app_core_documentation_graph_validator]] → `contains` → [[assistant_app_core_documentation_graph_validator_graphvalidator]]
- [[assistant_app_core_documentation_graph_validator_graphvalidator]] → `method` → [[assistant_app_core_documentation_graph_validator_graphvalidator_find_match]]
- [[assistant_app_core_documentation_graph_validator_graphvalidator]] → `method` → [[assistant_app_core_documentation_graph_validator_graphvalidator_validate_graph]]
- [[assistant_app_core_documentation_graph_validator_graphvalidator_validate_graph]] → `calls` → [[assistant_app_core_documentation_graph_validator_graphvalidator_find_match]]
- [[assistant_app_core_documentation_graph_validator_graphvalidator_validate_graph]] → `references` → [[assistant_app_core_documentation_graph_validator_py_any]]
- [[assistant_app_core_documentation_graph_validator_rationale_9]] → `rationale_for` → [[assistant_app_core_documentation_graph_validator_graphvalidator_validate_graph]]
- [[assistant_app_core_documentation_graph_validator_rationale_94]] → `rationale_for` → [[assistant_app_core_documentation_graph_validator_graphvalidator_find_match]]