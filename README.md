# Cryptocurrency-Performance-Web-App
Overview

This web app fetches real-time cryptocurrency data from the CoinMarketCap API and displays the top 10 cryptocurrencies with their 24h and 7d percentage changes. It uses Flask for the backend and Plotly for visualizing the cryptocurrency performance in a grouped bar chart.

	1.	Clone the repository:
 git clone https://github.com/arnie24/Cryptocurrency-Performance-Web-App.git
cd Cryptocurrency-Performance-Web-App

	2.	Set up a virtual environment (optional but recommended):
 python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

	3.	Install dependencies:
 pip install -r requirements.txt

 	4.	Set up environment variables:
	•	Create a .env file in the root of your project and add your CoinMarketCap API key (Free with making an account):
 COINMARKETCAP_API_KEY=your_api_key_here

	5.	Run the Flask app:
 python app.py

 
Features

	•	Display real-time data for the top 10 cryptocurrencies.
	•	Show percentage changes in 24h and 7d periods.
	•	Interactive Plotly chart for cryptocurrency performance comparison.
	•	Responsive design for better accessibility on mobile and desktop.

Technologies Used

	•	Python (Flask)
	•	Plotly (for charting)
	•	Pandas (for data manipulation)
	•	HTML/CSS (for frontend)
	•	CoinMarketCap API (for cryptocurrency data)
	•	Git (version control)
Feel free to fork the repository, submit issues, or open pull requests. If you’d like to contribute, please follow these steps:
	1.	Fork the repository.
	2.	Create a feature branch.
	3.	Submit a pull request with a description of the changes.

License

This project is open source and available under the MIT License.
	•	Data is provided by CoinMarketCap.
