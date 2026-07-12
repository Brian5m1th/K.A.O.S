# assistant\app\domain\ports\evidence_port.py

## Símbolos

- [[assistant_app_domain_ports_evidence_port]] — code: evidence_port.py
- [[assistant_app_domain_ports_evidence_port_evidencelevel]] — code: EvidenceLevel
- [[assistant_app_domain_ports_evidence_port_evidencemetric]] — code: EvidenceMetric
- [[assistant_app_domain_ports_evidence_port_evidencereport]] — code: EvidenceReport
- [[assistant_app_domain_ports_evidence_port_evidenceport]] — code: EvidencePort
- [[assistant_app_domain_ports_evidence_port_evidenceport_provider_name]] — code: .provider_name()
- [[assistant_app_domain_ports_evidence_port_evidenceport_collect]] — code: .collect()
- [[assistant_app_domain_ports_evidence_port_evidenceport_get_metric]] — code: .get_metric()
- [[assistant_app_domain_ports_evidence_port_evidenceport_get_history]] — code: .get_history()
- [[assistant_app_domain_ports_evidence_port_evidenceport_health]] — code: .health()
- [[assistant_app_domain_ports_evidence_port_rationale_1]] — code: EvidencePort — Architecture evidence and decision support capability.  Aggregate
- [[assistant_app_domain_ports_evidence_port_rationale_28]] — code: A single evidence data point.
- [[assistant_app_domain_ports_evidence_port_rationale_40]] — code: Aggregated evidence report from all sources.
- [[assistant_app_domain_ports_evidence_port_rationale_52]] — code: Interface for evidence collection and architectural health assessment.      Sour
- [[assistant_app_domain_ports_evidence_port_rationale_74]] — code: Collect evidence from all configured sources.
- [[assistant_app_domain_ports_evidence_port_rationale_79]] — code: Get a specific evidence metric by name.
- [[assistant_app_domain_ports_evidence_port_rationale_84]] — code: Get historical evidence data for trend analysis.
- [[assistant_app_domain_ports_evidence_port_rationale_89]] — code: Check if all evidence sources are available.

## Dependências

- [[assistant_app_domain_ports_evidence_port]] → `contains` → [[assistant_app_domain_ports_evidence_port_evidencelevel]]
- [[assistant_app_domain_ports_evidence_port]] → `contains` → [[assistant_app_domain_ports_evidence_port_evidencemetric]]
- [[assistant_app_domain_ports_evidence_port]] → `contains` → [[assistant_app_domain_ports_evidence_port_evidenceport]]
- [[assistant_app_domain_ports_evidence_port]] → `contains` → [[assistant_app_domain_ports_evidence_port_evidencereport]]
- [[assistant_app_domain_ports_evidence_port]] → `imports_from` → [[assistant_app_domain_ports_evidence_port_py_abc]]
- [[assistant_app_domain_ports_evidence_port]] → `imports_from` → [[assistant_app_domain_ports_evidence_port_py_enum]]
- [[assistant_app_domain_ports_evidence_port_rationale_1]] → `rationale_for` → [[assistant_app_domain_ports_evidence_port]]
- [[assistant_app_domain_ports_evidence_port_evidencelevel]] → `inherits` → [[assistant_app_domain_ports_evidence_port_py_enum]]
- [[assistant_app_domain_ports_evidence_port_evidencelevel]] → `inherits` → [[assistant_app_domain_ports_evidence_port_py_str]]
- [[assistant_app_domain_ports_evidence_port_evidenceport_get_history]] → `references` → [[assistant_app_domain_ports_evidence_port_evidencemetric]]
- [[assistant_app_domain_ports_evidence_port_evidenceport_get_metric]] → `references` → [[assistant_app_domain_ports_evidence_port_evidencemetric]]
- [[assistant_app_domain_ports_evidence_port_rationale_28]] → `rationale_for` → [[assistant_app_domain_ports_evidence_port_evidencemetric]]
- [[assistant_app_domain_ports_evidence_port_evidenceport_collect]] → `references` → [[assistant_app_domain_ports_evidence_port_evidencereport]]
- [[assistant_app_domain_ports_evidence_port_rationale_40]] → `rationale_for` → [[assistant_app_domain_ports_evidence_port_evidencereport]]
- [[assistant_app_domain_ports_evidence_port_evidenceport]] → `method` → [[assistant_app_domain_ports_evidence_port_evidenceport_collect]]
- [[assistant_app_domain_ports_evidence_port_evidenceport]] → `method` → [[assistant_app_domain_ports_evidence_port_evidenceport_get_history]]
- [[assistant_app_domain_ports_evidence_port_evidenceport]] → `method` → [[assistant_app_domain_ports_evidence_port_evidenceport_get_metric]]
- [[assistant_app_domain_ports_evidence_port_evidenceport]] → `method` → [[assistant_app_domain_ports_evidence_port_evidenceport_health]]
- [[assistant_app_domain_ports_evidence_port_evidenceport]] → `method` → [[assistant_app_domain_ports_evidence_port_evidenceport_provider_name]]
- [[assistant_app_domain_ports_evidence_port_evidenceport]] → `inherits` → [[assistant_app_domain_ports_evidence_port_py_abc]]
- [[assistant_app_domain_ports_evidence_port_rationale_52]] → `rationale_for` → [[assistant_app_domain_ports_evidence_port_evidenceport]]
- [[assistant_app_domain_ports_evidence_port_rationale_74]] → `rationale_for` → [[assistant_app_domain_ports_evidence_port_evidenceport_collect]]
- [[assistant_app_domain_ports_evidence_port_rationale_79]] → `rationale_for` → [[assistant_app_domain_ports_evidence_port_evidenceport_get_metric]]
- [[assistant_app_domain_ports_evidence_port_rationale_84]] → `rationale_for` → [[assistant_app_domain_ports_evidence_port_evidenceport_get_history]]
- [[assistant_app_domain_ports_evidence_port_rationale_89]] → `rationale_for` → [[assistant_app_domain_ports_evidence_port_evidenceport_health]]