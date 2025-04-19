import os
import time
from binance.client import Client
from binance.enums import *

api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')
client = Client(api_key, api_secret)

def get_price(symbol='BTCUSDT'):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

def place_market_buy(symbol='BTCUSDT', usdt_amount=10):
    price = get_price(symbol)
    quantity = round(usdt_amount / price, 6)
    order = client.create_order(
        symbol=symbol,
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        quantity=quantity
    )
    return order

def place_market_sell(symbol='BTCUSDT', quantity=0.001):
    order = client.create_order(
        symbol=symbol,
        side=SIDE_SELL,
        type=ORDER_TYPE_MARKET,
        quantity=quantity
    )
    return order

def trade_with_strategy(symbol='BTCUSDT', buy_amount=10, sl=0.98, tp=1.05):
    buy_order = place_market_buy(symbol, buy_amount)
    entry_price = get_price(symbol)
    while True:
        current_price = get_price(symbol)
        pnl = current_price / entry_price
        if pnl <= sl:
            place_market_sell(symbol, float(buy_order['executedQty']))
            break
        elif pnl >= tp:
            place_market_sell(symbol, float(buy_order['executedQty']))
            break
        time.sleep(15)
