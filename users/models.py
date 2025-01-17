from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    def user_projects(self):
        projects = set()
        
        for team in self.teams.all():
            projects.update(team.projects.all())
        
        return projects