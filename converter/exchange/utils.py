def get_api_data(market, api):
    if market == "ЦБ РФ":
        date_time = api.get('Timestamp')[:10]
        curr_rate = api.get("Valute")
        curr_rate["RUB"] = {"Nominal": 1, "Value": 1}
    
    elif market == "Forex":
        curr_rate = api.get('rates')
        date_time = api.get('date')

    return curr_rate, date_time


def money_amount(market, amount_input, base_curr, quote_curr):
    if market == 'ЦБ РФ':
        amount_out = round(amount_input * (base_curr['Value'] * quote_curr['Nominal'] / (quote_curr['Value'] * base_curr['Nominal'])), 4)
                
    else:
        amount_out = round(amount_input * (quote_curr / base_curr), 4)

    return amount_out 