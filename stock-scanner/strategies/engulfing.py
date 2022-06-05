def is_engulfing(df):
    cond1 = df['Open'][-2] > df['Close'][-2] # prev candle is red
    cond2 = df['Open'][-3] > df['Close'][-3] # prev 2 candles are red
    cond3 = df['Open'][-4] > df['Close'][-4] # prev 3 candles are red  
    cond4 = df['Open'][-1] < df['Close'][-1]
    cond5 = df['Open'][-1] < df['Close'][-2]   
    cond6 = df['Close'][-1] > df['Open'][-2]   
    return (cond1 and cond2 and cond3 and cond4 and cond5 and cond6)

