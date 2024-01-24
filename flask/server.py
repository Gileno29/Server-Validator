#!/usr/bin/env python
import os
from src import  ssh
from flask import Flask,  render_template
from pymongo import MongoClient
from flask import request
from src import FieldsValidator


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

@app.route('/valida_ssh', methods=['POST','GET'])
def valida_ssh():
    ip=''
    port=''
    password=''
    port=''
    username=''
    dados={}
    validator=FieldsValidator.FieldValidador()
    print(request.form)
    if validator.ip_is_valid(request.form['ip']):
         ip=request.form['ip']
    else:
        error="Ip is not Valid"
        return error
   
    if validator.is_not_null(request.form['username']):
        username = request.form['username']
    else:
        erro='username esta vazio'
        return erro
   
    if validator.is_not_null(request.form['password']):
         password = request.form['password']
    else:
        erro='senha esta vazio'
        return erro
    
    port=request.form['port']
    ip=request.form['ip']    
    conexao=ssh.test_ssh_connection(ip, password,username, port)
    if 'Servidor acessivel' in conexao:
        dados={'ip': ip, 'port':port, 'password':password, 'username':username}
        return render_template('ssh.html', conexao=conexao, dados=dados )
    else:
        dados=None
        return render_template('ssh.html', conexao=conexao)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)

