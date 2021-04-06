from django.db import models

# Create your models here.



class user(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Mate:
        ordering = ['c_time']