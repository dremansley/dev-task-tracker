from django.urls import path
from users.views import UserDetail

urlpatterns = [
    path('', UserDetail.as_view(), name='user_details'),
]
