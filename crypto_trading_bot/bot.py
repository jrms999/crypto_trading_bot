import ccxt
import pandas as pd
import time
from config import *
from utils import get_ohlcv, crossover_signal

exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True
})

def trade():
    while True:
        try:
            df = get_ohlcv(exchange, SYMBOL, TIMEFRAME)
            signal = crossover_signal(df, SHORT_MA, LONG_MA)
            balance = exchange.fetch_balance()

            if signal == 'buy' and balance['USDT']['free'] > TRADE_AMOUNT * df['close'].iloc[-1]:
                print("Buying...")
                exchange.create_market_buy_order(SYMBOL, TRADE_AMOUNT)
            elif signal == 'sell' and balance['BTC']['free'] > TRADE_AMOUNT:
                print("Selling...")
                exchange.create_market_sell_order(SYMBOL, TRADE_AMOUNT)
            else:
                print("No action.")

        except Exception as e:
            print("Error:", e)

        time.sleep(60)

if __name__ == '__main__':
    trade()
