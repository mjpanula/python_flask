from flask import Flask, redirect, request, url_for
import html_generator as h

app = Flask(__name__)

@app.route("/")
def get_root():    
    return h.make_body("titteli", h.form())

@app.route("/", methods = ["POST"])
def post_test():    
    return redirect(url_for("/"))
    