from rest_framework.response import Response

def validate_and_return(serializer, success_return_message):
    if serializer.is_valid():
        serializer.save()
        return Response (
            {
                "message": success_return_message,
                "data": serializer.data,
                "status": "success"
            },
            status=200,
            )
    return Response(
            {"message": "Invalid data", "errors": serializer.errors, "status": "error"},
            status=400,
        )