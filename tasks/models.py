from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    class Priority(models.TextChoices):
        LOW = "LOW", "Low Priority"
        MEDIUM = "MEDIUM", "Medium Priority"
        HIGH = "HIGH", "High Priority"

    class Status(models.TextChoices):
        TO_DO = "TO_DO", "To Do"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        FOR_QA = "FOR_QA", "For QA"
        DONE = "DONE", "Done"

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    priority = models.CharField(
        max_length=6,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    status = models.CharField(
        max_length=11,
        choices=Status.choices,
        default=Status.TO_DO
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks_created"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks_assigned"
    )
    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)

    estimated_time = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.title
