# See https://www.geeksforgeeks.org/python/how-to-use-yfinance-api-with-python/

import yfinance as yf
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/stocks/<stock>")
def stock(stock):
    stkperiod="1d"
    ticker = yf.Ticker(stock)

    # Historical data
    historical_data = ticker.history(period=stkperiod).to_json()

    # Fetch basic financials
    financials = ticker.financials.to_json()

    # Fetch stock actions like dividends and splits
    actions = ticker.actions.to_json()

    data = {
        f"historical-{stkperiod}": historical_data,
        "financials": financials,
        "actions": actions}
    
    return jsonify(data)

@app.route("/stocks/<stock>/<stkperiod>")
def stocks(stock, stkperiod):
    ticker = yf.Ticker(stock)

    # Historical data
    historical_data = ticker.history(period=stkperiod).to_json()

    # Fetch basic financials
    financials = ticker.financials.to_json()

    # Fetch stock actions like dividends and splits
    actions = ticker.actions.to_json()

    data = {
        f"historical-{stkperiod}": historical_data,
        "financials": financials,
        "actions": actions}
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)