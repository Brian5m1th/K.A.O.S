---
description: Regras TypeScript para o K.A.O.S
globs: ["desktop/**/*.ts", "desktop/**/*.tsx"]
---
# TypeScript Rules

- Strict mode obrigatorio (tsconfig strict: true)
- Imports absolutos com `@/` (`@/shared/ui/button`)
- `import type` para imports type-only
- Nao use `any` — prefira `unknown` e type guards
- Use `interface` para props de componentes, `type` para unions
- Nao use `export default` para hooks ou utilitarios (apenas paginas)
- Nao deixe `TODO`, `FIXME` ou `console.log` em codigo final
- Use `const` em vez de `let` sempre que possivel
- Mantenho componentes com menos de 200 linhas
- Funcoes puras e hooks customizados em vez de logica inline
- Nao use `@ts-ignore` ou `@ts-expect-error` sem justificativa documentada
