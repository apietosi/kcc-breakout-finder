import requests
import json
import hmac
import hashlib
import time

def generate_signature(secret, data):
    return hmac.new(secret.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()

def place_order(api_key, api_secret, symbol, side, order_size, leverage, order_type, stop_loss, take_profit):
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
        'stopLoss': stop_loss,
        'takeProfit': take_profit
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
    return response.text
