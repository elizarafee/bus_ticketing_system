from django.urls import path
from . import views

app_name = "pessengers"
urlpatterns = [
    path("", views.index, name="index")
]