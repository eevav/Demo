from flask import Flask, render_template, request
#from processing import do_calculation
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    data = pd.read_csv("Backlog_europe.csv")
    return render_template("home.html",
                        kogus=len(data),
                        kogus2=len(data[data['Profile_type'] == 'PERSONAL']),
    kogus3=len(data[data['Profile_type'] == 'BUSINESS']))

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)