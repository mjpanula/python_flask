from flask import Flask, redirect, request
from data_structures import MySingleStringHolder
import html_helper as h

my_data = MySingleStringHolder("Hello World")

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def root_get():
    html_body = h.form(h.form_name) + "<br>My data: " + my_data.get()
    html = h.root("Otsikko", html_body)
    return html

@app.route("/", methods = ["POST"])
def root_post():    
    my_data.set(request.form[h.form_name])
    return redirect("/")

if __name__ == "__main__":
    app.run()
    