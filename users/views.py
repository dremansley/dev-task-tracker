from django.shortcuts import render
from rest_framework.views import APIView
from utils.mixins import UserGroupPermissionMixin
from rest_framework.response import Response

class UserDetail(UserGroupPermissionMixin, APIView):
    required_groups = ["Project Admin", "Developer", "Viewer"]

    def get(self, request, *args, **kwargs):
        return Response({"message": "User DEtails"})
