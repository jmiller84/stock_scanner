def is_golden_cross(df):
    df['SMA_S'] = df['Close'].rolling(50).mean()
    df['SMA_L'] = df['Close'].rolling(200).mean()
    
    if df['SMA_L'][-2] > df['SMA_S'][-2] and df['SMA_S'][-1] > df['SMA_L'][-1]:
        return True

    return False
