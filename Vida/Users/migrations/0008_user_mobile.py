# Generated by Django 3.1.3 on 2022-03-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_remove_user_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(default='----', max_length=200),
        ),
    ]
