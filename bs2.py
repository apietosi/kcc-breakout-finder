import requests
import json

def get_breakout_price(api_key, api_secret, symbol, timeframe, num_candles):
    url = f'https://futures.kucoin.com/api/v1/market/candles?symbol={symbol}&timeframe={timeframe}&limit={num_candles}'
    response = requests.get(url)

    data = json.loads(response.text)
    candles = data['data']['candles']

    high = max([float(candle[2]) for candle in candles])
    low = min([float(candle[3]) for candle in candles])

    breakout_price = (high + low) / 2
    return breakout_price
