import paramiko
import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import pyperclip

def test_ssh_connection():
    hostname = entry_hostname.get()
    username = entry_username.get()
    password = entry_password.get()

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)

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
        messagebox.showinfo("Resultados", result_message)

        # Copiar a mensagem para a área de transferência
        pyperclip.copy(result_message)
        messagebox.showinfo("Copiado", "A mensagem foi copiada para a área de transferência.")
    except paramiko.AuthenticationException:
        messagebox.showerror("Erro de autenticação", "Falha na autenticação. Verifique o nome de usuário e senha.")
    except paramiko.SSHException as e:
        messagebox.showerror("Erro de conexão SSH", f"Erro na conexão SSH: {str(e)}")
    except paramiko.Exception as e:
        messagebox.showerror("Erro", f"Erro: {str(e)}")