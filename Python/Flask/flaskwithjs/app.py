from flask import Flask, render_template, request
from random import random
from datetime import datetime
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def mainpage():
    return render_template("mainpage.html")

@app.route("/number")
def numbers():
    num = int(random()*10000)
    print(f"Number: {num}")
    return str(num)

@app.route("/clock")
def clocks():
    dt = datetime.now()
    return json.dumps({"time": datetime.strftime(dt,"%H:%M:%S"), "date": datetime.strftime(dt,"%d %B %Y")})

if __name__ == "__main__":
    app.run(debug=True)