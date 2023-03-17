import requests
import json
import hmac
import hashlib
import time

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

# Function to generate signature
def generate_signature(secret, data):
    return hmac.new(secret.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()

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
method = 'POST'
timestamp = str(int(time.time() * 1000))
path = '/api/v1/orders'
data = {
    'symbol': symbol,
    'side': side,
    'size': order_size,
    'leverage': leverage,
    'type': order_type,
    'stopLoss': stop_loss,  # optional
    'takeProfit': take_profit  # optional
}
data_str = json.dumps(data)
signature_str = f"{timestamp}{method}{path}{data_str}"
signature = generate_signature(api_secret, signature_str)

headers = {
    'KC-API-KEY': api_key,
    'KC-API-SIGN': signature,
    'KC-API-TIMESTAMP': timestamp,
    'KC-API-PASSPHRASE': api_secret, # Replace with the API passphrase if one is required
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=data_str)

# Print the response
print(response.text)
