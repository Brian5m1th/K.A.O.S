---
description: Regras GitHub Actions para o K.A.O.S
globs: [".github/**/*.yml", ".github/**/*.yaml"]
---
# GitHub Actions Rules

- CI obrigatorio em todo PR: ruff + pytest + tsc
- Secrets nunca hardcoded — use `${{ secrets.XXX }}`
- Cache de dependencias Python (uv) e Node (npm)
- Build desktop apenas em tags de release
- Nao execute workflows completos em `push` para branches de feature
- Use `matrix` para testar multiplas versoes quando necessario
- Timeout razoavel: 10min para CI, 30min para release
- Notificacoes apenas em falha
