from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.mixins import UserGroupPermissionMixin
from projects.models import Project
from .serializers import ProjectSerializer
from tasks.models import Task
from tasks.serializers import TaskSerializer

class ProjectListView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):

        projects = request.user.user_projects()
        serialized = ProjectSerializer(projects, many=True)

        return Response({"projects": serialized.data, "status":"success"}, status=200)
    
    
class ProjectCreateView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin"]

    def post(self, request, *args, **kwargs):
        
        serialize_input = ProjectSerializer(data=request.data)

        if serialize_input.is_valid():
            project = serialize_input.save()
            return Response({"message": f"Created Project '{project.title}' Successfully"}, status=201)
        
        return Response({"message": "Invalid Data", "status":"error", "errors": serialize_input.errors}, status=400)
    

class ProjectUpdateView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin"]

    def patch(self, request, *args, **kwargs):

        user_projects = request.user.user_projects()
        project = get_object_or_404(Project, pk=kwargs.get("project_id"), is_deleted=False)

        if project in user_projects:
            serializer = ProjectSerializer(project, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Project updated successfully",
                        "data": serializer.data,
                        "status": "success",
                    },
                    status=200,
                )

            return Response(
                {"message": "Invalid data", "errors": serializer.errors, "status": "error"},
                status=400,
            )
        return Response(
            {"message": "You do not have permission to edit this project", "status": "error"},
            status=403,
        )
    
        
class ProjectDeleteView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin"]

    def patch(self, request, *args, **kwargs):

        project = get_object_or_404(Project, pk=kwargs.get("project_id"), is_deleted=False)

        if project.project_lead != request.user and not request.user.is_superuser:
            return Response(
                    {"message": "Only the project leader or superuser can delete this project", "status": "error"},
                    status=403,
                )

        project.is_deleted = True
        project.is_active = False
        project.save()

        return Response(
                {"message": "Project has been marked as deleted", "status": "success"},
                status=200,
            )
        

class ProjectTaskListView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):

        user_projects = request.user.user_projects()
        project = get_object_or_404(Project, pk=kwargs.get("project_id"), is_deleted=False)
   
        if project not in user_projects:
            return Response(
            {"message": "You do not have permission to view this project", "status": "error"},
            status=403
            )
        
        tasks = Task.objects.filter(project=project)
        serializer = TaskSerializer(tasks, many=True)
        return Response({"tasks": serializer.data}, status=200)
        
       