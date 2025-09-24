from flask import Flask, render_template, request,flash,redirect,url_for,session
import flask
from flask_cors import CORS


import os
import subprocess
from datetime import datetime
import os
import json

from circularize import makespans


app=Flask(__name__)
app.secret_key = "keytest" 

CORS(app, origins=[
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5501",
    "http://127.0.0.1:5503"
])



@app.route("/")
def index():
    # render template looks in template folder by default
    return render_template('index.html')

@app.route("/specsform",methods=["GET","POST"])
def specsform():
    return render_template('specsform.html')

# this needs to accept post requests since its receiving the form
@app.route('/circletextoutput',methods=["GET","POST"])
def circletextoutput():

    specsdict=dict(
    maintext=request.form.get('maintext'),
    repeats=request.form.get('repeats'),
    )
    # do something with radius later
    radius=request.form.get('radius')
    # semicircle is a boolean?
    semicircle = bool(request.form.get("semicircle"))

    # I need to pass text length to the css somehow.
    '''
    Ideas:
    1. Put the text length as a hidden element on the page and read from it with JavaScript. Then use the JS to update the CSS.
    2. update it with python somehow
    '''
    spans=makespans(**specsdict)


    return render_template('circletext.html',spans=spans,semicircle=semicircle)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

