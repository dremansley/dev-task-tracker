from rest_framework.views import APIView
from utils.mixins import UserGroupPermissionMixin
from tasks.models import Task
from tasks.serializers import ChoiceSerializer
from rest_framework.response import Response
from tasks.serializers import TaskSerializer

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


class TaskCreate(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer"]
    
    def post(self, request, *args, **kwargs):

        request_data = request.data.copy()
        request_data['created_by'] = request.user.id

        serialize_input = TaskSerializer(data=request_data)

        if serialize_input.is_valid():
            task = serialize_input.save()
            return Response({"message": f"Created Task '{task.title}' Successfully"}, status=201)
        
        return Response({"message": "Invalid Data", "status":"error", "errors": serialize_input.errors}, status=400)
        