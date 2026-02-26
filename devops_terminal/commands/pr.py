
import requests
from rich.prompt import Prompt
from devops_terminal.core.config import load_accounts

def execute():
    accs = load_accounts()
    user = Prompt.ask("Account")
    if user not in accs:
        print("Account missing"); return
    token = accs[user]["token"]
    repo = Prompt.ask("owner/repo")
    title = Prompt.ask("Title")
    head = Prompt.ask("Head branch")
    base = Prompt.ask("Base branch")
    headers={"Authorization":f"token {token}"}
    data={"title":title,"head":head,"base":base}
    r=requests.post(f"https://api.github.com/repos/{repo}/pulls",headers=headers,json=data)
    print(r.json())
