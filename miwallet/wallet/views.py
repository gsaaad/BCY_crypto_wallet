from django.shortcuts import render
from django.urls import path
import requests
# Create your views here.

def index(request):
    return render(request, 'index2.htm')

def home(request):
   # get the list of todos
#    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
   # transfor the response to json objects
    url = "https://investing-cryptocurrency-markets.p.rapidapi.com/coins/list"

    querystring = {"edition_currency_id":"12","time_utc_offset":"28800","lang_ID":"1","sort":"MARKETCAP_DN","page":"1"}

    headers = {
        "X-RapidAPI-Key": "204482477cmshdd6f520fedecd46p1ea1fbjsne7e8a3e634f6",
        "X-RapidAPI-Host": "investing-cryptocurrency-markets.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
#    todos = response.json()
    total_data = response.json()['data']
    print(total_data)
    # print("RESPONSE:", response)
    # print("TOTAL DATA:                   ",total_data)
    # print(type(total_data))
    
    # print("----------------------")
    data_dict = total_data[0]
    print(type(data_dict))
    ("---------------")
    screen_data = data_dict['screen_data']
    crypto_data = screen_data['crypto_data']
    # get top
    crypto_data = crypto_data[:15]
    print(type(crypto_data))
    print(len(crypto_data))
    print(crypto_data)
    
    # print()
    

    return render(request, "home.html", {"data": crypto_data})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')