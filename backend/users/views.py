from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.models import Message
from users.serializers import UserDetailSerializer, UserCreateSerializer, MessageSerializer

USER_MODEL = get_user_model()


class UserCreateView(generics.CreateAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
    authentication_classes = []


class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'patch']

    def get_object(self):
        return self.request.user


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
