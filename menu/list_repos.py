
from config import GITHUB_DIR, PINNED_FILE
from utils import pause

def execute():
    print("Repositories:")
    if PINNED_FILE.exists():
        print("Pinned:")
        print(PINNED_FILE.read_text())
    for r in GITHUB_DIR.iterdir():
        if r.is_dir():
            print("-", r.name)
    pause()
