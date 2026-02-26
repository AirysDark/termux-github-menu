
import requests
from rich.prompt import Prompt
from devops_terminal.core.config import load_accounts

def execute():
    accs=load_accounts()
    user=Prompt.ask("Account")
    if user not in accs: print("Missing"); return
    token=accs[user]["token"]
    repo=Prompt.ask("owner/repo")
    title=Prompt.ask("Title")
    body=Prompt.ask("Body")
    headers={"Authorization":f"token {token}"}
    r=requests.post(f"https://api.github.com/repos/{repo}/issues",headers=headers,json={"title":title,"body":body})
    print(r.json())
