# assistant\app\notifications\service.py

## Símbolos

- [[assistant_app_notifications_service]] — code: service.py
- [[assistant_app_notifications_service_notificationservice]] — code: NotificationService
- [[assistant_app_notifications_service_notificationservice_notify]] — code: .notify()
- [[assistant_app_notifications_service_notificationservice_list]] — code: .list()
- [[assistant_app_notifications_service_notificationservice_mark_read]] — code: .mark_read()
- [[assistant_app_notifications_service_notificationservice_mark_all_read]] — code: .mark_all_read()
- [[assistant_app_notifications_service_notificationservice_clear]] — code: .clear()

## Dependências

- [[assistant_app_notifications_service_notificationservice_notify]] → `references` → [[assistant_app_notifications_models_notificationlevel]]
- [[assistant_app_notifications_service_notificationservice_list]] → `references` → [[assistant_app_notifications_models_notification]]
- [[assistant_app_notifications_service_notificationservice_notify]] → `references` → [[assistant_app_notifications_models_notification]]
- [[assistant_app_notifications_service]] → `contains` → [[assistant_app_notifications_service_notificationservice]]
- [[assistant_app_notifications_service_notificationservice]] → `method` → [[assistant_app_notifications_service_notificationservice_clear]]
- [[assistant_app_notifications_service_notificationservice]] → `method` → [[assistant_app_notifications_service_notificationservice_list]]
- [[assistant_app_notifications_service_notificationservice]] → `method` → [[assistant_app_notifications_service_notificationservice_mark_all_read]]
- [[assistant_app_notifications_service_notificationservice]] → `method` → [[assistant_app_notifications_service_notificationservice_mark_read]]
- [[assistant_app_notifications_service_notificationservice]] → `method` → [[assistant_app_notifications_service_notificationservice_notify]]