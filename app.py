from flask import Flask, redirect, request, url_for
import html_generator as h

app = Flask(__name__)

some_data = "Hello World"

@app.route("/")
def root_get():    
    return h.make_body("titteli", h.form() + "<br>" + some_data)

@app.route("/", methods = ["POST"])
def root_post():
    global some_data # käytetään globaalia muuttujaa
    some_data = request.form['fname']
    return redirect(url_for("root_get"))

app.run()
    