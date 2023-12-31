from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    email = models.EmailField(verbose_name='Почта')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.last_name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        return super().save(*args, **kwargs)


class Message(models.Model):
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    sender = models.ForeignKey(User, verbose_name='Отправитель', on_delete=models.CASCADE)
