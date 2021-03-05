from django.db import models

# Create your models here.
class Bus(models.Model):
    bus_name = models.CharField(max_length=60)
    bus_code = models.CharField(max_length=10)
    