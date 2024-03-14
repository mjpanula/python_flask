from flask import Flask, redirect, request, jsonify
from data_structures import MySingleStringHolder
import html_helper as h

my_data = MySingleStringHolder("Hello World")
circle_coordinates = {"x": 100, "y": 100, "radius": 50}

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def root_get():
    html_body = h.form(h.form_name) + "<br>Circle: " + str(circle_coordinates) + "<br>"
    html_body += open('canvas.html', 'r').read()
    html = h.root("Otsikko", html_body)
    return html

@app.route("/", methods = ["POST"])
def root_post():    
    coords = request.form[h.form_name].split(",")
    global circle_coordinates
    circle_coordinates = {"x": int(coords[0]), "y": int(coords[1]), "radius": int(coords[2])}
    
    return redirect("/")

@app.route("/circle-coordinates", methods = ["GET"])
def circle_get():    
    return jsonify(circle_coordinates)

if __name__ == "__main__":
    app.run()
    