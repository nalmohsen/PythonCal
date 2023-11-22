# currency_converter.py
import requests

def convert_currency(from_currency, to_currency, amount, api_key):
    api_url = 'http://api.exchangerate.host/live'
    api_params = {
        'access_key': api_key,
        'currencies': f'{to_currency},{from_currency}',
        'source': 'USD',
        'format': 1
    }

    response = requests.get(api_url, params=api_params)
    response.raise_for_status()

    data = response.json()

    if 'quotes' in data:
        exchange_rate = data['quotes'][f'USD{to_currency}']
        converted_amount = round(float(amount) / exchange_rate, 2)
        return converted_amount
    else:
        error_message = data.get('error', 'Error converting currencies.')
        raise ValueError(error_message)
