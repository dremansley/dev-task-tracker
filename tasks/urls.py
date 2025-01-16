from django.urls import path
from tasks.views import PriorityList, TaskStatusList

urlpatterns = [
    path('priorities/', PriorityList.as_view(), name='priorities_list'),
    path("status-list/", TaskStatusList.as_view(), name="status_list")
]
