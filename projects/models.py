from django.db import models

# Create your models here.
# projects/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User


class Department(models.Model):
    DEPARTMENT_CHOICES = [
        ('design', _('Дизайнеры')),
        ('frontend', _('Фронтенд-разработчики')),
        ('backend', _('Бэкенд-разработчики')),
        ('testing', _('Тестировщики')),
    ]
    
    name = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, unique=True, verbose_name=_('Отдел'))
    
    class Meta:
        verbose_name = _('Отдел')
        verbose_name_plural = _('Отделы')
    
    def __str__(self):
        return self.get_name_display()


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(blank=True, verbose_name=_('Описание'))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects', verbose_name=_('Создал'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Создано'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Обновлено'))
    departments = models.ManyToManyField(Department, related_name='projects', blank=True, verbose_name=_('Отделы'))  # Для распределения
    members = models.ManyToManyField(User, related_name='projects', blank=True, verbose_name=_('Участники'))

    class Meta:
        verbose_name = _('Проект')
        verbose_name_plural = _('Проекты')
    
    def __str__(self):
        return self.name