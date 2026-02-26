
from repo_select import select_repo
from config import GITHUB_DIR
from utils import run, pause

def execute():
    repo = select_repo()
    if repo:
        msg = input("Commit message: ")
        run("git add .", cwd=GITHUB_DIR / repo)
        run(f'git commit -m "{msg}"', cwd=GITHUB_DIR / repo)
    pause()
