from django import forms

class registerForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    # user_name = forms.CharField(max_length=12)
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())