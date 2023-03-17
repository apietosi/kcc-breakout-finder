import time
from bs2 import get_breakout_price
from buysell import get_order_side
from kcc_var_1 import place_order

# Set your API key and secret
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Set other parameters
symbol = 'BTC-USDT'
timeframe = '1h'
num_candles = 100
order_size = 1
leverage = 10
order_type = 'market'
stop_loss = 9500
take_profit = 10500

# Define the main loop
def main():
    while True:
        try:
            # Get the breakout price
            breakout_price = get_breakout_price(api_key, api_secret, symbol, timeframe, num_candles)

            # Get the order side
            side = get_order_side(api_key, api_secret, symbol, breakout_price)

            # Place the order
            response = place_order(api_key, api_secret, symbol, side, order_size, leverage, order_type, stop_loss, take_profit)

            print(response)
            
            # Sleep for some time before running the loop again
            time.sleep(60 * 60)  # Sleep for 1 hour

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)  # Sleep for 1 minute before retrying

if __name__ == "__main__":
    main()
