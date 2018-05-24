# -*- coding: utf-8 -*-
"""
    Flask-upload-dropzone
    ===================================
    Summary: flask file upload with Dropzone.js.
    Author: Grey Li
    Repository: https://github.com/helloflask/flask-upload-dropzone
    License: MIT
"""
import os

from flask import Flask, render_template, request

app = Flask(__name__)
#app.config['UPLOADED_PATH'] = os.getcwd() + '/upload'
app.config['UPLOADED_PATH'] = "c:/webServer/uploads"

@app.route('/dropzoneUploadTest', methods=['GET', 'POST'])
def dropzoneUploadTest():
    if request.method == 'POST':
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('dropzoneUploadTest.html')

if __name__ == '__main__':
    app.run(host='192.168.161.46',debug=True)