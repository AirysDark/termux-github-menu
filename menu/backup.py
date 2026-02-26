
from repo_select import select_repo
from config import GITHUB_DIR
from utils import pause, timestamp
import zipfile
import os

def execute():
    repo = select_repo()
    if repo:
        ts = timestamp()
        zip_path = GITHUB_DIR / f"{repo}_backup_{ts}.zip"
        with zipfile.ZipFile(zip_path, "w") as z:
            for root, _, files in os.walk(GITHUB_DIR / repo):
                for f in files:
                    full = os.path.join(root, f)
                    z.write(full)
        print("Backup created:", zip_path)
    pause()
