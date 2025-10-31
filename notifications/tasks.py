# notifications/tasks.py
from celery import shared_task
from django.core.mail import send_mail  # Placeholder для email (опционально)

@shared_task
def send_notification(email, message):
    """
    Placeholder Celery task для уведомлений (email или Slack).
    В бета-версии — print; позже — реальный send_mail.
    """
    print(f"Notification sent to {email}: {message}")  # Заглушка для теста
    # Реальная логика (раскомментируй позже):
    # send_mail(
    #     'Kanban Update',
    #     message,
    #     'from@kanban.com',  # Настрой EMAIL_HOST в settings
    #     [email],
    #     fail_silently=False,
    # )
    return "Notification sent"