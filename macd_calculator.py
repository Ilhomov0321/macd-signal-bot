import pandas as pd
import ta

def calculate_macd(dataframe):
    """
    MACD, Signal va Histogramni hisoblaydi va DataFrame'ga qo'shadi.
    """
    macd = ta.trend.MACD(
        close=dataframe['close'], 
        window_slow=26, 
        window_fast=12, 
        window_sign=9
    )

    dataframe['MACD'] = macd.macd()
    dataframe['Signal'] = macd.macd_signal()
    dataframe['Histogram'] = macd.macd_diff()
    
    return dataframe

def get_macd_signal(dataframe):
    """
    MACD va Signal chiziqlarini kesishmalarini aniqlaydi va signalni chiqaradi.
    """
    if len(dataframe) < 2:
        return "NO SIGNAL"

    last_row = dataframe.iloc[-1]
    prev_row = dataframe.iloc[-2]

    macd_now = last_row['MACD']
    signal_now = last_row['Signal']
    macd_prev = prev_row['MACD']
    signal_prev = prev_row['Signal']

    if macd_prev < signal_prev and macd_now > signal_now:
        return "BUY"
    elif macd_prev > signal_prev and macd_now < signal_now:
        return "SELL"
    
    return "NO SIGNAL"
