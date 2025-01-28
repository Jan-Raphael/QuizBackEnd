# accounts/urls.py
from django.urls import path
from .views import GetUsers, GetUser

urlpatterns = [
    path('users/', GetUsers.as_view(), name='get_users'),
    path('users/<int:pk>/', GetUser.as_view(), name='get_user'),
]
