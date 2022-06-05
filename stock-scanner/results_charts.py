import os
from scan_results import *
from create_chart import create_chart

def results_charts():
    # Delete previous results and create new html files
    previous_files = ('/Users/joemiller/Documents/Coding/Stock-Scanner/stock-scanner/templates/results')
    for f in os.listdir(previous_files):
        os.remove(os.path.join(previous_files, f))

    if len(results_golden_cross) <1:
        with open('/Users/joemiller/Documents/Coding/Stock-Scanner/stock-scanner/templates/results/results_golden_cross.html', 'a') as f:
            f.write("The scan returned no results for this strategy today")
    else:
        for symbol, company in results_golden_cross.items():
            fig = create_chart(symbol, company)
            with open('/Users/joemiller/Documents/Coding/Stock-Scanner/stock-scanner/templates/results/results_golden_cross.html', 'a') as f:
                f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))

    if len(results_engulfing) <1:
        with open('/Users/joemiller/Documents/Coding/Stock-Scanner/stock-scanner/templates/results/results_engulfing.html', 'a') as f:
            f.write("The scan returned no results for this strategy today")
    else:
        for symbol, company in results_engulfing.items():
            fig = create_chart(symbol, company)
            with open('/Users/joemiller/Documents/Coding/Stock-Scanner/stock-scanner/templates/results/results_engulfing.html', 'a') as f:
                f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))

    if len(results_breakingout) <1:
        with open('/Users/joemiller/Documents/Coding/Stock-Scanner/stock-scanner/templates/results/results_breaking_out.html', 'a') as f:
            f.write("The scan returned no results for this strategy today")
    else:
        for symbol, company in results_breakingout.items():
            fig = create_chart(symbol, company)
            with open('/Users/joemiller/Documents/Coding/Stock-Scanner/stock-scanner/templates/results/results_breaking_out.html', 'a') as f:
                f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))

