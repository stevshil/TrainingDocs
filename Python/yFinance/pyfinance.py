import yfinance as yf
from pprint import pprint

# Define the ticker symbol
ticker_symbol = "AAPL"

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch historical market data
historical_data = ticker.history(period="1y").to_json()  # data for the last year
print("Historical Data:")
pprint(historical_data)

# Fetch basic financials
financials = ticker.financials.to_json()
print("\nFinancials:")
pprint(financials)

# Fetch stock actions like dividends and splits
actions = ticker.actions.to_json()
print("\nStock Actions:")
pprint(actions)