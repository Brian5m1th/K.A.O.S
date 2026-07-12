# graphify\tests\fixtures\sample_scoped_calls.pas

## Símbolos

- [[graphify_tests_fixtures_sample_scoped_calls]] — code: sample_scoped_calls.pas
- [[graphify_tests_fixtures_sample_scoped_calls_scopedcallsunit]] — code: ScopedCallsUnit
- [[graphify_tests_fixtures_sample_scoped_calls_tfirstwidget]] — code: TFirstWidget
- [[graphify_tests_fixtures_sample_scoped_calls_pas_tobject]] — code: TObject
- [[graphify_tests_fixtures_sample_scoped_calls_tfirstwidget_configure]] — code: Configure()
- [[graphify_tests_fixtures_sample_scoped_calls_tfirstwidget_reset]] — code: Reset()
- [[graphify_tests_fixtures_sample_scoped_calls_tsecondwidget]] — code: TSecondWidget
- [[graphify_tests_fixtures_sample_scoped_calls_tsecondwidget_configure]] — code: Configure()
- [[graphify_tests_fixtures_sample_scoped_calls_tsecondwidget_reset]] — code: Reset()
- [[graphify_tests_fixtures_sample_scoped_calls_tbasewidget]] — code: TBaseWidget
- [[graphify_tests_fixtures_sample_scoped_calls_tbasewidget_prepare]] — code: Prepare()
- [[graphify_tests_fixtures_sample_scoped_calls_tderivedwidget]] — code: TDerivedWidget
- [[graphify_tests_fixtures_sample_scoped_calls_tderivedwidget_run]] — code: Run()

## Dependências

- [[graphify_tests_fixtures_sample_scoped_calls]] → `contains` → [[graphify_tests_fixtures_sample_scoped_calls_scopedcallsunit]]
- [[graphify_tests_fixtures_sample_scoped_calls_scopedcallsunit]] → `contains` → [[graphify_tests_fixtures_sample_scoped_calls_tbasewidget]]
- [[graphify_tests_fixtures_sample_scoped_calls_scopedcallsunit]] → `contains` → [[graphify_tests_fixtures_sample_scoped_calls_tderivedwidget]]
- [[graphify_tests_fixtures_sample_scoped_calls_scopedcallsunit]] → `contains` → [[graphify_tests_fixtures_sample_scoped_calls_tfirstwidget]]
- [[graphify_tests_fixtures_sample_scoped_calls_scopedcallsunit]] → `contains` → [[graphify_tests_fixtures_sample_scoped_calls_tsecondwidget]]
- [[graphify_tests_fixtures_sample_scoped_calls_tfirstwidget]] → `inherits` → [[graphify_tests_fixtures_sample_scoped_calls_pas_tobject]]
- [[graphify_tests_fixtures_sample_scoped_calls_tfirstwidget]] → `method` → [[graphify_tests_fixtures_sample_scoped_calls_tfirstwidget_configure]]
- [[graphify_tests_fixtures_sample_scoped_calls_tfirstwidget]] → `method` → [[graphify_tests_fixtures_sample_scoped_calls_tfirstwidget_reset]]
- [[graphify_tests_fixtures_sample_scoped_calls_tbasewidget]] → `inherits` → [[graphify_tests_fixtures_sample_scoped_calls_pas_tobject]]
- [[graphify_tests_fixtures_sample_scoped_calls_tsecondwidget]] → `inherits` → [[graphify_tests_fixtures_sample_scoped_calls_pas_tobject]]
- [[graphify_tests_fixtures_sample_scoped_calls_tfirstwidget_configure]] → `calls` → [[graphify_tests_fixtures_sample_scoped_calls_tfirstwidget_reset]]
- [[graphify_tests_fixtures_sample_scoped_calls_tsecondwidget]] → `method` → [[graphify_tests_fixtures_sample_scoped_calls_tsecondwidget_configure]]
- [[graphify_tests_fixtures_sample_scoped_calls_tsecondwidget]] → `method` → [[graphify_tests_fixtures_sample_scoped_calls_tsecondwidget_reset]]
- [[graphify_tests_fixtures_sample_scoped_calls_tsecondwidget_configure]] → `calls` → [[graphify_tests_fixtures_sample_scoped_calls_tsecondwidget_reset]]
- [[graphify_tests_fixtures_sample_scoped_calls_tbasewidget]] → `method` → [[graphify_tests_fixtures_sample_scoped_calls_tbasewidget_prepare]]
- [[graphify_tests_fixtures_sample_scoped_calls_tderivedwidget]] → `inherits` → [[graphify_tests_fixtures_sample_scoped_calls_tbasewidget]]
- [[graphify_tests_fixtures_sample_scoped_calls_tderivedwidget_run]] → `calls` → [[graphify_tests_fixtures_sample_scoped_calls_tbasewidget_prepare]]
- [[graphify_tests_fixtures_sample_scoped_calls_tderivedwidget]] → `method` → [[graphify_tests_fixtures_sample_scoped_calls_tderivedwidget_run]]