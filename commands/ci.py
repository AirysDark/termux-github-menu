
import requests,time
from rich.prompt import Prompt
from devops_enterprise.core.config import load_accounts

def execute():
    accs=load_accounts()
    user=Prompt.ask("Account")
    if user not in accs: print("Missing"); return
    token=accs[user]["token"]
    repo=Prompt.ask("owner/repo")
    headers={"Authorization":f"token {token}"}
    while True:
        r=requests.get(f"https://api.github.com/repos/{repo}/actions/runs",headers=headers).json()
        print("Latest status:",r["workflow_runs"][0]["status"])
        time.sleep(10)
