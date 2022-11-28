from django.shortcuts import render, redirect
from .login import loginForm
from .register import registerForm
from .register import MongoDBUserForm
from .payment import checkAddressForm
from miwallet import utils
from pymongo import MongoClient
import blockcypher
import blockcypher.utils as bcUtils

# Create your views here.


token='df29ec63ab9047cc9520edae52e1ead2'

def index(request):   
    
    return render(request, 'index2.htm')

def home(request):
   # get the list of todos
#    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
   # transfor the response to json objects
   
    crypto_data = utils.get_top_fifteen_coins()

    return render(request, "home.html", {"data": crypto_data})

def news(request):
    
    crypto_news = utils.get_crypto_news()


    return render(request, "news.html", {"data": crypto_news})

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
    mongoUserForm = MongoDBUserForm()
    front_end_message = ''

    
    if request.method == 'POST':
        form = registerForm(data=request.POST)
        mongoUserForm = MongoDBUserForm(data=request.POST)
        if form.is_valid and mongoUserForm.is_valid:
            print("VALIDATED!")
            
            #mongoDBconnection
            db = client['miWallets']
            Users = db['Users']
            form_data = mongoUserForm.data
            
            print("FORM DATA:",form_data)
            # check if user already registered
            result = Users.find_one({"email":form_data['email']})
            if result:
                #we have this email in our record.. did you mean to login?
                print("We found this email in our records.. Did you mean to login?")
                front_end_message='We found this email in our records.. did you mean to login?' 
            else:
               
                form_user_name = form_data['username']
                form_first_name = form_data['first_name']
                form_last_name = form_data['last_name']
                form_dob = form_data['date_of_birth']
                form_email = form_data['email']
                form_password = form_data['password']
                
                user_entry = {"user_name": form_user_name,
                              "first_name": form_first_name,
                              "last_name": form_last_name,
                              "dob": form_dob,
                              "email": form_email,
                              "password": form_password,
                              "Wallet":[]
                              }
                # mongoDB add new user
                Users.insert_one(user_entry)
                
                #save() django admin
                user = form.save()
                user_profile = mongoUserForm.save(commit=False)
                user_profile.user = user
                user_profile.save()
                print('user',user)
            
                print("REGISTRATION COMPLETE! WELCOME TO MIWALLET")
                
                return redirect('/home')
        else:{
            front_end_message("data was not validated... registration was not successful... try again later")
        }        
    return render(request, 'register.html', {'form': form, "MongoDBUserForm": mongoUserForm, "message": front_end_message})

def payment(request):
    form = checkAddressForm()
    front_end_message = ''

    if request.method == 'POST':
        form = checkAddressForm(request.POST)
        if form.is_valid():
            from_address = form.cleaned_data["from_address"]
            to_address = form.cleaned_data["to_address"]
            symbol = form.cleaned_data["coin_symbol"]
            amount = form.cleaned_data["amount_to_send"]
            print('validating data..')
            print("from address", from_address, "to address", to_address, "amount", amount, "symbol", symbol)
            is_valid_coin = bcUtils.is_valid_coin_symbol(symbol)

            print("is valid coin????", is_valid_coin, not is_valid_coin)
            if(is_valid_coin):    
                is_valid_address_one = utils.is_valid_pre_payment(from_address,symbol)
                is_valid_address_two = utils.is_valid_pre_payment(to_address,symbol)
                #todo frontend notification
                print("validity test for address 1: {}".format(from_address),is_valid_address_one)
                print("validity test for address 2: {}".format(to_address),is_valid_address_two)
                #if both addresses are valid, coin is valid and addresses are valid with coin
                
                if is_valid_address_one and is_valid_address_two:
                    print("valid adddresses and coin...")
                    
                    #get private key
                    address_one_details = utils.search_address(from_address)
                    # print("from_address details:...", address_one_details)
                    address_one_priv_key = address_one_details['private']
                    address_one_pub_key = address_one_details['public']

                    
                    #inputs
                    inputs =[{'address':from_address}]
                    outputs = [{'address': to_address, "value": amount}]
                    
                    #todo front end notification
                    print("sending payment {} from address: {} to address: {}".format(amount, from_address, to_address))
                    
                    #create unsigned transactions
                    create_unsigned_tx = blockcypher.create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol = symbol, api_key=token, verify_tosigntx=True, change_address=from_address)
                    print("unsigned tx", create_unsigned_tx)
                    
                    to_sign_tx = {}
                    to_sign_tx['tosign_tx'] = create_unsigned_tx['tosign_tx']
                    to_sign_tx['tosign'] = create_unsigned_tx['tosign']
                    
                    #verify transaction
                    verify_unsigned = blockcypher.verify_unsigned_tx(unsigned_tx=to_sign_tx, outputs=outputs, coin_symbol=symbol, change_address= from_address)
                    input_addresses = blockcypher.get_input_addresses(create_unsigned_tx)
                    tx=to_sign_tx['tosign']
                    
                    #signatures
                    tx_signatures = blockcypher.make_tx_signatures(tx, privkey_list = [address_one_priv_key], pubkey_list=[address_one_pub_key])
                    addresses_pubkeys = [address_one_pub_key]
                    
                    #finalize and broadcast transaction
                    #todo frontend notification
                    front_end_message=''
                    try:
                        broadcast_tx = blockcypher.broadcast_signed_transaction(create_unsigned_tx,tx_signatures, pubkeys=addresses_pubkeys, coin_symbol=symbol, api_key=token)
                        print("broadcasting is:.....", broadcast_tx)
                        front_end_message = "Broadcast transaction successful!"
                    except:
                        front_end_message = "Failed to broadcast transaction!"
                    
                else:
                    front_end_message='Please check if the address is entered correctly'
            else:
                print("{} is not a valid coin on BlockCypher(BC)".format(symbol))
                front_end_message = "{} is not a valid coin on BlockCypher(BC)".format(symbol)
    return render(request, 'payment.html', {'form': form, "message": front_end_message})