from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    project_start = models.DateTimeField(null=True,blank=True)
    project_expiry = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    project_lead = models.ForeignKey(CustomUser, related_name="projects_leading", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    