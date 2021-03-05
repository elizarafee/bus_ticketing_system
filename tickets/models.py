from django.db import models
from phone_field import PhoneField

# Create your models here.
class Bus(models.Model):
    bus_name = models.CharField(max_length=60)
    bus_code = models.CharField(max_length=10)
    
class Bus_Stop(models.Model):
    bus_stop_name = models.CharField(max_length=60)
    bus_stop_code = models.CharField(max_length=10)

class Ticket(models.Model):
    pessenger_name = models.CharField(max_length=50)
    phone_number = PhoneField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=254)
    departure = models.CharField(max_length=50)
    arrival = models.CharField(max_length=50)
    bus_code = models.CharField(max_length=10)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)