from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def register(request):
    return HttpResponse("User Register Page")

def login(request):
    return HttpResponse("User Login Page")
