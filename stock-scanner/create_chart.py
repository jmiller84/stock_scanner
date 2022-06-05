import yfinance as yf
import plotly.graph_objects as go
import datetime
from datetime import date

start_date = date.today() - datetime.timedelta(days=365*2)
end_date = date.today()

def create_chart(symbol, company):
    df = yf.download(symbol, start_date, end_date)
    df['SMA_S'] = df['Close'].rolling(50).mean()
    df['SMA_L'] = df['Close'].rolling(200).mean()
    df['SMA_5'] = df['Close'].rolling(5).mean()

    fig = go.Figure(data=[go.Candlestick(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'], name = "Daily Candles"),
                    go.Scatter(x=df.index, y=df.SMA_5, line=dict(color='red', width=1), name= "SMA 5"),
                    go.Scatter(x=df.index, y=df.SMA_S, line=dict(color='orange', width=1), name= "SMA 50"),
                    go.Scatter(x=df.index, y=df.SMA_L, line=dict(color='green', width=1), name= "SMA 200")])

    fig.update_layout(xaxis_rangeslider_visible=False, title= "{} - {} Daily Chart".format(symbol, company))

    return fig