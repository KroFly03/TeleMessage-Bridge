from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from bot.models import TgUser
from users.models import Message
from users.tasks import send_message

USER_MODEL = get_user_model()


class PasswordField(serializers.CharField):
    def __init__(self, **kwargs):
        kwargs['style'] = {'input_type': 'password'}
        kwargs.setdefault('write_only', True)
        super().__init__(**kwargs)
        self.validators.append(validate_password)


class UserCreateSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)
    password_repeat = PasswordField(required=True)

    class Meta:
        model = USER_MODEL
        fields = '__all__'
        read_only_fields = (
            'id', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_repeat']:
            raise ValidationError({'password': ['Разные пароли.']})
        return attrs

    def create(self, validated_data):
        del validated_data['password_repeat']
        return super().create(validated_data)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = '__all__'
        read_only_fields = (
            'id', 'username', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined',
            'groups', 'user_permissions')


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'sender')

    def validate_sender(self, sender: USER_MODEL) -> USER_MODEL:
        try:
            TgUser.objects.get(user=sender)
        except TgUser.DoesNotExist:
            raise ValidationError(['Нужно подтвердить аккаунт в телеграмм прежде чем отправлять сообщения.'])

        return sender

    def create(self, validated_data):
        sender = validated_data['sender']

        tg_user: TgUser = TgUser.objects.get(user=sender)

        with transaction.atomic():
            send_message.delay(tg_user.chat_id, sender.username, validated_data['text'])
            return super().create(validated_data)
