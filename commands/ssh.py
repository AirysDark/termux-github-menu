
import paramiko
from rich.prompt import Prompt

def execute():
    host=Prompt.ask("Host")
    user=Prompt.ask("User")
    cmd=Prompt.ask("Command")
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username=user)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    print(stdout.read().decode())
    ssh.close()
