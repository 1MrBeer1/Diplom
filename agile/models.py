from django.db import models

# Create your models here.
# agile/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from tasks.models import Task
from accounts.models import User


class Sprint(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название спринта'))
    start_date = models.DateField(verbose_name=_('Дата начала'))
    end_date = models.DateField(verbose_name=_('Дата окончания'))
    goal = models.TextField(blank=True, verbose_name=_('Цель спринта'))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sprints', verbose_name=_('Создал'))
    tasks = models.ManyToManyField(Task, blank=True, related_name='sprints', verbose_name=_('Задачи спринта'))

    class Meta:
        verbose_name = _('Спринт')
        verbose_name_plural = _('Спринты')
    
    def __str__(self):
        return self.name

    def calculate_burndown_data(self):
        """Расчёт burndown: velocity = sum(story_points * progress) по дням (используем в views с pandas)."""
        # Placeholder: В views.py реализуем с pandas для JSON/чарта
        total_points = self.tasks.aggregate(total=models.Sum('story_points'))['total'] or 0
        completed_points = sum(task.story_points * task.progress for task in self.tasks.all())
        return {'total': total_points, 'completed': completed_points, 'remaining': total_points - completed_points}