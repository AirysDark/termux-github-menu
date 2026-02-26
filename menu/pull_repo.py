from utils import select_repo, run
from config import GITHUB_DIR

def execute():
    repo = select_repo()
    if repo:
        run(f"cd {GITHUB_DIR}/{repo} && git pull")
