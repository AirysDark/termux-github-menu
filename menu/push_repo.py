from utils import select_repo, run
from config import GITHUB_DIR
import datetime
import zipfile
import os

def execute():
    repo = select_repo()
    if not repo:
        return

    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_path = GITHUB_DIR / f"{repo}_backup_{ts}.zip"

    with zipfile.ZipFile(zip_path, "w") as z:
        for root, dirs, files in os.walk(GITHUB_DIR / repo):
            for file in files:
                full = os.path.join(root, file)
                z.write(full)

    msg = input("Commit message: ")
    run(f"cd {GITHUB_DIR}/{repo} && git add . && git commit -m \"{msg}\" && git push")
