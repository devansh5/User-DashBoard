# Generated by Django 3.0.4 on 2020-04-01 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maze', '0006_auto_20200401_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='signup_confirmation',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
