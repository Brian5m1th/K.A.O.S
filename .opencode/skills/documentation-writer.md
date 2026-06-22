---
description: Skill para documentacao no K.A.O.S
---
# Documentation Writer

## Descricao
Criacao e manutencao de documentacao tecnica seguindo o schema Obsidian e KIRL.

## Responsabilidades
- Criar SDDs seguindo template padrao (YAML frontmatter + markdown)
- Manter documentacao do KIRL (FeatureRegistry, DRL, Audit)
- Escrever guias (instalacao, usuario, desenvolvedor, operacoes)
- Garantir frontmatter YAML completo (id, type, owner, status)
- Manter wikilinks entre documentos (`[[id]]`)
- Gerar documentacao automatica via KIRL (SDDGenerator, FeatureCatalog)

## Criterios de Qualidade
- Frontmatter YAML obrigatorio em todo documento
- Links bidirecionais entre documentos relacionados
- SDDs com secoes: Objetivo, Arquitetura, Implementacao, API, Testes
- Linguagem clara e objetiva
- Exemplos de uso reais (comandos, codigo)
