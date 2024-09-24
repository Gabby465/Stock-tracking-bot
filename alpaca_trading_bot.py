import alpaca_trade_api as tradeapi
import time

# Alpaca API credentials (replace with your own)
API_KEY = 'PKMYJSNW3PQEXH7D03X0'
API_SECRET = '1Z2LaTfkhtXhoR7fEqqmiS8wIhhYeIVhasHIqC5r'
BASE_URL = 'https://paper-api.alpaca.markets/v2'

# Initialize Alpaca API connection
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Define stock symbol and trading thresholds
symbol = 'AAPL'  # Apple stock symbol
buy_price_threshold = 150.00  # Buy when the price is below this
sell_price_threshold = 160.00  # Sell when the price is above this

# Function to check the current stock price
def get_current_price(symbol):
    barset = api.get_barset(symbol, 'minute', 1)
    return barset[symbol][0].c  # Current price

# Function to place a buy order
def buy_stock(symbol, quantity):
    api.submit_order(
        symbol=symbol,
        qty=quantity,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    print(f"Bought {quantity} shares of {symbol}")

# Function to place a sell order
def sell_stock(symbol, quantity):
    api.submit_order(
        symbol=symbol,
        qty=quantity,
        side='sell',
        type='market',
        time_in_force='gtc'
    )
    print(f"Sold {quantity} shares of {symbol}")

# Main trading loop
while True:
    try:
        # Get the current price of the stock
        price = get_current_price(symbol)
        print(f"Current price of {symbol}: {price}")

        # Check if we should buy or sell
        if price < buy_price_threshold:
            print(f"Price is below {buy_price_threshold}, buying stock...")
            buy_stock(symbol, 10)  # Buy 10 shares
        elif price > sell_price_threshold:
            print(f"Price is above {sell_price_threshold}, selling stock...")
            sell_stock(symbol, 10)  # Sell 10 shares

        # Wait before checking again (1 minute)
        time.sleep(60)

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(60)
