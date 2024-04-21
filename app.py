import os
from flask import Flask, render_template, request, redirect, url_for
from cvzone.HandTrackingModule import HandDetector
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle file upload here
        uploaded_files = request.files.getlist('files')
        if uploaded_files:
            for file in uploaded_files:
                # Save the uploaded file to the 'presentation' folder
                file.save(os.path.join('presentation', file.filename))
            return redirect(url_for('present'))
    return render_template('index.html')

@app.route('/present')
def present():
    pathImages = sorted(os.listdir('presentation'), key=len)
    return render_template('presentation.html', images=pathImages)