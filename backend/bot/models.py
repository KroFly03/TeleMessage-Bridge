from django.contrib.auth import get_user_model
from django.db import models
from django.utils.crypto import get_random_string

USER_MODEL = get_user_model()


class TgUser(models.Model):
    chat_id = models.BigIntegerField(primary_key=True, editable=False, unique=True)
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    verification_code = models.CharField(max_length=20, null=True, blank=True)

    @property
    def is_verified(self) -> bool:
        return bool(self.user)

    @staticmethod
    def _generate_verification_code() -> str:
        return get_random_string(20)

    def update_verification_code(self) -> None:
        self.verification_code = self._generate_verification_code()
        self.save(update_fields=['verification_code'])

    class Meta:
        verbose_name = 'Телеграмм-пользователь'
        verbose_name_plural = 'Телеграмм-пользователи'

    def __str__(self):
        return self.chat_id
