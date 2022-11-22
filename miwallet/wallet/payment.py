from django import forms

class checkAddressForm(forms.Form):
    from_address = forms.CharField(max_length=34)
    to_address = forms.CharField(max_length=34)
    coin_symbol = forms.CharField(max_length=4)
    amount_to_send = forms.IntegerField(min_value=100)
    
    # symbol = forms.CharField(max_length=3)
    