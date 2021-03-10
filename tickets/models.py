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
    departure = models.ForeignKey(Bus_Stop, on_delete=models.CASCADE, related_name="r_departure")
    arrival = models.ForeignKey(Bus_Stop, on_delete=models.CASCADE, related_name="r_arrival")
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="r_bus")
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Departure: {self.departure}, Arrival: {self.arrival}, Bus: {self.bus}, Date: {self.date}, Time: {self.time}"

class Passenger(models.Model):
    passenger_name = models.CharField(max_length=50)
    phone_number = PhoneField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=254)
    ticket = models.ManyToManyField(Ticket, blank=True, related_name='passengers')

    def __str__(self):
        return f"Passenger Name: {self.passenger_name}, Phone Number: {self.phone_number}, Email: {self.email}"

# python3 manage.py shell
# from tickets.models import *
# bus0 = Bus(bus_name = 'BusA', bus_code = 'busA00')
# bus1 = Bus(bus_name = 'BusA', bus_code = 'busA01')
# bus2 = Bus(bus_name = 'BusB', bus_code = 'busB10')
# bus3 = Bus(bus_name = 'BusB', bus_code = 'busB11')
# busstop1 = Bus_Stop(bus_stop_name = 'Kajalshah', bus_stop_code = 'kaj')
# busstop2 = Bus_Stop(bus_stop_name = 'Mazor Tilla', bus_stop_code = 'maz')
# busstop3 = Bus_Stop(bus_stop_name = 'Zindabazar', bus_stop_code = 'zin')
# busstop4 = Bus_Stop(bus_stop_name = 'Lamabazar', bus_stop_code = 'Lam')
# busstop5 = Bus_Stop(bus_stop_name = 'Kumarpara', bus_stop_code = 'kum')
# busstop6 = Bus_Stop(bus_stop_name = 'Chowhatta', bus_stop_code = 'cho')
# busstop7 = Bus_Stop(bus_stop_name = 'Mirer Moydan', bus_stop_code = 'mir')
# t1 = Ticket(passenger_name= 'A',phone_number= +441,email= 'a.email.com',departure= busstop1,arrival= busstop2,bus_name= bus0)
# t2 = Ticket(passenger_name= 'B',phone_number= +442,email= 'b.email.com',departure= busstop2,arrival= busstop1,bus_name= bus3)
# t3 = Ticket(passenger_name= 'C',phone_number= +443,email= 'c.email.com',departure= busstop4,arrival= busstop7,bus_name= bus2)
# t4 = Ticket(passenger_name= 'D',phone_number= +444,email= 'd.email.com',departure= busstop6,arrival= busstop5,bus_name= bus1)
# t5 = Ticket(passenger_name= 'E',phone_number= +445,email= 'e.email.com',departure= busstop2,arrival= busstop3,bus_name= bus3)
# t6 = Ticket(passenger_name= 'F',phone_number= +446,email= 'f.email.com',departure= busstop7,arrival= busstop1,bus_name= bus2)
# t7 = Ticket(passenger_name= 'G',phone_number= +447,email= 'g.email.com',departure= busstop4,arrival= busstop3,bus_name= bus0)