# stock_scanner

S&P 500 Stock Scanner built using Python and Flask

The program scans a list of approximately 500 companies to find daily buying opportunities for potential day traders and investors. 

Using the yahoo finance library to download daily price data for all of the companies the program then applies 3 different trading strategies to each of the datasets to see if there are any possible buying opportunities for the current day.

The program updates using crontab everyday at 10.30pm GMT as daily price data is updated at 10.00pm GMT.

The results are displayed on a web app which can be viewed at:

https://jmiller84.pythonanywhere.com/home


The 3 Strategies

Golden Cross Strategy

The golden cross strategy is trigged when the 50 SMA crosses above the 200 SMA.

2.  Engulfing Strategy 

The engulfing strategy is trigged when the chart displays 3 consecutive red candles followed by a large green candle showing a possible price reversal 

3. Breakout Strategy 

The breakout strategy is trigged after a period of price consolidation in which the stock has traded within a tight range of 3% or less from the past 15 candles and then price closes above this tight range.
