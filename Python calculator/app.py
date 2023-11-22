# app.py
from flask import Flask, render_template, request
from currency_converter import convert_currency
from validator import is_valid_currency_code, is_valid_amount

app = Flask(__name__)

API_KEY = '39580e228253ad8f2ccabf6aa71b7e52'

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']

        # Validate currency codes and amount
        if not is_valid_currency_code(from_currency) or not is_valid_currency_code(to_currency):
            raise ValueError("Invalid currency code entered.")
        if not is_valid_amount(amount):
            raise ValueError("Invalid amount entered.")

        # Convert currency using utility function
        converted_amount = convert_currency(from_currency, to_currency, amount, API_KEY)

        # Get the currency symbol for the target currency (for display purposes)
        currency_symbol = get_currency_symbol(to_currency)

        result_message = f"{currency_symbol} {converted_amount}"
    except ValueError as ve:
        result_message = f"An error occurred: {str(ve)}"
    except Exception as e:
        result_message = f"An unexpected error occurred: {str(e)}"

    return render_template('result.html', result_message=result_message)

def get_currency_symbol(currency_code):
    symbols = {
        'USD': '$',
        'AUD': 'A$',
        'BRL': 'R$',
        'GBP': '£',
        'BGN': 'лв',
        'CAD': 'CA$',
        'CNY': '¥',
        'HRK': 'kn',
        'CZK': 'Kč',
        'DKK': 'kr',
        'EUR': '€',
        'HKD': 'HK$',
        'HUF': 'Ft',
        'ISK': 'kr',
        'IDR': 'Rp',
        'INR': '₹',
        # Add more currencies and symbols as needed
    }
    return symbols.get(currency_code, currency_code)

if __name__ == "__main__":
    app.run(debug=True)


