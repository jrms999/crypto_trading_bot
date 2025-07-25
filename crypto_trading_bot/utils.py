import pandas as pd

def get_ohlcv(exchange, symbol, timeframe):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df

def crossover_signal(df, short_ma, long_ma):
    df['short'] = df['close'].rolling(short_ma).mean()
    df['long'] = df['close'].rolling(long_ma).mean()

    if df['short'].iloc[-2] < df['long'].iloc[-2] and df['short'].iloc[-1] > df['long'].iloc[-1]:
        return 'buy'
    elif df['short'].iloc[-2] > df['long'].iloc[-2] and df['short'].iloc[-1] < df['long'].iloc[-1]:
        return 'sell'
    else:
        return 'hold'
