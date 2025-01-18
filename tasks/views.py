from rest_framework.views import APIView
from utils.mixins import UserGroupPermissionMixin
from tasks.models import Task
from tasks.serializers import ChoiceSerializer
from rest_framework.response import Response
from tasks.serializers import TaskModelSerializer, TaskSerializer
from django.shortcuts import get_object_or_404
from utils.funcs import validate_and_return
from projects.models import Project


class PriorityListView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):
        priority_list = ChoiceSerializer(Task.TaskPriority.choices, many=True)
        return Response({"priority_list": priority_list.data, "status": "success"}, status=200)
    
class TaskStatusListView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):
        status_options_list = ChoiceSerializer(Task.TaskStatus.choices, many=True)
        return Response({"status_list": status_options_list.data, "status": "success"}, status=200)
    
class TaskTypeListView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):
        type_options_list = ChoiceSerializer(Task.TaskType.choices, many=True)
        return Response({"type_list": type_options_list.data, "status": "success"}, status=200)
    

class TaskDetailView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):

        user_projects = request.user.user_projects()

        task_id = kwargs.get("task_id")
        task = get_object_or_404(Task, pk=task_id)

        if task.project in user_projects:
            serializer = TaskSerializer(task, many=False)
            return Response({"task": serializer.data, "status":"success"}, status=200)
        return Response(
            {"message": "You do not have permission to view this task", "status": "error"},
            status=403,
        )

class TaskCreateView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer"]
    
    def post(self, request, *args, **kwargs):

        request_data = request.data.copy()
        user_projects = request.user.user_projects()

        project_id = request_data.get("project")

        if not project_id:
            return Response(
                {"message": "Project is required", "status": "error"},
                status=400
            )
        
        project = get_object_or_404(Project, pk=project_id)
        
        if project not in user_projects:
            return Response(
                {"message": "You do not have permission to create a task for this project", "status": "error"},
                status=403
            )
       
        request_data['created_by'] = request.user.id
        serialize_input = TaskModelSerializer(data=request_data)
        return validate_and_return(serialize_input, f"Created Task Successfully")


class TaskUpdateView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer"]

    def patch(self, request, *args, **kwargs):

        user_projects = request.user.user_projects()
        task = get_object_or_404(Task, pk=kwargs.get("task_id"))

        if task.project not in user_projects:
            return Response(
                {"message": "You do not have permission to modify this task", "status": "error"},
                status=403
            )

        serializer = TaskSerializer(task, data=request.data, partial=True)
        return validate_and_return(serializer, "Task updated successfully")


# TODO: TASK DELETE VIEW