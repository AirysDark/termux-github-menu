
from devops_terminal.core.utils import select_repo, run
from rich.prompt import Prompt
from devops_terminal.core.config import GITHUB_DIR

def execute():
    repo = select_repo()
    if not repo: return
    print("1.List 2.Create 3.Switch")
    c = Prompt.ask("Choice")
    if c=="1": run(f"cd {GITHUB_DIR}/{repo} && git branch -a")
    elif c=="2":
        name=Prompt.ask("Branch name")
        run(f"cd {GITHUB_DIR}/{repo} && git checkout -b {name}")
    elif c=="3":
        name=Prompt.ask("Branch name")
        run(f"cd {GITHUB_DIR}/{repo} && git checkout {name}")
