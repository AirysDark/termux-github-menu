
from repo_select import select_repo
from config import GITHUB_DIR
from utils import run, pause
import time

def execute():
    repo = select_repo()
    if not repo:
        return
    print("Watching (Ctrl+C to stop)...")
    try:
        while True:
            run("git add .", cwd=GITHUB_DIR / repo)
            run('git commit -m "Auto commit"', cwd=GITHUB_DIR / repo)
            run("git push", cwd=GITHUB_DIR / repo)
            time.sleep(10)
    except KeyboardInterrupt:
        pass
    pause()
