# Generated by Django 3.2.5 on 2023-01-15 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_management_app', '0011_alter_roles_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp_management_app.roles'),
        ),
    ]
