from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return self.name


class token_1(models.Model):

    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
