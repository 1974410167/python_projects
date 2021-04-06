from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class user(models.Model):

    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=24)
    file = models.FileField(upload_to='uploads/')
    image = models.ImageField(upload_to='uploads/')


    def __str__(self):
        return self.name