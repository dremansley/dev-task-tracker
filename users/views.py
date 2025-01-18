from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer

class UserDetail(APIView):

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user, many=False)
        return Response({"user":serializer.data})
