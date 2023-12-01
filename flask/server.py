#!/usr/bin/env python
import os

from flask import Flask,  render_template
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient("mongo:27017")

@app.route('/')
def principal():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return render_template('index.html')

@app.route('/ssh')
def valida_ssh():
    return render_template('ssh.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)

