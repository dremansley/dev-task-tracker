from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):

    class TaskPriority(models.TextChoices):
        LOW = "LOW", "Low Priority"
        MEDIUM = "MEDIUM", "Medium Priority"
        HIGH = "HIGH", "High Priority"

    class TaskStatus(models.TextChoices):
        TO_DO = "TO_DO", "To Do"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        FOR_QA = "FOR_QA", "For QA"
        DONE = "DONE", "Done"
    
    class TaskType(models.TextChoices):
        BUG = "BUG", "Bug"
        FEATURE = "FEATURE", "Feature"
        IMPROVEMENT = "IMPROVEMENT", "Improvement"

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    priority = models.CharField(
        max_length=6,
        choices=TaskPriority.choices,
        default=TaskPriority.MEDIUM
    )
    status = models.CharField(
        max_length=11,
        choices=TaskStatus.choices,
        default=TaskStatus.TO_DO
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
    type = models.CharField(
        max_length=15,
        choices=TaskType.choices,
        default=TaskType.FEATURE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    estimated_time = models.IntegerField(
        null=True,
        blank=True
        )
    
    @property
    def is_overdue(self):
        from django.utils import timezone
        return self.due_date and self.due_date < timezone.now() and self.status != self.TaskStatus.DONE
    
    def task_completion_time(self):
        from datetime import timedelta
        if self.status == self.TaskStatus.DONE and self.completion_date:
            return self.updated_at - self.created_at
        return timedelta(0)
    
    def save(self, *args, **kwargs):
        if self.status == Task.TaskStatus.DONE and not self.completion_date:
            self.completion_date = timezone.now()
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

