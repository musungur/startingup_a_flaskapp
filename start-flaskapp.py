'''
Starting flask app
'''
from flask import Flask
import os
import time
import sys

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World"

if __name__ == "__main__":
    localhost = "127.0.0.1"
    app = app.run(debug=True,host=localhost,port=5002)
