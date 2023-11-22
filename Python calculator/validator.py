# validator.py
def is_valid_currency_code(currency_code):
    # Add your currency code validation logic here
    # For simplicity, assuming any non-empty string is valid
    return bool(currency_code)

def is_valid_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False
