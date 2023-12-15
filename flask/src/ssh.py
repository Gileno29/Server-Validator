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
    if sudo_password_required:
        data['password']=' not same'
    else:
        data['password']='same'

    return data


def test_ssh_connection(ip, password, user, porta=22):
    hostname = ip
    port=porta
    username = password
    password = user
    conected=None
    client=None
    data={}
       
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password, port=port)
        conected=1
    except Exception as e:
        conected=0


    if conected==1:
    # Verificar se o usuário está no grupo sudo
        '''stdin, stdout, stderr = client.exec_command("groups")
        groups = stdout.read().decode().strip().split(" ")
        if "sudo" in groups:
            group_message = "O usuário está no grupo sudo."
        else:
            group_message = "O usuário NÃO está no grupo sudo."

        # Verificar se a senha é a mesma do usuário root
        stdin, stdout, stderr = client.exec_command("sudo -n true", get_pty=True)
        sudo_password_required = "sudo: a password is required" in stderr.read().decode()
        if sudo_password_required:
            password_message = [False, "A senha não é a mesma do usuário root."]
            return password_message
        else:
            password_message = "A senha é a mesma do usuário root."'''
        
        data= isSudo(client)
    
        if data["grupo"]=="is sudo" and  data['password']=='same':
            client.close()
            return ["Servidor acessivel", None]
            
        else:
            client.close()

            return ["Servidor Inacessivel", [data["grupo"],data["password"] ] ]

    # Exibir mensagem com os resultados
    #result_message = f"Conexão SSH estabelecida com sucesso!\n\n{group_message}\n{password_message}"
    return "Validado"


