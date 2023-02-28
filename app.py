import requests
import streamlit as st

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
amount = st.number_input("Enter amount")
from_currency = st.text_input("Enter currency to convert from").upper()
to_currency = st.text_input("Enter currency to convert to").upper()
convert_button = st.button("Convert")

# Convert the currency and display the result
if convert_button:
    converted_amount = currency_converter(amount, from_currency, to_currency)
    if converted_amount:
        st.write(f"{amount} {from_currency} = {converted_amount} {to_currency}")
    else:
        st.write("Unable to perform currency conversion. Please check your input and try again.")
