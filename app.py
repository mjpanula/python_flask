from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Tämä on HTTP-pyyntöön vastaus (response)"