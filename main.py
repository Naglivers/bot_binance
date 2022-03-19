from binance.client import Client
from secrets import api_secret, api_key

client = Client (api_key, api_secret)
status = client.get_account_status()
print(status)

info = client.get_account()
for item in info:
    print(item)

from binance.enums import *
order = client.create_order(
    symbol='BRLUSDT',
    side=SIDE_BUY,
    type=ORDER_TYPE_MARKET,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='0.00001')

balance = client.get_asset_balance(asset='BTC')