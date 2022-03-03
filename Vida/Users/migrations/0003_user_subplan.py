# Generated by Django 3.1.3 on 2022-03-03 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0002_subplan_status'),
        ('Users', '0002_remove_user_subplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subplan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HomeApp.subplan'),
        ),
    ]
