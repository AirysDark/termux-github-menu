
from devops_terminal.core.utils import select_repo, run
from devops_terminal.core.config import GITHUB_DIR

def execute():
    repo = select_repo()
    if repo:
        run(f"cd {GITHUB_DIR}/{repo} && git pull --rebase")
