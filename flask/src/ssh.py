import paramiko

def isSudo(conection):
    stdin, stdout, stderr = conection.exec_command("groups")
    groups = stdout.read().decode().strip().split(" ")
    data={}
    if "sudo" in groups:
        group_message = "O usuário está no grupo sudo."
        data['grupo']="is sudo"
    else:
        data['grupo']="is not sudo"
    
    # Verificar se a senha é a mesma do usuário root
    stdin, stdout, stderr = conection.exec_command("sudo -n true", get_pty=True)
    sudo_password_required = "sudo: a password is required" in stderr.read().decode()
    print("Sudo password require", sudo_password_required)
    if sudo_password_required:
        data['password']='not same'
    else:
        data['password']='same'
    return data


def conexao(dados):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=dados['ip'], username=dados['user'], password=dados['password'], port=dados['porta'])
        return [True, client]
    except Exception as e:
        return [False, e]

def test_ssh_connection(ip, password, user, porta=22,):
    dados={'ip':ip,'password':password,'user':user,'porta':porta}
    conectado=conexao(dados)
    data={}
   
    if conectado[0]==True:
        data= isSudo(conectado[1])
    
        if (data["grupo"]=="is sudo" and  data['password']=='same'):
           conectado[1].close()
           return [{'status':"Servidor acessivel", 'Permissao':'Possui permissão de super usuario'}]
        elif data["grupo"]=="is not sudo" and  data['password']=='same':
            return [{'status':"Servidor acessivel", 'Permissao':'Não possui permissão de super usuario, é preciso acessar pelo usuario root'}]
  


    # Exibir mensagem com os resultados
    #result_message = f"Conexão SSH estabelecida com sucesso!\n\n{group_message}\n{password_message}"
    return  [{'status':"Servidor Inacessivel", "conected":conectado}]


