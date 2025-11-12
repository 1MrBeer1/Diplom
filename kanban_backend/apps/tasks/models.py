from django.db import models
from django.conf import settings
from django_fsm import FSMField, transition


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "To Do"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        CHECKING = "CHECKING", "Checking"
        DONE = "DONE", "Done"
        REJECTED = "REJECTED", "Rejected"
        BUGFIX = "BUGFIX", "Bug Fix"
        RELEASED = "RELEASED", "Released"

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE, related_name="tasks")
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks_assigned"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks_created"
    )

    # Kanban
    column = models.CharField(
        max_length=50,
        choices=Status.choices,
        default=Status.TODO,
        help_text="Текущая колонка на Kanban-доске",
    )
    order = models.PositiveIntegerField(default=0)

    status = FSMField(max_length=32, default=Status.TODO, choices=Status.choices, protected=True) # type: ignore
    department = models.CharField(max_length=100, blank=True)
    priority = models.CharField(max_length=20, default="Medium")
    deadline = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.title} [{self.column}]"

    # FSM transitions
    @transition(field=status, source=Status.TODO, target=Status.IN_PROGRESS)
    def start(self): ...

    @transition(field=status, source=Status.IN_PROGRESS, target=Status.CHECKING)
    def submit_for_check(self): ...

    @transition(field=status, source=Status.CHECKING, target=Status.DONE)
    def approve(self): ...

    @transition(field=status, source="*", target=Status.REJECTED)
    def reject(self): ...

    @transition(field=status, source=Status.REJECTED, target=Status.TODO)
    def reopen(self): ...

    @transition(field=status, source=Status.DONE, target=Status.RELEASED)
    def release(self): ...
