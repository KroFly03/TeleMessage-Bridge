from django.urls import path

from users.views import UserCreateView, UserDetailView, MessageCreateView

app_name = 'users'

urlpatterns = [
    path('', UserCreateView.as_view(), name='users'),
    path('/me', UserDetailView.as_view(), name='users-me'),
    path('/me/messages', MessageCreateView.as_view(), name='users-message'),
]
