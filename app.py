from flask import Flask, render_template, request,flash,redirect,url_for,session
import flask
from flask_cors import CORS


import os
import subprocess
from datetime import datetime
import os
import json

from circularize import makeoutputdiv


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

@app.route('/circletextoutput')
def circletextoutput():

    specsdict=dict(
    maintext=request.form.get('maintext'),
    repeats=request.form.get('repeats'),
    )
    radius=request.form.get('radius')

    outputdiv,textlength=makeoutputdiv(**specsdict)


    return render_template('circletext.html',outputdiv=outputdiv)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

