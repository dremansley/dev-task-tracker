from rest_framework import serializers
from tasks.models import Task
from users.serializers import UserSerializer

class ChoiceSerializer(serializers.Serializer):
    value = serializers.CharField()
    display_name = serializers.CharField()

    def to_representation(self, instance):
        return {
            'value': instance[0],
            'display_name': instance[1]
        }
    
class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class TaskSerializer(serializers.Serializer):
    user = UserSerializer()

    class Meta:
        model = Task
        fields = "__all__"


class TaskPreviewSerializer(serializers.Serializer):

    status = serializers.SerializerMethodField()
    priority = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ("title", "status", "priority",)

    def get_status(self, obj):
        return ChoiceSerializer(obj.get_status_display()).data
    
    def get_priority(self, obj):
        return ChoiceSerializer(obj.get_priority_display()).data
    

