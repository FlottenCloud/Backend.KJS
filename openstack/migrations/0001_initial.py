# Generated by Django 4.1 on 2022-08-21 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenstackInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor_id', models.CharField(max_length=50)),
                ('ram_size', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
                ('volume_size', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
            ],
        ),
    ]
