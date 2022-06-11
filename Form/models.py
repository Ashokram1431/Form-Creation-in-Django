from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    age = models.IntegerField()