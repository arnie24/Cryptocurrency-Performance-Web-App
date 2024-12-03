from dotenv import load_dotenv
import os
import requests
import pandas as pd

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("COINMARKETCAP_API_KEY")

# Ensure API key is loaded
if API_KEY:
    print(f"API Key loaded successfully: {API_KEY}")
else:
    print("Failed to load API Key. Check your .env file.")
# Step 1: Fetch data from CoinMarketCap
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
headers = {"X-CMC_PRO_API_KEY": API_KEY}
params = {"start": 1, "limit": 100, "convert": "USD"}

response = requests.get(url, headers=headers, params=params)

# Check for successful response
if response.status_code != 200:
    raise Exception(f"API Request failed with status code {response.status_code}: {response.text}")

data = response.json()

# Step 2: Convert to DataFrame
coins = pd.DataFrame(data['data'])

# Step 3: Feature Engineering
# Extract relevant columns from nested JSON
coins['percent_change_24h'] = coins['quote'].apply(lambda x: x['USD']['percent_change_24h'])
coins['volume_change_24h'] = coins['quote'].apply(lambda x: x['USD']['volume_change_24h'])

# Step 4: Predict rapidly growing coins
# Filter coins with >10% growth in the past 24 hours
growing_coins = coins[coins['percent_change_24h'] > 10]

# Display results
print(growing_coins[['name', 'symbol', 'percent_change_24h']])

