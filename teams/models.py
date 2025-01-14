from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(to=User, related_name="teams")
    projects = models.ManyToManyField(to="projects.Project", related_name="teams")

    def __str__(self):
        return self.name