#!/usr/bin/env python
import os
from src import  ssh
from flask import Flask,  render_template
from pymongo import MongoClient
from flask import request


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
def valida_template():
    return render_template('ssh.html')

@app.route('/valida_ssh', methods=['POST'])
def valida_ssh():
    username = request.form['username']
    print(username)
    password = request.form['password']
    print(password)
    port=request.form['port']
    ip=request.form['ip']
    ssh.test_ssh_connection()

   

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)

