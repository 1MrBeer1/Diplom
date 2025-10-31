from django.db import models

# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    ROLE_CHOICES = [
        ('seo', _('SEO')),  # Создаёт проекты, видит все этапы
        ('admin', _('Администратор')),  # Технический мониторинг (логи, сервер)
        ('head_design', _('Начальник отдела дизайнеров')),
        ('head_frontend', _('Начальник отдела фронтенд-разработчиков')),
        ('head_backend', _('Начальник отдела бэкенд-разработчиков')),
        ('head_testing', _('Начальник отдела тестировщиков')),
        ('worker_design', _('Дизайнер')),
        ('worker_frontend', _('Фронтенд-разработчик')),
        ('worker_backend', _('Бэкенд-разработчик')),
        ('worker_testing', _('Тестировщик')),
    ]
    
    role = models.CharField(
        max_length=20,  # Увеличено для новых ролей
        choices=ROLE_CHOICES,
        default='worker_design',  # По умолчанию базовый worker
        verbose_name=_('Роль')
    )
    email = models.EmailField(
        unique=True,
        verbose_name=_('Email')
    )
    department = models.ForeignKey('projects.Department', on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"