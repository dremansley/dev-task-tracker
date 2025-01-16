from rest_framework.views import APIView
from rest_framework.response import Response
from utils.mixins import UserGroupPermissionMixin
from projects.models import Project
from .serializers import ProjectSerializer

class ProjectListView(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
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