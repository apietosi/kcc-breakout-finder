import requests
import json

def get_order_side(api_key, api_secret, symbol, breakout_price):
    url = f'https://futures.kucoin.com/api/v1/market/ticker?symbol={symbol}'
    response = requests.get(url)

    data = json.loads(response.text)
    price = data['data']['lastPrice']

    if price > breakout_price:
        side = 'buy'
    else:
        side = 'sell'
    return side
