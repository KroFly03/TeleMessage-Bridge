# Generated by Django 4.2.4 on 2023-08-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_alter_tguser_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='verification_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]