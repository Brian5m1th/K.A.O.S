# assistant\app\llm\metrics.py

## Símbolos

- [[assistant_app_llm_metrics]] — code: metrics.py
- [[assistant_app_llm_metrics_metricentry]] — code: MetricEntry
- [[assistant_app_llm_metrics_providermetrics]] — code: ProviderMetrics
- [[assistant_app_llm_metrics_providermetrics_init]] — code: .__init__()
- [[assistant_app_llm_metrics_providermetrics_record]] — code: .record()
- [[assistant_app_llm_metrics_providermetrics_ainvoke_and_record]] — code: .ainvoke_and_record()
- [[assistant_app_llm_metrics_providermetrics_estimate_cost]] — code: ._estimate_cost()
- [[assistant_app_llm_metrics_providermetrics_summary]] — code: .summary()
- [[assistant_app_llm_metrics_providermetrics_global_summary]] — code: .global_summary()
- [[assistant_app_llm_metrics_providermetrics_global_token_rate]] — code: .global_token_rate()
- [[assistant_app_llm_metrics_rationale_108]] — code: Aggregate metrics across all ProviderMetrics instances.
- [[assistant_app_llm_metrics_rationale_124]] — code: Approximate token throughput (tokens/sec) from recent global entries.

## Dependências

- [[assistant_app_llm_metrics]] → `contains` → [[assistant_app_llm_metrics_metricentry]]
- [[assistant_app_llm_metrics]] → `contains` → [[assistant_app_llm_metrics_providermetrics]]
- [[assistant_app_llm_metrics_providermetrics_ainvoke_and_record]] → `calls` → [[assistant_app_llm_metrics_metricentry]]
- [[assistant_app_llm_metrics_providermetrics_record]] → `references` → [[assistant_app_llm_metrics_metricentry]]
- [[assistant_app_llm_metrics_providermetrics]] → `method` → [[assistant_app_llm_metrics_providermetrics_ainvoke_and_record]]
- [[assistant_app_llm_metrics_providermetrics]] → `method` → [[assistant_app_llm_metrics_providermetrics_estimate_cost]]
- [[assistant_app_llm_metrics_providermetrics]] → `method` → [[assistant_app_llm_metrics_providermetrics_global_summary]]
- [[assistant_app_llm_metrics_providermetrics]] → `method` → [[assistant_app_llm_metrics_providermetrics_global_token_rate]]
- [[assistant_app_llm_metrics_providermetrics]] → `method` → [[assistant_app_llm_metrics_providermetrics_init]]
- [[assistant_app_llm_metrics_providermetrics]] → `method` → [[assistant_app_llm_metrics_providermetrics_record]]
- [[assistant_app_llm_metrics_providermetrics]] → `method` → [[assistant_app_llm_metrics_providermetrics_summary]]
- [[assistant_app_llm_metrics_providermetrics_ainvoke_and_record]] → `calls` → [[assistant_app_llm_metrics_providermetrics_record]]
- [[assistant_app_llm_metrics_providermetrics_ainvoke_and_record]] → `calls` → [[assistant_app_llm_metrics_providermetrics_estimate_cost]]
- [[assistant_app_llm_metrics_providermetrics_ainvoke_and_record]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_llm_metrics_rationale_108]] → `rationale_for` → [[assistant_app_llm_metrics_providermetrics_global_summary]]
- [[assistant_app_llm_metrics_rationale_124]] → `rationale_for` → [[assistant_app_llm_metrics_providermetrics_global_token_rate]]