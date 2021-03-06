from django.shortcuts import render
from .models import Bus, Bus_Stop, Ticket
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

