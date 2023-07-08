from django.shortcuts import render
import requests

from .forms import ExchangeForm
from .models import ExchangeMarket
from .utils import get_api_data, money_amount


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
           
            amount_out = money_amount(market, amount_input, base_curr, quote_curr)

            context = {'form': form, 
                       'amount_out': amount_out, 
                       'curr_rates': curr_rates,
                       'date_time': date_time}
            
            return render(request, 'exchange/index.html', context=context)
    
    else:
        form = ExchangeForm()
        context = {'form': form}
    
    return render(request, 'exchange/index.html', context=context)
