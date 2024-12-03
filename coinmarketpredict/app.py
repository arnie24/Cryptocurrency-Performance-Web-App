from flask import Flask, render_template
from dotenv import load_dotenv
import os
import requests
import pandas as pd
import plotly.express as px

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()
API_KEY = os.getenv("COINMARKETCAP_API_KEY")

# Define the route to show data
@app.route('/')
def index():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {"X-CMC_PRO_API_KEY": API_KEY}
    params = {"start": 1, "limit": 10, "convert": "USD"}

    # Fetch data from CoinMarketCap API
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # Convert to DataFrame
    coins = pd.DataFrame(data['data'])

    # Extract relevant features
    coins['percent_change_24h'] = coins['quote'].apply(lambda x: x['USD']['percent_change_24h'])
    coins['percent_change_7d'] = coins['quote'].apply(lambda x: x['USD']['percent_change_7d'])

    # Debugging: Print all coins with 24h and 7d changes
    print(coins[['name', 'symbol', 'percent_change_24h', 'percent_change_7d']])

    # Reshape the data for a grouped bar chart
    grouped_data = coins.melt(
        id_vars=['name'],
        value_vars=['percent_change_24h', 'percent_change_7d'],
        var_name='Change Period',
        value_name='Percentage Change'
    )

    # Create the Plotly grouped bar chart
    fig = px.bar(
        grouped_data,
        x='name',
        y='Percentage Change',
        color='Change Period',
        barmode='group',
        title="Cryptocurrency Performance - 24h vs 7d Growth",
        labels={'name': 'Cryptocurrency', 'Percentage Change': 'Growth (%)'}
    )

    # Convert Plotly figure to HTML for embedding
    fig_html = fig.to_html(full_html=False)

    # Render HTML template with the data and the chart
    return render_template('index.html', coins=coins, plot_html=fig_html)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)