from django.db import models
from datetime import datetime
# Create your models here.



class User(models.Model):

    account = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    balance = models.IntegerField(null=True)
    is_vip = models.BooleanField(default=False)

    createime = models.
    last_time =

