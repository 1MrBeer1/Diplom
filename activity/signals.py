# activity/signals.py
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from tasks.models import Task
from activity.models import ActivityLog
from notifications.tasks import send_notification  # Placeholder для Celery

@receiver(pre_save, sender=Task)
def log_status_change(sender, instance, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.status != instance.status:
            # Рекурсивный лог для итераций (апдейты)
            ActivityLog.objects.create(
                user=instance.assignee or old_instance.assignee,
                task=instance,
                action='move',
                status_change=f"{old_instance.status} -> {instance.status}",
                description=f"Статус изменён. Что сделано: {instance.completion_notes if instance.status == 'выполнена' else ''}",
                department=instance.department
            )
            instance.update_progress()  # Авто-обновление progress
            # Уведомление: Рекурсивно для heads/testers
            if instance.status in ['выполнена', 'не_готова', 'баг_фикс']:
                send_notification.delay(instance.assignee.email, f"Задача {instance.title} обновлена")

@receiver(post_save, sender=Task)
def update_burndown(sender, instance, **kwargs):
    if instance.sprints.exists():  # Если в спринте, обновить метрики
        for sprint in instance.sprints.all():
            # Рекурсивный recalc для velocity (в views используем pandas для полного)
            pass  # Placeholder: Триггер на agile/views.py для burndown recalc