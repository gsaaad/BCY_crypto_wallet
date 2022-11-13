from django.shortcuts import render
from django.urls import path
# Create your views here.

def index(request):
    return render(request, 'index2.htm')

def login(request):
    return render(request, 'login.htm')

def register(request):
    return render(request, 'register.htm')