# Generated by Django 4.1 on 2022-08-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_info',
            name='token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]