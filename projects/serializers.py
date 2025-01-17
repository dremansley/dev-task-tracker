from .models import Project
from rest_framework import serializers
from users.serializers import UserNameSerializer

class ProjectSerializer(serializers.ModelSerializer):

    project_lead = serializers.SerializerMethodField()

    def get_project_lead(self, obj):
        return UserNameSerializer(obj.project_lead).data

    class Meta:
        model = Project
        fields = "__all__"

    