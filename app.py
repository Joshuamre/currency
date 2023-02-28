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
amount = st.number_input("Enter amount", value=1.5, step=0.1, format="%.1f")
from_currency = st.text_input("Enter currency to convert from", value="USD").upper()
to_currency = st.text_input("Enter currency to convert to", value="EUR").upper()

# Convert the currency and display the result in real-time
if from_currency and to_currency:
    converted_amount = currency_converter(amount, from_currency, to_currency)
    if converted_amount:
        st.write(f"{amount:.1f} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        st.write("Unable to perform currency conversion. Please check your input and try again.")
