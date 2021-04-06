from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
import datetime
from django.utils import timezone

class Student(models.Model):


    name=models.CharField(max_length=20)
    teacher=models.ForeignKey('Teacher',on_delete=models.CASCADE)
    c_time=models.DateTimeField('添加日期',default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['name']

class Teacher(models.Model):

    name=models.CharField(max_length=20)

    score=models.CharField(max_length=20,default='语文')

    c_time=models.DateTimeField('添加日期',default=timezone.now)
    def __str__(self):
        return self.name