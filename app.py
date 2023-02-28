import requests
import streamlit as st
import pycountry

api_key = "7242dd2b7c3816ab6ff463e9"

def currency_converter(amount, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['conversion_result']
    else:
        return None

# Set up the Streamlit app
st.title("Currency Converter")

# Autocomplete for currency codes
currencies = [currency.alpha_3 for currency in pycountry.currencies]
from_currency = st.selectbox("From Currency", currencies)
to_currency = st.selectbox("To Currency", currencies)

# Button to switch "from" and "to" currencies
if st.button("Switch currencies"):
    from_currency, to_currency = to_currency, from_currency

amount = st.number_input("Enter amount", value=1.5, step=0.1, format="%.1f")

# Convert the currency and display the result in real-time
if from_currency and to_currency:
    converted_amount = currency_converter(amount, from_currency, to_currency)
    if converted_amount:
        st.write(f"{amount:.1f} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        st.write("Unable to perform currency conversion. Please check your input and try again.")
