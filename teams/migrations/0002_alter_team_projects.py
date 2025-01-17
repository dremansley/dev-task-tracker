# Generated by Django 5.1.5 on 2025-01-17 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_project_lead_alter_project_description'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='projects',
            field=models.ManyToManyField(related_name='project_teams', to='projects.project'),
        ),
    ]