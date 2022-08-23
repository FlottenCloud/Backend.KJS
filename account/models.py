from django.db import models

class Account_info(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=100)
    # token = models.CharField(max_length=200, null=True)
    # api_key = models.CharField(max_length=200)
    # secret_key = models.CharField(max_length=200)

    class Meta:
        #table name
        db_table = 'accounts_info'

