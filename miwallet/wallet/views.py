from django.shortcuts import render, redirect
from django.urls import path
from django.contrib.auth.models import auth
from .login import loginForm
from .register import registerForm
from .payment import checkAddressForm
from .pay_process import check_valid_address
from miwallet import utils
from pymongo import MongoClient

import django.contrib.auth as auth
# Create your views here.

def home(request):
    return render(request, 'index2.htm')

def index(request):
   # get the list of todos
#    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
   # transfor the response to json objects
   
    crypto_data = utils.get_top_fifteen_coins()

    return render(request, "home.html", {"data": crypto_data})

def login(request):
    client = MongoClient('mongodb+srv://gsaaad:mongodjango@cluster0.4yjqtsv.mongodb.net/?retryWrites=true&w=majority', 27017)

    print("LOGIN")
    print("----------")
    form = loginForm()
    
    if request.method == 'POST':
        form = loginForm(request.POST)
        
        if form.is_valid():
            print("FORM VALIDATED!")
            form_email =form.cleaned_data['email']
            form_password = form.cleaned_data['password']
            print("Email: "+form_email)
            print("Password: "+form_password)
            db = client['miWallets']
            Users = db['Users']
            print(form_email)
            
            is_valid_user = Users.find_one({"email":form_email})
            # print(is_valid_user)
            
            
            if is_valid_user:
                print("we found your email in your mongo database!")
                print("checking password...")
                is_valid_password = is_valid_user['password'] == form_password
                print("valid password? ", is_valid_password)
                if is_valid_password:
                    print("successful login, valid email and password. AUTH!")
                    print("user {} has been authenticated".format(form_email))
                    return redirect('/home')
                    
                else:
                    print("invalid password... try again or reset password")
                # router to home!
     
    return render(request, 'login.html', {'form':form})

def register(request):
    client = MongoClient('mongodb+srv://gsaaad:mongodjango@cluster0.4yjqtsv.mongodb.net/?retryWrites=true&w=majority', 27017)
    print("REGISTER")
    print("----------")
    form = registerForm()
    
    if request.method == 'POST':
        form = registerForm(request.POST)
        
        if form.is_valid():
            print("VALIDATED!")
            form_firstname = form.cleaned_data['first_name']
            form_lastname = form.cleaned_data['last_name']
            form_email = form.cleaned_data['email']
            form_password = form.cleaned_data['password']
            form_dob = str(form.cleaned_data['dob'])
            print("First_name"+ form_firstname)
            print("last_name"+ form_lastname)
            # print("user_name"+ form.cleaned_data['user_name'])
            print("Email: "+form_email)
            print("date of birth: ",form_dob)
            print("Password: "+form_password)
            db = client['miWallets']
            Users = db['Users']
            
            result = Users.find_one({"email": form.cleaned_data['email']})
            
            if result:
                #we have this email in our record.. did you mean to login?
                print("We found this email in our records.. Did you mean to login?")
            else:
                # not found in database, create new
                user = {"first_name": form_firstname, 
                    "last_name": form_lastname, 
                    'email': form_email,
                    'password': form_password,
                    'dob': (form_dob),
                    'Wallet': []
                    #todo give them a wallet ID, based on database?
                    }
                Users.insert_one(user)
                print("REGISTRATION COMPLETE! WELCOME TO MIWALLET")
                return redirect('/home')
                
    return render(request, 'register.html', {'form': form})

def payment(request):
    form = checkAddressForm()

    if request.method == 'POST':
        form = checkAddressForm(request.POST)
        
        if form.is_valid():
            print("validated")
            address = form.cleaned_data["address"]
            is_valid_address = check_valid_address(address)
            
            
            
    return render(request, 'payment.html', {'form': form})