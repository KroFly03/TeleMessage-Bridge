from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from bot.models import TgUser


class TgUserSerializer(serializers.ModelSerializer):
    verification_code = serializers.CharField(write_only=True)

    def validate_verification_code(self, code: str) -> str:
        try:
            tg_user = TgUser.objects.get(verification_code=code)
        except TgUser.DoesNotExist:
            raise ValidationError(['Неверный код подтверждения.'])
        else:
            if tg_user.is_verified:
                raise ValidationError(['Пользователь уже подтвержден.'])

            self.instance = tg_user
            return code

    class Meta:
        model = TgUser
        fields = '__all__'
