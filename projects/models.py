from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    project_start = models.DateTimeField(null=True,blank=True)
    project_expiry = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    