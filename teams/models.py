from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(to=CustomUser, related_name="teams")
    projects = models.ManyToManyField(to="projects.Project", related_name="project_teams")

    def __str__(self):
        return self.name