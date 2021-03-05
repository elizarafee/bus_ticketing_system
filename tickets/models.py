from django.db import models
from phone_field import PhoneField

# Create your models here.
class Bus(models.Model):
    bus_name = models.CharField(max_length=60)
    bus_code = models.CharField(max_length=10)
    
class Bus_Stop(models.Model):
    bus_stop_name = models.CharField(max_length=60)
    bus_stop_code = models.CharField(max_length=10)
