# kaos-research\technology-observatory\observatory.py

## Símbolos

- [[kaos_research_technology_observatory_observatory]] — code: observatory.py
- [[kaos_research_technology_observatory_observatory_check_github_repo]] — code: check_github_repo()
- [[kaos_research_technology_observatory_observatory_check_pypi_version]] — code: check_pypi_version()
- [[kaos_research_technology_observatory_observatory_main]] — code: main()
- [[kaos_research_technology_observatory_observatory_rationale_1]] — code: Technology Observatory — Continuous tech ecosystem monitoring.  Tracks GitHub ac
- [[kaos_research_technology_observatory_observatory_rationale_45]] — code: Check GitHub repo stats via gh CLI (requires gh auth).
- [[kaos_research_technology_observatory_observatory_rationale_59]] — code: Check latest PyPI version via pip index.

## Dependências

- [[kaos_research_technology_observatory_observatory]] → `contains` → [[kaos_research_technology_observatory_observatory_check_github_repo]]
- [[kaos_research_technology_observatory_observatory]] → `contains` → [[kaos_research_technology_observatory_observatory_check_pypi_version]]
- [[kaos_research_technology_observatory_observatory]] → `contains` → [[kaos_research_technology_observatory_observatory_main]]
- [[kaos_research_technology_observatory_observatory_rationale_1]] → `rationale_for` → [[kaos_research_technology_observatory_observatory]]
- [[kaos_research_technology_observatory_observatory_main]] → `calls` → [[kaos_research_technology_observatory_observatory_check_github_repo]]
- [[kaos_research_technology_observatory_observatory_rationale_45]] → `rationale_for` → [[kaos_research_technology_observatory_observatory_check_github_repo]]
- [[kaos_research_technology_observatory_observatory_main]] → `calls` → [[kaos_research_technology_observatory_observatory_check_pypi_version]]
- [[kaos_research_technology_observatory_observatory_rationale_59]] → `rationale_for` → [[kaos_research_technology_observatory_observatory_check_pypi_version]]