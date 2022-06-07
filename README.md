# stock_scanner

S&P 500 Stock Scanner built using Python and Flask

This program scans a list of approximately 500 companies to find daily buying opportunities for potential day traders and investors. 

Using the yahoo finance library to download daily price data for all of the companies the program then applies 3 different trading strategies to each of the datasets to see if there are any possible buying opportunities for the current day.

The program updates using crontab everyday at 10.30pm GMT I selected this time as daily stock trading data is updated at 10.00pm GMT.

I have built a basic front end to display the results using Flask the flask application can be viewed here:

https://jmiller84.pythonanywhere.com/home


The 3 Trading Strategies implemented by the program are:

1. The Golden Cross Strategy

The golden cross strategy is trigged when the 50 SMA line crosses above the 200 SMA line. This simple moving average crossover strategy is thouhgt to be a good indication that a stock is moving into an uptred.

2.  Engulfing Strategy 

The engulfing strategy is trigged when the chart displays 3 consecutive red candles followed by a large green candle showing a possible price reversal in the stock.

3. Breakout Strategy 

The breakout strategy is trigged after a period of price consolidation in which the stock has traded within a tight range of 3% or less from the past 15 candles and then the current candle closes above this range. Often stocks will see an explosive move upwards after an extended period of consilidation this strategy flags these occuracnes.
