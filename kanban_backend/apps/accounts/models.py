from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Roles(models.TextChoices):
        CEO = "CEO", "CEO"
        ADMIN = "ADMIN", "Admin"
        HEAD_DESIGN = "HEAD_DESIGN", "Head Design"
        DESIGNER = "DESIGNER", "Designer"
        HEAD_BACKEND = "HEAD_BACKEND", "Head Backend"
        BACKEND_DEV = "BACKEND_DEV", "Backend Dev"
        HEAD_FRONTEND = "HEAD_FRONTEND", "Head Frontend"
        FRONTEND_DEV = "FRONTEND_DEV", "Frontend Dev"
        HEAD_QA = "HEAD_QA", "Head QA"
        QA_TESTER = "QA_TESTER", "QA Tester"

    role = models.CharField(max_length=32, choices=Roles.choices, default=Roles.ADMIN)
    department = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
