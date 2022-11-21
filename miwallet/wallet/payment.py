from django import forms

class checkAddressForm(forms.Form):
    address = forms.CharField(max_length=34)
    # symbol = forms.CharField(max_length=3)
    