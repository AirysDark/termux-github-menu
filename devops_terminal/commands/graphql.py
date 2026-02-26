
import requests
from rich.prompt import Prompt
from devops_enterprise.core.config import load_accounts

def execute():
    accs=load_accounts()
    user=Prompt.ask("Account")
    if user not in accs: print("Missing"); return
    token=accs[user]["token"]
    query=Prompt.ask("GraphQL query")
    r=requests.post("https://api.github.com/graphql",
        headers={"Authorization":f"bearer {token}"},
        json={"query":query})
    print(r.json())
