from django.db import models

# Create your models here.
from django.urls import reverse

class Student(models.Model):

    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('HaoYuan:detail_url',args=[str(self.id)])


