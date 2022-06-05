def is_consolidating(df):
    recent_candles = df[-16:-1]
    max_close = recent_candles['Close'].max()
    min_close = recent_candles['Close'].min()

    if min_close > (max_close * 0.97):
        return True
        
    return False

def is_breakingout(df):
    last_close = df[-1:]['Close'].values[0]
    
    if is_consolidating(df):
        recent_closes = df[-16:-1]
        if last_close > recent_closes['Close'].max():
            return True

    return False


        
