from os import name
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
stations = pd.read_csv("data/stations.txt", skiprows=17)

@app.route("/")
def home():
    return render_template("home.html", data=stations[['STAID', 'STANAME                                 ']].to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    file_name = "data/TG_STAID"+ str(station).zfill(6) + ".txt"
    df = pd.read_csv(file_name, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE']==date]["   TG"].squeeze()/10

    return {"station": station, "date": date, "temperature": temperature }


@app.route("/api/v1/yearly/<station>/<year>")
def api_year(station, year):
    file_name = "data/TG_STAID"+ str(station).zfill(6) + ".txt"
    df = pd.read_csv(file_name, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    results = df[df['    DATE'].str.startswith(str(year))]

    return results.to_dict(orient='records')

if __name__ == "__main__":
    app.run(debug=True, port=5000)