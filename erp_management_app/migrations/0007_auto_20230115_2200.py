# Generated by Django 3.2.5 on 2023-01-15 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_management_app', '0006_auto_20230115_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='otp_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_counter',
            field=models.IntegerField(default=0),
        ),
    ]
