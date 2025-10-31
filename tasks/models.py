from django.db import models

# Create your models here.
# tasks/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from projects.models import Project, Department


class KanbanColumn(models.Model):
    COLUMN_TYPES = [
        ('todo', 'To Do'),  # Поставлена
        ('in_progress', 'In Progress'),  # Выполняется
        ('done', 'Done'),  # Выполнена / Релиз
    ]
    name = models.CharField(max_length=50, choices=COLUMN_TYPES, verbose_name=_('Колонка'))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='columns', verbose_name=_('Проект'))
    order = models.IntegerField(default=0, verbose_name=_('Порядок'))

    class Meta:
        unique_together = ('project', 'name')
    
    def __str__(self):
        return f"{self.project.name} - {self.get_name_display()}"


class Task(models.Model):
    STATUS_CHOICES = [
        ('поставлена', _('Задача поставлена')),  # Начало, assign to worker
        ('выполняется', _('Задача выполняется')),  # Worker перемещает
        ('выполнена', _('Задача выполнена')),  # Worker завершает, to head for check
        ('на_проверке', _('На проверке')),  # Head reviews
        ('не_готова', _('Не готова')),  # Head returns with comment
        ('баг_фикс', _('Баг-фикс')),  # To worker for fix
        ('релиз', _('Релиз')),  # Final, after testing
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]
    
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    description = models.TextField(blank=True, verbose_name=_('Описание'))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', verbose_name=_('Проект'))
    column = models.ForeignKey(KanbanColumn, on_delete=models.CASCADE, related_name='tasks', default=1, verbose_name=_('Колонка'))
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks', verbose_name=_('Отдел'))
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks', verbose_name=_('Исполнитель'))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='поставлена', verbose_name=_('Статус'))
    reviewer_comment = models.TextField(blank=True, verbose_name=_('Комментарий проверяющего'))
    completion_notes = models.TextField(blank=True, verbose_name=_('Что сделано (при сдаче на проверку)'))
    progress = models.FloatField(default=0.0, verbose_name=_('Прогресс (0-1 для Agile)'))  # Для частичного завершения story_points
    story_points = models.PositiveIntegerField(default=1, verbose_name=_('Story Points'))  # Для Agile
    due_date = models.DateTimeField(null=True, blank=True, verbose_name=_('Срок'))
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium', verbose_name=_('Приоритет'))
    tags = models.JSONField(default=list, blank=True, verbose_name=_('Метки'))  # Для PostgreSQL
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Создано'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Обновлено'))

    class Meta:
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')
    
    def __str__(self):
        return f"{self.title} ({self.get_status_display()}) - {self.department}"
    
    def update_progress(self):
        """Автоматический расчёт progress по статусу (для итеративности)."""
        status_to_progress = {
            'поставлена': 0.0,
            'выполняется': 0.5,
            'выполнена': 0.8,
            'на_проверке': 0.8,
            'не_готова': 0.7,  # Частичное, для апдейтов
            'баг_фикс': 0.9,
            'релиз': 1.0,
        }
        self.progress = status_to_progress.get(self.status, 0.0)
        self.save(update_fields=['progress'])  # Рекурсивный вызов через signal