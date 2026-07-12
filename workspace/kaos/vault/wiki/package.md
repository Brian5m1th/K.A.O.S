# package.json

## Símbolos

- [[package]] — code: package.json
- [[package_name]] — code: name
- [[package_version]] — code: version
- [[package_type]] — code: type
- [[package_private]] — code: private
- [[package_description]] — code: description
- [[package_scripts]] — code: scripts
- [[package_scripts_commitlint]] — code: commitlint
- [[package_devdependencies]] — code: devDependencies
- [[package_devdependencies_commitlint_cli]] — code: @commitlint/cli
- [[commitlint_cli]] — code: @commitlint/cli
- [[package_devdependencies_commitlint_config_conventional]] — code: @commitlint/config-conventional
- [[commitlint_config_conventional]] — code: @commitlint/config-conventional

## Dependências

- [[package]] → `contains` → [[package_description]]
- [[package]] → `contains` → [[package_devdependencies]]
- [[package]] → `contains` → [[package_name]]
- [[package]] → `contains` → [[package_private]]
- [[package]] → `contains` → [[package_scripts]]
- [[package]] → `contains` → [[package_type]]
- [[package]] → `contains` → [[package_version]]
- [[package_scripts]] → `contains` → [[package_scripts_commitlint]]
- [[package_devdependencies]] → `contains` → [[package_devdependencies_commitlint_cli]]
- [[package_devdependencies]] → `contains` → [[package_devdependencies_commitlint_config_conventional]]
- [[package_devdependencies_commitlint_cli]] → `imports` → [[commitlint_cli]]
- [[package_devdependencies_commitlint_config_conventional]] → `imports` → [[commitlint_config_conventional]]