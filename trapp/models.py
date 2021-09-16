from os import name
from django.db import models

# Create your models here.
class Dmdl(models.Model):

    name= models.CharField(max_length=20)
    email = models.CharField(max_length=15)
    phoneno= models.CharField(max_length=15)
    Message = models.TextField()


    def __str__(self):
        return self.name

