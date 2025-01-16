from rest_framework.views import APIView
from utils.mixins import UserGroupPermissionMixin
from tasks.models import Task
from tasks.serializers import ChoiceSerializer
from rest_framework.response import Response
from tasks.serializers import TaskModelSerializer, TaskSerializer


class PriorityListView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):
        priority_list = ChoiceSerializer(Task.Priority.choices, many=True)
        return Response({"priority_list": priority_list.data, "status": "success"}, status=200)


class TaskStatusListView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):
        status_options_list = ChoiceSerializer(Task.Status.choices, many=True)
        return Response({"status_list": status_options_list.data, "status": "success"}, status=200)
    

class TaskDetailView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get("task_id")
        task = Task.objects.filter(id=task_id).first()
        if task:
            #TODO: Check if the user has permission to vuew this task via project access
            serializer = TaskSerializer(task, many=False)
            return Response({"task": serializer.data}, status=200)
        return Response({"message":"Task not found"}, status=404)


class TaskListView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):

        tasks = Task.objects.filter(project=kwargs.get("project_id"))
        serializer = TaskSerializer(tasks, many=True)

        return Response({"tasks": serializer.data}, status=200)
    

class TaskCreateView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer"]
    
    def post(self, request, *args, **kwargs):

        request_data = request.data.copy()
        request_data['created_by'] = request.user.id

        serialize_input = TaskModelSerializer(data=request_data)

        if serialize_input.is_valid():
            task = serialize_input.save()
            return Response({"message": f"Created Task '{task.title}' Successfully"}, status=201)
        
        return Response({"message": "Invalid Data", "status":"error", "errors": serialize_input.errors}, status=400)
        