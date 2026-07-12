# graphify\tests\fixtures\bindings.xaml

## Símbolos

- [[graphify_tests_fixtures_bindings]] — code: bindings.xaml
- [[graphify_tests_fixtures_bindings_window]] — code: Window
- [[binding_invoice_tax]] — code: Invoice.Tax
- [[binding_converter_taxconverter]] — code: TaxConverter
- [[graphify_tests_fixtures_bindings_rootpanel]] — code: RootPanel
- [[graphify_tests_fixtures_bindings_xaml_xaml_stackpanel]] — code: StackPanel
- [[graphify_tests_fixtures_bindings_usertext]] — code: UserText
- [[xaml_textblock]] — code: TextBlock
- [[binding_user_name]] — code: User.Name
- [[graphify_tests_fixtures_bindings_totaltext]] — code: TotalText
- [[binding_order_total]] — code: Order.Total
- [[binding_converter_moneyconverter]] — code: MoneyConverter
- [[graphify_tests_fixtures_bindings_savebutton]] — code: SaveButton
- [[graphify_tests_fixtures_bindings_xaml_xaml_button]] — code: Button
- [[graphify_tests_fixtures_bindings_xaml_binding_savecommand]] — code: SaveCommand
- [[graphify_tests_fixtures_bindings_modetext]] — code: ModeText

## Dependências

- [[graphify_tests_fixtures_bindings]] → `contains` → [[graphify_tests_fixtures_bindings_window]]
- [[graphify_tests_fixtures_bindings_window]] → `references` → [[binding_converter_taxconverter]]
- [[graphify_tests_fixtures_bindings_window]] → `references` → [[binding_invoice_tax]]
- [[graphify_tests_fixtures_bindings_window]] → `contains` → [[graphify_tests_fixtures_bindings_modetext]]
- [[graphify_tests_fixtures_bindings_window]] → `contains` → [[graphify_tests_fixtures_bindings_rootpanel]]
- [[graphify_tests_fixtures_bindings_window]] → `contains` → [[graphify_tests_fixtures_bindings_savebutton]]
- [[graphify_tests_fixtures_bindings_window]] → `contains` → [[graphify_tests_fixtures_bindings_totaltext]]
- [[graphify_tests_fixtures_bindings_window]] → `contains` → [[graphify_tests_fixtures_bindings_usertext]]
- [[graphify_tests_fixtures_bindings_rootpanel]] → `references` → [[graphify_tests_fixtures_bindings_xaml_xaml_stackpanel]]
- [[graphify_tests_fixtures_bindings_usertext]] → `references` → [[binding_user_name]]
- [[graphify_tests_fixtures_bindings_usertext]] → `references` → [[xaml_textblock]]
- [[graphify_tests_fixtures_bindings_modetext]] → `references` → [[xaml_textblock]]
- [[graphify_tests_fixtures_bindings_totaltext]] → `references` → [[xaml_textblock]]
- [[graphify_tests_fixtures_bindings_totaltext]] → `references` → [[binding_converter_moneyconverter]]
- [[graphify_tests_fixtures_bindings_totaltext]] → `references` → [[binding_order_total]]
- [[graphify_tests_fixtures_bindings_savebutton]] → `references` → [[graphify_tests_fixtures_bindings_xaml_binding_savecommand]]
- [[graphify_tests_fixtures_bindings_savebutton]] → `references` → [[graphify_tests_fixtures_bindings_xaml_xaml_button]]