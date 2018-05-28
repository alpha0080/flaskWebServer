import os
import json
import sys

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

app = Flask(__name__)




if __name__ == '__main__':
    ##app.run(host='192.168.161.46',debug=True)
    app.run(debug=True)