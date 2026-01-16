from main import app
from flask import render_template

@app.route("/")
def mainPage():
    return render_template("index.html")