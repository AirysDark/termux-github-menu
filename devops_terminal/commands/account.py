
from rich.prompt import Prompt
from devops_terminal.core.config import load_accounts, save_accounts

def execute():
    accs = load_accounts()
    print("1.Add 2.List")
    c = Prompt.ask("Choice")
    if c=="1":
        name=Prompt.ask("Account name")
        token=Prompt.ask("Token")
        accs[name]={"token":token}
        save_accounts(accs)
        print("Saved.")
    elif c=="2":
        for a in accs: print(a)
