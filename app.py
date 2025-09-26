from flask import Flask, render_template, request,flash,redirect,url_for,send_file
from io import BytesIO
from PIL import Image
from werkzeug.utils import secure_filename
import uuid, time



import flask
from flask_cors import CORS


import os
import subprocess
from datetime import datetime
import os
import json

from circularize import makespans
UPLOAD_FOLDER = "static/uploads" 

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
    
    

    # I need to pass text length to the css somehow.
    '''
    Ideas:
    1. Put the text length as a hidden element on the page and read from it with JavaScript. Then use the JS to update the CSS.
    2. update it with python somehow
    '''
    imagefile = request.files["image"]

    path = None
    if imagefile and imagefile.filename:  #
        def check_deletion():
            now = time.time()
            for f in os.listdir(UPLOAD_FOLDER):
                filepath = os.path.join(UPLOAD_FOLDER, f)
                if os.path.isfile(filepath):
                    # delete if older than 3600 seconds (1 hour)

                    wait=False
                    if not wait:
                        os.remove(filepath)
                    elif wait:
                        if now - os.path.getmtime(filepath) > 3600:
                            os.remove(filepath)
        check_deletion()

        # Extract extension
        ext = os.path.splitext(imagefile.filename)[1].lower()  # e.g. ".png" or ".jpg"
        if ext not in [".png", ".jpg", ".jpeg"]:
            return render_template("error.html", message="Unsupported file type"), 400

        # Generate safe unique filename
        filename = secure_filename(imagefile.filename)
        path = os.path.join("static/uploads", filename)

        # Save file
        imagefile.save(path)
        


    

    spans=makespans(**specsdict)
    full_inputs = dict(
        spans=spans,
        radius=request.form.get('radius'),
        semicircle=request.form.get('semicircle') == 'on',
        # added defaults
        colorone=request.form.get('colorone','#045393'),
        colortwo=request.form.get('colortwo','#fbd08b'),
        animationduration=f'{request.form.get('animationduration')}s',
        imageurl=path
        
    )


    return render_template('circletext.html',**full_inputs)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

