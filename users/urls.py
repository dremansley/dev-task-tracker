from django.urls import path
from users.views import UserDetail, AuthCheck

urlpatterns = [
    path('', UserDetail.as_view(), name='user_details'),
    path("auth-check/", AuthCheck.as_view(), name="user-auth-check")
]
