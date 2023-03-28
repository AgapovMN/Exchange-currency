from django.shortcuts import render
import requests

from .forms import ExchangeForm
from .models import ExchangeMarket


def get_api_data(market, api):
    if market == "ЦБ РФ":
        date_time = api.get('Timestamp')[:10]
        curr_rate = api.get("Valute")
        curr_rate["RUB"] = {"Nominal": 1, "Value": 1}
    
    elif market == "Forex":
        curr_rate = api.get('rates')
        date_time = api.get('date')

    return curr_rate, date_time


def currency_calculator(request):
    data = dict()
    for item in ExchangeMarket.objects.all():
        api_data = requests.get(url=item.api_url).json()
        data[item.marketname] = api_data
    
    if request.method == 'POST':
        form = ExchangeForm(request.POST)

        if form.is_valid():
            response = form.cleaned_data
            market = str(response['marketname'])
            amount_input = response['amount_input']
            api = data[market]

            curr_rates, date_time = get_api_data(market, api)

            base_curr = curr_rates[response['base_curr']]
            quote_curr = curr_rates[response['quote_curr']]

            if market == 'ЦБ РФ':
                amount_out = round(amount_input * (base_curr['Value'] * quote_curr['Nominal'] / (quote_curr['Value'] * base_curr['Nominal'])), 4)
                
            elif market == 'Forex':
                amount_out = round(amount_input * (quote_curr / base_curr), 4)

            context = {'form': form, 
                       'amount_out': amount_out, 
                       'curr_rates': curr_rates,
                       'date_time': date_time}
            
            return render(request, 'exchange/index.html', context=context)
    
    else:
        form = ExchangeForm()
        context = {'form': form}
    
    return render(request, 'exchange/index.html', context=context)
