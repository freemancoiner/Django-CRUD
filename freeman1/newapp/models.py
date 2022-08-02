from django.db import models

# Create your models here.
class schools(models.Model):
    name = models.CharField(max_length=23)
    address = models.CharField(max_length=23)

class Country(models.model):
    name = models.CharField(max_length=23)
