from rest_framework import serializers
from tasks.models import Task
from users.serializers import UserNameSerializer

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


class TaskSerializer(serializers.ModelSerializer):

    created_by = UserNameSerializer()
    assigned_to = UserNameSerializer()
    status = serializers.ChoiceField(choices=Task.TaskStatus)
    priority = serializers.ChoiceField(choices=Task.TaskPriority)
    type = serializers.ChoiceField(choices=Task.TaskType)
    task_completion_time = serializers.SerializerMethodField()
    is_overdue = serializers.SerializerMethodField()
    completion_date = serializers.SerializerMethodField()

    def get_task_completion_time(self, obj):
        return obj.task_completion_time().total_seconds()
    
    def get_is_overdue(self, obj):
        return obj.is_overdue
    
    def get_completion_date(self, obj):
        return obj.completion_date

    class Meta:
        model = Task
        fields = ("id",
                  "title", 
                  "description",
                  "priority",
                  "status",
                  "type",
                  "created_by",
                  "assigned_to",
                  "project",
                  "created_at",
                  "updated_at",
                  "due_date",
                  "completion_date",
                  "task_completion_time",
                  "is_overdue"
                  )


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
    

