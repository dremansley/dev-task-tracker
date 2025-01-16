from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.mixins import UserGroupPermissionMixin
from projects.models import Project
from .serializers import ProjectSerializer


class ProjectListView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(is_deleted=False)
        serialized = ProjectSerializer(projects, many=True)

        return Response({"projects": serialized.data, "status":"success"}, status=200)
    
    
class ProjectCreateView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin"]

    def post(self, request, *args, **kwargs):
        serialize_input = ProjectSerializer(data=request.data)

        if serialize_input.is_valid():
            project = serialize_input.save()
            return Response({"message": f"Created Project {project.title} Successfully"}, status=201)
        
        return Response({"message": "Invalid Data", "status":"error", "errors": serialize_input.errors}, status=400)
    

class ProjectUpdateView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin"]

    def patch(self, request, *args, **kwargs):
  
        project = get_object_or_404(Project, pk=kwargs.get("project_id"), is_deleted=False)

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
    
        
class ProjectDeleteView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin"]

    def patch(self, request, *args, **kwargs):

        project = get_object_or_404(Project, pk=kwargs.get("project_id"), is_deleted=False)

        if project.project_lead == request.user or request.user.is_superuser:

            project.is_deleted = True
            project.is_active = False
            project.save()

            return Response(
                    {"message": "Project has been deleted", "status": "success"},
                    status=200,
                )
        
        return Response(
                    {"message": "Only the project leader can delete this project", "status": "success"},
                    status=400,
                )


        