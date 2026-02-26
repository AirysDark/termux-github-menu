
from devops_terminal.core.utils import select_repo, run
from rich.prompt import Prompt
from devops_terminal.core.config import GITHUB_DIR

def execute():
    repo = select_repo()
    if repo:
        msg = Prompt.ask("Commit message")
        run(f"cd {GITHUB_DIR}/{repo} && git add . && git commit -m \"{msg}\" && git push")
