# Generated by Django 4.2.4 on 2023-08-18 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('chat_id', models.BigIntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('verification_code', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Телеграмм-пользователь',
                'verbose_name_plural': 'Телеграмм-пользователи',
            },
        ),
    ]
