from django.db import models
from phone_field import PhoneField

# Create your models here.
class Bus(models.Model):
    bus_name = models.CharField(max_length=60)
    bus_code = models.CharField(max_length=10)

    def __str__(self):
        return f"Bus Name: {self.bus_name}, Bus Code: {self.bus_code}"
    
class Bus_Stop(models.Model):
    bus_stop_name = models.CharField(max_length=60)
    bus_stop_code = models.CharField(max_length=10)

    def __str__(self):
        return f"Bus Stop Name: {self.bus_stop_name}, Bus Stop Code: {self.bus_stop_code}"

class Ticket(models.Model):
    pessenger_name = models.CharField(max_length=50)
    phone_number = PhoneField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=254)
    departure = models.ForeignKey(Bus_Stop, on_delete=models.CASCADE, related_name="r_departure")
    arrival = models.ForeignKey(Bus_Stop, on_delete=models.CASCADE, related_name="r_arrival")
    bus_name = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="r_bus_name", default='Bus')
    bus_code = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="r_bus_code", default='Bus Code')
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Pessenger Name: {self.pessenger_name}, Phone Number: {self.phone_number} ,Email: {self.email}, Departure: {self.departure}, Arrival: {self.arrival}, Bus Code: {self.bus_code}, Bus Code: {self.bus_code}, Date: {self.date}, Time: {self.time}"