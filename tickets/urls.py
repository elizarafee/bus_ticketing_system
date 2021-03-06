from django.urls import path
from . import views

app_name = "tickets"
urlpatterns = [
    path("buses/", views.bus_index, name="bus_index"),
    path("busstops/", views.bus_stop_index, name="bus_stop_index"),
    path("tickets/", views.ticket_index, name="ticket_index"),
]