from django.contrib import admin
from .models import Bus, Bus_Stop, Ticket, Passenger

# Register your models here.
admin.site.register(Bus)
admin.site.register(Bus_Stop)
admin.site.register(Ticket)
admin.site.register(Passenger)