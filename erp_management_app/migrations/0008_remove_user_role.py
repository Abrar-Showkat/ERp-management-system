# Generated by Django 3.2.5 on 2023-01-15 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp_management_app', '0007_auto_20230115_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
