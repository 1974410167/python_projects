from django.db import models
from django.urls import reverse
# Create your models here.

class Publish(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('mid1:detail',args=[str(self.id)])

