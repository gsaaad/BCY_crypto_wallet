from django.shortcuts import render
from django.urls import path
import requests
# Create your views here.

def index(request):
    return render(request, 'index2.htm')

def home(request):
   # get the list of todos
   response = requests.get('https://jsonplaceholder.typicode.com/todos/')
   # transfor the response to json objects
   print(response)
   todos = response.json()
   return render(request, "home.html", {"todos": todos})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')