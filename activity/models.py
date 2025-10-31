# activity/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from projects.models import Project
from tasks.models import Task, Department


class ActivityLog(models.Model):
    ACTION_CHOICES = [
        ('create', 'Создано'),
        ('update', 'Обновлено'),
        ('delete', 'Удалено'),
        ('move', 'Перемещено'),  # Статус change
        ('comment', 'Комментарий'),
        ('review', 'Проверка'),  # Head review
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Проект'))
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Задача'))
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Отдел'))
    action = models.CharField(max_length=20, choices=ACTION_CHOICES, verbose_name=_('Действие'))
    status_change = models.CharField(max_length=20, blank=True, verbose_name=_('Изменение статуса'))  # e.g., 'поставлена -> выполняется'
    description = models.TextField(verbose_name=_('Описание'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('Время'))

    class Meta:
        verbose_name = _('Лог активности')
        verbose_name_plural = _('Логи активности')
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user} - {self.action} ({self.timestamp})"