import ccxt
import pandas as pd

def fetch_data(symbol="XAUT/USDT", timeframe="15m", limit=100):
    exchange = ccxt.bitfinex()
    try:
        ohlcv = exchange.fetch_ohlcv(symbol=symbol, timeframe=timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        print(f"Xatolik: {e}")
        return pd.DataFrame()
