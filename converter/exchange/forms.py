from django import forms
from .models import ExchangeMarket

curr_list = (['RUB', 'USD', 'EUR', 'CNY', 'AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'VND', 'HKD', 'GEL', 'DKK', 'AED', 'EGP', 'INR', 'IDR', 'KZT', 'CAD', 'QAR', 'KGS', 'MDL', 'NZD', 'NOK', 'PLN', 'RON', 'XDR', 'SGD', 'TJS', 'THB', 'TRY', 'TMT', 'UZS', 'UAH', 'CZK', 'SEK', 'CHF', 'RSD', 'ZAR', 'KRW', 'JPY'] for _ in range(2))

CHOICES = list(zip(*curr_list))


class ExchangeForm(forms.Form):
    marketname = forms.ModelChoiceField(queryset=ExchangeMarket.objects.all(), widget=forms.Select(attrs={'class': 'select-maket'}), label="Рынок обмена", initial='ЦБ РФ')

    base_curr = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'select-field'}))

    quote_curr = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'select-field'}))

    amount_input = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'input', 'step': '0.01'}))

    
    