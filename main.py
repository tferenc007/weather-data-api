from os import name
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def about(word):
    df = pd.read_csv("data/dictionary.csv", sep=',')

    definition = df.loc[df['word']==word]["definition"].squeeze()
    return {"definition": definition, "word": word}
if __name__ == "__main__":
    app.run(debug=True, port=5000)