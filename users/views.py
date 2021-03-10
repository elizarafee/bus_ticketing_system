from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
import random

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(request, "users/login.html", {
                'message' : 'Invalid Credentials!'
            })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
            'message' : 'Logged out!'
        })
