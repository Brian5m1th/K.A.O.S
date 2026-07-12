# assistant\app\router\intent_classifier.py

## Símbolos

- [[assistant_app_router_intent_classifier]] — code: intent_classifier.py
- [[assistant_app_router_intent_classifier_intentclassifier]] — code: IntentClassifier
- [[assistant_app_router_intent_classifier_intentclassifier_init]] — code: .__init__()
- [[assistant_app_router_intent_classifier_intentclassifier_get_provider]] — code: ._get_provider()
- [[assistant_app_router_intent_classifier_intentclassifier_match_keyword]] — code: ._match_keyword()
- [[assistant_app_router_intent_classifier_intentclassifier_classify]] — code: .classify()

## Dependências

- [[assistant_app_router_intent_classifier_intentclassifier]] → `uses` → [[assistant_app_domain_command_commandtype]]
- [[assistant_app_router_intent_classifier_intentclassifier]] → `uses` → [[assistant_app_domain_intent_intentresult]]
- [[assistant_app_router_intent_classifier_intentclassifier_classify]] → `references` → [[assistant_app_domain_intent_intentresult]]
- [[assistant_app_router_intent_classifier_intentclassifier_match_keyword]] → `references` → [[assistant_app_domain_intent_intentresult]]
- [[assistant_app_router_intent_classifier_intentclassifier]] → `uses` → [[assistant_app_domain_workflow_workflowtype]]
- [[assistant_app_router_intent_classifier_intentclassifier]] → `uses` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_router_intent_classifier_intentclassifier_get_provider]] → `calls` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_router_intent_classifier]] → `contains` → [[assistant_app_router_intent_classifier_intentclassifier]]
- [[assistant_app_router_intent_classifier_intentclassifier]] → `method` → [[assistant_app_router_intent_classifier_intentclassifier_classify]]
- [[assistant_app_router_intent_classifier_intentclassifier]] → `method` → [[assistant_app_router_intent_classifier_intentclassifier_get_provider]]
- [[assistant_app_router_intent_classifier_intentclassifier]] → `method` → [[assistant_app_router_intent_classifier_intentclassifier_init]]
- [[assistant_app_router_intent_classifier_intentclassifier]] → `method` → [[assistant_app_router_intent_classifier_intentclassifier_match_keyword]]
- [[assistant_app_router_intent_classifier_intentclassifier_classify]] → `calls` → [[assistant_app_router_intent_classifier_intentclassifier_get_provider]]
- [[assistant_app_router_intent_classifier_intentclassifier_classify]] → `calls` → [[assistant_app_router_intent_classifier_intentclassifier_match_keyword]]