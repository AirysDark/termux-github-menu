
from rich.prompt import Prompt
from devops_enterprise.core.config import load_json,save_json,DEPLOY_FILE
from devops_enterprise.core.utils import run

def execute():
    profiles=load_json(DEPLOY_FILE)
    print("1.Add 2.Run")
    c=Prompt.ask("Choice")
    if c=="1":
        name=Prompt.ask("Profile name")
        cmd=Prompt.ask("Deploy command")
        profiles[name]={"cmd":cmd}
        save_json(DEPLOY_FILE,profiles)
        print("Saved.")
    elif c=="2":
        name=Prompt.ask("Profile name")
        if name in profiles:
            run(profiles[name]["cmd"])
