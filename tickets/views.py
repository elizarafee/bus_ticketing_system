from django.shortcuts import render
from .models import Bus, Bus_Stop, Ticket, Passenger
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
import random

# Create your views here.
def bus_index(request):
    return render(request, 'tickets/bus_index.html', {
       'buses': Bus.objects.all()
    })

def bus_stop_index(request):
    return render(request, 'tickets/bus_stop_index.html', {
       'busstops': Bus_Stop.objects.all()
    })

def ticket_index(request):
    return render(request, 'tickets/ticket_index.html', {
       'tickets': Ticket.objects.all()
    })

def passenger_index(request):
    return render(request, 'tickets/passenger_index.html', {
       'passengers': Passenger.objects.all()
    })

def bus(request, bus_id):
   bus = Bus.objects.get(id=bus_id)
   return render(request, 'tickets/bus.html', {
      'bus': bus
   })
   
def bus_stop(request, bus_stop_id):
   bus_stop = Bus_Stop.objects.get(id=bus_stop_id)
   return render(request, 'tickets/bus_stop.html', {
      'bus_stop_id': bus_stop_id,
      'bus_stop': bus_stop
   })

def ticket(request, ticket_id):
   ticket = Ticket.objects.get(id=ticket_id)
   return render(request, 'tickets/ticket.html', {
      'ticket': ticket,
      'passengers': ticket.passengers.all(),
      'non_passengers': Passenger.objects.exclude(ticket=ticket).all()
   })

def passenger(request, passenger_id):
   passenger = Passenger.objects.get(id=passenger_id)
   return render(request, 'tickets/passenger.html', {
      'passenger': passenger,
      # 'tickets': ticket.passengers.all()
   })

def book_ticket(request, ticket_id):
   if request.method == "POST":
      ticket = Ticket.objects.get(pk=ticket_id)
      passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
      passenger.ticket.add(ticket)
      return HttpResponseRedirect(reverse("tickets:ticket", args=(ticket.id,)))