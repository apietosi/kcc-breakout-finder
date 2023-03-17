import requests
import hmac
import hashlib
import time

# Configuration
API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'
SYMBOL = 'BTC-USDT'
ORDER_SIZE = 1
LEVERAGE = 10
ORDER_TYPE = 'market'  # or 'limit'
STOP_LOSS = 9500  # optional
TAKE_PROFIT = 10500  # optional

# Function to generate signature
def generate_signature(secret, data):
    return hmac.new(secret.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()

def place_order(api_key, api_secret, symbol, order_size, leverage, order_type, stop_loss=None, take_profit=None):
    url = 'https://futures.kucoin.com/api/v1/orders'
    method = 'POST'
    timestamp = str(int(time.time() * 1000))
    path = '/api/v1/orders'
    data = {
        'symbol': symbol,
        'side': 'buy',  # or 'sell'
        'size': order_size,
        'leverage': leverage,
        'type': order_type,
    }
    if stop_loss:
        data['stopLoss'] = stop_loss
    if take_profit:
        data['takeProfit'] = take_profit

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

    try:
        response = requests.post(url, headers=headers, data=data_str)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error occurred: {err}")
        return None

    return response.json()


def main():
    response = place_order(API_KEY, API_SECRET, SYMBOL, ORDER_SIZE, LEVERAGE, ORDER_TYPE, STOP_LOSS, TAKE_PROFIT)

    if response:
        print(response)


if __name__ == '__main__':
    main()
