
import requests
from rich.prompt import Prompt
from devops_terminal.core.config import load_accounts

def execute():
    accs=load_accounts()
    user=Prompt.ask("Account")
    if user not in accs: print("Missing"); return
    token=accs[user]["token"]
    repo=Prompt.ask("owner/repo")
    headers={"Authorization":f"token {token}"}
    r=requests.get(f"https://api.github.com/repos/{repo}/actions/runs",headers=headers)
    print(r.json())
