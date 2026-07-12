# assistant\app\api\notifications.py

## Símbolos

- [[assistant_app_api_notifications]] — code: notifications.py
- [[assistant_app_api_notifications_list_notifications]] — code: list_notifications()
- [[assistant_app_api_notifications_mark_read]] — code: mark_read()
- [[assistant_app_api_notifications_mark_all_read]] — code: mark_all_read()

## Dependências

- [[assistant_app_api_notifications]] → `contains` → [[assistant_app_api_notifications_list_notifications]]
- [[assistant_app_api_notifications]] → `contains` → [[assistant_app_api_notifications_mark_all_read]]
- [[assistant_app_api_notifications]] → `contains` → [[assistant_app_api_notifications_mark_read]]
- [[assistant_app_api_notifications]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_notifications_mark_read]] → `calls` → [[assistant_app_notifications_service_notificationservice_mark_read]]
- [[assistant_app_api_notifications_mark_all_read]] → `calls` → [[assistant_app_notifications_service_notificationservice_mark_all_read]]