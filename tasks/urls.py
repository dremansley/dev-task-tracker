from django.urls import path
from tasks.views import PriorityListView, TaskStatusListView, TaskTypeListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('priorities/', PriorityListView.as_view(), name='priorities_list'),
    path("status-list/", TaskStatusListView.as_view(), name="status_list"),
    path("task-type-list/", TaskTypeListView.as_view(), name="type_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("<int:task_id>/", TaskDetailView.as_view(), name="task_detail"),
    path("update/<int:task_id>/", TaskUpdateView.as_view(), name="task_detail"),
    path("delete/<int:task_id>/", TaskDeleteView.as_view(), name="task_delete")
]
