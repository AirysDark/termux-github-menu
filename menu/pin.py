
from repo_select import select_repo
from config import PINNED_FILE
from utils import pause

def execute():
    repo = select_repo()
    if repo:
        with open(PINNED_FILE, "a") as f:
            f.write(repo + "\n")
    pause()
