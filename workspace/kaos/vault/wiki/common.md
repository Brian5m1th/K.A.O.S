# .specify\scripts\powershell\common.ps1

## Símbolos

- [[specify_scripts_powershell_common]] — code: common.ps1
- [[specify_scripts_powershell_common_find_specifyroot]] — code: Find-SpecifyRoot()
- [[specify_scripts_powershell_common_resolve_specifyinitdir]] — code: Resolve-SpecifyInitDir()
- [[specify_scripts_powershell_common_get_reporoot]] — code: Get-RepoRoot()
- [[specify_scripts_powershell_common_get_currentbranch]] — code: Get-CurrentBranch()
- [[specify_scripts_powershell_common_save_featurejson]] — code: Save-FeatureJson()
- [[specify_scripts_powershell_common_get_featurepathsenv]] — code: Get-FeaturePathsEnv()
- [[specify_scripts_powershell_common_test_fileexists]] — code: Test-FileExists()
- [[specify_scripts_powershell_common_test_dirhasfiles]] — code: Test-DirHasFiles()
- [[specify_scripts_powershell_common_get_invokeseparator]] — code: Get-InvokeSeparator()
- [[specify_scripts_powershell_common_format_speckitcommand]] — code: Format-SpecKitCommand()
- [[specify_scripts_powershell_common_get_python3command]] — code: Get-Python3Command()
- [[specify_scripts_powershell_common_resolve_template]] — code: Resolve-Template()
- [[specify_scripts_powershell_common_resolve_templatecontent]] — code: Resolve-TemplateContent()

## Dependências

- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_find_specifyroot]]
- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_format_speckitcommand]]
- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_get_currentbranch]]
- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_get_featurepathsenv]]
- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_get_invokeseparator]]
- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_get_python3command]]
- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_get_reporoot]]
- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_resolve_specifyinitdir]]
- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_resolve_template]]
- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_resolve_templatecontent]]
- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_save_featurejson]]
- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_test_dirhasfiles]]
- [[specify_scripts_powershell_common]] → `contains` → [[specify_scripts_powershell_common_test_fileexists]]
- [[specify_scripts_powershell_common_get_reporoot]] → `calls` → [[specify_scripts_powershell_common_find_specifyroot]]
- [[specify_scripts_powershell_common_get_reporoot]] → `calls` → [[specify_scripts_powershell_common_resolve_specifyinitdir]]
- [[specify_scripts_powershell_common_get_featurepathsenv]] → `calls` → [[specify_scripts_powershell_common_get_reporoot]]
- [[specify_scripts_powershell_common_get_featurepathsenv]] → `calls` → [[specify_scripts_powershell_common_get_currentbranch]]
- [[specify_scripts_powershell_common_get_featurepathsenv]] → `calls` → [[specify_scripts_powershell_common_save_featurejson]]
- [[specify_scripts_powershell_common_format_speckitcommand]] → `calls` → [[specify_scripts_powershell_common_get_invokeseparator]]
- [[specify_scripts_powershell_common_resolve_templatecontent]] → `calls` → [[specify_scripts_powershell_common_get_python3command]]