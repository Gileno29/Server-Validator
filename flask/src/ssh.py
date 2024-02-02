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


def test_ssh_connection(ip, password, user, porta=22):
    conected=[{'Conectado':1, 'erro':None}]
    client=None
    data={}
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=ip, username=user, password=password, port=porta)
        print(client)
        conected=1
    except Exception as e:
        print(e)
        conected[0]['Conectado']=0
        conected[0]['erro']=e

    if conected[0]['Conectado']==1:
        data= isSudo(client)
    
        if (data["grupo"]=="is sudo" and  data['password']=='same'):
            client.close()
            return [{'Status':"Servidor acessivel", 'Permissao':'Possui permissão de super usuario'}]
        elif data["grupo"]=="is not sudo" and  data['password']=='same':
            return [{'Status':"Servidor acessivel", 'Permissao':'Não possui permissão de super usuario, é preciso acessar pelo usuario root'}]
           

    # Exibir mensagem com os resultados
    #result_message = f"Conexão SSH estabelecida com sucesso!\n\n{group_message}\n{password_message}"
    return  ["Servidor Inacessivel", conected ]


