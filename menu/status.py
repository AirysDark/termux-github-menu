
from repo_select import select_repo
from config import GITHUB_DIR
from utils import run, pause

def execute():
    repo = select_repo()
    if repo:
        run("git status", cwd=GITHUB_DIR / repo)
    pause()
