from django import forms
from wallet.models import MongoDBUser

class registerForm(forms.Form):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # user_name = forms.CharField(max_length=12)
    # email = forms.EmailField()
    # date_of_birth = forms.DateField()
    # wallet = forms.CharField(max_length=34,min_length=34)
    password = forms.CharField(widget=forms.PasswordInput())
class MongoDBUserForm(forms.ModelForm):
        class Meta():
            model = MongoDBUser
            fields = ('first_name', 'last_name','user_name','date_of_birth','email')
    
  
