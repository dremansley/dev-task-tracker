from django.urls import path
from tasks.views import PriorityList, TaskStatusList, TaskCreate

urlpatterns = [
    path('priorities/', PriorityList.as_view(), name='priorities_list'),
    path("status-list/", TaskStatusList.as_view(), name="status_list"),
    path("create/", TaskCreate.as_view(), name="task_create")
]
