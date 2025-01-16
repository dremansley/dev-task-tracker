from rest_framework import serializers
from tasks.models import Task

class ChoiceSerializer(serializers.Serializer):
    value = serializers.CharField()
    display_name = serializers.CharField()

    def to_representation(self, instance):
        return {
            'value': instance[0],
            'display_name': instance[1]
        }
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"