from django.db import models

# Create your models here.


class User(models.Model):
    gender_list = [
        ("man","男"),
        ("woman",'女')
    ]

    name = models.CharField(max_length=64)
    pwd = models.CharField(max_length=64)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=5,choices=gender_list)

    def __str__(self):
        return self.name

class Token(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    token = models.CharField(max_length=128)

