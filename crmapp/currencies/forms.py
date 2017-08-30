from django import forms

from .models import Currency

class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ('currency_name', 'desc', 'address_one',
                  'address_two', 'exchange', 'investment', 'phone',
        )
        widgets = {
            'currency_name': forms.TextInput(
                attrs={
                    'placeholder':'Bitcoin',
                    'class':'col-md-12 form-control'
                }
            ),
            'desc': forms.Textarea(
                attrs={
                    'placeholder':'Enter a description',
                    'class':'form-control'
                }
            ),
            'address_one': forms.TextInput(
                attrs={
                    'placeholder':'BTC Address',
                    'class':'gi-form-addr form-control'
                }
            ),
            'address_two': forms.TextInput(
                attrs={
                    'placeholder':'Alt BTC Addr',
                    'class':'gi-form-addr form-control'
                }
            ),
            'exchange': forms.TextInput(
                attrs={
                    'placeholder':'PoloniEx',
                    'class':'gi-form-addr form-control'
                }
            ),
            'investment': forms.TextInput(
                attrs={
                    'placeholder':'$4,440',
                    'class':'gi-form-addr form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder':'Phone',
                    'class':'gi-form-addr form-control'
                }
            ),
        }