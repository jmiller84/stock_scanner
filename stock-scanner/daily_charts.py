import os
from create_chart import create_chart

# Delete previous html files and generate new charts

def daily_charts():
    previous_files = ('/Users/joemiller/Documents/Coding/Stock-Scanner/stock-scanner/templates/price_charts')
    for f in os.listdir(previous_files):
        os.remove(os.path.join(previous_files, f))

    symbols = {'BTC-USD':'Bitcoin', 'ETH-USD':'Etherium', 'SPY':'S&P 500', 'TSLA':'Tesla'}

    for symbol, company in symbols.items():  
        fig = create_chart(symbol, company)

        with open('/Users/joemiller/Documents/Coding/Stock-Scanner/stock-scanner/templates/price_charts/price_chart_{}.html'.format(symbol), 'w') as f:
            f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))
