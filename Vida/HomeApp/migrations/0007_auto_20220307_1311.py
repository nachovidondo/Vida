# Generated by Django 3.1.3 on 2022-03-07 12:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HomeApp', '0006_auto_20220305_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]