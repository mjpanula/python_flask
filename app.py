from flask import Flask, redirect, request
import html_generator as h

app = Flask(__name__)

some_data = "Hello World"
form_name = "fname"

@app.route("/", methods = ["GET"])
def root_get():
    html_body = h.form(form_name) + "<br>" + some_data
    html = h.root("Otsikko", html_body)
    return html

@app.route("/", methods = ["POST"])
def root_post():
    global some_data # käytetään globaalia muuttujaa
    some_data = request.form[form_name]
    return redirect("/")

if __name__ == "__main__":
    app.run()
    