from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
import random

# Create your views here.
def index(request):
    return HttpResponse("Welcome")