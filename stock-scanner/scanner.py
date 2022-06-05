import yfinance as yf
import datetime
from strategies.golden_cross import is_golden_cross
from strategies.engulfing import is_engulfing
from strategies.breakout import is_breakingout 
from datetime import date

def scan():
    start_date = date.today() - datetime.timedelta(days=365)
    end_date = date.today()

    golden_cross = {}
    engulfing = {}
    breakingout = {}
    failed_symbols = {}

    with open('companies.csv') as f:
        companies = f.read().splitlines()
        for company in companies:
            symbol = company.split(',')[0]
            company_name = company.split(',')[1]
            df  = yf.download(symbol,start_date, end_date)
                
            try:
                is_golden_cross(df)
                if is_golden_cross(df):
                    golden_cross[symbol] = company_name
                if is_engulfing(df):
                    engulfing[symbol] = company_name
                if is_breakingout(df):
                    breakingout[symbol] = company_name
            except:
                print('Symbol may have been delisted')
                failed_symbols[symbol] = company_name

        print("Golden Cross triggered: ", golden_cross)
        print("Engulfing triggered: ", engulfing)
        print("Breakout detected: ", breakingout)
        print("Failed symbols: ", failed_symbols)

    results_file = open("scan_results.py", "w")
    results_file.write("results_golden_cross = " + str(golden_cross) + "\n")
    results_file.write("results_engulfing = " + str(engulfing) + "\n")
    results_file.write("results_breakingout = " + str(breakingout) + "\n")
    results_file.close()