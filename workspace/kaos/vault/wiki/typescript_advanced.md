# graphify\tests\fixtures\typescript_advanced.ts

## Símbolos

- [[graphify_tests_fixtures_typescript_advanced]] — code: typescript_advanced.ts
- [[graphify_tests_fixtures_typescript_advanced_iuserrepository]] — code: IUserRepository
- [[graphify_tests_fixtures_typescript_advanced_iuserrepository_findbyid]] — code: .findById()
- [[graphify_tests_fixtures_typescript_advanced_iuserrepository_save]] — code: .save()
- [[graphify_tests_fixtures_typescript_advanced_userstatus]] — code: UserStatus
- [[graphify_tests_fixtures_typescript_advanced_userid]] — code: UserId
- [[graphify_tests_fixtures_typescript_advanced_user_repository]] — code: USER_REPOSITORY
- [[graphify_tests_fixtures_typescript_advanced_default_roles]] — code: DEFAULT_ROLES
- [[graphify_tests_fixtures_typescript_advanced_user_config]] — code: USER_CONFIG
- [[graphify_tests_fixtures_typescript_advanced_userservice]] — code: UserService
- [[graphify_tests_fixtures_typescript_advanced_userservice_constructor]] — code: .constructor()
- [[graphify_tests_fixtures_typescript_advanced_userservice_create]] — code: .create()
- [[graphify_tests_fixtures_typescript_advanced_userservice_bulkcreate]] — code: .bulkCreate()
- [[graphify_tests_fixtures_typescript_advanced_userservice_getbyid]] — code: .getById()
- [[graphify_tests_fixtures_typescript_advanced_usermodule]] — code: UserModule

## Dependências

- [[graphify_tests_fixtures_typescript_advanced]] → `contains` → [[graphify_tests_fixtures_typescript_advanced_default_roles]]
- [[graphify_tests_fixtures_typescript_advanced]] → `contains` → [[graphify_tests_fixtures_typescript_advanced_iuserrepository]]
- [[graphify_tests_fixtures_typescript_advanced]] → `contains` → [[graphify_tests_fixtures_typescript_advanced_user_config]]
- [[graphify_tests_fixtures_typescript_advanced]] → `contains` → [[graphify_tests_fixtures_typescript_advanced_user_repository]]
- [[graphify_tests_fixtures_typescript_advanced]] → `contains` → [[graphify_tests_fixtures_typescript_advanced_userid]]
- [[graphify_tests_fixtures_typescript_advanced]] → `contains` → [[graphify_tests_fixtures_typescript_advanced_usermodule]]
- [[graphify_tests_fixtures_typescript_advanced]] → `indirect_call` → [[graphify_tests_fixtures_typescript_advanced_userservice]]
- [[graphify_tests_fixtures_typescript_advanced]] → `contains` → [[graphify_tests_fixtures_typescript_advanced_userstatus]]
- [[graphify_tests_fixtures_typescript_advanced_iuserrepository]] → `method` → [[graphify_tests_fixtures_typescript_advanced_iuserrepository_findbyid]]
- [[graphify_tests_fixtures_typescript_advanced_iuserrepository]] → `method` → [[graphify_tests_fixtures_typescript_advanced_iuserrepository_save]]
- [[graphify_tests_fixtures_typescript_advanced_userservice_getbyid]] → `calls` → [[graphify_tests_fixtures_typescript_advanced_iuserrepository_findbyid]]
- [[graphify_tests_fixtures_typescript_advanced_userservice]] → `method` → [[graphify_tests_fixtures_typescript_advanced_userservice_bulkcreate]]
- [[graphify_tests_fixtures_typescript_advanced_userservice]] → `method` → [[graphify_tests_fixtures_typescript_advanced_userservice_constructor]]
- [[graphify_tests_fixtures_typescript_advanced_userservice]] → `method` → [[graphify_tests_fixtures_typescript_advanced_userservice_create]]
- [[graphify_tests_fixtures_typescript_advanced_userservice]] → `method` → [[graphify_tests_fixtures_typescript_advanced_userservice_getbyid]]
- [[graphify_tests_fixtures_typescript_advanced_userservice]] → `references` → [[injectable]]
- [[graphify_tests_fixtures_typescript_advanced_usermodule]] → `references` → [[graphify_tests_fixtures_typescript_advanced_ts_module]]