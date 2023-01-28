import requests
import json

# Set your API key and secret
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Set the symbol for the futures contract you want to trade
symbol = 'BTC-USDT'

# Set the timeframe for the chart data (1min, 5min, 15min, 30min, 60min, 1day, 1week)
timeframe = '1h'

# Set the number of candles to look back for the breakout calculation
num_candles = 100

# Send a request to the Kucoin Futures API to get the chart data
url = f'https://futures.kucoin.com/api/v1/market/candles?symbol={symbol}&timeframe={timeframe}&limit={num_candles}'
headers = {'KC-API-KEY': api_key, 'KC-API-SECRET': api_secret}
response = requests.get(url, headers=headers)

# Parse the response and extract the chart data
data = json.loads(response.text)
candles = data['data']['candles']

# Calculate the high and low over the past num_candles candles
high = max([candle[2] for candle in candles])
low = min([candle[3] for candle in candles])

# Calculate the breakout price as the average of the high and low
breakout_price = (high + low) / 2

# Print the breakout price
print(f'Breakout price: {breakout_price}')
