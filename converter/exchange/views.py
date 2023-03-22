from django.shortcuts import render
import requests
from decimal import Decimal as D


def currency_calculator(request):
    api = requests.get(url='https://www.cbr-xml-daily.ru/daily_json.js').json()

    date_time = api.get('Timestamp')

    curr_rate = api.get("Valute")
    curr_rate["RUB"] = {"Name": "Российский рубль", "Value": 1}
    curr_rate = dict(sorted(curr_rate.items()))
   

    if request.method == 'GET':
        form = {'curr_rate': curr_rate, 'date_time': date_time}
        return render(request, 'exchange/index.html', context=form)

    if request.method == 'POST':
        base_curr = request.POST.get('base_curr')
        quote_curr = request.POST.get('quote_curr')
        amount_input = request.POST.get('amount_input')

        amount_out = round(D(amount_input) * D(curr_rate[base_curr]['Value']) / D(curr_rate[quote_curr]['Value']), 2)

        form = {'base_curr': base_curr,
                'quote_curr': quote_curr,
                'amount_input': amount_input,
                'amount_out': amount_out,
                'curr_rate': curr_rate,
                'date_time': date_time
        }

        return render(request, 'exchange/index.html', context=form)
