from django.db import models

class Sprint(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(to="projects.Project", on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    tasks = models.ManyToManyField(to="tasks.Task", related_name="sprints")

    def __str__(self):
        return f"{self.name} - {self.project.name}"