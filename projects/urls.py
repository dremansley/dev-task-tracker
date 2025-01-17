from django.urls import path
from .views import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ProjectTaskListView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path("<int:project_id>/tasks/", ProjectTaskListView.as_view(), name="project_task_list"),
    path("create/", ProjectCreateView.as_view(), name="project_create"),
    path("update/<int:project_id>/", ProjectUpdateView.as_view(), name="project_update"),
    path("delete/<int:project_id>/", ProjectDeleteView.as_view(), name="project_delete")
]
