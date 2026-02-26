
from utils import run, pause

def execute():
    name = input("Git username: ")
    email = input("Git email: ")
    run(f'git config --global user.name "{name}"')
    run(f'git config --global user.email "{email}"')
    print("✅ Git config updated.")
    pause()
