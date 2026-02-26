
from repo_select import select_repo
from config import PINNED_FILE
from utils import pause

def execute():
    repo = select_repo()
    if repo and PINNED_FILE.exists():
        lines = PINNED_FILE.read_text().splitlines()
        lines = [l for l in lines if l != repo]
        PINNED_FILE.write_text("\n".join(lines))
    pause()
