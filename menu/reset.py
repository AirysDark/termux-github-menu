
from config import PINNED_FILE, LAST_USED_FILE
from utils import pause

def execute():
    confirm = input("Reset history? (y/n): ")
    if confirm.lower() == "y":
        if PINNED_FILE.exists():
            PINNED_FILE.unlink()
        if LAST_USED_FILE.exists():
            LAST_USED_FILE.unlink()
        print("Reset complete.")
    pause()
