# Generated by Django 3.2.5 on 2023-01-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_management_app', '0003_remove_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]
