import streamlit as st
import requests

# Function to fetch cryptocurrency prices from an open API
def get_crypto_prices():
    # Make a GET request to the API endpoint
    response = requests.get("https://api.coincap.io/v2/assets")
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        
        # Extract the cryptocurrency prices from the data
        crypto_prices = {asset['symbol']: asset['priceUsd'] for asset in data['data']}
        
        # Return the cryptocurrency prices as a dictionary
        return crypto_prices
    else:
        # If the request was not successful, return an empty dictionary
        return {}

# Get the cryptocurrency prices
crypto_prices = get_crypto_prices()
# Set the title of the web app
st.title("Crypto Converter")
st.write("This is a simple app that allows you to convert between Crypto and Fiat currencies. Both Fiat and Crypto prices are always up to date with the latest prices thanks to the CoinCap API.")
# Prompt the user to choose the conversion type

st.write("---")
st.write("On this module choose the conversion type you want to perform")
conversion_type = st.selectbox("Select conversion type", ["Fiat to Crypto", "Crypto to Crypto"])
st.markdown("---")
if conversion_type == "Fiat to Crypto":
    # Prompt the user to choose a fiat currency
    fiat_currency = st.selectbox("Select a fiat currency", ["USD", "EUR", "GBP"])
    # Prompt the user to enter the amount
    amount = st.number_input("Enter the amount", min_value=0.0)
    # Prompt the user to choose a cryptocurrency
    crypto_currency = st.selectbox("Select a cryptocurrency", list(crypto_prices.keys()))
    
    # Check if the selected cryptocurrency exists in the prices dictionary
    if crypto_currency in crypto_prices:
        # Get the price of the selected cryptocurrency
        crypto_price = float(crypto_prices[crypto_currency])
        
        # Calculate the converted amount
        converted_amount = amount / crypto_price
        
        # Print the result
        st.write(f"The converted amount is {converted_amount:.8f} {crypto_currency}")
    else:
        st.write("Invalid cryptocurrency selected")
        
else:
    # Prompt the user to choose the source cryptocurrency
    source_crypto_currency = st.selectbox("Select a source cryptocurrency", list(crypto_prices.keys()))
    
    # Prompt the user to enter the amount
    amount = st.number_input("Enter the amount", min_value=0.0)
    
    # Prompt the user to choose the target cryptocurrency
    target_crypto_currency = st.selectbox("Select a target cryptocurrency", list(crypto_prices.keys()))
    
    # Check if both selected cryptocurrencies exist in the prices dictionary
    if source_crypto_currency in crypto_prices and target_crypto_currency in crypto_prices:
        # Get the prices of the selected cryptocurrencies
        source_crypto_price = float(crypto_prices[source_crypto_currency])
        target_crypto_price = float(crypto_prices[target_crypto_currency])
        
        # Calculate the converted amount
        converted_amount = (amount * source_crypto_price) / target_crypto_price
        
        # Print the result
        st.write(f"The converted amount is {converted_amount:.8f} {target_crypto_currency}")
    else:
        st.write("Invalid cryptocurrencies selected")

st.write("Made with ❤️ by [NickBalatos](https://github.com/NickBalatos)")
