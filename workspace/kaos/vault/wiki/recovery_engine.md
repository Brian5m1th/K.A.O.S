# assistant\app\core\documentation\recovery_engine.py

## Símbolos

- [[assistant_app_core_documentation_recovery_engine]] — code: recovery_engine.py
- [[assistant_app_core_documentation_recovery_engine_recoveryengine]] — code: RecoveryEngine
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_is_protected]] — code: .is_protected()
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_encoding]] — code: .fix_encoding()
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_inject_frontmatter]] — code: .inject_frontmatter()
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]] — code: .fix_file()
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_get_valid_stems]] — code: .get_valid_stems()
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_wikilinks]] — code: .fix_wikilinks()
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_normalize_target]] — code: ._normalize_target()
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_match_stem]] — code: ._match_stem()
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_split_combined_link]] — code: ._split_combined_link()
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_standardize_sections]] — code: .standardize_sections()
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_generate_stub]] — code: .generate_stub()
- [[assistant_app_core_documentation_recovery_engine_rationale_67]] — code: Verifica se o arquivo é considerado READ-ONLY.
- [[assistant_app_core_documentation_recovery_engine_rationale_89]] — code: Corrige os caracteres mal codificados.
- [[assistant_app_core_documentation_recovery_engine_rationale_109]] — code: Injeta bloco de frontmatter se estiver ausente ou inválido.
- [[assistant_app_core_documentation_recovery_engine_rationale_120]] — code: Aplica correções a um arquivo markdown e retorna o status.
- [[assistant_app_core_documentation_recovery_engine_rationale_198]] — code: Corrige e normaliza os wikilinks [[Target]] no conteúdo.
- [[assistant_app_core_documentation_recovery_engine_rationale_367]] — code: Garante a estrutura padrão de seções requisitada.
- [[assistant_app_core_documentation_recovery_engine_rationale_398]] — code: Gera um stub para features que não possuem documentação nem relacionamentos sufi

## Dependências

- [[assistant_app_core_documentation_recovery_engine]] → `contains` → [[assistant_app_core_documentation_recovery_engine_recoveryengine]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine]] → `method` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_encoding]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine]] → `method` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine]] → `method` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_wikilinks]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine]] → `method` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_generate_stub]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine]] → `method` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_get_valid_stems]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine]] → `method` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_inject_frontmatter]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine]] → `method` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_is_protected]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine]] → `method` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_match_stem]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine]] → `method` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_normalize_target]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine]] → `method` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_split_combined_link]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine]] → `method` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_standardize_sections]]
- [[assistant_app_core_documentation_recovery_engine_rationale_67]] → `rationale_for` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_is_protected]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]] → `calls` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_is_protected]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_is_protected]] → `references` → [[assistant_app_core_documentation_recovery_engine_py_path]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]] → `references` → [[assistant_app_core_documentation_recovery_engine_py_path]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_wikilinks]] → `references` → [[assistant_app_core_documentation_recovery_engine_py_path]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_generate_stub]] → `references` → [[assistant_app_core_documentation_recovery_engine_py_path]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_inject_frontmatter]] → `references` → [[assistant_app_core_documentation_recovery_engine_py_path]]
- [[assistant_app_core_documentation_recovery_engine_rationale_89]] → `rationale_for` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_encoding]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]] → `calls` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_encoding]]
- [[assistant_app_core_documentation_recovery_engine_rationale_109]] → `rationale_for` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_inject_frontmatter]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]] → `calls` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_inject_frontmatter]]
- [[assistant_app_core_documentation_recovery_engine_rationale_120]] → `rationale_for` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]] → `references` → [[assistant_app_core_documentation_recovery_engine_py_any]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]] → `calls` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_wikilinks]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]] → `calls` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_standardize_sections]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_docs_root]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_file]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_wikilinks]] → `calls` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_get_valid_stems]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_get_valid_stems]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_docs_root]]
- [[assistant_app_core_documentation_recovery_engine_rationale_198]] → `rationale_for` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_fix_wikilinks]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_match_stem]] → `calls` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_normalize_target]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_split_combined_link]] → `calls` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_normalize_target]]
- [[assistant_app_core_documentation_recovery_engine_rationale_367]] → `rationale_for` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_standardize_sections]]
- [[assistant_app_core_documentation_recovery_engine_rationale_398]] → `rationale_for` → [[assistant_app_core_documentation_recovery_engine_recoveryengine_generate_stub]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_generate_stub]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_docs_root]]
- [[assistant_app_core_documentation_recovery_engine_recoveryengine_generate_stub]] → `calls` → [[assistant_app_core_runtime_path_resolver_runtimepathresolver_resolve]]