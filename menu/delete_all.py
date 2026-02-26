
from config import GITHUB_DIR
from utils import pause
import shutil

def execute():
    confirm = input("Delete ALL repos? (y/n): ")
    if confirm.lower() == "y":
        for r in GITHUB_DIR.iterdir():
            if r.is_dir():
                shutil.rmtree(r)
        print("All repos deleted.")
    pause()
