from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
import io
import csv

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def uploadXlsm():
    if request.method == 'POST':
        print('POST')
        f = request.files['fileToUpload']
        if not f:
            return "No file"
        stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
        csv_input = csv.reader(stream, delimiter=';')
        print(csv_input)
        for row in csv_input:
            print(row)

        return render_template('upload.html')
