# Generated by Django 4.1 on 2022-08-21 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_info_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account_info',
            name='token',
        ),
    ]
