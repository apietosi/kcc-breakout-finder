import requests
import json

# Set your API key and secret
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Set the symbol for the futures contract you want to trade
symbol = 'BTC-USDT'

# Set the breakout price
breakout_price = 10000

# Set the order size and other trade parameters
order_size = 1
leverage = 10
order_type = 'market'  # or 'limit'
stop_loss = 9500  # optional
take_profit = 10500  # optional

# Set the order side ('buy' or 'sell') based on the current price
url = f'https://futures.kucoin.com/api/v1/market/ticker?symbol={symbol}'
response = requests.get(url)
data = json.loads(response.text)
price = data['data']['lastPrice']
if price > breakout_price:
    side = 'buy'
else:
    side = 'sell'

# Place the order
url = 'https://futures.kucoin.com/api/v1/orders'
headers = {'KC-API-KEY': api_key, 'KC-API-SECRET': api_secret}
data = {
    'symbol': symbol,
    'side': side,
    'size': order_size,
    'leverage': leverage,
    'type': order_type,
    'stopLoss': stop_loss,  # optional
    'takeProfit': take_profit  # optional
}
response = requests.post(url, headers=headers, json=data)

# Print the response
print(response.text)
