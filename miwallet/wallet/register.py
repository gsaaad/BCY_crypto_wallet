from django import forms
from django.contrib.auth.models import User
from wallet.models import MongoDBUser

class registerForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username", "first_name", "last_name", "email","password")
        
class MongoDBUserForm(forms.ModelForm):
        class Meta():
            model = MongoDBUser
            fields = ('date_of_birth', "wallet_address")
    
  
