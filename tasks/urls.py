from django.urls import path
from tasks.views import PriorityListView, TaskStatusListView, TaskTypeListView, TaskCreateView

urlpatterns = [
    path('priorities/', PriorityListView.as_view(), name='priorities_list'),
    path("status-list/", TaskStatusListView.as_view(), name="status_list"),
    path("task-type-list/", TaskTypeListView.as_view(), name="type_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
]
