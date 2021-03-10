from django.contrib import admin
from .models import Bus, Bus_Stop, Ticket, Passenger

# Register your models here.
class BusAdmin(admin.ModelAdmin):
    list_display = ("id", "bus_name", "bus_code")

class bus_stopAdmin(admin.ModelAdmin):
    list_display = ("id", "bus_stop_name", "bus_stop_code")

class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "departure", "arrival", "bus", "date", "time")

class PassengerAdmin(admin.ModelAdmin):
    list_display = ("id", "passenger_name", "phone_number", "email")
    filter_horizontal = ("ticket",)

admin.site.register(Bus, BusAdmin)
admin.site.register(Bus_Stop, bus_stopAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Passenger, PassengerAdmin)