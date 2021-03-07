from django.urls import path
from . import views

app_name = "tickets"
urlpatterns = [
    path("buses/", views.bus_index, name="bus_index"),
    path("busstops/", views.bus_stop_index, name="bus_stop_index"),
    path("tickets/", views.ticket_index, name="ticket_index"),
    path("bus/<str:bus_id>", views.bus, name="bus"),
    path("busstop/<str:bus_stop_id>", views.bus_stop, name="busstop"),
    path("ticket/<str:ticket_id>", views.ticket, name="ticket"),
]