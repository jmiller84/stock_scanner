from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/daily_charts")
def daily_charts():
    return render_template('daily_charts.html')

@app.route("/scan_results")
def scan_results():
    return render_template('scan_results.html')

@app.route("/demo_results")
def demo_results():
    return render_template('demo_results.html')
