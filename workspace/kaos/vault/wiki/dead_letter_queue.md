# assistant\app\orchestrator\dead_letter_queue.py

## Símbolos

- [[assistant_app_orchestrator_dead_letter_queue]] — code: dead_letter_queue.py
- [[assistant_app_orchestrator_dead_letter_queue_failedexecution]] — code: FailedExecution
- [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue]] — code: DeadLetterQueue
- [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_add]] — code: .add()
- [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_list_all]] — code: .list_all()
- [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_count]] — code: .count()
- [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_clear]] — code: .clear()

## Dependências

- [[assistant_app_orchestrator_dead_letter_queue]] → `contains` → [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue]]
- [[assistant_app_orchestrator_dead_letter_queue]] → `contains` → [[assistant_app_orchestrator_dead_letter_queue_failedexecution]]
- [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_add]] → `references` → [[assistant_app_orchestrator_dead_letter_queue_failedexecution]]
- [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_list_all]] → `references` → [[assistant_app_orchestrator_dead_letter_queue_failedexecution]]
- [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue]] → `method` → [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_add]]
- [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue]] → `method` → [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_clear]]
- [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue]] → `method` → [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_count]]
- [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue]] → `method` → [[assistant_app_orchestrator_dead_letter_queue_deadletterqueue_list_all]]