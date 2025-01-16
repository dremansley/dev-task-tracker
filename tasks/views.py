from rest_framework.views import APIView
from utils.mixins import UserGroupPermissionMixin
from tasks.models import Task
from tasks.serializers import ChoiceSerializer
from rest_framework.response import Response

def index():
    return True

class PriorityList(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):
        priority_list = ChoiceSerializer(Task.Priority.choices, many=True)
        return Response({"data": priority_list.data, "status": "success"}, status=200)


class TaskStatusList(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):
        status_options_list = ChoiceSerializer(Task.Status.choices, many=True)
        return Response({"data": status_options_list.data, "status": "success"}, status=200)
