import paramiko


def test_ssh_connection(ip, password, user, porta=22):
    hostname = ip
    port=porta
    username = password
    password = user

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password, port=port)

        # Verificar se o usuário está no grupo sudo
        stdin, stdout, stderr = client.exec_command("groups")
        groups = stdout.read().decode().strip().split(" ")
        if "sudo" in groups:
            group_message = "O usuário está no grupo sudo."
        else:
            group_message = "O usuário NÃO está no grupo sudo."

        # Verificar se a senha é a mesma do usuário root
        stdin, stdout, stderr = client.exec_command("sudo -n true", get_pty=True)
        sudo_password_required = "sudo: a password is required" in stderr.read().decode()
        if sudo_password_required:
            password_message = "A senha não é a mesma do usuário root."
        else:
            password_message = "A senha é a mesma do usuário root."

        client.close()

        # Exibir mensagem com os resultados
        result_message = f"Conexão SSH estabelecida com sucesso!\n\n{group_message}\n{password_message}"
        return result_message
    except Exception as e:
        print(e)