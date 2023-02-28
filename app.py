import requests
import pandas as pd
import streamlit as st
import plotly.express as px

api_key = "7242dd2b7c3816ab6ff463e9"

from_currency = st.text_input("From Currency")
to_currency = st.text_input("To Currency")

def currency_converter(amount, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['conversion_result']
    else:
        st.write(f"Error: {response.json()['error-type']}")
        return None

amount = st.number_input("Enter amount", value=1.5, step=0.1, format="%.1f")

# Convert the currency and display the result in real-time
if from_currency and to_currency:
    converted_amount = currency_converter(amount, from_currency.upper(), to_currency.upper())
    if converted_amount:
        st.write(f"{amount:.1f} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}")
        
        # Get historical exchange rates
        history_url = f"https://v6.exchangerate-api.com/v6/{api_key}/history/{from_currency}/{to_currency}"
        history_response = requests.get(history_url)
        if history_response.status_code == 200:
            history_data = history_response.json()['history']
            df = pd.DataFrame(history_data.items(), columns=["Date", "Exchange Rate"])
            df["Date"] = pd.to_datetime(df["Date"])
            fig = px.line(df, x="Date", y="Exchange Rate", title=f"{from_currency.upper()}/{to_currency.upper()} Exchange Rates")
            st.plotly_chart(fig)
        else:
            st.write(f"Error: {history_response.json()['error-type']}")
