from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    def get_roles(self, obj):
        return obj.groups.values_list("name", flat=True)

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "is_superuser", "roles")
    

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name")